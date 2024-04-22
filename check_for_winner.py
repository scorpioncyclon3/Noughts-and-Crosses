def check_for_winner(board):
  won = False
  winner = 'None'
  #horizontal lines
  if board[0][0] == board[0][1] == board[0][2] != '-':
    #print('Row 0 win')
    won = True
    winner = board[0][1]
  elif board[1][0] == board[1][1] == board[1][2] != '-':
    #print('Row 1 win')
    won = True
    winner = board[1][1]
  elif board[2][0] == board[2][1] == board[2][2] != '-':
    #print('Row 2 win')
    won = True
    winner = board[2][1]
  #vertical lines
  elif board[0][0] == board[1][0] == board[2][0] != '-':
    #print('Column 0 win')
    won = True
    winner = board[1][0]
  elif board[0][1] == board[1][1] == board[2][1] != '-':
    #print('Column 1 win')
    won = True
    winner = board[1][1]
  elif board[0][2] == board[1][2] == board[2][2] != '-':
    #print('Column 2 win')
    won = True
    winner = board[1][2]
  #diagonals
  elif board[0][0] == board[1][1] == board[2][2] != '-':
    #print('Diagonal win')
    won = True
    winner = board[1][1]
  elif board[0][2] == board[1][1] == board[2][0] != '-':
    #print('Diagonal win')
    won = True
    winner = board[1][1]
  #draw
  if not '-' in board[0] and not '-' in board[1] and not '-' in board[2]:
    won = True
  
  
  
  return(won, winner)
