from random import randint
import copy
from check_for_winner import check_for_winner
def hard(available_moves):
  print()
  def getboard():
    #get board
    with open('board.txt', 'r') as file:
      board = []
      for line in file:
        line = line.strip('\n')
        line = line.split()
        board.append(line)
    return(board)
  
  
  
  #creates a dictionary evaluating each move
  evaluations = {}
  for move in available_moves:
    evaluations[move] = float(0)
  print(evaluations)



  board = getboard()
  #calculates 1 move ahead
  #goes through every possible move
  for available_move1 in available_moves:
    #copies the board over to a temporary list
    temp_board1 = copy.deepcopy(board)
    #simulates the move
    temp_board1[available_move1[1]][available_move1[0]] = 'O'
    #removes the move for future simulations
    available_moves1 = available_moves[::]
    available_moves1.remove(available_move1)
    #checks for a winner
    won, winner = check_for_winner(temp_board1)
    #if the move won
    if won == True:
      evaluations[available_move1] += 1.0
    elif won == False:
      
      #calculates 2 moves ahead
      #goes through every possible move
      for available_move2 in available_moves1:
        #copies the board over to a temporary list
        temp_board2 = copy.deepcopy(temp_board1)
        #simulates the move
        temp_board2[available_move2[1]][available_move2[0]] = 'X'
        #removes the move for future simulations
        available_moves2 = available_moves1[::]
        available_moves2.remove(available_move2)
        #checks for a winner
        won, winner = check_for_winner(temp_board2)
        #if the move won
        if won == True and winner == 'X':
          evaluations[available_move1] -= 0.1
        
        elif won == False:
          
          #calculates 3 moves ahead
          #goes through every possible move
          for available_move3 in available_moves2:
            #copies the board over to a temporary list
            temp_board3 = copy.deepcopy(temp_board2)
            #simulates the move
            temp_board3[available_move3[1]][available_move3[0]] = 'O'
            #removes the move for future simulations
            available_moves3 = available_moves2[::]
            available_moves3.remove(available_move3)
            #checks for a winner
            won, winner = check_for_winner(temp_board3)
            #if the move won
            if won == True:
              evaluations[available_move1] += 0.01
            
            elif won == False:
              
              #calculates 4 moves ahead
              #goes through every possible move
              for available_move4 in available_moves3:
                #copies the board over to a temporary list
                temp_board4 = copy.deepcopy(temp_board3)
                #simulates the move
                temp_board4[available_move4[1]][available_move4[0]] = 'X'
                #removes the move for future simulations
                available_moves4 = available_moves3[::]
                available_moves4.remove(available_move4)
                #checks for a winner
                won, winner = check_for_winner(temp_board4)
                #if the move won
                if won == True and winner == 'X':
                  evaluations[available_move1] -= 0.001

                elif won == False:
                  
                  #calculates 5 moves ahead
                  #goes through every possible move
                  for available_move5 in available_moves4:
                    #copies the board over to a temporary list
                    temp_board5 = copy.deepcopy(temp_board4)
                    #simulates the move
                    temp_board5[available_move5[1]][available_move5[0]] = 'O'
                    #removes the move for future simulations
                    available_moves5 = available_moves4[::]
                    available_moves5.remove(available_move5)
                    #checks for a winner
                    won, winner = check_for_winner(temp_board5)
                    #if the move won
                    if won == True:
                      evaluations[available_move1] += 0.0001
        
                    elif won == False:
                      
                      #calculates 6 moves ahead
                      #goes through every possible move
                      for available_move6 in available_moves5:
                        #copies the board over to a temporary list
                        temp_board6 = copy.deepcopy(temp_board5)
                        #simulates the move
                        temp_board6[available_move6[1]][available_move6[0]] = 'X'
                        #removes the move for future simulations
                        available_moves6 = available_moves5[::]
                        available_moves6.remove(available_move6)
                        #checks for a winner
                        won, winner = check_for_winner(temp_board6)
                        #if the move won
                        if won == True and winner == 'X':
                          evaluations[available_move1] -= 0.00001



  #picks the best moves
  max_val = max(evaluations.values())
  max_keys = []
  for move in evaluations:
    if evaluations[move] == max_val:
      max_keys.append(move)
  #debugging
  print(evaluations)
  print(max_val,'max_val')
  print('max:')
  print(max_keys)
  print('available:')
  print(available_moves)
  print()


  
  #picks a random move
  location = randint(0,len(max_keys)-1)
  location = max_keys[location]
  print('selected',str(location[0]),str(location[1]))
  return(location)
