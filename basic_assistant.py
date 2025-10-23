import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import webbrowser
import datetime
from deep_translator import GoogleTranslator
import uuid  
import random


import urllib.parse


recognizer = sr.Recognizer()

# speak
def speak(text, language="en"):
    """Speak text aloud with optional translation"""
    print("Assistant:", text)
    if language != "en":
        text = GoogleTranslator(source="auto", target=language).translate(text)

   
    filename = f"voice_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# listen
def listen():
    """Listen to user voice and return text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Network error, please check your internet connection.")
        return ""

def setup_voice_and_language():
    print("\nChoose Language:")
    print("1. English")
    print("2. Hindi")
    print("3. Telugu")

    lang_choice = input("Enter language (1/2/3): ").strip()
    if lang_choice == "1":
        language = "en"
    elif lang_choice == "2":
        language = "hi"
    elif lang_choice == "3":
        language = "te"
    else:
        language = "en"

    return language


jokes = [
    "Why did the computer show up at work late? It had a hard drive!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It forgot to close its Windows!"
]


def run_assistant():
    language = setup_voice_and_language()
    speak("Hello! I am your voice assistant Siri. Say something!", language)

    while True:
        command = listen()
        if not command:
            continue

        
        if "stop" in command or "exit" in command or "quit" in command:
            speak("Okay, goodbye!", language)
            break
        
        elif "thank you" in command:
            speak("You are welcome! Goodbye!", language)
            break
        

        # time and date
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}", language)

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today’s date is {current_date}", language)
            
        elif "day" in command:
            current_day = datetime.datetime.now().strftime("%A")
            speak(f"Today is {current_day}", language)
            
        elif "month" in command:
            current_month = datetime.datetime.now().strftime("%B")
            speak(f"This month is {current_month}", language)   
            
        elif "year" in command:
            current_year = datetime.datetime.now().strftime("%Y")
            speak(f"This year is {current_year}", language) 
            
        elif "what is my name" in command:
            speak("Your name is idk:))", language)
            
        

        # opening apps r websites
        elif "open youtube" in command:
            speak("Opening YouTube", language)
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google", language)
            webbrowser.open("https://www.google.com")

        elif "open chatgpt" in command:
            speak("Opening ChatGPT", language)
            webbrowser.open("https://chat.openai.com")

        elif "open notepad" in command:
            speak("Opening Notepad", language)
            os.system("notepad.exe")

        elif "open calculator" in command:
            speak("Opening Calculator", language)
            os.system("calc.exe")
            
        elif "open command prompt" in command:
            speak("Opening Command Prompt", language)
            os.system("cmd.exe")
            
        elif "open camera" in command:
            speak("Opening Camera", language)
            os.system("start microsoft.windows.camera:")
            
        elif "open settings" in command:
            speak("Opening Settings", language)
            os.system("start ms-settings:") 
        
        elif "open spotify" in command:
            speak("Opening Spotify", language)
            os.system("start spotify:")
            
        elif "open word" in command:
            speak("Opening Microsoft Word", language)
            os.system("start winword:")
            
        elif "open excel" in command:
            speak("Opening Microsoft Excel", language)
            os.system("start excel:")   
            
        elif "open powerpoint" in command:
            speak("Opening Microsoft PowerPoint", language)
            os.system("start powerpnt:")
            
        elif "open edge" in command:
            speak("Opening Microsoft Edge", language)
            os.system("start msedge:")
            
        elif "open firefox" in command:
            speak("Opening Mozilla Firefox", language)
            os.system("start firefox:")
            
        elif "open chrome" in command:
            speak("Opening Google Chrome", language)
            os.system("start chrome:")
            
        elif "open vlc" in command:
            speak("Opening VLC Media Player", language)
            os.system("start vlc:") 
            
        

        elif "call daddy" in command:
            speak("Opening WhatsApp to call Daddy", language)
    
            # use ur own no.
            phone_number = "919876543210" 
            
            
            message = "Hello!!, calling you now!"  
            msg = urllib.parse.quote(message)
            url = f"https://wa.me/{phone_number}?text={msg}"
            # # Open in default browser
            webbrowser.open(url)
            
        
           
        elif "send email to dad" in command:
            speak("Opening email client to send email to Dad", language)
            
            to_email = "ur_email@gmail.com"  
            subject = "Sample"
            body = "Hello Daddy, I am testing my voice assistant.:)"

            
            mailto_link = f"mailto:{to_email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
            webbrowser.open(mailto_link)

        
        elif "your name" in command:
            speak("My name is Siri", language)

        elif "who made you" in command or "who created you" in command:
            speak("I was created by Srija Chinthakunta", language)

        elif "joke" in command:
            joke = random.choice(jokes)
            speak(joke, language)

        elif "how are you" in command:
            speak("I am doing great! How about you?", language)
            
        elif "thank you" in command:
            speak("You are welcome!", language)
            
        elif "good morning" in command:
            speak("Good morning to you too!", language)
            
        elif "good night" in command:
            speak("Good night! Sleep well!", language)
            
        

        elif "what can you do" in command:
            speak("I can assist you with various tasks like telling the time, opening applications, and having a chat!", language)
            
        
            
        elif "tell me a story" in command:
            speak("Once upon a time, in a land far away, there lived a curious programmer who created a helpful voice assistant!", language)
            
        elif "motivate me" in command:
            speak("Believe in yourself! You can achieve anything you set your mind to!", language)
            
        elif "weather" in command:
            speak("I am unable to fetch weather updates right now, but I hope it's all good where you are:)!", language)
            
            
       
        

        # default message
        else:
            speak("I heard you say " + command, language)



if __name__ == "__main__":
    run_assistant()
