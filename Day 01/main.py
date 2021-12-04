from data import list

largerNumbers = 0
smallerNumbers = 0
previousNumber = 0
currentNumber = 0

for currentNumber, i in enumerate(list):
    try:
        value = list[currentNumber] + list[currentNumber + 1] + list[currentNumber + 2]
    except:
        print("There were {} larger numbers\nThere were {} smaller numbers".format(largerNumbers, smallerNumbers))
    finally:
        if(previousNumber == 0):
            print(value, "(N/A - no previous sum)")
        elif(value > previousNumber):
            print(value, "(Increased)")
            largerNumbers += 1
        else:
            print(value, "(Decreased)")
            smallerNumbers += 1 
        previousNumber = value