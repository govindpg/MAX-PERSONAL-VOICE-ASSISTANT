import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
import pywhatkit
import subprocess
import ctypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Max: Listening...")
            audio = r.listen(source)
            try:
                query = r.recognize_google(audio)
                print(f"master:{query}")
                return query
                break
            except:
                print("Try Again")


while True:
    query = command().lower()  ## takes user command

    if 'name' in query:
        speak("I am max...Your Digital Employee! ")
    elif 'are you single' in query:
        answers = ['I am in a relationship with wifi', 'No, I love spending time thinking about my crush wifi']
        speak(random.choice(answers))
    elif 'hate' in query:
        speak("I hate when people called me a machine")
    elif 'love' in query:
        speak("I loves to chat with machines like you")
    ### time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak({time})
    elif 'ok' in query:
        speak("ok..")

    ### celebrity
    elif 'who is' in query:
        query = query.replace('who is', "")
        speak(wikipedia.summary(query, 2))

    ### Joke
    elif 'joke' in query:
        speak(pyjokes.get_joke())

    ### news
    elif 'news' in query:
        def trndnews():
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
            page = requests.get(url).json()
            article = page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                print(i + 1, results[i])
            speak("here are the top trending news....!!")
            speak("Do yo want me to read!!!")
            reply = command().lower()
            reply = str(reply)
            if reply == "yes please":
                speak(results)
            else:
                speak('ok!!!!')
                pass

        trndnews()

        ### music
    elif 'music' in query:
        music_dir = 'E:\\music'
        songs = os.listdir(music_dir)
        song = random.randint(0, len(songs) - 1)
        print(songs[song])
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "play" in query:
        song = query.replace('play', '')
        speak('playing'+ song)
        pywhatkit.playonyt(song)
    
    elif "who are you" in query:
        speak("i am max your personal assistant")
    
    elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
    elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

    elif "who made you" in query or "who created you" in query:
            speak("I have been created by Govind.")
    

    elif "why you came to world" in query:
            speak("Thanks to Govind. further It's a secret")

    elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

    elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

    elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

    elif "bye" in query:
        speak("Bye! and Have a nice day ! ")
        break
    

    else:
        speak("I don't understand what you are saying")