import time
"""
asterisk = "*"
space = " "
no_space = 5
no_asterisk = 5
increment = False

try:
    while True:
        time.sleep(0.1)

        print(space * no_space, end="")
        for ast in range(no_asterisk):
            print(asterisk, end="")
        print()

        if not increment:
            no_space -= 1
            if no_space == 0:
                increment = True
        else:
            no_space += 1
            if no_space == 5:
                increment = False
except KeyboardInterrupt:
    print("Goodbye!")
"""
1,4,9,16,25, 36, 49 , 64
3,5,7,9, 11, 13, 15

max_dash = 21
min_dash = 1

dash_count=min_dash
dash="-"
while True:
    print(dash * dash_count+3, end="")
    dash_count += 1
    if dash_count == max_dash:
        dash_count = 0
