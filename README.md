# 🤖 Ari — AI Voice Assistant

Ari is a personal AI voice-assistant project built in Python, focused on local speech recognition and practical desktop automation.

> **Status:** Active development 🚧

## ✨ Features

- 🎙️ Microphone input
- 🧠 Local speech-to-text with **Faster-Whisper**
- 🗣️ Voice-command processing
- 🔎 Optional OCR support with **Tesseract**
- ⚙️ Configurable model and assistant settings
- 🪟 Windows-friendly PowerShell launch script
- 🔒 Designed with local-first processing in mind

## 🧰 Tech Stack

- Python
- Faster-Whisper
- NumPy
- SoundDevice
- Tesseract OCR (optional)
- PowerShell

## 📁 Project Structure

```text
Ari-AI-Assistant/
├── src/
│   ├── main.py
│   ├── audio.py
│   ├── commands.py
│   └── ocr.py
├── config.example.json
├── requirements.txt
├── run.ps1
├── .gitignore
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/BlockZGaming/Ari-AI-Assistant.git
cd Ari-AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Ari

Copy `config.example.json` to `config.json` and adjust the settings.

### 5. Run

```bash
python src/main.py
```

Or on Windows:

```powershell
.\run.ps1
```

## 🧠 Whisper Model

The default configuration uses `base.en`, matching the model used during Ari's development. You can change the model in `config.json` depending on your hardware.

## 🔎 OCR

OCR is optional. If Tesseract is installed and configured, Ari can use the OCR helper to extract text from an image.

## 🛣️ Roadmap

- [x] Local speech-to-text
- [x] Configurable Whisper model
- [x] Basic command routing
- [x] Optional OCR module
- [ ] Wake-word activation
- [ ] Better conversational responses
- [ ] Desktop automation
- [ ] Plugin system
- [ ] Cross-platform support

## 🤝 Contributing

Issues, ideas and pull requests are welcome.

## 📜 License

MIT License
