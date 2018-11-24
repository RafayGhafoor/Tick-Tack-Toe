import random
import sys

board = [str(elements) for elements in range(1, 10)]
toss_winner = random.randint(1, 2)  # 1 - player 1; 2 - player 2
toss_loser = 2 if toss_winner == 1 else 1
win_combination = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (2, 4, 6),
    (0, 4, 8),
)


def draw_board():  # this function draws tic tac toe
    print(board[0] + "  |  " + board[1] + "  |  " + board[2])
    print("-------------")
    print(board[3] + "  |  " + board[4] + "  |  " + board[5])
    print("-------------")
    print(board[6] + "  |  " + board[7] + "  |  " + board[8])
    print()


def determine_move(toss=toss_winner):
    return p1_pointer if toss == 1 else p2_pointer


def check_winner(combo):
    if board[combo[0]] == board[combo[1]] == board[combo[2]]:
        if board[combo[0]] == p1_pointer:
            print("Player 1 with pointer {} has won".format(p1_pointer))
            sys.exit()
        else:
            print("Player 2 with pointer {} has won".format(p2_pointer))
            sys.exit()


def make_move(player, pointer):

    draw_board()
    while True:
        index = int(input("Player {}: Choose your index: ".format(player)))
        print()

        if board[index - 1] in "XO":
            print("This place is already taken!\n")
            continue

        board[index - 1] = pointer
        break


if __name__ == "__main__":
    while True:

        p1_pointer = input("Do you want to X or O: ").upper()
        print()

        if p1_pointer not in "XO":
            print("Invalid Input")
            continue
        break

    p2_pointer = "O" if p1_pointer == "X" else "X"
    user_move = determine_move()  # Determines the player pointer which goes first
    print("Player {} has won the toss and will go first".format(toss_winner))

    total_moves = 0

    while True:

        make_move(toss_winner, user_move)

        if total_moves == 4:
            print("The match ended in a draw")
            break

        for moves in win_combination:
            check_winner(moves)

        make_move(
            toss_loser, pointer=p2_pointer if user_move == p1_pointer else p1_pointer
        )

        for moves in win_combination:
            check_winner(moves)

        total_moves += 1
