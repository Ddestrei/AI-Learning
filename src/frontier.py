from state import State
from functions import up, down, right, left


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
        # print(x, y)
        board[x][y] = 'A'
        next_move = 0
        if x + 1 < board_x_size:
            if board[x + 1][y] == ' ' or board[x + 1][y] == 'B':
                self.states.append(
                    down(State(x, y, '', state), board[x + 1][y]))
                next_move += 1

        if x - 1 >= 0:
            if board[x - 1][y] == ' ' or board[x - 1][y] == 'B':
                self.states.append(
                    up(State(x, y, '', state), board[x - 1][y]))
                next_move += 1

        if y + 1 < board_y_size:
            if board[x][y + 1] == ' ' or board[x][y + 1] == 'B':
                self.states.append(
                    right(State(x, y, '', state), board[x][y + 1]))
                next_move += 1

        if y - 1 >= 0:
            if board[x][y - 1] == ' ' or board[x][y - 1] == 'B':
                self.states.append(
                    left(State(x, y, '', state), board[x][y - 1]))
                next_move += 1

        self.states.remove(state)

        return None
