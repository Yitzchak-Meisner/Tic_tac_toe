def run_game():
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    x_or_o = True
    while True:
        row, col = getInput()
        x_or_o = updateBoard(row, col, x_or_o, board)
        if isHaveAWinner(board):
            if x_or_o:
                print("o is the winner")
            else:
                print("x is the winner")
            break
        if isDraw(board):
            print('draw!!!')
            break


def getInput():
    row = input('enter the row: ')
    col = input('enter the column: ')
    return row, col


def isInputValid(row, col):
    if row.isdigit() and col.isdigit():
        if 1 <= int(row) <= 3 and 1 <= int(col) <= 3:
            return True
        else:
            return False
    else:
        return False


def updateBoard(row, col, x_or_o, board):
    if isInputValid(row, col):
        row, col = int(row), int(col)
        if board[row - 1][col - 1] == '-':
            if x_or_o:
                board[row - 1][col - 1] = 'x'
                x_or_o = False
            else:
                board[row - 1][col - 1] = 'o'
                x_or_o = True
            for i in board:
                print(*i)
        else:
            print('The slot you selected is already taken!!! ')
    else:
        print('the input is not valid!!! ')
    return x_or_o


def isHaveAWinner(board) -> bool:
    return (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != '-') or \
            (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != '-') or \
            (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != '-') or \
            (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != '-') or \
            (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != '-') or \
            (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != '-') or \
            (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != '-') or \
            (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != '-')


def isDraw(board) -> bool:
    return board[0][0] != '-' and board[0][1] != '-' and board[0][2] != '-' and \
            board[1][0] != '-' and board[1][1] != '-' and board[1][2] != '-' and \
            board[2][0] != '-' and board[2][1] != '-' and board[2][2] != '-'


run_game()
