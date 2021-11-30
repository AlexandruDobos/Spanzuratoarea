import random

numberOfChances = 0
continueGame = True
semaphore = False
categories = ['MANCARE', 'SPORT', 'TARI']

def Initialize():
    while True:
        print(f"Introdu categoria: {' | '.join(categories)}")
        userInput = input()
        if userInput.upper() in categories:
            return userInput
        else:
            print("!!! Introdu o categorie corecta !!!")


def OpenFile(index):
    name = "categories\\" + index
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
        print("Categoria aleasa:", category)
        words = OpenFile(category)
        word = list(ChooseRandomWord(words))
        SetNumberOfChances(word)
        print(f"Jocul incepe. Ai {numberOfChances} incercari.\n")

        guessWord = list("_" * len(word))
        copyNumberOfChances = numberOfChances
        while numberOfChances > 0:
            print(*guessWord, "\n")
            userLetterInput = input("Introdu o litera: ").upper()
            if len(userLetterInput) == 1:
                if userLetterInput.isalpha():
                    if userLetterInput not in word:
                        numberOfChances = numberOfChances - 1
                    else:
                        for position, character in enumerate(word):
                            if character == userLetterInput:
                                guessWord[position] = userLetterInput
            else:
                numberOfChances = numberOfChances - 1
            if guessWord == word:
                print("Felicitari, ai castigat.\n")
                print(f"Cuvantul a fost {''.join(word)}. Ai gresit de {copyNumberOfChances - numberOfChances} ori in incercarea de a ghici cuvantul.")
                numberOfChances = 0
            else:
                print(f"\nMai ai {numberOfChances} incercari. \n")
        if not UserContinueGame():
            continueGame = False


if __name__ == '__main__':
    Game()
