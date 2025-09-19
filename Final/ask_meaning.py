from meaning import basic_words_meanings as A

def get_meaning():
    word = input("Enter a word: ").strip().capitalize()
    meaning = A.get(word)
    if meaning:
        print(f"{word}: {meaning}")
    else:
        print("Sorry, that word is not in the dictionary. It is Too Complicated or it is in wrong spelling")