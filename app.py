import streamlit as st
import wikipedia
import spacy
import pyttsx3
import speech_recognition as sr

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Initialize TTS engine
engine = pyttsx3.init()

# Set up Streamlit page
st.set_page_config(page_title="NLP Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot using NLP & Wikipedia")
st.markdown("This chatbot uses **spaCy** + **Wikipedia** to understand and answer your questions!")

# Text-to-speech function
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to process and answer question
def get_answer(question):
    doc = nlp(question)
    keywords = " ".join([token.text for token in doc if token.is_alpha and not token.is_stop])
    
    try:
        summary = wikipedia.summary(keywords, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your question is too broad. Try being more specific.\nOptions: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return f"An error occurred: {e}"

# Optional: Voice input
def listen_to_user():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        st.info("🎙️ Listening... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your voice."
    except sr.RequestError:
        return "Voice recognition service is not available."

# Input mode: Text or Voice
input_mode = st.radio("Choose input method:", ("Text", "Voice"))

# Input and response
if input_mode == "Text":
    user_input = st.text_input("Ask me anything:")
    if st.button("Ask"):
        if user_input:
            answer = get_answer(user_input)
            st.markdown(f"**Answer:** {answer}")
            if st.checkbox("🔊 Speak the answer"):
                speak_text(answer)

else:  # Voice input
    if st.button("🎤 Listen and Ask"):
        spoken_input = listen_to_user()
        st.markdown(f"**You said:** {spoken_input}")
        if "Sorry" not in spoken_input:
            answer = get_answer(spoken_input)
            st.markdown(f"**Answer:** {answer}")
            if st.checkbox("🔊 Speak the answer"):
                speak_text(answer)
