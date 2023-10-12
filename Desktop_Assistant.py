import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)

    engine.runAndWait()

def wishMe():

    hour=int(datetime.datetime.now().hour)

    if hour<=12:
        speak("Good Morning sir!!")

    elif hour>12 and hour<=16:
        speak("Good Afternoon sir!!")

    else:
        speak("Good evening sir!!")

    speak("I am mocco in your service, Please tell me how can i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-us")
        print(f"user said:{query}\n")
    
    except Exception as e:
        print("sorry, Say it again.")
        return "none"
    
    return query


if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            print(result)
            speak(result)
        
        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")
        
        elif "stack overflow" in query:
            webbrowser.open("stackoverflow.com")
            
        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M")
            speak(f"sir, time is {time}")
        
        elif "vs code" in query:
            path="C:\\Users\\sudhir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "play music" in query:
            num=random.randint(1,4)
            music_path="E:\\music"
            songs=os.listdir(music_path)
            os.startfile(os.path.join(music_path ,songs[num]))



        elif "go to sleep" in query:
            speak("ok ,I am going to sleep, call me back in case you need me sir!! ")
            exit()

