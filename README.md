# CRM Minimal – Fullstack Aplikacja (React + Flask)

Prosty system CRM do zarządzania klientami i notatkami. Stworzony jako projekt portfolio w technologii fullstack: **React + Flask + SQLite**.

## Demo (wersja online)

- Frontend: https://67fd19b1a0129273333b6cde--idyllic-druid-763ca8.netlify.app
- Backend: https://railway.com/invite/0zVNcRgpJjn

## Funkcje

- Dodawanie i przeglądanie klientów
- Edycja danych klienta
- Dodawanie notatek/interakcji do każdego klienta
- Responsywny design z użyciem Tailwind CSS

## Stack technologiczny

- **Frontend:** React, Tailwind CSS
- **Backend:** Flask (Python), Flask-CORS
- **Baza danych:** SQLite
- **Hosting:** Railway (backend), Netlify (frontend)

## Uruchomienie lokalne

### Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
python init_db.py
python app.py

### Struktura

crm-portfolio/
├── backend/
│   ├── app.py              # Główny plik backendu (Flask)
│   ├── init_db.py          # Skrypt inicjalizujący bazę danych
│   ├── database            # Plik bazy danych (SQLite)
│   └── requirements.txt    # Zależności Pythona

├── frontend/
│   ├── public/             # Pliki statyczne (favicon, itp.)
│   ├── src/
│   │   ├── App.jsx         # Komponent główny Reacta
│   │   ├── App.css         # Style
│   │   ├── index.css       # Główne style globalne
│   │   ├── main.jsx        # Punkt wejścia do aplikacji
│   │   ├── vite-env.d.ts   # Typy Vite (TS)
│   │   └── assets/         # Folder na obrazki / zasoby
│   ├── .env                # Zmienne środowiskowe
│   ├── index.html          # Główny HTML ładowany przez Vite
│   ├── package.json        # Zależności NPM
│   ├── vite.config.ts      # Konfiguracja Vite
│   └── tailwind.config.js  # TailwindCSS config

├── README.md               # Dokumentacja
├── .gitignore              # Pliki ignorowane przez Git
└── venv/                   # (lokalne środowisko Python)
