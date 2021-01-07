import pyttsx3

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


def main():
    print("This Program will help you by reading any text!!")
    print("Paste your Text:")
    print()
    text = input()
    speak(text)



if __name__ == "__main__":
    main()