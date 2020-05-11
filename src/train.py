#! /usr/bin/env python3

import os
import chess.pgn
from state import State

path = '../data/pgn'

def main():
    for filename in os.listdir(path):
        pgn = os.path.join(path, filename)
        pgn = open(pgn)
        game = chess.pgn.read_game(pgn)
        bitb = []

        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
            bb = State(board).serialize()
            bitb.append(bb)

if __name__ == '__main__':
    main()
