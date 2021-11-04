import random

def numbertoString(n):
    if n == 0:
        return "rock"
    if n == 1:
        return "paper"
    if n == 2:
        return "scissors"

def logic(a, b):
    type(a)
    type(b)
    compare = a - b + 3
    if compare % 3 == 0:
        return "draw"
    if (compare % 3 + 1) % 2 == 0:
        return "win"
    if (compare % 3) % 2 == 0:
        return "lose"

def game(level):
    gameover = False
    while gameover == False:
        userInputs = 7
        user = True
        try:
            while int(userInputs) < 0 or int(userInputs) > 4:
                userInputs = input("rock(0), paper (1), scissor(2):")
                user = True
        except:
            print("Wrong input!")
            user = False
        computerInput = 0
        if level == "e":
            computerInput = random.randint(0, 2)
        userInput = (int(userInputs))
        if (user == True):
            print("User: " + numbertoString(userInput))
            print("BOT: " + numbertoString(computerInput))
            print(logic(userInput, computerInput))
            userInputs = input("Continue playing [c] or back to menu [m]")
            if (userInputs.lower() == "m"):
                gameover = True
    mainmenu()

def gamemenu():
    print("Choose your playmode")
    print("a ... Against Computer")
    print("b ... Back to the menu")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "a":
        game("a")
    elif usinput == "b":
        mainmenu()
    else:
        print("Wrong input please try again")
        gamemenu()

def mainmenu():
    print("p ... playing th game")
    print("e ... exiting the game")
    usinput = input("Choose your option: \n")
    usinput = usinput.lower()
    if usinput == "e":
        print("Goodbye have a nice day")
    elif usinput == "p":
        gamemenu()
    else:
        print("Wrong input please try again")
        mainmenu()


if __name__ == '__main__':
    # Einleitung
    print()
    print("**************************")
    print("* SCISSOR | ROCK | PAPER *")
    print("**************************")
    print()

    mainmenu()


