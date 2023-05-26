import random
import os.path
import json
random.seed()


def draw_board(board):
    # develop code to draw the board
    print(" {} | {} | {} ".format(board[0][0], board[0][1], board[0][2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[1][0], board[1][1], board[1][2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[2][0], board[2][1], board[2][2]))
    pass


def welcome(board):
    print("Welcome to the game of NoughtsandCrosses.")
    draw_board(board)
    pass


def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    while True:
        try:
            cell = int(input("Enter the cell number to put X in: "))
            row, col = (cell-1)//3, (cell-1) % 3
            if board[row][col] == ' ':
                board[row][col] = 'X'
                return row, col
            else:
                print("Cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
        except IndexError:
            print("Invalid cell number. Try again.")


def choose_computer_move(board):
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col


def check_for_win(board, mark):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark or \
       board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def play_game(board):
    initialise_board(board)
    draw_board(board)
    mark = 'X'
    while True:
        if mark == 'X':
            print("Player's turn: ")
            get_player_move(board)
            draw_board(board)
            if check_for_win(board, mark):
                print("Player wins!")
                return 1
            if check_for_draw(board):
                print("Draw!")
                return 0
            mark = 'O'
        else:
            print("Computer's turn: ")
            choose_computer_move(board)
            draw_board(board)
            if check_for_win(board, mark):
                print("Computer wins!")
                return -1
            if check_for_draw(board):
                print("Draw!")
                return 0
            mark = 'X'


def menu():
    choice = input(
        "Enter '1' to play the game, '2' to save score, '3' to display leaderboard or 'q' to quit: ")
    while choice not in ['1', '2', '3', 'q']:
        choice = input(
            "Invalid option, enter '1' to play the game, '2' to save score, '3' to display leaderboard or 'q' to quit: ")
    return choice


def load_scores():
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as f:
            leaders = json.load(f)
    else:
        leaders = {}
    return leaders
 

def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open("leaderboard.txt", "w") as f:
        json.dump(leaders, f)
    print(f"{name}'s score of {score} has been saved to the leaderboard.")

    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    print("\nLEADERBOARD:")
    print("-------------")
    for i, (player, score) in enumerate(sorted(leaders.items(), key=lambda x: x[1], reverse=True), start=1):
        print(f"{i}. {player}: {score}")
    print("\n")
    pass