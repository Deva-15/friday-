# Friday

# 🤖 Friday AI — Personal Voice Assistant

> **Friday AI** is a personal desktop voice assistant built with Python, designed to understand voice commands, respond naturally, remember information, and automate tasks on the computer.

---

## 📌 About Friday

Friday is an AI-powered personal assistant inspired by intelligent assistants such as JARVIS.

The main goal is to create an assistant that can interact with the user through **voice, AI, memory, and computer automation**.

### Current capabilities

* 🎤 Voice input
* 🔊 Voice responses
* 🧠 AI conversations
* 💾 Personal memory
* 🖥️ Mac control
* 🌐 Google search
* ▶️ YouTube search
* 📱 Application opening
* ⏰ Reminder system
* 📂 File and folder access
* 🔋 System information
* 🤖 Automated computer actions

---

# 🏗️ Project Architecture

```text
                 🎤 Voice Input
                       │
                       ▼
              Speech Recognition
                       │
                       ▼
                 Friday AI
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     AI Processing            Command Processing
          │                         │
          ▼                         ▼
    Llama 3.2 / Ollama        Friday Tools
          │                         │
          └────────────┬────────────┘
                       │
                       ▼
                 🔊 Voice Output
                       │
                       ▼
                    User
```

---

# 📂 Project Structure

```text
Friday/
│
├── main.py
├── friday_ai.py
├── friday_tools.py
├── mac_control.py
├── search_bot.py
├── speak.py
├── listen.py
├── requirements.txt
├── README.md
│
└── venv/
```

### Main Components

| File               | Purpose                       |
| ------------------ | ----------------------------- |
| `main.py`          | Main application              |
| `friday_ai.py`     | AI communication              |
| `friday_tools.py`  | Assistant commands and tools  |
| `mac_control.py`   | Mac system controls           |
| `search_bot.py`    | Google and YouTube operations |
| `listen.py`        | Voice input                   |
| `speak.py`         | Voice output                  |
| `requirements.txt` | Python dependencies           |
| `README.md`        | Project documentation         |

---

# 🛠️ Technologies

* Python
* Ollama
* Llama 3.2
* Speech Recognition
* Text-to-Speech
* PyAutoGUI
* macOS automation
* Git
* GitHub

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/friday-ai.git
cd friday-ai
```

## 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Install and Start Ollama

Check Ollama:

```bash
ollama --version
```

Download the model:

```bash
ollama pull llama3.2
```

Check installed models:

```bash
ollama list
```

## 5. Start Friday

Start Ollama:

```bash
ollama serve
```

Then open another terminal:

```bash
cd Friday
source venv/bin/activate
python main.py
```

---

# 🎤 Example Commands

### Applications

```text
Open Safari
Open WhatsApp
Open Terminal
Open Finder
```

### Search

```text
Search Google for cybersecurity
Search YouTube for Python tutorials
Open GitHub
```

### System

```text
Check my battery
Take a screenshot
Increase volume
Decrease volume
Lock my Mac
```

### Memory

```text
Remember that my favourite subject is cybersecurity.

What is my favourite subject?
```

### Reminders

```text
Remind me to study at 7 PM.
```

Friday supports a user-friendly **12-hour time format** such as:

```text
7:00 AM
12:30 PM
6:00 PM
9:30 PM
```

---

# 🧠 Memory System

Friday can store useful information and recall it during future conversations.

Example:

```text
You: Remember that my favourite subject is cybersecurity.

Friday: I'll remember that.
```

Later:

```text
You: What is my favourite subject?

Friday: Your favourite subject is cybersecurity.
```

This allows Friday to become more personalized over time.

---

# ⏰ Reminder System

Friday includes a reminder system designed to help manage tasks and daily activities.

Example:

```text
You: Remind me to study cybersecurity at 7 PM.

Friday: Reminder set for 7:00 PM.
```

The reminder system uses a **12-hour AM/PM format** for easier interaction.

---

# 🖥️ Mac Automation

Friday can interact with macOS using automation tools.

Examples include:

```text
Open applications
Open folders
Take screenshots
Check battery
Control volume
Lock the Mac
Sleep the Mac
```

---

# 🌐 Web & YouTube

Friday can perform browser-based actions.

Examples:

```text
Search Google for ethical hacking
Search YouTube for Python tutorials
Open GitHub
Open websites
```

---

# 🔄 Updating Friday

Friday is an **actively developing project**.

New features, improvements, commands, and automation capabilities will be added regularly.

## Current Development

```text
✅ Voice input
✅ Voice output
✅ Llama 3.2 integration
✅ Ollama integration
✅ AI conversations
✅ Memory system
✅ Google search
✅ YouTube search
✅ Application opening
✅ Mac controls
✅ Reminder system
✅ 12-hour reminder format
🔄 Improved WhatsApp automation
🔄 Better command recognition
🔄 Expanded computer automation
🔄 More intelligent memory
🔄 Additional AI tools
```

## Update Log

### Version 1.0

* Created the basic Friday AI structure
* Added voice input
* Added voice output
* Added AI conversation
* Added Ollama + Llama 3.2

### Version 1.1

* Added memory functionality
* Added Google search
* Added YouTube search
* Added application opening
* Added Mac controls

### Version 1.2

* Added reminder functionality
* Added 12-hour AM/PM reminder format
* Improved command routing

### Version 1.3 — In Development

* Improving WhatsApp automation
* Improving application control
* Improving natural-language command handling
* Expanding Friday's automation capabilities

> **The README will be updated whenever major Friday features are added.**

---

# 🔮 Future Development

The long-term vision for Friday includes:

### 🧠 Advanced AI

* Better natural-language understanding
* Context-aware conversations
* Improved memory
* More intelligent task execution

### 🎙️ Wake Word

```text
"Hey Friday"
```

### 📱 Smartphone Integration

* Notifications
* Messages
* Calls
* Remote computer control

### 📅 Smart Scheduling

* Calendar integration
* Task management
* Study planning
* Daily routines

### 👁️ Computer Vision

* Image understanding
* Document analysis
* Desktop understanding
* Object recognition

### 🔐 Cybersecurity Assistant

Future versions may include cybersecurity-focused capabilities such as:

* Security monitoring
* Log analysis
* Network information
* Security alerts
* Defensive security tools

---

# 🎯 Vision

The ultimate goal is to develop Friday into a complete personal AI assistant that can:

```text
           🤖 FRIDAY AI
                │
     ┌──────────┼──────────┐
     │          │          │
     ▼          ▼          ▼
   🧠 AI      🎤 Voice   🖥️ Automation
     │          │          │
     └──────────┼──────────┘
                │
                ▼
         Personal Assistant
```

Friday is continuously evolving from a simple voice assistant into a **personal AI automation system**.

---

# 👨‍💻 Developer

**Dev Chakkani**

B.Tech — Computer Science & Engineering

### Interests

* Cybersecurity
* Ethical Hacking
* Artificial Intelligence
* Python
* Automation
* Cloud Security

---

# ⭐ Project Status

```text
🚀 ACTIVE DEVELOPMENT
```

Friday AI is continuously being updated with new features and capabilities.

**Built with Python, AI, and automation. 🤖**

# Video

