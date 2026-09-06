from collections import deque

def divideBy2(decNumber):
    remstack = deque()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.append(rem)
        decNumber = decNumber // 2

    binString = ""
    while len(remstack) != 0:
        binString = binString + str(remstack.pop())

    return binString

print("17 to binary is: " + divideBy2(17))
print("45 to binary is: " + divideBy2(45))
print("96 to binary is: " + divideBy2(96))