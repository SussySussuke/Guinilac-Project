#Create a 3 question that you want to ask your weak AI. Then program it to asnwer accordingly. Name your AI as Jacob.
import pyttsx3
import speech_recognition as sr
import pyaudio


def talk(txt):
    print(txt)
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.say(txt)
    engine.runAndWait()

running = True
tempUserN = ""
listener = sr.Recognizer()

def take_question(UserName):
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening..")
            voice = listener.listen(source)
            print("1")
            command = listener.recognize_google(voice)
            print("2")
            command = command.lower()
            print("3")
            if "jacob" in command:
                command = command.replace('jacob','')
                print("Command Read: "+ command)
                if 'name' in command and 'your' in command:
                    talk("My name is Jacob and AI version 6.9")
                elif 'how' in command and ('quit' in command or 'exit' in command):
                    talk("just say \"quit\"")
                elif ' quit' == command:
                    UserName = "QUIT"
                elif 'call me' in command:
                    command = command.replace('call me', '')
                    if command == "":
                        talk("Sorry didn't quiet get that...")
                    else:
                        UserName = command
                        talk("Alright, " + UserName)
                elif 'who annoys' in command and ('me' in command or 'you' in command):
                    talk("Naggers like Peter ")
                    print("O_O")
                elif 'what' in command and 'my name' in command:
                    if UserName == "":
                        talk("sorry, I don't know yet say `call me` then name, so I would know")
                    else:
                        talk("You're "+str(UserName))
                elif 'i love you' in command:
                    talk("Jacobs loves you")
                    print("<3")
                elif 'peter' in command and 'say' in command and 'what' in command:
                    talk("Luh!")
                elif '2 + 2' in command:
                    talk("is 4! minus 1 that's 3 quick MATH!")
            elif "quit" in command:
                UserName = "QUIT"
            else:
                print("Mic Read: "+command)
                talk("Please say \"Jacob\" to call me")
    except Exception as e:
        print(e)
        command = "No Mic"
        print(command)

    return UserName



talk("Hello I am Jacob, a \"SIMPLE\" not weak AI. just call my name to ask questions!")

while True:
    tempUserN = take_question(tempUserN)
    if tempUserN == "QUIT":
        talk("Goodbye")
        break
