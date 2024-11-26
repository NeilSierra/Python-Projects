import random
import time

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def updateBoard():
  global availableMoves, lines
  r1 = [board[0], board[1], board[2]]
  r2 = [board[3], board[4], board[5]]
  r3 = [board[6], board[7], board[8]]
  c1 = [board[0], board[3], board[6]]
  c2 = [board[1], board[4], board[7]]
  c3 = [board[2], board[5], board[8]]
  d1 = [board[0], board[4], board[8]]
  d2 = [board[2], board[4], board[6]]
  lines = [r1, r2, r3, c1, c2, c3, d1, d2]
  print("+ - - - - - + - - - - - + - - - - - +")
  print("|           |           |           |")
  print(f"|     {r1[0]}     |     {r1[1]}     |     {r1[2]}     |")
  print("|           |           |           |")
  print("+ - - - - - + - - - - - + - - - - - +")
  print("|           |           |           |")
  print(f"|     {r2[0]}     |     {r2[1]}     |     {r2[2]}     |")
  print("|           |           |           |")
  print("+ - - - - - + - - - - - + - - - - - +")
  print("|           |           |           |")
  print(f"|     {r3[0]}     |     {r3[1]}     |     {r3[2]}     |")
  print("|           |           |           |")
  print("+ - - - - - + - - - - - + - - - - - +")
  availableMoves = []
  for n in board:
    if n in range(1, 10): availableMoves.append(n)

def checkWin1():
  updateBoard()
  for line in lines:
    if line == ['X', 'X', 'X']:
      print("Computer wins the game!")
      return True
    elif line == ['O', 'O', 'O']:
      print("User wins the game!")
      return True
    elif availableMoves == []:
      print("There are no available moves, its a tie!")
      return True
  return False

def computerMove():
  global board
  print("Computer's turn!")
  time.sleep(2)
  index = random.choice(availableMoves) - 1
  board[index] = 'X'
  checkWin1()

updateBoard()
computerMove()