<div align="center">

# 🤖 Ari AI Assistant

### Local-first AI voice assistant built with Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Faster-Whisper](https://img.shields.io/badge/Speech-Faster--Whisper-6F42C1?style=for-the-badge)](https://github.com/SYSTRAN/faster-whisper)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 About

**Ari** is a personal AI voice-assistant project focused on local speech recognition, command routing and practical desktop automation. The project is designed to keep core voice processing local while remaining modular enough to expand with new capabilities.

## ✨ Features

- 🎙️ Microphone input with `sounddevice`
- 🧠 Local speech-to-text using **Faster-Whisper**
- 🗣️ Basic voice-command routing
- 🔎 Optional OCR with **Tesseract**
- ⚙️ JSON-based configuration
- 🪟 Windows PowerShell launcher
- 🔒 Local-first architecture

## 🎬 Example

```text
🤖 Ari starting...
🧠 Whisper model: base.en
🎙️ Listening...
🗣️ You: hello Ari
🤖 Ari: Hello! How can I help?
```

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Faster-Whisper | Speech recognition |
| NumPy | Audio data handling |
| SoundDevice | Microphone capture |
| Tesseract OCR | Optional image text extraction |
| PowerShell | Windows launcher |

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
├── LICENSE
└── README.md
```

## 🚀 Installation

```bash
git clone https://github.com/OmTalekarDev/Ari-AI-Assistant.git
cd Ari-AI-Assistant
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `config.example.json` to `config.json`, adjust the configuration, then run:

```bash
python src/main.py
```

Or on Windows:

```powershell
.\run.ps1
```

## 🗣️ Current Commands

```text
hello
hi ari
exit
quit
stop
goodbye
```

## 🛣️ Roadmap

- [x] Local speech-to-text
- [x] Configurable Whisper model
- [x] Basic command routing
- [x] Optional OCR helper
- [ ] Wake-word activation
- [ ] Better conversational responses
- [ ] Desktop automation
- [ ] Plugin system
- [ ] Cross-platform support

## 🤝 Contributing

Issues, feature ideas and pull requests are welcome.

## 📄 License

MIT License — see [LICENSE](LICENSE).

---

Built with Python by **[Om Talekar](https://github.com/OmTalekarDev)**.
