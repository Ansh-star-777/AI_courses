import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random

def speak(text):
  engine = pyttsx3.init()
  engine.setProperty('rate',150)
  engine.say(text)
  engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand.")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""
def respond_to_user(command):
    if "hi" in command or "hello" in command or "konichiwa" in command:
        speak("hi i am your voice assistent and how can i help you today")
    elif "how are you" in command:
        speak("I am good but i don't have feelings what about you?")
    elif "time" in command:
        time = datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye!")
        return False
    elif "joke" in command:
        speak(random.choice(["To the guy who invented the number 0 thanks for nothing","What do you call a sad strawberry - a blue berry","What do you call a guy who is really loud - mike"]))
    elif "created" in command:
        speak("The code which was created by typing and typer was student ansh")


    else:

        speak("I'm not sure how to help with that.")

    return True



def main():

    speak("Voice assistant activated. Say something!")

    while True:

        command = get_audio()

        if command and not respond_to_user(command):

            break



if __name__ == "__main__":

    main()