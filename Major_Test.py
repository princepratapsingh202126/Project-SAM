import pyttsx3
import datetime
import pyjokes
import os
import webbrowser

engine = pyttsx3.init()
now = datetime.datetime.now()
joke = pyjokes.get_joke()

boss_name = ['sam' , 'prince' , 'mordhwaj']

def say(text):
    engine.setProperty('rate' , 175 )
    engine.say(text)
    engine.runAndWait()

def boss():

    def greeting():
        inputfora1 = ['good', 'fine', 'nice','better','awesome']
        say("Hello Boss, how was your day ?")
        a1 = input("Hello Boss, how was your day ? \n")
        a1 = a1.lower()
        if any(element in a1 for element in inputfora1) :
           say("Well that's good to know....    ")

        else:
            say("Oh , Let me tell you a joke")
            say(joke)
            print(joke)

    def commands():
        
        def play_song():
            os.startfile("song.mp3")
            
        def open_site():
            say("Which Site Boss ?")
            site = input("Which Site Boss ?")
            sitelink = "www.",site,".com"
            webbrowser.open(sitelink)
            

        say("What is the command for me ?")
        command = input("What is the command for me ? \n")
        command = command.lower()
        
        if "song" in command :
            say("playing available song")
            print("Playing availabe song")
            play_song()
            
        elif "open site" in command :
            open_site()
            say ("opening ")
            print("Opening ")
            

        else :
            say ("Sorry , command not found .")


    greeting()
    commands()


    

def guest():
    say("Hello " + a)
    print("Hello " + a)
    

say("What is your name ?")
a = input("What is your name ? \n ")
a = a.lower()

if any(element in a for element in boss_name ):
    
    #taking password
    #say("What is the Password ?")
    #take_password = input("What is the password ?")
    #if take_password == "samishere" :
        boss()
        
    #else:
     #   print("Wrong Password")
      #  say("Go to hell buddy hahaha")

else:
    guest()