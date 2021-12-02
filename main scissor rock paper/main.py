import random
import sqlite3

def connectPlay(dbFile):
    try:
        conn = sqlite3.connect(dbFile)
        playTable = '''Create Table if not exists play(
                id integer Primary Key,
                user text not null, 
                bot text not null, 
                result text not null
                );'''
        cursor = conn.cursor()
        cursor.execute(playTable)
        conn.commit()
        cursor.close()

    except:
        print("Verbinden mit SQL Lite fehlgeschlagen!")
    finally:
        if conn:
            conn.close()

def insert(dbFile, userInput, computerInput, result):
    conn = sqlite3.connect(dbFile)
    sqlStatement = '''Insert into play(user, bot, result) Values(?,?,?)'''
    cursor = conn.cursor()
    game = (userInput, computerInput, result)
    cursor.execute(sqlStatement, game)
    conn.commit()
    return cursor.lastrowid

def selectUserWins(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(result) from play where result = "win"'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("User wins:", row)

def selectComputerWins(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(result) from play where result = "lose"'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Bot wins:", row)

def selectDraw(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(result) from play where result = "draw"'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Draw:", row)

def selectUserRock(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(bot) from play where user = 0'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Bot choose rock:", row)

def selectUserPaper(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(bot) from play where user = 1'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Bot choose paper:", row)

def selectUserScissor(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(bot) from play where user = 2'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Bot choose scissor:", row)

def selectUserSpock(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(bot) from play where user = 3'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Bot choose spock:", row)

def selectUserLizard(dbFile):
    conn = sqlite3.connect(dbFile)
    sqlStatementWins = '''Select count(bot) from play where user = 4'''
    cursor = conn.cursor()
    cursor.execute(sqlStatementWins)
    rows = cursor.fetchall()
    for row in rows:
        print("Bot choose lizard:", row)

def numbertoString(n):
    if n == 0:
        return "rock"
    if n == 1:
        return "paper"
    if n == 2:
        return "scissors"
    if n == 3:
        return "spock"
    if n == 4:
        return "lizard"

def logic(a, b):
    type(a)
    type(b)
    database = r"D:\Schule\5AHWII\SWP Rubner\Scissors_Stone_Paper_Spock_Lizard\RockScissorPaper.db"
    connectPlay(database)
    compare = a - b + 5
    if compare % 5 == 0:
        result = "draw"
        insert(database, a, b, result)
        return result
    if (compare % 5 + 1) % 2 == 0:
        result = "win"
        insert(database, a, b, result)
        return result
    if (compare % 5) % 2 == 0:
        result = "lose"
        insert(database, a, b, result)
        return result

def game(level):
    gameover = False
    while gameover == False:
        userInputs = 8
        user = True
        try:
            while int(userInputs) < 0 or int(userInputs) > 4:
                userInputs = input("rock(0), paper(1), scissor(2), spock(3), lizard(4):")
                user = True
        except:
            print("Wrong input, please try again")
            userInputs = input("rock(0), paper(1), scissor(2), spock(3), lizard(4):")
        computerInput = 0
        if level == "a":
            computerInput = random.randint(0, 4)
        userInput = (int(userInputs))
        if (user == True):
            print("User: " + numbertoString(userInput))
            print("BOT: " + numbertoString(computerInput))
            print(logic(userInput, computerInput))
            database = r"D:\Schule\5AHWII\SWP Rubner\Scissors_Stone_Paper_Spock_Lizard\RockScissorPaper.db"
            selectUserWins(database)
            selectComputerWins(database)
            selectDraw(database)
            selectUserRock(database)
            selectUserPaper(database)
            selectUserScissor(database)
            selectUserSpock(database)
            selectUserLizard(database)
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
        print("Wrong input, please try again")
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
        print("Wrong input, please try again")
        mainmenu()


if __name__ == '__main__':
    print()
    print("**************************")
    print("* SCISSOR | ROCK | PAPER *")
    print("**************************")
    print()
    mainmenu()


