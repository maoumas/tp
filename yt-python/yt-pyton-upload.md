*Proyecto: 
#Desarrollar un script para subir videos a YouTube automáticamente es un proyecto excelente para tu canal @TranslatedPressDE. Te ahorrará mucho tiempo en tareas repetitivas.
Para esto utilizaremos la YouTube Data API v3 oficial de Google y Python.
Aquí tienes la guía paso a paso y el código completo.
Paso 1: Configuración en Google Cloud (Indispensable)
Antes de tocar el código, necesitas "permiso" de YouTube para que tu script actúe en tu nombre.
 * Ve a la Google Cloud Console.
 * Crea un Nuevo Proyecto (llámalo YouTube-Uploader).
 * En el menú lateral, busca "APIs y servicios" > "Biblioteca".
 * Busca "YouTube Data API v3" y dale a Habilitar.
 * Ve a "APIs y servicios" > "Credenciales".
 * Dale a "Crear credenciales" > "ID de cliente de OAuth".
   * Si te pide configurar la "Pantalla de consentimiento", elige Externo.
   * IMPORTANTE: En la pantalla de consentimiento, agrega tu correo de Gmail (el del canal) como "Usuario de prueba" (Test User). Si no haces esto, el script no funcionará.
 * En tipo de aplicación elige "Aplicación de escritorio".
 * Descarga el archivo JSON de las credenciales, renómbralo a client_secrets.json y guárdalo en la misma carpeta donde pondrás el script.
Paso 2: Instalar librerías
Abre tu terminal y ejecuta:
pip install --upgrade google-api-python-client google-auth-oauthlib google-auth-httplib2

Paso 3: El Script (youtube_uploader.py)
Crea un archivo llamado youtube_uploader.py y pega el código. He añadido comentarios explicativos para que sepas qué hace cada parte.


#Cómo usarlo por primera vez
 * Asegúrate de tener en la carpeta:
   * youtube_uploader.py
   * client_secrets.json
   * Un video de prueba (ej. mi_video_final.mp4).
 * Ejecuta el script: python youtube_uploader.py
 * Se abrirá tu navegador. Inicia sesión con la cuenta de Google de @TranslatedPressDE.
 * Es posible que Google te muestre una advertencia de "App no verificada" (porque la acabas de crear). Dale a Configuración avanzada > Ir a YouTube-Uploader (no seguro).
 * Concede los permisos.
 * El script guardará un archivo token.pickle. Las próximas veces ya no te pedirá login, subirá el video directamente.
 
#Advertencias Importantes
 * Cuota Diaria: La API gratuita tiene un límite diario de cuota (aprox. 10,000 unidades). Subir un video cuesta 1,600 unidades. Esto significa que puedes subir unos 6 videos al día de forma gratuita.
 * Validación: Como es una app "de prueba", los videos se subirán como Privados por defecto (bloqueado por seguridad de YouTube) hasta que verifiques la app o simplemente los cambies a públicos manualmente en YouTube Studio tras la subida.
Siguiente paso integremos este script en una interfaz visual simple o prefieres usarlo así desde la terminal.

#Aplicacion para subir los video de YouTube

Haremos una interfaz gráfica (GUI) para que el proceso sea mucho más profesional, fácil de usar y alineado visualmente con el estilo "Dark Mode" y acentos rojos que hemos estado usando para TranslatedPress.
Usaremos la librería estándar tkinter de Python, por lo que no necesitas instalar nada extra para la interfaz (solo las librerías de Google que se instalaron en el paso anterior).
Estructura de la Aplicación
se ha diseñado la aplicación para que tenga:
 * Selector de Archivo: Para buscar el video en tu PC.
 * Campos de Metadatos: Título, Descripción, Etiquetas.
 * Opciones: Categoría y Privacidad (Privado/Público).
 * Barra de Estado: Para ver el progreso de la subida sin que la ventana se congele.

 
 El Código Completo (app_uploader.py)

Crea un nuevo archivo llamado app_uploader.py y pega el código. Asegúrate de que el archivo client_secrets.json esté en la misma carpeta.


#Pasos para usar la aplicación visual:
 * Asegúrate de tener el archivo client_secrets.json (el que descargaste de Google Cloud) en la misma carpeta que este nuevo script app_uploader.py.
 * Ejecuta el script:
   python app_uploader.py

 * Se abrirá una ventana oscura con detalles en rojo (estilo TranslatedPress).
 * Si es la primera vez, se abrirá el navegador para que inicies sesión en Google. Al volver, la app dirá "Estado: Conectado" en verde.
 * Selecciona tu video, llena los datos y pulsa el botón grande rojo "SUBIR A YOUTUBE".
 * Verás una barra de progreso llenarse mientras el video se sube.
¡Espero que esto sea exactamente lo que necesitabas para automatizar tu canal!

