import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random

def speak(audio):
    print(f"Aura: {audio}")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! I am Aura. How may I help you?")
    elif 12 <= hour < 17:
        speak("Good Afternoon! I am Aura. How may I help you?")
    else:
        speak("Good Evening! I am Aura. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:
        print("Say that again please...")
        return "none"

if __name__ == "__main__":
    wish()

    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results, please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("I could not find anything on Wikipedia for that.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("Opening GitHub.")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
            speak("Opening Stack Overflow.")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram.")

        elif 'open spotify' in query:
            webbrowser.open("https://www.spotify.com")
            speak("Opening Spotify.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'tell me a joke' in query or 'joke' in query:
            jokes = [
                "Why don’t skeletons fight each other? Because they don’t have the guts.",
                "I told my computer I needed a break, and it said: No problem, I’ll go to sleep.",
                "Why was the math book sad? Because it had too many problems.",
                "Why don’t eggs tell jokes? Because they’d crack each other up."
            ]
            speak(random.choice(jokes))

        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break
