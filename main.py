import pyttsx3
import datetime
import threading
import pyjokes
import queue
import time
import random

######################## Put Your Assigned Variables and functions here ...#################################
message_queue = queue.Queue()
############################################################################################################

class Sam():
    ####################### Class Variable and Funtion of Class Sam ... ####################################
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
    #------------------------------------------------------------------------------------------------------#

    @staticmethod
    def say(text):
        print(text)
        Sam.engine.say(text)
        Sam.engine.runAndWait()

    @staticmethod
    def remind():
        try:
            Sam.say("Enter the date and time (HH:MM:SS (24 Hours Format) DD-MM-YYYY) for the reminder: ")
            datestr = input()
            Sam.say("Enter the Reminder Message: ")
            remind_msg = input()
        except ValueError as e :
            Sam.say("Invalid Format , Please try again")
        remind_time =  datetime.datetime.strptime(datestr , "%H:%M:%S %d-%m-%Y")
        
        def process_remind():
             while True:
                now = datetime.datetime.now()
                if now >= remind_time:
                    message_queue.put(f"This is a Reminder. {remind_msg}")
                    break
                time.sleep(1)
        threading.Thread(target=process_remind, daemon=True).start()

    @staticmethod
    def greet():
        Sam.say("System Starting. Hello Boss , I am active and ready for command.")

    @staticmethod
    def rps_game():
        Sam.say("Game Start. Choose Rock, Paper, Scissors.")
        options = ["rock","paper","scissors"]
        while True:
            print("Choose Rock, Paper, Scissors.")
            user = input("Your Choice : ").lower()
            if user not in options:
                Sam.say('Invalid Choice.')
                continue
            comp = random.choice(options)
            Sam.say(f"I Choose {comp}")
            if user == comp :
                Sam.say("It's a Tie.")
            elif (user == "rock" and comp == "scissors") or \
                 (user == "scissors" and comp == "paper") or \
                 (user == "paper" and comp == "rock"):
                Sam.say("You Win !")
            else:
                Sam.say("I win!")
            Sam.say("Wanna play again? : ")
            again = input("yes/no :").lower()
            yes = [ 'yes',"yups","yeah","y" ]
            if any(element in again for element in yes):
                continue
            else:
                Sam.say("Exiting Game.")
                break

    def gtn_game():
        numc = random.choice('1','2','3','4','5','6','7','8','9','10')
        Sam.say("Choose a Integer between 1 to 10")
        while True:
            num = input()
            if num > numc :
                Sam.say("A little less.")
            elif num < numc:
                Sam.say("A lttle more.")
            else:
                Sam.say("Hurray! You got it.")
            Sam.say("Wanna play again? : ")
            again = input("yes/no :").lower()
            yes = [ 'yes',"yups","yeah","y" ]
            if any(element in again for element in yes):
                continue
            else:
                Sam.say("Exiting Game.")
                break

class Process():
    @staticmethod
    def take_command():
        command = input("Type Your Command : ")
        command = command.lower()
        if "remind" in command :
            Sam.remind()
        elif "joke" in command :
            Sam.say(pyjokes.get_joke())
        elif "exit" in command or "quit" in command :
            Sam.say("Good Bye . Quitting System.")
            exit()
        elif "game" in command:
            Sam.say("Which Game do you want to play")
            game = input("1. Rock, Paper, Scissors.\n"
                         "2. Guess the Number.")
            if game == "1":
                Sam.rps_game()
            elif game == "2":
                Sam.gtn_game()
            else:
                Sam.say("Invalid Choice")
        else:
            Sam.say("Command Not Found.")

Sam.greet()
while True:
    while not message_queue.empty():
        msg = message_queue.get()
        Sam.say(msg)

    Process.take_command()
