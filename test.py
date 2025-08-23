import datetime
import time
from features.voice_output  import say

class Time_management:
    @staticmethod
    def set_reminder():
        date_str = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ").strip()
        reminder_msg = input("Enter the reminder message: ")

        try:
            reminder_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("⚠️ Invalid format. Use YYYY-MM-DD HH:MM:SS")
            return

        print(f"✅ Reminder set for: {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("⌛ Waiting...")

        while True:
            now = datetime.datetime.now()
            print(f"[DEBUG] Now: {now.strftime('%H:%M:%S')} | Reminder: {reminder_time.strftime('%H:%M:%S')}")
            
            if now >= reminder_time:
                print("🔔 Reminder time reached!")
                say(reminder_msg)
                break

            time.sleep(1)

Time_management.set_reminder()
