#Countdown timer

print("--------------------------------------------------------------------------")
print("                             COUNTDOWN TIMER                                             ")
print("--------------------------------------------------------------------------")

#import module

import time

#user input
t = int(input("Enter the required time in seconds:"))



#countdown func.

def countdown(t):
    while t:
        mins , secs =divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins , secs)
        print(timer,end='\r')
        time.sleep(1)
        t -= 1
    print("TIME IS UP!")

countdown(t)


