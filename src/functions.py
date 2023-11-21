import os


def up(state, char):
    return state.go(-1, 0, char)


def down(state, char):
    return state.go(1, 0, char)


def left(state, char):
    return state.go(0, -1, char)


def right(state, char):
    return state.go(0, 1, char)


def read_map():
    board = []
    file = open(os.getcwd().replace("\\src", "\\Maps\\map2.txt"))
    line = file.readline()
    x_start = 0
    y_start = 0
    i = 0
    j = 0
    while line != '':
        buffor = []
        for c in line:
            if c != '\n':
                buffor.append(c)
                if c == 'A':
                    x_start = i
                    y_start = j
            j += 1
        i += 1
        j = 0

        board.append(buffor)
        line = file.readline()
    file.close()
    # print(board)
    return board, x_start, y_start
