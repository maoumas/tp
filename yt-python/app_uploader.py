import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import pickle
import threading
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# --- CONFIGURACIÓN DE ESTILO ---
STYLE_BG = "#121212"       # Fondo oscuro
STYLE_PANEL = "#1e1e1e"    # Paneles
STYLE_ACCENT = "#E62117"   # Rojo YouTube
STYLE_TEXT = "#e0e0e0"     # Texto blanco
STYLE_INPUT = "#2d2d2d"    # Fondo de inputs

# --- CONFIGURACIÓN DE YOUTUBE ---
CLIENT_SECRETS_FILE = "client_secrets.json"
TOKEN_FILE = 'token.pickle'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

class YouTubeUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TranslatedPress Uploader")
        self.root.geometry("600x750")
        self.root.configure(bg=STYLE_BG)
        
        self.youtube = None
        self.video_path = None

        self._setup_ui()
        self._check_auth()

    def _setup_ui(self):
        # Estilos personalizados para TTK
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", background=STYLE_BG, foreground=STYLE_TEXT, font=("Segoe UI", 10))
        style.configure("Header.TLabel", background=STYLE_BG, foreground=STYLE_ACCENT, font=("Segoe UI", 16, "bold"))
        style.configure("TButton", background=STYLE_PANEL, foreground="white", borderwidth=0)
        style.map("TButton", background=[("active", STYLE_ACCENT)])

        # --- HEADER ---
        header_frame = tk.Frame(self.root, bg=STYLE_BG, pady=20)
        header_frame.pack(fill="x")
        lbl_title = ttk.Label(header_frame, text="YOUTUBE UPLOADER PRO", style="Header.TLabel")
        lbl_title.pack()
        
        self.lbl_auth_status = tk.Label(header_frame, text="Estado: Desconectado", fg="#777", bg=STYLE_BG, font=("Segoe UI", 8))
        self.lbl_auth_status.pack()

        # --- FORMULARIO ---
        form_frame = tk.Frame(self.root, bg=STYLE_BG, padx=30)
        form_frame.pack(fill="both", expand=True)

        # 1. Selección de Archivo
        tk.Label(form_frame, text="ARCHIVO DE VIDEO", bg=STYLE_BG, fg=STYLE_ACCENT, font=("Segoe UI", 8, "bold")).pack(anchor="w", mt=10)
        
        file_frame = tk.Frame(form_frame, bg=STYLE_BG)
        file_frame.pack(fill="x", pady=5)
        
        self.btn_select = tk.Button(file_frame, text="Seleccionar Video", command=self.select_file, bg=STYLE_PANEL, fg="white", relief="flat", padx=15, pady=5)
        self.btn_select.pack(side="left")
        
        self.lbl_filename = tk.Label(file_frame, text="Ningún archivo seleccionado", bg=STYLE_BG, fg="#555", padx=10)
        self.lbl_filename.pack(side="left")

        # 2. Título
        tk.Label(form_frame, text="TÍTULO", bg=STYLE_BG, fg=STYLE_ACCENT, font=("Segoe UI", 8, "bold")).pack(anchor="w", mt=15)
        self.entry_title = tk.Entry(form_frame, bg=STYLE_INPUT, fg="white", insertbackground="white", relief="flat", font=("Segoe UI", 10))
        self.entry_title.pack(fill="x", ipady=8, pady=5)

        # 3. Descripción
        tk.Label(form_frame, text="DESCRIPCIÓN", bg=STYLE_BG, fg=STYLE_ACCENT, font=("Segoe UI", 8, "bold")).pack(anchor="w", mt=10)
        self.text_desc = tk.Text(form_frame, height=5, bg=STYLE_INPUT, fg="white", insertbackground="white", relief="flat", font=("Segoe UI", 10))
        self.text_desc.pack(fill="x", pady=5)

        # 4. Etiquetas
        tk.Label(form_frame, text="ETIQUETAS (separadas por coma)", bg=STYLE_BG, fg=STYLE_ACCENT, font=("Segoe UI", 8, "bold")).pack(anchor="w", mt=10)
        self.entry_tags = tk.Entry(form_frame, bg=STYLE_INPUT, fg="white", insertbackground="white", relief="flat", font=("Segoe UI", 10))
        self.entry_tags.pack(fill="x", ipady=8, pady=5)

        # 5. Opciones (Grid)
        opts_frame = tk.Frame(form_frame, bg=STYLE_BG)
        opts_frame.pack(fill="x", pady=15)

        # Privacidad
        tk.Label(opts_frame, text="PRIVACIDAD", bg=STYLE_BG, fg="#888", font=("Segoe UI", 8, "bold")).grid(row=0, column=0, sticky="w")
        self.combo_privacy = ttk.Combobox(opts_frame, values=["private", "unlisted", "public"], state="readonly")
        self.combo_privacy.current(0)
        self.combo_privacy.grid(row=1, column=0, sticky="ew", padx=(0, 10))

        # Categoría
        tk.Label(opts_frame, text="CATEGORÍA ID", bg=STYLE_BG, fg="#888", font=("Segoe UI", 8, "bold")).grid(row=0, column=1, sticky="w")
        self.combo_category = ttk.Combobox(opts_frame, values=["25 (News)", "28 (Tech)", "22 (Blog)"], state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=1, column=1, sticky="ew")

        opts_frame.columnconfigure(0, weight=1)
        opts_frame.columnconfigure(1, weight=1)

        # --- BOTÓN DE SUBIDA ---
        self.btn_upload = tk.Button(self.root, text="SUBIR A YOUTUBE", command=self.start_upload_thread, 
                                    bg=STYLE_ACCENT, fg="white", font=("Segoe UI", 12, "bold"), 
                                    relief="flat", pady=15, cursor="hand2")
        self.btn_upload.pack(fill="x", side="bottom", padx=30, pady=30)

        # --- BARRA DE ESTADO ---
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=100, mode="determinate")
        self.progress_bar.pack(fill="x", padx=30, side="bottom")
        self.lbl_status = tk.Label(self.root, text="Listo", bg=STYLE_BG, fg="#888")
        self.lbl_status.pack(side="bottom", pady=5)

    def _check_auth(self):
        """Verifica autenticación al iniciar en segundo plano."""
        threading.Thread(target=self.authenticate).start()

    def authenticate(self):
        if not os.path.exists(CLIENT_SECRETS_FILE):
            self.update_status(f"Falta {CLIENT_SECRETS_FILE}", error=True)
            return

        creds = None
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
                    creds = flow.run_local_server(port=0)
                except Exception as e:
                    self.update_status("Error Auth", error=True)
                    return
            
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)

        self.youtube = build('youtube', 'v3', credentials=creds)
        self.root.after(0, lambda: self.lbl_auth_status.config(text="Estado: Conectado a TranslatedPressDE", fg="#00FF00"))

    def select_file(self):
        filename = filedialog.askopenfilename(title="Seleccionar Video", filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv")])
        if filename:
            self.video_path = filename
            self.lbl_filename.config(text=os.path.basename(filename), fg="white")
            # Auto-llenar título con el nombre del archivo
            if not self.entry_title.get():
                clean_name = os.path.splitext(os.path.basename(filename))[0].replace("_", " ")
                self.entry_title.insert(0, clean_name)

    def update_status(self, text, error=False):
        color = "#FF0000" if error else "#888"
        self.lbl_status.config(text=text, fg=color)

    def start_upload_thread(self):
        if not self.youtube:
            messagebox.showerror("Error", "No autenticado con YouTube.")
            return
        if not self.video_path:
            messagebox.showerror("Error", "Selecciona un video primero.")
            return
        
        self.btn_upload.config(state="disabled", text="SUBIENDO...", bg="#444")
        threading.Thread(target=self.upload_video).start()

    def upload_video(self):
        title = self.entry_title.get()
        desc = self.text_desc.get("1.0", tk.END)
        tags = [tag.strip() for tag in self.entry_tags.get().split(",")]
        privacy = self.combo_privacy.get()
        cat_id = self.combo_category.get().split(" ")[0]

        body = {
            'snippet': {'title': title, 'description': desc, 'tags': tags, 'categoryId': cat_id},
            'status': {'privacyStatus': privacy, 'selfDeclaredMadeForKids': False}
        }

        try:
            self.root.after(0, lambda: self.update_status("Iniciando subida..."))
            
            media = MediaFileUpload(self.video_path, chunksize=1024*1024, resumable=True)
            request = self.youtube.videos().insert(part=','.join(body.keys()), body=body, media_body=media)

            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    progress = int(status.progress() * 100)
                    self.root.after(0, lambda p=progress: self.progress_bar.config(value=p))
                    self.root.after(0, lambda p=progress: self.update_status(f"Subiendo: {p}%"))

            self.root.after(0, lambda: self.upload_complete(response['id']))

        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error de Subida", str(e)))
            self.root.after(0, lambda: self.reset_ui())

    def upload_complete(self, video_id):
        self.update_status(f"¡Éxito! Video ID: {video_id}")
        self.progress_bar.config(value=100)
        messagebox.showinfo("Éxito", f"El video se ha subido correctamente.\nID: {video_id}")
        self.reset_ui()

    def reset_ui(self):
        self.btn_upload.config(state="normal", text="SUBIR A YOUTUBE", bg=STYLE_ACCENT)
        self.progress_bar.config(value=0)

# --- PATCH PARA PACK CON MARGEN SUPERIOR (mt) ---
def pack_patch(self, cnf={}, **kw):
    if 'mt' in kw:
        kw['pady'] = (kw.pop('mt'), kw.get('pady', 0))
    return self._pack(cnf, **kw)
tk.Widget.pack = pack_patch

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeUploaderApp(root)
    root.mainloop()
