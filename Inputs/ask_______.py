import ask_math
import sys
from ask_______ import asker
from ask_______ import Asker_TheWholeOfMyAIProjectIsInHere as H
from Functions import meaning

class Asker_TheWholeOfMyAIProjectIsInHere():
    def asker(wanted, exe):
        wanted = input("Enter the topic you want")
        if wanted.lower() == "math":
            ask_math.asker_math
        elif wanted.lower() == "maths":
            ask_math.asker_math
        elif wanted.lower() == "mathamatics":
            ask_math.asker_math
        elif wanted.lower() == "mathamatic":
            ask_math.asker_math
        elif wanted.lower() == "i want to do math":
            ask_math.asker_math
        elif wanted.lower() == "i want to do maths":
            ask_math.asker_math
        elif wanted.lower() == "i want to do mathamatics":
            ask_math.asker_math
        elif wanted.lower() == "i want to do mathamatic":
            ask_math.asker_math
        elif wanted.lower() == "want to do math":
            ask_math.asker_math
        elif wanted.lower() == "want to do maths":
            ask_math.asker_math
        elif wanted.lower() == "want to do mathamatics":
            ask_math.asker_math
        elif wanted.lower() == "want to do mathamatic":
            ask_math.asker_math
        elif wanted.lower() == "meanings":
            if __name__ == "__main__":
                meaning.get_meaning()
        elif wanted.lower() == "home":
            H()
        elif wanted.lower() == "exit":
            sys.exit
        elif wanted.lower() == "help":
            exe = input("1. Math\n2. Meaning\n999. Home\n9999.Exit")
            if exe == "1":
                ask_math.asker_math
            elif exe == "2":
                if __name__ == "__main__":
                    meaning.get_meaning()
            elif exe == "999":
                asker(wanted = any, exe = any)
            elif exe == "9999":
                sys.exit
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    asker(wanted = any, exe = any)