# The Rivet and the Zorzal (El Remache y el Zorzal)

### A Digital Historical Archive & Interactive Book
**Ford T City Hotel-Museum | Tacuarembó, Uruguay**

---

## 📖 About This Project

This repository hosts the source code and content for the digital presentation of **"The Rivet and the Zorzal"**. This interactive web experience documents the fascinating journey of a specific fuselage fragment recovered from the tragic 1935 plane crash in Medellín, Colombia, which claimed the life of the legendary Tango singer, Carlos Gardel.

The artifact—a melted piece of aluminum with a rivet still attached—is currently preserved and exhibited at the **Ford T City Hotel-Museum** in Tacuarembó, Uruguay.

This project serves as a digital companion to the physical exhibit, offering visitors and researchers a detailed account of the object's provenance, the scientific metallurgical studies performed to authenticate it, and the historical context of the Ford Trimotor aircraft.

## 📂 Repository Structure

The project is structured as a lightweight, static Single Page Application (SPA) requiring no external dependencies or backend. It is designed to be hosted via GitHub Pages.

```text
/
├── index.html                  # Multilingual Landing Page (Entry Point)
├── style.css (Optional)        # Shared styles (if separated)
│
├── es/                         # SPANISH Version
│   └── index.html              # Interactive Book (Español)
│
├── en/                         # ENGLISH Version
│   └── index.html              # Interactive Book (English)
│
├── de/                         # GERMAN Version
│   └── index.html              # Interactive Book (Deutsch)
│
├── [assets]                    # Images and Documents
│   ├── ford-model-t.jpg
│   ├── hotel-museo-fordt-city.jpg
│   ├── fragmento-fundido.jpg
│   ├── remache-fundido.jpg
│   ├── portada.jpg
│   ├── contraportada.jpg
│   └── logo-fordTCity-HotelMuseo.png
│
└── [documentation]             # PDF Reports
    ├── Info_IEM__UDELAR_25256.pdf
    └── remache_zarzal.pdf
