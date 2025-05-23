import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone(0) as source:
        print("listening...")
        eel.DisplayMessage("listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 500
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)
    
    try:
        print("recognizing...")
        eel.DisplayMessage("recognizing...")
        query = r.recognize_google(audio)
        print(f"User said {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        return ''
    
    return query.lower()

@eel.expose
def allCommand(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        

        if "open" in query:
            from engine.features import openCommand
            openCommand(query) 
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsapp
            message = ""
            contact_no, name = findContact(query)
            if (contact_no !=0):
                if 'send message' in query:
                    message = "message"
                    speak("What message to send") 
                    query = takecommand()
                elif "phone call" in query:
                    message = "call"
                else:
                    message = "video call"
                whatsapp(contact_no, query, message, name)
                
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    eel.ShowHood()