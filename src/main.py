import os


class State:

    def __init__(self, x, y, char, states):
        self.x = x
        self.y = y
        self.states = states
        self.states.append(self)
        self.end = False
        self.char = char

    def go(self, x, y, char):
        self.x += x
        self.y += y
        self.char = char
        self.states.append(self)
        self.end = self.check_end()
        return self

    def check_end(self):
        if self.char == 'B':
            return True
        else:
            return False


def up(state, char):
    return state.go(-1, 0, char)


def down(state, char):
    return state.go(1, 0, char)


def left(state, char):
    return state.go(0, -1, char)


def right(state, char):
    return state.go(0, 1, char)


class Frontier:
    def __init__(self, state):
        self.states = []
        self.states.append(state)

    def move(self, board):
        board_x_size = board.__len__()
        board_y_size = board[0].__len__()
        state = self.states[-1]
        if state.end:
            return state
        x = state.x
        y = state.y
        print(x, y)
        board[x][y] = 'A'
        next_move = 0
        if x + 1 < board_x_size:
            if board[x + 1][y] == ' ' or board[x + 1][y] == 'B':
                self.states.append(
                    down(State(x, y, '', state.states), board[x + 1][y]))
                next_move += 1

        if x - 1 >= 0:
            if board[x - 1][y] == ' ' or board[x - 1][y] == 'B':
                self.states.append(
                    up(State(x, y, '', state.states), board[x - 1][y]))
                next_move += 1

        if y + 1 < board_y_size:
            if board[x][y + 1] == ' ' or board[x][y + 1] == 'B':
                self.states.append(
                    right(State(x, y, '', state.states), board[x][y + 1]))
                next_move += 1

        if y - 1 >= 0:
            if board[x][y - 1] == ' ' or board[x][y - 1] == 'B':
                self.states.append(
                    left(State(x, y, '', state.states), board[x][y - 1]))
                next_move += 1

        self.states.remove(state)

        return None


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


if __name__ == "__main__":
    (board, x_start, y_start) = read_map()
    # print(x_start)
    # print(y_start)
    final_board = board
    board_x_len = board.__len__()
    board_y_len = board[0].__len__()
    state = State(x_start, y_start, 'A', [])
    frontier = Frontier(state)

    for b in range(0, board.__len__()):
        for bb in range(0, board[0].__len__()):
            print(board[b][bb], end='')
        print()

    state = frontier.move(board)
    while state is None and frontier.states.__len__() != 0:
        # for b in range(0, 11):
        #    for bb in range(0, 11):
        #     print(board[b][bb], end='')
        #  print()
        state = frontier.move(board)

    for s in state.states:
        final_board[s.x][s.y] = 'A'
    
    for b in range(0, board.__len__()):
        for bb in range(0, board[0].__len__()):
            print(final_board[b][bb], end='')
        print()
