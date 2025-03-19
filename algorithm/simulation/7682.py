import sys


def check(board):
    win_x = 0
    win_o = 0
    cnt_x = board.count('X')
    cnt_o = board.count('O')
    cnt_blank = board.count('.')

    for i in range(0, 9, 3):
        x = 0
        o = 0
        for j in range(i, i + 3):
            if board[j] == 'X':
                x += 1
            elif board[j] == 'O':
                o += 1
        if x == 3:
            win_x += 1
        elif o == 3:
            win_o += 1
    for i in range(3):
        x = 0
        o = 0
        for j in range(i, 9, 3):
            if board[j] == 'X':
                x += 1
            elif board[j] == 'O':
                o += 1
        if x == 3:
            win_x += 1
        elif o == 3:
            win_o += 1
    if board[0] == board[4] == board[8]:
        if board[4] == 'X':
            win_x += 1
        elif board[4] == 'O':
            win_o += 1
    if board[2] == board[4] == board[6]:
        if board[4] == 'X':
            win_x += 1
        elif board[4] == 'O':
            win_o += 1

    if cnt_x - cnt_o != 0 and cnt_x - cnt_o != 1:
        return False
    if win_o == 0 and win_x == 0 and cnt_blank > 0:
        return False
    if win_x >= 1 and win_o >= 1:
        return False
    if win_x > 2 or win_o > 2:
        return False
    if 2 >= win_x >= 1 != cnt_x - cnt_o:
        return False
    if 1 <= win_o <= 2 and cnt_x - cnt_o != 0:
        return False
    return True


while True:
    lst = sys.stdin.readline().strip()
    if lst == "end":
        break
    if check(lst):
        print('valid')
    else:
        print('invalid')
