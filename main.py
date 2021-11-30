import random

numberOfChances = 0
continueGame = True
semaphore = False
categories = ['MANCARE', 'SPORT', 'TARI']


def Initialize():
    print("-----   Introdu categoria [ 0 -", len(categories) - 1, "]   -----")
    while True:
        try:
            for i in range(0, len(categories)):
                print(f"[{i}] {categories[i]}")
            userInput = int(input("Ce categorie alegi?: "))
        except ValueError:
            print("Introdu o valoare corecta din cele prezentate.")
            continue
        else:
            if 0 <= userInput < len(categories):
                return int(userInput)
            else:
                print("--- !!! Introdu o valoare corecta din cele prezentate !!! ---")


def OpenFile(index):
    name = "categories\\" + categories[index]
    file = open(name, 'r')
    lines = []
    for readLine in file:
        line = readLine.strip()
        lines.append(line)
    return lines


def UserContinueGame():
    userInput = input("Doresti sa incepi un joc nou? DA / NU: ")
    while True:
        if not (
                userInput == "DA" or userInput == "NU" or userInput == "da" or userInput == "nu" or userInput == "Da" or userInput == "Nu"):
            print("--- !!! INTRODU O VALOARE CORECTA !!! ---")
            userInput = input("Doresti sa incepi un joc nou? DA / NU: ")
        else:
            if userInput == "DA" or userInput == "da" or userInput == "Da":
                return True
            else:
                return False


def ChooseRandomWord(words):
    global numberOfChances
    word = words[random.randint(0, len(words) - 1)]
    print(f"Cuvantul ales: {word}. Lungimea cuvantului ales: {len(word)}")
    return word


def SetNumberOfChances(word):
    global numberOfChances
    numberOfChances = len(word)


def Game():
    global continueGame
    global numberOfChances
    while continueGame:
        category = Initialize()
        print("Categoria aleasa:", categories[category])
        words = OpenFile(category)
        word = list(ChooseRandomWord(words))
        SetNumberOfChances(word)
        print(f"Jocul incepe. Ai {numberOfChances} incercari.\n")

        guessWord = list("_" * len(word))
        while numberOfChances > 0:
            print(*guessWord, "\n")
            userLetterInput = input("Introdu o litera: ").upper()
            if len(userLetterInput) == 1:
                if userLetterInput.isalpha():
                    if userLetterInput not in word:
                        numberOfChances = numberOfChances - 1
                    else:
                        for pos, char in enumerate(word):
                            if char == userLetterInput:
                                guessWord[pos] = userLetterInput
            else:
                numberOfChances = numberOfChances - 1
            if guessWord == word:
                print("Felicitari, ai castigat.\n")
                numberOfChances = 0
            else:
                print(f"\nMai ai {numberOfChances} incercari. \n")
        if not UserContinueGame():
            continueGame = False


if __name__ == '__main__':
    Game()
