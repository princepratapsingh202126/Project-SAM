import datetime
import time
import threading
import pyjokes
from voice_output import say

class Time_management():
    @staticmethod
    def set_reminder():
        date_str = input("Enter the date and time (YYYY-MM-DD HH:MM:SS) for the reminder: ")
        reminder_msg = input("Enter the reminder message: ")
        reminder_time = datetime.datetime.strptime(date_str , "%Y-%m-%d %H:%M:%S")
    
        if datetime.datetime.now() >= reminder_time:
            say(reminder_msg)
            watch = datetime.datetime.now()
            print(watch)
            
Time_management.set_reminder()