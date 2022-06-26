import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyaudio
# import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I'm Jarvis, How can i help you?")


def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 150
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language= 'en-in')
        print(f">>> {query}\n")

    except Exception as e:
        # print(e)
        print("I didn't get it sir. Can you please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = Command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak('According to wikipedia')
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            webbrowser.open("instagrm.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {strTime}")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\ranas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'my calculater' in query:
            cal_path = "C:\\Users\\ranas\\OneDrive\\Desktop\\My programs\\Calculator.py"
            os.startfile(cal_path)
        
        elif 'jokes' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        # elif 'youtube' in query:
        #     talk('playing')
        #     pywhatkit.playonyt(command)
        
        elif 'quit' in query:
            exit

        else:
            speak("I didn't get it sir. Could you please repeat...")
