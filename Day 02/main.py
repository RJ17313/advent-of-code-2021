from data import list

horizontalPosition = 0
depth = 0
aim = 0

for i, val in enumerate(list):
    value = val.split(" ")

    if(value[0] == "forward"):
        horizontalPosition += int(value[1])
        depth = depth + aim * int(value[1])
    elif(value[0] == "up"):
        aim -= int(value[1])
    else:
        aim += int(value[1])
finalValue = horizontalPosition * depth
print("Your depth is {}\nYour horizontal position is {}\nMulitplied together, these values are {}\nYour aim was {}".format(depth, horizontalPosition, finalValue, aim))