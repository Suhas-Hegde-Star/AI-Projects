import ask_math

def asker(wanted):
    wanted = input("Enter the topic you want")
    if wanted.lower() == "math":
        ask_math.asker_math
    else:
        print("Invalid Input")