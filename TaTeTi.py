import random

def drawBoard(board):
  print(board[7] + '|' + board[8] + '|' + board[9])
  print('-+-+-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-+-+-')
  print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():          
  letter = ''
  while not (letter == 'X' or letter == 'O'):
    print('Que simbolo elegis: X o O?')
    letter = input().upper()
  if letter == 'X':
    return ['X', 'O']
  else:
    return ['O', 'X']

def whoGoesFirst():
  if random.randint(0, 1) == 0:
    return 'computadora'
  else:
    return 'jugador/a'

def makeMove(board, letter, move):
  board[move] = letter

def isWinner(bo, le):
   return ((bo[7] == le and bo[8] == le and bo[9] ==le) or # Across the top
   (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
   (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
   (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
   (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
   (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
   (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
   (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
  boardCopy = []
  for i in board:
    boardCopy.append(i)
  return boardCopy

def isSpaceFree(board, move):
  return board[move] == ' '

def getPlayerMove(board):
  move = ' '
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
    print('Cual es tu proximo movimiento? (1-9)')
    move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
  possibleMoves = []
  for i in movesList:
    if isSpaceFree(board, i):
      possibleMoves.append(i)
  if len(possibleMoves) != 0:
    return random.choice(possibleMoves)
  else:
    return None

def getComputerMove(board, computerLetter):
  if computerLetter == 'X':
    playerLetter = 'O'
  else:
    playerLetter = 'X'
  for i in range(1, 10):
    boardCopy = getBoardCopy(board)
    if isSpaceFree(boardCopy, i):
      makeMove(boardCopy, computerLetter, i)
      if isWinner(boardCopy, computerLetter):
        return i
  for i in range(1, 10):
    boardCopy = getBoardCopy(board)
    if isSpaceFree(boardCopy, i):
      makeMove(boardCopy, playerLetter, i)
      if isWinner(boardCopy, playerLetter):
        return i
  move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
  if move != None:
    return move
  if isSpaceFree(board, 5):
    return 5
  return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
  for i in range(1, 10):
    if isSpaceFree(board, i):
      return False
  return True

def emp(d):
  if (d == True):
    print('Bienvenidos a Ta-Te-Ti!')
    while True:
      theBoard = [' '] * 10
      playerLetter, computerLetter = inputPlayerLetter()
      turn = whoGoesFirst()
      print('El/La ' + turn + ' va primero')
      gameIsPlaying = True
      while gameIsPlaying:
        if turn == 'jugador/a':
          drawBoard(theBoard)
          move = getPlayerMove(theBoard)
          makeMove(theBoard, playerLetter, move)
          if isWinner(theBoard, playerLetter):
            drawBoard(theBoard)
            print('Bien! Ganaste el juego!')
            gameIsPlaying = False
          else:
            if isBoardFull(theBoard):
              drawBoard(theBoard)
              print('Empate!')
              break
            else:
              turn = 'computadora'
        else:
          move = getComputerMove(theBoard, computerLetter)
          makeMove(theBoard, computerLetter, move)
          if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print('¡La computadora te ha derrotado! Tú pierdes.')
            gameIsPlaying = False
          else:
            if isBoardFull(theBoard):
              drawBoard(theBoard)
              print('El juego es un empate!')
              break
            else:
              turn = 'jugador/a'
      print('Queres jugar otra vez? (si o no)')
      if not input().lower().startswith('s'):
        break
