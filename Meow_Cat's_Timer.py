import time
import sys
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print('\r', timer, end='')
        time.sleep(1)
        seconds -=1
    print("\nCountdown finished.")

countdown_time = input("Enter your countdown time in seconds: ")
countdown(int(countdown_time))
