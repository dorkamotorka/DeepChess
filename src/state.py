import chess
import numpy as np


class State(object):
    def __init__(self, board=chess.Board()):
        assert board.is_valid()
        self.board = board

    def edges(self):
        return list(self.board.legal_moves)

    def key(self):
        return (self.board.board_fen(), self.board.turn, self.board.castling_rights, self.board.ep_square)

    def serialize(self):
        bb = np.zeros((64), dtype=np.int8)
        for i in range(64):
            pp = self.board.piece_at(i)
            if pp is not None:
                bb[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                        "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[pp.symbol()]
       
        if self.board.has_queenside_castling_rights(chess.WHITE):
            assert bb[0] == 4
            bb[0] = 7

        if self.board.has_kingside_castling_rights(chess.WHITE):
            assert bb[7] == 4
            bb[7] = 7

        if self.board.has_queenside_castling_rights(chess.BLACK):
            assert bb[56] == 8+4
            bb[56] = 8+7
        if self.board.has_kingside_castling_rights(chess.BLACK):
            assert bb[63] == 8+4
            bb[63] = 8+7


        if self.board.ep_square is not None:
            assert bb[self.board.ep_square] == 0
            bb[self.board.ep_square] = 8
        bb = bb.reshape(8,8)
        
        # binary state
        state = np.zeros((5,8,8), np.uint8)

        state[0] = (bb>>3)&1
        state[1] = (bb>>2)&1
        state[2] = (bb>>1)&1
        state[3] = (bb>>0)&1

        state[4] = (self.board.turn*1.0)

        return state

if __name__ == '__main__':
    s = State()
