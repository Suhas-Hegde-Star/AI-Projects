from Functions import maths as m1
from ask_______ import Asker_TheWholeOfMyAIProjectIsInHere as H
import sys

def asker_math(want, exe):
    want = input("Enter what you want in Maths (Basic Words)")
    if want .lower() == "addition":
        m1.add
    elif want .lower() == "subtraction":
        m1.sub
    elif want .lower() == "multiplication":
        m1.mul
    elif want .lower() == "division":
        m1.div
    elif want .lower() == "square":
        m1.square
    elif want .lower() == "root" or want .lower() == "square root":
        m1.root
    elif want.lower() == "exponentation":
        m1.exponentation
    elif want.lower() == "cube":
        m1.cube
    elif want.lower() == "home":
        H()
    elif want.lower() == "cube":
        sys.exit
    elif want.lower() == "help":
        exe = input("1. Addition\n2. Subtraction\n3. MUltiplication\n4. Division\n5. Square\n6. Root\n7. Exponentation 8. Cube\n9. Area of Triangle\n10. Area of Rectangle\n11. Fibonacci numbers\n999.Home\n9999. Exit")
        if exe .lower() == "1":
            m1.add
        elif exe .lower() == "2":
            m1.sub
        elif exe .lower() == "3":
            m1.mul
        elif exe .lower() == "4":
            m1.div
        elif exe .lower() == "5":
            m1.square
        elif exe .lower() == "6":
            m1.root
        elif exe.lower() == "7":
            m1.exponentation
        elif exe.lower() == "8":
            m1.cube
        elif exe.lower() == "9":
            m1.rect
        elif exe.lower() == "10":
            m1.tri
        elif exe.lower() == "11":
            m1.fibonacci
        elif exe.lower() == "999":
            H()
        elif exe.lower() == "9999":
            sys.exit
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")