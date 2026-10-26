# Program to calculate the square of a number

while True:
    n = input ("Please enter a number: (0 to exit) ")
    n = int(n)
    if n == 0:
        break
    print ("square of", n, "is", n*n)

# for positive number

while True:
    n = input ("Please enter a positive number (0 to exit) : ")
    n = int (n)
    if n < 0:
        print ("We only accept positive numbers. Please try again.")
        continue
    if n == 0:
        break
    print ("square of", n, "is", n*n)


# break and continue 

terminate = False
while not terminate:
    number1 = input ("please enter a number : ")
    number1 = int (number1)
    number2 = input ("please enter another number : ")
    number2 = int (number2)
    
while True:
    operation = input ("please enter add/sub or quit to exit : ")
    if operation == "quit":
        terminate = True
        break
    if operation not in ["add", "sub"]:
        print ("Invalid operation. Please try again.")
        continue
    if operation == "add":
        print ("The sum is", number1 + number2)
        break
    if operation == "sub":
        print ("The difference is", number1 - number2)
        break
