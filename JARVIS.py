import pyttsx3
import webbrowser
import speech_recognition as sr
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("i am jarvis programmed by rohit singh")

def takeCommand():
    #it takes microphine input from the user and returns string ouoput

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I AM LISTNING")
        speak('i am listening')
        r.pause_threshold =1
        audio=r.listen(source)
        
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query









if __name__ =="__main__" :
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching  wikipedia')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\ROHIT SINGH'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        
        elif 'tell me  something about your developer' in query:
            speak("he is such a nice and humble man")

        elif 'tell me something about yourself' in query:
            speak("i am jarvis,created by rohit singh using python")
            
            


        



        



        



