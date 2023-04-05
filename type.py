from time import sleep
import sys
def type(text):
    for char in text:
        print(char,end="")
        sys.stdout.flush()
        sleep(0.1)