import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
