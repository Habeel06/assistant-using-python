import speech_recognition as sr #recognize speech
import pyttsx3 #text to voice
import pywhatkit#access web(ytin this case)
import datetime
import wikipedia
import pyjokes 
from termcolor import colored
import colorama 
colorama.init()




r = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    # engine.say('What can i do for you today!')
    engine.runAndWait()




talk('Initiating cybertron in three two one')
talk('cybertron initiated')
print(colored('''░█████╗░██╗░░░██╗██████╗░███████╗██████╗░████████╗██████╗░░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗████╗░██║
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝░░░██║░░░██████╔╝██║░░██║██╔██╗██║
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝''','red'))
talk('What can I do for you today master ')
print('WELCOME')
while True:
    print(colored("listening...",'yellow'))

    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2) #adjusting
            audio= r.listen(source)#listening
            text1=r.recognize_google(audio)

    def  run_cybertron():
        command=text1
        # print(command)
    
        if 'play' in command:
            song=command.replace('play',"")
            talk('playing'+song+'on youtube')
            pywhatkit.playonyt(song)
            print('playing'+song)

        elif 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk("Current time is"+time)

        elif 'tell me about' in command:
            name=command.replace('tell me about','')
            info =wikipedia.summary(name,2)
            print(info)
            talk(info)


        elif 'who made you' in command:
            talk('Mir Habeel Ahmad made me')


        elif 'i shall go' in command:
            talk('Have a nice day!!!')
            print('bye bye')
            
        elif 'joke' in command:
            talk(pyjokes.get_joke()) 
        
        elif 'close' in command:
            talk('dont be lazy;;to stop me just close the program ')
            print('bye bye')
        
        elif 'help' in command:
            talk('i can do many things ;i can tell you a joke;tell you time,and i can also play music on youtube and much more')
            print('''JOKES
            MUSIC
            TIME AND MUCH MORE ''')

        else:
            talk('Please say the command again')



    run_cybertron()
