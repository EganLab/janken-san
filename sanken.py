from servo import *

while (1):
    value = input("Please enter a string:\n")

    print(int(value))
    runServo(int(value))
    if value == '1':
        break
