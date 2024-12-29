import time
from datetime import datetime

def set_alarm(alarm_time):
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            print("Alarm ringing!")
            break
        time.sleep(1)

def main():
    alarm_time = input("Enter alarm time in HH:MM:SS format: ")
    print("Alarm set!")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
