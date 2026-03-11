#!/usr/bin/python3


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_player_move(player):
    try:
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None
    except EOFError:
        print("Input ended. Exiting game.")
        return "exit"
    except KeyboardInterrupt:
        print("\nGame interrupted.")
        return "exit"

    if row not in range(3) or col not in range(3):
        print("Invalid move. Row and column must be 0, 1, or 2.")
        return None

    return row, col


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        move = get_player_move(player)
        if move == "exit":
            break
        if move is None:
            continue

        row, col = move
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

if __name__ == "__main__":
    tic_tac_toe()