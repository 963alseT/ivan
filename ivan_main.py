import pyaudio
from vosk import KaldiRecognizer, Model
import random
import pyttsx3
from time import ctime
import webbrowser
import time
import cv2
from datetime import datetime
import pyjokes
import wikipedia as wiki
import os
import keyboard

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

cap = cv2.VideoCapture(0)
object_detector = cv2.createBackgroundSubtractorMOG2()

model = Model(r"C:\Users\fionn\Desktop\IVAN\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

x1 = y1 = x2 = y2 = 0
pTime = 0
cTime = time.time()

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()

def respond(voice_data):
    if there_exists(['hey', 'hi', 'hello']):
        greetings = [f"hello, how can I help you"]
        speak(greetings)

    if there_exists(["how are you", "how are you doing"]):
        speak(f"I'm very well, thanks for asking")

    if there_exists(["what are you"]):
        speak("my name is eyevan, i am a virtual assistant built by finn")

    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time_ = ctime().split(" ")[3].split(":")[0:2]
        if time_[0] == "00":
            hours = '12'
        else:
            hours = time_[0]
        minutes = time_[1]
        time_ = f'{hours} {minutes}'
        speak("time you got a watch")
        time.sleep(1)
        speak(time_)

    if there_exists(["what is the date", "what's todays date", "what is todays date"]):
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        speak(current_date)

    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    if there_exists(["play"]):
        search_term = voice_data.split("play")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists(['summarize']):
        search_term = voice_data.split('summarize')[-1]
        speak(wiki.summary(search_term))

    if there_exists(['tell me about']):
        search_term = voice_data.split('about')[-1]
        speak(wiki.summary(search_term, sentences=5))

    if there_exists(["do you like sausages"]):
        speak("I'm a virtual assistant, I cannot taste anything")

    if there_exists(["oasis"]):
        url = "https://media.tenor.com/frzbOpYVggQAAAAC/hell-no-hell-to-the-no.gif"
        webbrowser.get().open(url)

    if there_exists(["bombastic","side eye"]):
        url = f"https://us-tuna-sounds-images.voicemod.net/8ec5a1cf-78d3-4b61-8be9-cd74550c4a9f-1679552231095.jpg"
        webbrowser.get().open(url)

    if there_exists(["do you want to build a snowman"]):
        speak("yes, but I can't")

    if there_exists(["pepe"]):
        url = "https://ichef.bbci.co.uk/news/976/cpsprodpb/16620/production/_91408619_55df76d5-2245-41c1-8031-07a4da3f313f.jpg"
        webbrowser.get().open(url)

    if there_exists(["say a joke", "tell a joke", "tell me a joke"]):
        joke = pyjokes.get_joke(language="en")
        speak(joke)

#, category="chuck"

    if there_exists(["siri", "alexa"]):
        speak("don't talk to me about that fucking piece of shit")

    if there_exists(["roll", "roll a DE twenty"]):
        num = random.randint(1, 20)
        speak(f"rolled a {num}")

    if there_exists(["cheese", "she's"]):
        url = "https://deliciousfoodandwine.com/wp-content/uploads/2015/03/Dollarphotoclub_53674521.jpg"
        webbrowser.get().open(url)

    if there_exists(["star wars"]) and 'tell me about' not in voice_data:
        speak("Do you mean that movie about Darth Spock, with the red sword, who lives on the death star in star trek")
        
    if there_exists(["read a poem", "read me a poem"]):
        speak("Here is a classic poem by prostetnic vogon jeltz")
        speak("Oh freddled gruntbuggly. Thy micturations are to me, As plurdled gabbleblotchits, in midsummer morning, On a lurgid bee. That mordiously hath blurted out, Its earted jurtles, grumbling. Into a rancid festering confectious organ squealer. Now the jurpling slayjid agrocrustles, Are slurping hagrilly up the axlegrurts. And living glupules frart and stipulate, Like jowling meat'ed liverslime. Groop: I implore thee, my foonting turlingdromes. And hooptiously drangle me, With crinkly bindlewurdles, mashurbitries. Or else I shall rend thee in the gobberwarts with my blurglecruncheon. See if I don't!")

    if there_exists(["who are you", "what is your name", "what's your name"]):
        speak("I am Intellegence via artificial nexus, but my friends call me Eyevan, nice to meet you")

    if there_exists(["camera", "Camera"]):
        while True:
            ret, frame = cap.read()
            height, width, _ = frame.shape
            mask = object_detector.apply(frame)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area < 25:
                    cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)

            cv2.imshow("camera", frame)
            #cv2.imshow("mask", mask)
            
            key = cv2.waitKey(1)
            if key == 0:
                break
            if there_exists(["quit"]):
                break
        cap.release()
        cv2.destroyAllWindows()

    if there_exists(["secrets"]):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.get().open(url)

    if there_exists(["thanks", "thank you"]):
        speak("You're welcome")
    
    if there_exists(["exit", "goodbye", "shut up"]):
        speak("going offline")
        
        exit()

while True:
    stream.start_stream()
    data = stream.read(4096, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        voice_data = recognizer.Result()
        #print(voice_data[14:-3])
        respond(voice_data)

        #To Chuck Norris, everything contains a vulnerability.