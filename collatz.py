def collatz(number):

    if number % 2 == 0:
        print(number//2,  end=' ')
        return number//2
    else:
        print(3 * number + 1, end=' ')
        return 3*number+1

number = int(input("Enter a number."))
while True:
    number = collatz(number)
    if number == 1:
       break