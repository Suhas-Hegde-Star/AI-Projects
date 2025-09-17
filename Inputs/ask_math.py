from Functions import maths as m1

def asker_math(want):
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
    else:
        print("Invalid Input")