El archivo que estás abriendo, tp-master-2025-de.html, es una aplicación web de teleprompter. Aparece en negro porque está diseñado para ser utilizado con un guion que tú le proporciones.
Para utilizarlo, sigue estos pasos:
 * Abre la consola del desarrollador: En tu navegador, haz clic derecho en la página y selecciona "Inspeccionar" o presiona F12.
 * Pega tu guion: En la consola, escribe el siguiente código y presiona Enter:
<!-- end list -->
const guion = [
  { type: 'title', content: 'TÍTULO DEL PROGRAMA' },
  { type: 'instruction', content: 'INSTRUCCIONES PARA EL PRESENTADOR' },
  { type: 'text', content: 'Este es el texto que el presentador leerá.' }
];

const scriptContainer = document.getElementById('script-container');
guion.forEach(item => {
    let el;
    if (item.type === 'title') { el = document.createElement('h2'); el.className = 'timestamp'; }
    else if (item.type === 'instruction') { el = document.createElement('p'); el.className = 'instruction'; }
    else { el = document.createElement('p'); el.className = 'speaker-text'; }
    el.textContent = item.content;
    scriptContainer.appendChild(el);
});

Personaliza el guion: Reemplaza los textos entre comillas por el contenido que desees. Puedes añadir más elementos al array guion.
Controles:
 * Iniciar/Pausar: Presiona el botón "START" o la barra espaciadora.
 * Velocidad: Usa los botones "+" y "-" para ajustar la velocidad de desplazamiento.
 * Tamaño de letra: Usa los botones "A+" y "A-" para cambiar el tamaño del texto.
 * Reiniciar: Presiona el botón de reinicio para volver al principio del guion.
¡Disfruta de tu teleprompter!
