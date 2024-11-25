import random
import time

board = [1, 2, 3, 4, 5, 6, 7, "X", 9]
r1 = [board[0], board[1], board[2]]
r2 = [board[3], board[4], board[5]]
r3 = [board[6], board[7], board[8]]
c1 = [board[0], board[3], board[6]]
c2 = [board[1], board[4], board[7]]
c3 = [board[2], board[5], board[8]]
d1 = [board[0], board[4], board[8]]
d2 = [board[2], board[4], board[6]]
lines = [r1, r2, r3, c1, c2, c3, d1, d2]

def updateMoves():
  global availableMoves
  availableMoves = []
  for n in board:
    if n in range(1, 10): availableMoves.append(n)
