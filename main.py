import speech_recognition as sr #recognize speech
import pyttsx3 #text to voice
import pywhatkit#access web(yt in this case)
import datetime
import wikipedia
import pyjokes 





listener = sr.Recognizer() #create a listener that recognizes speech
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    # engine.say('What can i do for you today!')
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source: # use microphone as a source 
            print('listening...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
        if 'cybertron' in command:
            command=command.replace('cybertron',"")
            # print(command)
    except:
     pass
    return command
talk('Initiating cybertron in five four three two one') # just some normal printing statements
talk('cybertron initiated')
print('''░█████╗░██╗░░░██╗██████╗░███████╗██████╗░████████╗██████╗░░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗████╗░██║
██║░░╚═╝░╚████╔╝░██████╦╝█████╗░░██████╔╝░░░██║░░░██████╔╝██║░░██║██╔██╗██║
██║░░██╗░░╚██╔╝░░██╔══██╗██╔══╝░░██╔══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║
╚█████╔╝░░░██║░░░██████╦╝███████╗██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
░╚════╝░░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝''')
talk('What can I do for you today master ')
print('WELCOME')


def  run_cybertron():
    command=take_command()    
    # print(command)
   
    if 'play' in command:
        song=command.replace('play',"")
        talk('playing'+song+'on youtube')
        pywhatkit.playonyt(song)
        print('playing'+song)

    elif 'time' in command: #you can add more features like this using elif!!
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


while True:
   run_cybertron()
