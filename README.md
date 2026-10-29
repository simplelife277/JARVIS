# 🤖 Jarvis AI Assistant

A Python-based AI voice assistant that helps users perform tasks through voice commands and interact with Google's Gemini AI.

## ✨ Features

- 🧠 **Gemini AI Integration** – Get AI-powered responses to questions.
- 🎤 **Speech Recognition** – Convert voice commands into text.
- 🔊 **Text-to-Speech** – Hear responses spoken aloud.
- 🕒 **Date and Time** – Get the current date and time.
- 📝 **Open Notepad** – Launch Notepad using voice commands.
- 🌐 **Open Chrome** – Open the Chrome browser.
- ❌ **Close Notepad** – Close Notepad through supported commands.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Speech Recognition
- Text-to-Speech
- Python Virtual Environment

## 📁 Project Structure

```text
my-agent/
├── src/
│   ├── main.py
│   ├── jarvis.py
│   ├── gemini_ai.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   ├── wake_word.py
│   └── other test files
├── .env.local
├── uv.lock
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/simplelife277/jarvis-.git
cd jarvis-
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the packages required by your project. If you use `uv`, run:

```bash
uv sync
```

### 4. Configure your Gemini API key

Create a local environment file and add your API key:

```text
GEMINI_API_KEY=your_api_key_here
```

Keep your actual API key private. Never upload `.env.local` or other secret files to GitHub.

### 5. Run the assistant

```bash
python src/main.py
```

## 🚀 Future Improvements

- Add a wake-word activation system.
- Improve voice-command accuracy.
- Add more desktop automation features.
- Build a graphical user interface.
- Add more AI-powered tasks.

## 👨‍💻 Author

**simplelife277**

Aspiring Python Backend Developer | Learning Python, AI, APIs, and Backend Development.

## 📄 License

This project is intended for educational and personal learning purposes.
