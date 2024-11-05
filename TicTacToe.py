import time
import random

boardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameLoop = True
again = ''

def updateAllLines():
  global rowOne, rowTwo,  rowThree, columnOne, columnTwo, columnThree, diagonalLeft, diagonalRight, allBoardLines

  rowOne = (boardValues[0], boardValues[1], boardValues[2])
  rowTwo = (boardValues[3], boardValues[4], boardValues[5])
  rowThree = (boardValues[6], boardValues[7], boardValues[8])

  columnOne =  (boardValues[0], boardValues[3], boardValues[6])
  columnTwo =  (boardValues[1], boardValues[4], boardValues[7])
  columnThree = (boardValues[2], boardValues[5], boardValues[8])

  diagonalLeft =  (boardValues[0], boardValues[4], boardValues[8])
  diagonalRight = (boardValues[2], boardValues[4], boardValues[6])

  allBoardLines = (rowOne, rowTwo, rowThree, columnOne, columnTwo, columnThree, diagonalLeft, diagonalRight)

def updatePossibleMoves():
  global possibleMoves

  possibleMoves = [move for move in boardValues if move != 'X' and move != 'O']

def checkWinner():
  global gameLoop

  for lines in allBoardLines:
    if lines == ('O', 'O', 'O'):
      print('\nUser has three O\'s in a line. User wins!')
      gameLoop = False
      time.sleep(5)
      break
    elif lines == ('X', 'X', 'X'):
      print('\nComputer has three X\'s in a line. Computer wins!')
      gameLoop = False
      time.sleep(5)
      break
    elif possibleMoves == []:
      print('\nAll spaces are taken. It\'s a tie!')
      gameLoop = False
      time.sleep(5)
      break

def displayBoard():
  print('+-----------+-----------+-----------+' +
        '\n|           |           |           |' +
        f'\n|     {boardValues[0]}     |     {boardValues[1]}     |     {boardValues[2]}     |' +
        '\n|           |           |           |' +
        '\n+-----------+-----------+-----------+' +        
        '\n|           |           |           |' +
        f'\n|     {boardValues[3]}     |     {boardValues[4]}     |     {boardValues[5]}     |' +
        '\n|           |           |           |' +
        '\n+-----------+-----------+-----------+' +        
        '\n|           |           |           |' +
        f'\n|     {boardValues[6]}     |     {boardValues[7]}     |     {boardValues[8]}     |' +
        '\n|           |           |           |' +
        '\n+-----------+-----------+-----------+')

def computerMove():
  updatePossibleMoves()

  print('\nComputer is choosing a move...')
  time.sleep(3)
  cMove = random.choice(possibleMoves)
  boardValues[cMove - 1] = 'X'
  print(f'Computer chose move {cMove}!')

  updateAllLines()

  displayBoard()

  checkWinner()

def userMove():
  global uMove

  updatePossibleMoves()

  while True:
    uMove = input('\nEnter your move: ')
    if uMove not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
      print('Invalid move. Please enter an integer.')
      continue
    elif int(uMove) in possibleMoves:
      boardValues[int(uMove) - 1] = 'O'
      print(f'User chose move {uMove}!')
      break
    else:
      print('Invalid move. Please enter a number that is not taken.')
      continue

  updateAllLines()

  displayBoard()

  checkWinner()

def gameStart():
  global again

  while True:
    playGame = input(f'\nWould you like to play the game{again}? (Yes/No): ')
    if playGame.lower() == 'yes':
      print('Starting the game...')
      time.sleep(3)
      while gameLoop == True:
        computerMove()
        userMove()
      else:
        again = ' again'
        continue
    elif playGame.lower() == 'no':
      print('Thanks for playing the game!')
      break
    else:
      print('Invalid input. Please enter Yes or No.')
      continue
  
gameStart()