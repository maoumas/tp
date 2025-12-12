require('dotenv').config();
const express = require('express');
const session = require('express-session');
const passport = require('passport');
const GitHubStrategy = require('passport-github2').Strategy;
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const speechsdk = require('microsoft-cognitiveservices-speech-sdk');

const app = express();
const upload = multer({ dest: 'uploads/' });

// Configuración de sesión
app.use(session({
    secret: 'superseguro',
    resave: false,
    saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Configuración OAuth con GitHub
passport.use(new GitHubStrategy({
    clientID: process.env.GITHUB_CLIENT_ID,
    clientSecret: process.env.GITHUB_CLIENT_SECRET,
    callbackURL: process.env.GITHUB_CALLBACK_URL
}, (accessToken, refreshToken, profile, done) => {
    return done(null, profile);
}));

passport.serializeUser((user, done) => done(null, user));
passport.deserializeUser((obj, done) => done(null, obj));

// Middleware para proteger rutas
function ensureAuth(req, res, next) {
    if (req.isAuthenticated()) return next();
    res.redirect('/');
}

// Rutas
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views/index.html'));
});

app.get('/auth/github', passport.authenticate('github', { scope: ['user:email'] }));

app.get('/auth/github/callback',
    passport.authenticate('github', { failureRedirect: '/' }),
    (req, res) => res.redirect('/upload')
);

app.get('/upload', ensureAuth, (req, res) => {
    res.sendFile(path.join(__dirname, 'views/upload.html'));
});

// Procesar archivo y generar MP3
app.post('/procesar', ensureAuth, upload.single('archivo'), async (req, res) => {
    try {
        const texto = fs.readFileSync(req.file.path, 'utf8');
        const voz = req.body.voz;

        // Configuración Azure Speech
        const speechConfig = speechsdk.SpeechConfig.fromSubscription(process.env.AZURE_KEY, process.env.AZURE_REGION);
        speechConfig.speechSynthesisVoiceName = voz;

        const audioFile = path.join(__dirname, 'public/output.mp3');
        const audioConfig = speechsdk.AudioConfig.fromAudioFileOutput(audioFile);

        const synthesizer = new speechsdk.SpeechSynthesizer(speechConfig, audioConfig);

        await synthesizer.speakTextAsync(texto);

        // Descargar el archivo generado
        res.download(audioFile, 'resultado.mp3');
    } catch (error) {
        console.error(error);
        res.status(500).send('Error al generar el audio.');
    }
});

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`✅ Servidor corriendo en http://localhost:${PORT}`));
