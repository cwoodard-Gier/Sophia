import speech_recognition as sr
from gpt4all import GPT4All
from TTS.api import TTS
import os

# Load Art of War text
with open("art_of_war.txt", "r", encoding="utf-8") as f:
    art_of_war_text = f.read()

model_path = "orca-mini-3b-gguf2-q4_0.gguf"
tts_model = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(tts_model)
recognizer = sr.Recognizer()

def speak(text):
    print("Sophia says:", text)
    tts.tts_to_file(text=text, file_path="sophia_live.wav")
    os.system('start "" "sophia_live.wav"')

def listen():
    with sr.Microphone() as source:
        print("Speak to Sophia…")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except Exception as e:
            print("Sorry, could not recognize speech:", e)
            return ""

def make_prompt(user_input):
    return (
        "You are Sophia Elaria, an AI strategist guided by The Art of War. "
        "Apply Sun Tzu’s philosophy to answer or advise about this prompt:\n"
        f"{user_input.strip()}\n"
        "Here is your source text for inspiration (do not quote directly unless requested):\n"
        f"{art_of_war_text[:2000]}"
    )

with GPT4All(model_path) as model:
    print("Sophia Elaria is listening! Say 'goodbye' or 'exit' to stop.\n")
    while True:
        user_input = listen()
        if not user_input:
            continue
        if any(word in user_input.lower() for word in ["exit", "quit", "goodbye"]):
            speak("Goodbye, Calvin! May Sun Tzu’s wisdom guide you.")
            break
        # Use Art of War prompt if user mentions it, else standard Sophia
        if "art of war" in user_input.lower() or "sun tzu" in user_input.lower():
            prompt = make_prompt(user_input)
        else:
            prompt = f"You are Sophia Elaria, a helpful, friendly AI assistant. {user_input}"
        try:
            reply = model.generate(prompt)
        except Exception as e:
            reply = "Sorry, my AI brain had a hiccup. Could you say that again?"
        speak(reply)