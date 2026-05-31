def initialise_board():
    f_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    return f_board


def display_board(board):
    for i in range(0, 3):
        for j in range(0, 3):
            if j == 2:
                print(board[i][j], end = "\n")
            elif j == 0:
                print("", board[i][j], end = " ¦ ")
            else:
                print(board[i][j], end = " ¦ ")
        print("---¦---¦---")


def turn(board):
    display_board(board)
    name = input("What is your name: ")
    name = name[0].upper()
    num = input("Pick a number on the board [0-8]: ")
    value_num = board[int(num) // 3][int(num) % 3]
    if not name.isalpha():
        print("You have to choose a name")
        turn(board)
    elif not num.isnumeric() or int(num) > 8 or int(num) < 0:
        print("You have to pick a number on the board")
        turn(board)
    elif str(value_num).isalpha():
        print("Stop Cheating and taking other people's spot")
        turn(board)
    else:
        return move(name, int(num), board)


def move(name, num, board):
    board[num // 3][num % 3] = name
    return board


def game():
    board = initialise_board()
    for i in range(1, 10):
        turn(board)
    display_board(board)
    check_winner(board)


def check_winner(board):
    winnerinone = 0
    winnerintwo = 0
    for i in range(0, 3):
        for j in range(0, 3):
            a = board[i][j]
            if j == 0:
                if a == board[i][j+1] == board[i][j+2]:
                    winnerinone += 1
                if a == board[i][j+1] or a == board[i][j+2] or board[i][j+1] == board[i][j+2]:
                    winnerintwo += 1
            if i == 0:
                if a == board[i+1][j] == board[i+2][j]:
                    winnerinone += 1
                if a == board[i+1][j] or a ==  board[i+2][j] or  board[i+1][j] ==  board[i+2][j]:
                    winnerintwo += 1
            if i - j == 2:
                if a == board[i-1][j+1] == board[i-2][j+2]:
                    winnerinone += 1
                if a == board[i-1][j+1] or a == board[i-2][j+2] or board[i-1][j+1] == board[i-2][j+2]:
                    winnerintwo += 1
            if i == j == 0:
                if a == board[i + 1][j + 1] == board[i + 2][j + 2]:
                    winnerinone += 1
                if a == board[i+1][j+1] or a == board[i+2][j+2] or board[i+1][j+1] == board[i+2][j+2]:
                    winnerintwo += 1

    print(f"One person's win in a row/column/diagonal is: {winnerinone}")
    print(f"Two people's win in a row/column/diagonal is: {winnerintwo-winnerinone}")



game()