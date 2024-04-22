import pygame
from random import randint
from check_for_winner import check_for_winner
from Move_Selection.easy import easy
from Move_Selection.medium import medium
from Move_Selection.hard import hard

board = open('board.txt', 'w')
for i in range(0,3):
  board.write('- - -\n')

tile_size = 100
turn = 'X'
clicked = False
available_moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
print(board)



pygame.init()
screen = pygame.display.set_mode((tile_size * 3, tile_size * 3))
pygame.display.set_caption('Noughts and Crosses')
clock = pygame.time.Clock()
running = True
won = False
winner = 'None'
selecting = True
difficulty = 'Easy'



while running == True:
  clock.tick(10)
  #interactions
  for event in pygame.event.get():
    #exit
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      running = False
    #clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
      click_x, click_y = pygame.mouse.get_pos()
      
      clicked = True
      print('Clicked at', click_x, click_y)


  
  if selecting == True:
    difficulties = {
      30: 'EASY',
      90: 'MEDIUM',
      150: 'HARD',
      210: '2 PLAYER'
    }
    screen.fill((50, 50, 55))
    comicsans = pygame.font.Font("COMIC.ttf", 30)
    #creates buttons
    for y in range(30, 270, 60):
      rect = pygame.Rect(50, y, 200, 50)
      #adds rectangles
      pygame.draw.rect(screen, (200, 200, 200), rect)
      pygame.draw.rect(screen, (0, 0, 0), rect, 5)
      #renders the text
      label = comicsans.render(difficulties[y], 1, (0, 0, 0))
      #gets the dimnsions of the text
      text_width = comicsans.size(difficulties[y])[0]
      text_height = comicsans.size(difficulties[y])[1]
      #changes the text position
      x = int(150-(text_width/2))
      y = int(y-((text_height-50)/2))
      #adds the text
      screen.blit(label, (x, y))
    
    if clicked:
      if 50<click_x<250 and 30<click_y<80:
        difficulty = 'Easy'
        selecting = False
      if 50<click_x<250 and 90<click_y<140:
        difficulty = 'Medium'
        selecting = False
      if 50<click_x<250 and 150<click_y<200:
        difficulty = 'Hard'
        selecting = False
      if 50<click_x<250 and 210<click_y<260:
        difficulty = 'TwoPlayer'
        selecting = False
      clicked = False
        
  
  
  elif won == False:
    #gets board
    with open('board.txt', 'r') as file:
      board = []
      for line in file:
        line = line.strip('\n')
        line = line.split()
        board.append(line)
    
    click_x = int(click_x / tile_size)
    click_y = int(click_y / tile_size)
    if turn == 'X':
      #makes sure the user has actually made their selection
      if clicked:
        #checks if the selection is valid
        if (click_x,click_y) in available_moves:
          print('Moved')
          #replaces the selected location with X
          board[click_y][click_x] = 'X'
          #logs that the move has been used up
          available_moves.remove((click_x,click_y))
          turn = 'O'
        else:
          print('Invalid Move')
        clicked = False
    elif turn == 'O':
      #if there are spaces to fill
      if available_moves:
        #easy difficulty
        if difficulty == 'Easy':
          location = easy(board, available_moves)
        #medium difficulty
        if difficulty == 'Medium':
          location = medium(available_moves)
        #hard difficulty
        if difficulty == 'Hard':
          location = hard(available_moves)
          print('location')
          print(location)
        
        
        
        #two player mode
        if difficulty == 'TwoPlayer':
          #makes sure the user has actually made their selection
          if clicked:
            if (click_x,click_y) in available_moves:
              #checks if the selection is valid
              print('Moved')
              #sets the location
              location = (click_x,click_y)
            else:
              print('Invalid Move')
            clicked = False
          #clears the location if the user has not yet clicked
          else:
            location = ()



        #if a location has been selected
        if location:
          print(location)
          #replaces the selected location with the ai's icon
          board[location[1]][location[0]] = 'O'
          #logs that the move has been used up
          available_moves.remove((location[0],location[1]))
          turn = 'X'
    else:
      print(turn)
    
  
    
    won, winner = check_for_winner(board)
  
  
    
    #makes board
    screen.fill((50,50,55))
    #creates boxes
    for x in range(0, tile_size * 3, tile_size):
      for y in range(0, tile_size * 3, tile_size):
        #draws lines
        rect = pygame.Rect(x, y, tile_size, tile_size)
        pygame.draw.rect(screen, (255,255,255), rect, 5)
        #adds noughts
        if board[int(y/100)][int(x/100)] == 'O':
          pygame.draw.circle(screen, (255,255,255), [x+50, y+50], 35, 10)
        #adds crosses
        if board[int(y/100)][int(x/100)] == 'X':
          pygame.draw.line(screen, (255,255,255), [x+25,y+25], [x+75,y+75], width=10)
          pygame.draw.line(screen, (255,255,255), [x+25,y+75], [x+75,y+25], width=10)
  
  
  
    #rejoins board and saves it
    new_board = []
    for line in board:
      new_board.append(' '.join(line))
    replacement = open('board.txt', 'w')
    replacement.write('\n'.join(new_board))
    replacement.close()


  
  else:
    if winner == 'X':
      screen.fill((0,0,0))
      bingus = pygame.image.load("Hi_Bingus.png")
      bingus = pygame.transform.scale(bingus, (tile_size*3,tile_size*3))
      screen.blit(bingus, (0, 0))
      #gets font
      comicsans = pygame.font.Font("COMIC.ttf", 50)
      #renders text
      label = comicsans.render("You win!", 1, (0,0,255))
      screen.blit(label, (50, 100))
    elif winner == 'O':
      screen.fill((0,0,0))
      bingus = pygame.image.load("Hi_Bingus.png")
      bingus = pygame.transform.scale(bingus, (tile_size*3,tile_size*3))
      screen.blit(bingus, (0, 0))
      #gets font
      comicsans = pygame.font.Font("COMIC.ttf", 50)
      #renders text
      label = comicsans.render("You lose :(", 1, (255,0,0))
      screen.blit(label, (25, 100))
    elif winner == 'None':
      screen.fill((0,0,0))
      bingus = pygame.image.load("Hi_Bingus.png")
      bingus = pygame.transform.scale(bingus, (tile_size*3,tile_size*3))
      screen.blit(bingus, (0, 0))
      #gets font
      comicsans = pygame.font.Font("COMIC.ttf", 50)
      #renders text
      label = comicsans.render("Tie!", 1, (0,255,0))
      screen.blit(label, (100, 100))
  
  pygame.display.flip()

pygame.display.quit()
