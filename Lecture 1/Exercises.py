def exercise1():
    string = input("Enter a string: ")
    n = int(input("Enter a number: "))

    print(len(string))
    print(string[n])

def exercise2():
    list = input("Enter a list of numbers separated by spaces: ").split()
    print("The list of numbers is:", list)
    print("The reversed list is:", list[::-1])

def exercise3():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = n1 + n2
    print("The sum of the two numbers is:", n3, " type:", type(n3))