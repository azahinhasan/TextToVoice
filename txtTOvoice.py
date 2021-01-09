import pyttsx3
import speech_recognition as sr
import os

os.system('cmd /c "pip3 install pyttsx3"')
print()
print("-------------------------------------")
print()

engine = pyttsx3.init()

def speak(txt):
    newVoiceRate = 120
    engine.setProperty('rate',newVoiceRate)
    pyttsx3.speak(txt)
    #engine.say(txt)


def TextToVoice():
    print("This Program will help you by reading any text!!")
    print("Paste your Text:")
    print()
    text = input()
    speak(text)

def VoiceToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(sr.Microphone())
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")


def wrongInput():
    print("Wrong Input!")

    
def main():
    option = input("Chose Your Option: 1> TestToVoice , 2> VoiceToText")
    
    if option == 1:
        TextToVoice()
    elif option == 2:
        VoiceToText()
    else:
        wrongInput()
        



if __name__ == "__main__":
    main()