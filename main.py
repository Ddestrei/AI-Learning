##B#
#  #
# ##
# A##


class State:

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.states = []
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
        if x + 1 < board_x_size:
            if board[x + 1][y] == ' ' or board[x + 1][y] == 'B':
                self.states.append(
                    down(State(x, y, ''), board[x + 1][y]))

        if x - 1 >= 0:
            if board[x - 1][y] == ' ' or board[x - 1][y] == 'B':
                self.states.append(
                    up(State(x, y, ''), board[x - 1][y]))

        if y + 1 < board_y_size:
            if board[x][y + 1] == ' ' or board[x][y + 1] == 'B':
                self.states.append(
                    right(State(x, y, ''), board[x][y + 1]))

        if y - 1 >= 0:
            if board[x][y - 1] == ' ' or board[x][y - 1] == 'B':
                self.states.append(
                    left(State(x, y, ''), board[x][y - 1]))

        self.states.remove(state)

        return None


def read_map():
    board = []
    file = open("Maps/map3.txt")
    line = file.readline()
    while line != '':
        buffor = []
        for c in line:
            if c != '\n':
                buffor.append(c)
        board.append(buffor)
        line = file.readline()
    file.close()
    print(board)
    return board


if __name__ == "__main__":
    board = read_map()
    state = State(10, 9, 'A')
    frontier = Frontier(state)

    for b in range(0, 11):
        for bb in range(0, 11):
            print(board[b][bb], end='')
        print()

    state = frontier.move(board)
    while state is None and frontier.states.__len__() != 0:
        #for b in range(0, 11):
        #    for bb in range(0, 11):
           #     print(board[b][bb], end='')
          #  print()
        state = frontier.move(board)

    for b in range(0, 11):
        for bb in range(0, 11):
            print(board[b][bb], end='')
        print()
