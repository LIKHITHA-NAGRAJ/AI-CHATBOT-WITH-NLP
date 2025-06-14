# AI-CHATBOT-WITH-NLP
COMPANY : CODTECH IT SOLUTIONS

NAME : LIKHITHA N

INTERN ID : CT06DL625

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTOSH

# 🤖 AI Chatbot with NLP using spaCy and Wikipedia

This project is developed as part of the **CODTECH Internship Task-3**. It is an intelligent, interactive AI chatbot that utilizes **Natural Language Processing (NLP)** and **Wikipedia** to provide informative responses. Built with Python and Streamlit, the chatbot can interact with users through text or voice input, analyze queries using spaCy, retrieve relevant information from Wikipedia, and even read responses aloud using text-to-speech.

---

## 📌 Project Objective

The primary goal of this task is to build an **AI chatbot** that:
- Understands user input using **NLP techniques** (via spaCy)
- Extracts meaningful keywords from the text
- Searches for relevant information using the **Wikipedia API**
- Responds either via text display or **text-to-speech**
- Optionally takes input via microphone
- Provides a **user-friendly GUI** using Streamlit

---

## 🛠️ Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| `Python` | Core programming language |
| `spaCy` | NLP processing and keyword extraction |
| `wikipedia` | Wikipedia API for fetching content |
| `SpeechRecognition` | Accepting voice commands |
| `pyttsx3` | Text-to-speech (TTS) for responses |
| `Streamlit` | For creating an interactive web-based GUI |
| `VS Code` | Editor platform used for development |
| `Anaconda` | For managing Python environments and packages |

---

## 🧠 How It Works

1. **User Input**: User types a question or speaks using a microphone (optional).
2. **NLP with spaCy**: The chatbot processes the input using spaCy to identify important keywords (entities/nouns).
3. **Wikipedia Search**: It uses the top keyword to search Wikipedia and retrieve the most relevant summary.
4. **Response Output**:
   - Text response is displayed in the GUI.
   - Optionally, the chatbot reads the answer aloud using `pyttsx3`.

---

## 🖥️ Platform Used

- Developed using **Visual Studio Code (VS Code)**
- Environment managed using **Anaconda** and virtual environments
- GUI deployed via **Streamlit**, allowing easy web-based interaction
  
📸 Features Demonstrated
✅ Text input from users

✅ Voice input (microphone support)

✅ NLP-powered keyword extraction using spaCy

✅ Wikipedia content summarization

✅ Text-to-speech response using pyttsx3

✅ Fully responsive web interface via Streamlit

🌍 Real-World Applications
Educational Assistant: Helps students by answering factual questions from Wikipedia.

Voice-Enabled Kiosks: Can be integrated into help desks or information booths.

Language Learning: Ideal for language learners to practice asking questions.

Accessibility: Voice and TTS make it usable for visually impaired users.

Smart Devices: Basic framework for building voice-controlled AI assistants.

🚀 Future Scope
This project can be enhanced further by:

Adding a chatbot memory to handle follow-up questions

Integrating OpenAI’s GPT models for generative answers

Multilingual support using spaCy pipelines

Deploying on cloud platforms (Streamlit Cloud, Heroku, etc.)
