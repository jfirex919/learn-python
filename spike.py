import time
from time import sleep

max = 7
odd_number = [1]
for i in range(0,max):
    odd_number.append(odd_number[i]+2)

line_number = [1]
for i in range(0,max):
    line_number.append(line_number[i]+odd_number[i+1])


increment = True
i=0
while True:

    sleep(.1)
    print("-" * line_number[i], end="")
    print()

    if increment:
        i += 1
        if i == max-1:
            increment = False
    elif not increment:
        i -= 1
        if i == 0:
            increment = True

