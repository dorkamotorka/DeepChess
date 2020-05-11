import chess
import numpy as np


class State(object):
    def __init__(self, board=chess.Board()):
        assert board.is_valid()
        self.board = board

    def serialize(self):
        BB = np.zeros((64), dtype=np.int8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
                BB[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                        "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[pp.symbol()]
        return BB

if __name__ == '__main__':
    s = State()
