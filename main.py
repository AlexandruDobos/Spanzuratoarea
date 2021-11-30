numberOfChances = 5
continueGame = True
semaphore = False
categories = ['MANCARE', 'SPORT', 'TARI']


def initialize():
    print("-----   Introdu categoria [ 0 -", len(categories), "]   -----")
    while True:
        try:
            for i in range(0, len(categories)):
                print("[", i, "]", categories[i])
            userInput = int(input("Ce categorie alegi?: "))
        except ValueError:
            print("Introdu o valoare corecta din cele prezentate.")
            continue
        else:
            if userInput >= 0 and userInput < len(categories):
                return int(userInput)
            else:
                print("--- !!! Introdu o valoare corecta din cele prezentate !!! ---")


def openFile(index):
    name = "categories\\" + categories[index]
    file = open(name, 'r')
    lines = []
    for readLine in file:
        line = readLine.strip()
        lines.append(line)
    return lines


def userContinueGame():
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


def game():
    global continueGame
    while continueGame:
        category = initialize()
        print("Categoria aleasa:", categories[category])
        openFile(category)
        if not userContinueGame():
            continueGame = False


if __name__ == '__main__':
    game()
