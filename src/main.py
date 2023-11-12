from state import State
from frontier import Frontier
from functions import read_map

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

    print()

    for b in range(0, board.__len__()):
        for bb in range(0, board[0].__len__()):
            print(board[b][bb], end='')
        print()
