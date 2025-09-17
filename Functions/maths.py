import math

def square(num, sq):
    num = int(input("Enter the number "))
    sq = num ** 2
    print("The square of", num, "is", sq)

def root(num, rot):
    num = int(input("Enter the number "))
    rot = math.sqrt(num)
    print("The square root of", num, "is", rot)
def add(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print("The sum of", n1, "and", n2, "is", n2 + n1)

def sub(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    if n2 > n1:
        print("The difference of", n1, "and", n2, "is", n2 - n1)
    else:
        print("The difference of", n1, "and", n2, "is", n1 - n2)

def mul(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print("The product of", n1, "and", n2, "is", n2 * n1)

def div(n1, n2):
    n1 = float(input("Enter the first number "))
    n2 = float(input("Enter the second number "))
    print( n1, "divided by", n2, "is", n1 / n2)