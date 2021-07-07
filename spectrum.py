import pyttsx3
import datetime
import speech_recognition as sr # to take users voice as an input
import wikipedia
import webbrowser
import os #To placy music etc from my pc
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #Help in taking voices available to our computer
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sharuf !!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sharuf !!")
    elif hour >= 18 and hour < 20:
        speak("Good Evening Sharuf !!")
    else:
        speak("Good Night Sharuf !!")
    speak("I am Spectrum sir. Please tell me how may I help you sir")
def takeCommand():
    #takes input from the user from microphone and returns string output
    r = sr.Recognizer() # Recognizer class will help us to recognize the voices from the user
    with sr.Microphone() as source:#We are using microphone as source to recognize the voice of user
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Rcognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:#If any error come during recognization of audio then say that again will be printed on screen
        print("Say that again please")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    if True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)#Searching in wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Sharuf Das\\Music\\songs'
            songs = os.listdir(music_dir)#it will show list of all songs
            print(songs)
            os.startfile(os.path.join(music_dir,songs[22]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            CodePath = "C:\\Users\\Sharuf Das\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CodePath)
     




































































