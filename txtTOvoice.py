import pyttsx3
import speech_recognition as sr
import os

#os.system('cmd /c "pip3 install pyttsx3"')
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
    print("Paste your Text:")
    print()
    text = input()
    speak(text)
    main()

def VoiceToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source,timeout=8)
        #phrase_time_limit  listen duraning and timeout watihing duration
        #audio = r.listen(source,timeout=3, phrase_time_limit=3)
        #print(r.recognize_google(audio, show_all=True))
        try:
            #text = r.recognize_google(audio, show_all=True)
            text = r.recognize_google(audio)
            print("{}".format(text))
        except:
            print("Sorry could not recognize what you said")
        
        main()


def wrongInput():
    print("Wrong Input!")
    print()

    
def main():
    #print("This Program will help to VoiceToText and TextToVOice")
    print()
    option = input("Chose Your Option: 1> TestToVoice :: 2> VoiceToText : ")
    
    if option == '1':
        TextToVoice()
    elif option == '2':
        VoiceToText()
    else:
        wrongInput()
        main()
        



if __name__ == "__main__":
    main()