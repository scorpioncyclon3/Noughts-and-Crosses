from random import randint
from check_for_winner import check_for_winner
def medium(available_moves):
  def getboard():
    #get board
    with open('board.txt', 'r') as file:
      board = []
      for line in file:
        line = line.strip('\n')
        line = line.split()
        board.append(line)
    return(board)


  
  #goes through each possible option to check for immediate wins
  for available_move in available_moves:
    board = getboard()
    temp_board = board
    temp_board[available_move[1]][available_move[0]] = 'O'
    won, winner = check_for_winner(temp_board)
    if won == True:
      print('winning move o')
      return(available_move)


  
  #goes through each possible option to check for immediate loss
  for available_move in available_moves:
    board = getboard()
    temp_board = board
    temp_board[available_move[1]][available_move[0]] = 'X'
    won, winner = check_for_winner(temp_board)
    if won == True:
      print('blocking x win')
      return(available_move)


  
  #picks a random move
  location = randint(0,len(available_moves)-1)
  location = available_moves[location]
  return(location)
