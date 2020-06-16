from servo import *
from random import *

robot = 0
man = 0

while (1):
    x = randint(1, 3)
    print("input 1 to 3 :")
    print("1: scissors")
    print("2: rock")
    print("3: paper")

    value = input("Enter your choice: ")
    human = int(value)

    if human == 0:
        break

    # 1 = scissors = GPIO17
    # 2 = rock = GPIO27
    # 3 = paper = GPIO22
    # 17 keo 27 bua 22 la

    mapping = [17, 27, 22]
    naming = ['scissors', 'rock', 'paper']

    runServo(mapping[x-1])

    if human == 1:
        if x == 1:
            print('Robot ' + naming[x-1] +
                  ' x human ' + naming[human-1]+' : Draw')
        elif x == 2:
            print(
                'Robot ' + naming[x-1]+' x human ' + naming[human-1]+' : Robot win')
            robot += 1
        else:
            print(
                'Robot ' + naming[x-1]+' x human ' + naming[human-1]+' : Human win')
            man += 1
    elif human == 2:
        if x == 1:
            print(
                'Robot ' + naming[x-1]+' x human ' + naming[human-1]+' : Human win')
            man += 1
        elif x == 2:
            print('Robot ' + naming[x-1]+' x human ' +
                  naming[human-1]+' : Draw')
        else:
            print(
                'Robot' + naming[x-1]+' x human ' + naming[human-1]+': Robot win')
            robot += 1
    else:
        if x == 1:
            print(
                'Robot ' + naming[x-1]+' x human ' + naming[human-1]+' : Robot win')
            robot += 1
        elif x == 2:
            print(
                'Robot ' + naming[x-1]+' x human ' + naming[human-1]+' : Human win')
            man += 1
        else:
            print('Robot ' + naming[x-1] +
                  ' x human ' + naming[human-1]+' : Draw')

    print('Scoreboard Robot vs Human: %d : %d' % (robot, man))
