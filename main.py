import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import smtplib

# Initiating text to speech for Jarvis to interact with us
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    '''
    this function gives the output of the AI through speakers
    '''
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir, I am Jarvis your personal assistant. What do you want me to do")
    if hour >= 12 and hour < 18:
        speak("Good Afternoon sir, I am Jarvis your personal assistant. What do you want me to do")
    if hour >= 18 and hour < 21:
        speak("Good Evening sir, I am Jarvis your personal assistant. What do you want me to do")
    if hour >= 21 and hour < 0:
        print("How is your night going sir,  I am Jarvis your personal assistant. What do you want me to do")


def takeCommand():
    '''
    this function takes the input from the user as speech and turn it into string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}")
        except Exception as e:
            print("Could not listen")
            return "None"
        return query


def pause():
    '''
    this function is for pausing the AI for a specific given number of seconds
    '''
    speak("For how much time sir")
    a = takeCommand()
    a = int(a)
    time.sleep(a)


def email(to, content):
    '''
    this function is used to send emails by speech. Note- enable acces to low apps in gmail
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('person you have to send', to , content)
    server.close()




if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            # using wikipedia to search any topic
            speak("Searching")
            query = query.replace("wikipedi", "")
            summary = wikipedia.summary(query, sentences=3)
            print(summary)
            speak(summary)


        if 'open youtube' in query:
            # opening youtube
            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
            speak("Opened Youtube")


        if 'open google' in query:
            # opening google
            speak("Opening Google")
            webbrowser.open("www.google.com")
            speak("Opend Google")


        if 'open users' in query:
            # opening any file in your computer
            speak("opening users")
            os.startfile(r"C:\Users")


        if 'play music' in query:
            # playing music from a specified folder
            music = r"Specify folder location here"
            songs = os.listdir(music)
            print(songs)
            os.startfile((os.path.join(music, songs[0])))


        if 'open app' in query:  #write the name of your application instead of open app
            # opeing any app by inserting it's file location and then puting \the_app_name.exe
            app = r"the location of your app, find it by right clcking and open file location"  #enter the file location
            os.startfile(app)


        if 'stop' in query:
            # used for pausing the programme
            pause()


        if 'send email to xxx' in query:
            # used to send email
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'person you have to send'
                email(to, content)
                speak("Sent")
            except Exception as e:
                speak("Couldn't send")


        if 'shutdown' in query:
            # used to shut down the computer
            speak("Shutting Down the computer sir")
            os.system('shut down /s /t 1')


        if 'close assistant' in query:
            # used to close the AI
            exit()
