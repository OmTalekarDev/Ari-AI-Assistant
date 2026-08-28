<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7F5AF0,100:2CB67D&height=220&section=header&text=Ari%20AI%20Assistant&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Local-first%20AI%20voice%20assistant&descAlignY=58&descSize=18" alt="Ari AI Assistant banner" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/BlockZGaming/Ari-AI-Assistant"><img src="https://img.shields.io/github/stars/BlockZGaming/Ari-AI-Assistant?style=for-the-badge&logo=github" alt="GitHub stars" /></a>
  <a href="https://github.com/BlockZGaming/Ari-AI-Assistant/issues"><img src="https://img.shields.io/github/issues/BlockZGaming/Ari-AI-Assistant?style=for-the-badge" alt="GitHub issues" /></a>
  <a href="https://github.com/BlockZGaming/Ari-AI-Assistant/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="MIT License" /></a>
</p>

# 🤖 Ari AI Voice Assistant

Ari is a personal AI voice-assistant project built in Python, focused on local speech recognition and practical desktop automation.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Faster-Whisper](https://img.shields.io/badge/Speech-Faster--Whisper-6F42C1)](https://github.com/SYSTRAN/faster-whisper)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](.)

> A local-first voice assistant prototype with speech recognition, command routing, and optional OCR support.

## 🎬 Demo

### Example terminal session

```text
🤖 Ari starting...
🧠 Whisper model: base.en
🎙️ Listening for 5 seconds...
🗣️ You: hello Ari
🤖 Ari: Hello! How can I help?
🎙️ Listening for 5 seconds...
🗣️ You: goodbye
👋 Ari: Goodbye!
```

> 📸 **Demo screenshots coming soon.** Once the assistant is running reliably on your machine, add a screenshot or screen recording here to showcase the real application.

## ✨ Features

- 🎙️ Microphone input with `sounddevice`
- 🧠 Local speech-to-text using **Faster-Whisper**
- 🗣️ Basic voice-command routing
- 🔎 Optional OCR with **Tesseract**
- ⚙️ JSON-based configuration
- 🪟 Windows PowerShell launcher
- 🔒 Local-first architecture

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

### 1. Clone

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

### 4. Create your configuration

Copy `config.example.json` to `config.json` and adjust the values for your system.

### 5. Run

```bash
python src/main.py
```

Or use:

```powershell
.\run.ps1
```

## 🧠 Whisper Model

The default configuration uses the `base.en` Faster-Whisper model. You can change the model in `config.json` depending on your hardware and accuracy/speed requirements.

## 🔎 OCR

OCR is optional. Install Tesseract separately, then use the helper in `src/ocr.py` to extract text from an image.

## 🗣️ Current Commands

Ari currently recognizes simple commands such as:

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

Issues, feature ideas, and pull requests are welcome.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Built with Python by **Om Talekar** (`BlockZGaming`).
