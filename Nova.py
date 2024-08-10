import speech_recognition as sr
import webbrowser 
import pyttsx3 
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()
newsapikey = "0a0c359ddf1c42e3aa67d65bd757ccbf"

def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()

def aiprocess(command):
    client = OpenAI(
    api_key = "YOUR openAI API KEY",
)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named nova, skilled in general tasks like alexa and google."},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def speak(text):
    tts =  gTTS(text)
    tts.save('hey.mp3')
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the MP3 file
    pygame.mixer.music.load('hey.mp3')
    # Play the MP3 file
    pygame.mixer.music.play()
    # Wait for the music to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove('hey.mp3')
    
def processcomand(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=0a0c359ddf1c42e3aa67d65bd757ccbf")
        if r.status_code == 200:
            data = r.json()
            headlines = [article['title'] for article in data['articles']]
            for idx,headlines in enumerate(headlines, 1):
                speak(headlines)
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")     
    else:
        output = aiprocess(c)
        speak(output)
        
if __name__ == "__main__" :
    speak("Hi i am nova, How may i help you")
    while True:
        #listen for the wake word "nova"
        #obtain audio from the microphone
        r = sr.Recognizer()

        #recognize speech usiing Sphinx
        print("Recognizing....!")
        try:
            with sr.Microphone() as source :
                print("Please say something")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "nova"):
                speak("Yes")
                #Listen for command
                with sr.Microphone() as source :
                    print("nova is active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcomand(command)
        
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that")
        except Exception as e:
            print("Error; {0}".format(e))