Aquí tienes un **Prompt detallado en inglés** diseñado para copiar y pegar en una IA de codificación (como ChatGPT, Claude o DeepSeek). Este prompt recopila todas las especificaciones técnicas, módulos y la lógica descrita en las transcripciones del video sobre "X-Prompt 2" y "Grok" [1-4].

El objetivo es generar un código HTML/JS único que replique la funcionalidad de la herramienta descrita.

***

### Prompt to Copy and Paste / Prompt para Copiar y Pegar

**Role:** Expert Full-Stack Web Developer & UI/UX Designer.

**Task:** Create a single-file, responsive HTML5 application (with embedded CSS and JavaScript) called "**Grok Video Prompt Generator Ultimate**." This app must function as a prompt builder specifically optimized for the Grok AI video model. The design should be modern, "cyberpunk/high-tech" aesthetic (dark mode), and fully responsive for mobile, tablet, and desktop [2].

**Core Functionality:**
The user will input parameters into several "Modules." When the user clicks "Generate Prompt," the app must concatenate all selected values into a single, optimized text string to be pasted into Grok.

**Structure & Modules (Must implement all of the following):**

**1. Header:**
*   Title: "Grok Video Generator - Channel Edition"
*   Language Toggle: Button to switch interface labels between English and Spanish [4].
*   "Community" Button: A link placeholder for social sharing [5].

**2. Module I: The Scene (Core)**
*   **Inputs:** Text fields for "Subject & Action" and "Context & Location" [6, 7].
*   **Token Priority Slider:** A range slider (100% to 140%) to adjust the weight of the core prompt. Explain in a tooltip that this manages token allowance for audio [7].

**3. Module II: Visual Style**
*   **Dropdown:** Include 30+ styles (e.g., Cyberpunk, Cinematic, 16mm Film, Lego World, Pixar Style, Western, Anime, Realistic) [4, 7].
*   **Artistic Weight Slider:** A range slider (up to 140%) to control the intensity of the style [8].

**4. Module III: Cinematography & Lenses**
*   **Dropdown - Shot Type:** Extreme Wide, Wide, Medium, Close-up, Extreme Close-up [8].
*   **Dropdown - Lens:** 16mm, 35mm, 50mm, 85mm, Macro [8].

**5. Module IV: Lighting & Atmosphere**
*   **Dropdown - Lighting:** Rembrandt, Dramatic, Soft, Neon, Natural, Studio [8].
*   **Input - Atmosphere/Weather:** Text field (e.g., Fog, Rain, Dust) [8].

**6. Module V: Camera Movement**
*   **Dropdown:** Static, Pan Left/Right, Tilt Up/Down, Handheld, Fast Action Swipe, Drone Shot [9].

**7. Module VI: Audio System (The Critical Feature)**
*   **Toggle Switch:** "Activate Audio Module" (Must remain disabled/hidden unless toggled) [9].
*   **Section A - Environment:** Inputs for "SFX/Ambience" (e.g., waves, city noise) and "Music" (e.g., action, jazz) [10].
*   **Section B - Voice & Dialogue (Anti-Babble Logic):**
    *   **Checkbox:** Enable Voice.
    *   **Input - Character Name:** (Must match the Subject in Module I) [11].
    *   **Dropdown - Voice Type:** Male, Female, Robot, Child [11].
    *   **Dropdown - Accent:** Mexico, Spain, Argentina, USA, UK [11].
    *   **Dropdown - Emotion:** Neutral, Angry, Happy, Whispering, Urgent, Sarcastic [11, 12].
    *   **Input - Script/Dialogue:** A text field limited to **max 10 words** (strictly enforced with a word counter to prevent lip-sync errors/balbuceo) [13].

**8. Module VII: Output & Management**
*   **"Virtual Professor" Box:** A dynamic text area that explains in natural language what the prompt is doing (e.g., "You are designing a scene with a woman speaking...") [13, 14].
*   **Action Buttons:**
    *   "Generate Prompt": Assembles the final string.
    *   "Copy to Clipboard": Copies the result.
    *   "Download .txt": Downloads the prompt as a text file [4, 15].

**Logic Requirements:**
*   **Prompt Construction:** The final output string should follow this structure: `[Visual Style] :: [Scene Description] :: [Camera/Light Details] :: --audio "[SFX/Music] --voice [Name, Type, Emotion, Accent]: "[Script]"`
*   **Anti-Babble Optimization:** If "Voice" is active, ensure the prompt structure strictly separates the dialogue to assist Grok's lip-sync stability [9, 16].

**Code Output:**
Provide the complete, functional code in a single code block.

***

### Explicación de los elementos clave incluidos

Este prompt asegura que la aplicación generada cumpla con "todo lo especificado" en tus fuentes:

1.  **Límite de Tokens (140%):** Se especifica explícitamente en el Módulo I y II, ya que las fuentes indican que al añadir audio, se redujo el límite del 200% al 140% para ahorrar recursos [7, 8].
2.  **Sistema Modular de Audio:** Se detalla la división exacta entre "Ambiente/Música" y "Voz", incluyendo los campos específicos de **Acento** (México, Argentina, etc.) y **Emoción** (Enojado, Feliz, etc.) que son la "frutilla del postre" mencionada en la transcripción [9, 11].
3.  **Lógica Anti-Balbuceo:** Se incluye la restricción estricta de **10 palabras** para el guion, tal como advierte la fuente para evitar que el algoritmo falle en la sincronización labial [13].
4.  **Funcionalidades de Interfaz:** Se solicita el botón de "Descargar .txt", el cambio de idioma y el cuadro del "Profesor Virtual" que explica el prompt, características presentes en la versión 1.9.6 [4, 14].
***
fuentes

https://youtu.be/Z_qCqPP3BrA
https://www.clicmayores.com/xprompt2.html
