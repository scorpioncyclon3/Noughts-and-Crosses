from random import randint
def easy(board, available_moves):
  #picks a random move
  location = randint(0,len(available_moves)-1)
  location = available_moves[location]
  return(location)
