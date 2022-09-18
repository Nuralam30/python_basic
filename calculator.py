
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2


while True:
    print("1 Add")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")

    choice = int(input("Enter your selection :"))

    if choice in (1,2,3,4):
        num1 = int(input("Enter first number :"))
        num2 = int(input("Enter second number :"))

        if choice == 1:
            print(num1, '+', num2, '=', add(num1, num2))
        
        elif choice == 2:
            print(num1, '-', num2, '=', sub(num1, num2))

        elif choice == 3:
            print(num1, 'x', num2, '=', mul(num1, num2))

        else:
            print(num1, '/', num2, '=', div(num1, num2))


        next = input("Want to calculate again (yes/no) :")
        if next == 'yes':
            continue
        else:
            break
        
    else:
        print('Is not valid option')

    

