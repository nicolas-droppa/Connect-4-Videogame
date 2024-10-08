import os


def clearScreen():
    os.system('cls||clear')


def newLine():
    print("‎")


def printBoard(board, players):
    # Prints the board
    print("+---" * len(board[1]), end="+\n")
    for i in range(len(board)):
        print(". ", end="")
        for j in range(len(board[0])):
            printFigure(board[i][j], players)
            print(" . ", end="")
        print("")
    print("+---" * len(board[1]), end="+")
    print()
    # Prints letters describing columns
    print(" ", end="")
    for i in range(len(board[1])):
        print(" ", end="")
        print(chr(i + 65), end="")
        print("  ", end="")
    print("")
    print("+---" * len(board[1]), end="+")
    print("")


def printFigure(code, players):
    match code:
        case 1:
            print(players[0][0], end="")
        case 2:
            print(players[1][0], end="")
        case _:
            print(" ", end="")


def initBoard():
    rows, cols = (6, 7)
    board = [[0 for i in range(cols)] for j in range(rows)]
    return board


def getNameAndFigure(player):
    clearScreen()
    print("Name for the " + player + " player: ", end="")
    name = input("")
    print("Figure for the " + player + " player: ", end="")
    figure = input("")
    return name, figure


def displayPlayerInMenu(num, players):
    print(num, end="")
    print(".", end="")
    if not players[num-1][0] == " ":
        print(" [ ", end="")
        print(players[num-1][0], end=" ] ")
        print(players[num-1][1], end="")
    print("")


def displayPlayerInEnd(num, players):
    if not players[num-1][0] == " ":
        print(" [ ", end="")
        print(players[num-1][0], end=" ] ")
        print(players[num-1][1], end="")
    print("")


def displayOptions(players):
    print("1. Setup player 1")
    print("2. Setup player 2")
    if checkSetPlayers(players):
        print("3. Start the game")
    else:
        print("[!] 3. Start the game [You have not set-up players correctly]")
    print("4. Start game with default players")
    print("5. Quit")


def displayMenu(players):
    clearScreen()
    print("Players:")
    displayPlayerInMenu(1, players)
    displayPlayerInMenu(2, players)
    newLine()
    print("Options:")
    displayOptions(players)


def takeInput(validInput):
    while True:
        newLine()
        choice = input("Enter your choice: ")
        if choice in validInput:
            return choice
        else:
            print("Invalid input! [ " + choice + " ]")


def menuSelection(input, players):
    match input:
        case "1":
            players[0][1], players[0][0] = getNameAndFigure("first")
            return False
        case "2":
            players[1][1], players[1][0] = getNameAndFigure("second")
            return False
        case "3":
            return True
        case "4":
            [[players[0][1], players[0][0]], [players[1][1], players[1][0]]] = [["Player 1", "X"], ["Player 2", "O"]]
            return True
        case "5":
            quit(0)


def checkSetPlayers(players):
    if players[0][0] == " " or players[0][1] == " ":
        return False
    elif players[1][0] == " " or players[1][1] == " ":
        return False
    else:
        return True


def initGame():
    players = [[" ", " "], [" ", " "]]
    turn = 0
    while True:
        displayMenu(players)
        if menuSelection(takeInput(["1", "2", "3", "4", "5"]), players):
            if checkSetPlayers(players):
                return turn, players


def currentPlayerTurn(turn, players):
    clearScreen()
    if turn % 2 == 0:
        print("[ " + players[0][0] + " ] " + players[0][1] + "'s turn:")
    else:
        print("[ " + players[1][0] + " ] " + players[1][1] + "'s turn:")


def refactorInput(input):
    match input:
        case 'a' | 'A':
            return 0
        case 'b' | 'B':
            return 1
        case 'c' | 'C':
            return 2
        case 'd' | 'D':
            return 3
        case 'e' | 'E':
            return 4
        case 'f' | 'F':
            return 5
        case 'g' | 'G':
            return 6


def playerMove(move, turn, board, players):
    for i in range(5, -1, -1):
        if board[i][move] == 0:
            if turn % 2 == 0:
                board[i][move] = 1
            else:
                board[i][move] = 2
            if checkForWin(i, move, board):
                endGame(turn % 2, board, players)
            return True
    return False


def checkForWin(pos1, pos2, board):
    (posX, posY, pos1copy, pos2copy) = (0, 0, 0, 0)
    for direction in range(4):
        # using grid like system with x and y-axis
        # top left -> [0][0]
        # top right -> [0][6]
        # bottom left -> [5][0]
        # bottom right -> [5][6]
        # to represent where to check next symbol in row
        match direction:
            case 0:
                posX = -1
                posY = 0
            case 1:
                posX = -1
                posY = -1
            case 2:
                posX = 0
                posY = -1
            case 3:
                posX = 1
                posY = -1

        pos1copy = pos1
        pos2copy = pos2
        for i in range(0, 4, 1):
            sameInRow = 0
            for j in range(0, 4, 1):
                change1 = posX * i
                change2 = posY * i
                if pos1copy + posX * j - change1 < 0 or pos1copy + posX * j - change1 > 5:
                    break
                elif pos2copy + posY * j - change2 < 0 or pos2copy + posY * j - change2 > 6:
                    break
                else:
                    if board[pos1copy][pos2copy] == board[pos1copy + posX * j - change1][pos2copy + posY * j - change2]:
                        sameInRow = sameInRow + 1
                        if sameInRow == 4:
                            return True
                    else:
                        break
    return False



def endGame(end, board, players):
    clearScreen()
    printBoard(board, players)
    newLine()
    match end:
        case 0:  # player 1 won
            print(" Result : ")
            displayPlayerInEnd(1, players)
            print(" won the game!")
        case 1:  # player 2 won
            print(" Result : ")
            displayPlayerInEnd(2, players)
            print(" won the game!")
        case 2:  # draw
            print(" Result : It's a draw!")
            displayPlayerInEnd(1, players)
            displayPlayerInEnd(2, players)
    quit(0)


def startGame():
    turn, players = initGame()
    playingBoard = initBoard()

    while True:
        clearScreen()
        currentPlayerTurn(turn, players)
        printBoard(playingBoard, players)
        if turn > 41:
            endGame(2, playingBoard, players)  # draw
        if playerMove(
            refactorInput(
                takeInput(
                    ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g"]
                )
            ), turn, playingBoard, players):
            turn = turn + 1


startGame()