def now():
    from datetime import datetime
    return datetime.today().strftime("%m/%d/%Y %I:%M:%S %p")


def writeToFile(data):
    fh = open('history.txt', 'a')
    fh.write(data + '\n')
    fh.close()


def readFromFile(lineNumber):
    results = ''
    fh = open('history.txt', 'r')
    lines = fh.readlines()
    fh.close()
    lastlines = lines[-int(lineNumber):]
    for line in lastlines:
        results += line
    return results


import random
import os.path
moreDice = 1
lastAmount = 0
lastType = 0
allowedTypes = [4, 6, 8, 10, 12, 20, 100]
menuItems = {'h': 'show roll history', 'r': 'repeat the last amount and type', 'q': 'quit the program'}

while moreDice > 0:
    sum = 0

    menuChoice = (input('How many dice do you need (? for help)? ').lower())

    # we will end the app if they press 0 or q.
    if menuChoice == '0' or menuChoice == 'q':
        break

    # show them all the menu options if they press ?
    if menuChoice == '?':
        for key in menuItems:
            print(key + ': ' + menuItems[key])
        print('\n')
        continue

    # show them roll history for requested returns
    if menuChoice == 'h':
        if os.path.isfile('history.txt'):
            lineNumber = input('How many lines of history do you want? ')
            print('Here is your history: \n' + str(readFromFile(lineNumber)))
        else:
            print('There is currently no history. \n')
        continue

    # setting the dice amount in case they aren't repeating
    diceAmount = menuChoice

    # repeat the last dice amount and dice type they chose
    if menuChoice == 'r':
        if lastType == 0:
            print('There is nothing to repeat. \n')
            continue
        else:
            diceAmount = lastAmount
            diceType = lastType

    # if they didn't say repeat, get a type from them.
    if menuChoice != 'r':
        diceType = int(input(f'Which dice {allowedTypes} do you need? '))

    if diceType not in allowedTypes:
        print('That is not a valid dice type. \n')
        continue

    dice = [random.randint(1, diceType) for _ in range(int(diceAmount))]
    print(dice)
    for diceRolls in dice:
        sum += diceRolls
    print('Sum = ' + str(sum), end='\n \n')
    writeToFile(str(now()) + ': Dice Roll = ' + str(diceAmount) + ' d' + str(diceType) + ': ' + str(dice) + '; Sum: ' + str(sum))

    lastAmount = diceAmount
    lastType = diceType
