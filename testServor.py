from servo import *

while (1):
    value = input("Enter your choice: ")
    human = int(value)

    # 1 = scissors = GPIO17
    # 2 = rock = GPIO27
    # 3 = paper = GPIO22
    # 17 keo 27 bua 22 la

    mapping = [22, 27, 17]
    naming = ['paper', 'rock', 'scissors']

    if human == 0:
        runDownServo()
    else:
        runUpServo(mapping[human-1])
