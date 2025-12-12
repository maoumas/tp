import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# --- CONFIGURACIÓN ---
# El archivo que descargaste de Google Cloud
CLIENT_SECRETS_FILE = "client_secrets.json"
# Nombre del archivo donde guardaremos tu sesión para no loguearte siempre
TOKEN_FILE = 'token.pickle'
# Permisos necesarios (solo subir y gestionar videos)
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def autenticar_youtube():
    """Maneja la autenticación OAuth2."""
    creds = None
    
    # Verifica si ya tenemos una sesión guardada
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    # Si no hay credenciales válidas, inicia el login en el navegador
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Guarda las credenciales para la próxima vez
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return build('youtube', 'v3', credentials=creds)

def subir_video(youtube, file_path, title, description, tags, category_id="25", privacy="private"):
    """Sube un video al canal autenticado."""
    
    print(f"📤 Iniciando subida: {title}...")

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id # 25 = Noticias y Política, 28 = Ciencia/Tecnología
        },
        'status': {
            'privacyStatus': privacy, # 'private', 'unlisted', 'public'
            'selfDeclaredMadeForKids': False
        }
    }

    # Prepara el archivo (chunksize ajustable para conexiones lentas)
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )

    # Ejecuta la subida mostrando progreso
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"🚀 Subiendo... {int(status.progress() * 100)}%")

    print(f"✅ ¡Video subido con éxito! ID: {response['id']}")
    print(f"🔗 Link: https://youtu.be/{response['id']}")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    # 1. Autenticar
    try:
        youtube_service = autenticar_youtube()
        
        # 2. Configurar detalles del video
        VIDEO_A_SUBIR = "mi_video_final.mp4" # Asegúrate de que este archivo exista
        TITULO = "Análisis Político: Impacto de las Elecciones 2025"
        DESCRIPCION = "En este video analizamos los resultados... \n\n#Politica #Noticias"
        TAGS = ["política", "noticias", "análisis", "alemania"]
        
        # 3. Subir
        # NOTA: Recomiendo subir como 'private' o 'unlisted' primero para revisar
        subir_video(youtube_service, VIDEO_A_SUBIR, TITULO, DESCRIPCION, TAGS, privacy="private")
        
    except FileNotFoundError:
        print("❌ Error: No se encuentra el archivo 'client_secrets.json' o el video.")
    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")
