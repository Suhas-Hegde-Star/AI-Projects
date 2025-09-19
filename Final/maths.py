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

def cube(num, cu):
    num = int(input("Enter the number "))
    cu = num ** 3
    print("The cube of", num, "is", cu)

def exponentation(num, ra, ans):
    num = int(input("Enter the base "))
    ra = int(input("Enter the exponent "))
    ans = num ** ra
    print("The number", num, "raised to", ra, "is", ans)

def rect(length, breadth, area):
    length = float(input("Enter the Length of the Rectangle "))
    breadth = float(input("Enter the Breadth of the Rectangle "))
    area = length * breadth
    print("The area of the square with", length, "length", "and", breadth, "breadth is", area)

def tri(o, t, th, waa, area, s):
    while True:
        waa = input("Is the tiangle equlateral(Type y or n) ")
        if waa.lower() == "y":
            o = float(input("Enter the length of the side "))
            s = (o + o + o) / 2
            area = math.sqrt(s * (s - o) * (s - o) * (s - o))
            print("The area of the triangle is:", area)
        elif waa.lower() == "n":
            o = float(input("Enter the length of side a: "))
            t = float(input("Enter the length of side b: "))
            th = float(input("Enter the length of side c: "))
            s = (o + t + th) / 2
            area = math.sqrt(s * (s - o) * (s - t) * (s - th))
            print("The area of the triangle is:", area)
        else:
            print("Invalid Input. Try again ")

def fibonacci(n):
    n = int(input("Till Which fibonacci number do you want? "))
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(fib_sequence)