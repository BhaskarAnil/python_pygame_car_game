# Car Game

# Import pygame and random modules
import pygame
import random

# function to print player vehicle on screen
def player(player_x_position, player_y_position,player_img ):
   screen.blit(player_img, (player_x_position, player_y_position))

# function to print opposite vehicle on screen
def opposite_vehicle(opposite_vehicle_x_position, opposite_vehicle_y_position):
   opposite_vehicle_image = pygame.image.load('elements_images/oppvehicle2.png')
   screen.blit(opposite_vehicle_image, (opposite_vehicle_x_position, opposite_vehicle_y_position))

# function to check collision
def check_for_collision(positions):                  
   player_position_x = positions['player_x_position']
   player_positon_y = positions['player_y_position']
   opposite_car_position_x = positions['opposite_vehicle_x_position']
   opposite_car_position_y = positions['opposite_vehicle_y_position']
   distance_between_player_opposite_car = (((player_position_x - opposite_car_position_x)**2)+((player_positon_y - opposite_car_position_y)**2))**(0.5)
   if distance_between_player_opposite_car < 60 and positions['jump'] == 0 :
      return True
   return False

# function to print guide to play messages
def guide_to_play_messages():
   # fonts 
   small_font = pygame.font.SysFont('Consolas',20)
   font = pygame.font.SysFont('Consolas',32)
   # messages
   print_guide = font.render('Guide : ',True,(255,255,255))
   screen.blit(print_guide,(10,250))
   print_up_to_start = small_font.render('Press (^) To Start', True,(255,255,255))
   screen.blit(print_up_to_start,(10,300))
   print_move_left = small_font.render('Use (<) To Move Left', True,(255,255,255))
   screen.blit(print_move_left,(10,350))
   print_move_right = small_font.render('Use (>) To Move Rightt', True,(255,255,255))
   screen.blit(print_move_right,(10,400))
   print_move_up = small_font.render('Use (^) To Move Forward', True,(255,255,255))
   screen.blit(print_move_up,(10,450))
   print_move_down = small_font.render('Use (v) To Move Backward', True,(255,255,255))
   screen.blit(print_move_down,(10,500))
   print_move_jump = small_font.render('Use Space Bar To Jump', True,(255,255,255))
   screen.blit(print_move_jump,(10,550))

# function to update player movements 
def player_movements(player_x_position, player_y_position):
   player_x_change = 0
   player_y_change = 0
   if event.type == pygame.KEYUP :
      player_x_change = 0
   if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_LEFT :
         if player_x_position > 5 :
            player_x_change = -5
      if event.key == pygame.K_RIGHT :
         if player_x_position < 220 :
            player_x_change = 5
      if event.key == pygame.K_UP :
         if player_y_position > 5 :
            player_y_change = -5
      if event.key == pygame.K_DOWN :
         if player_y_position < 810 :
            player_y_change = 5
   player_x_position += player_x_change
   player_y_position += player_y_change
   return player_x_position,player_y_position

# code to print white lines on road
def lines_on_road():
   line_y_pos = 10
   for line in range(1,12):
      screen.blit(road_lines_img,(100,line_y_pos))
      screen.blit(road_lines_img,(200,line_y_pos))
      line_y_pos = line_y_pos + 90

pygame.init()  # Initialize pygame
pygame.mixer.init()  # Initialize mixer for music
pygame.mixer.music.load("background_sound/car_moving.mp3")  # Load music
screen = pygame.display.set_mode((300,900))  # Set window size
pygame.display.set_caption('Car Game')  # Set title
running = True   # While loop running condition
level = 0  # Set level (speed)
road_lines_img =  pygame.image.load('elements_images/line.png')  # Road lines
clock = pygame.time.Clock()  # Initialize clock

player_x_position =  120  # player initial positions
player_y_position =  800

# fonts 
small_font = pygame.font.SysFont('Consolas',20)
font = pygame.font.SysFont('Consolas',32)

# initial score 
score = 0

# initial jump condition
jump = 0

# collision
collision = True

# Infinite loop 
while running:
   
   # Quit condition (By breaking infinite loop)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      
      # Jump condition
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_SPACE:
            if jump == 0:
                  jump = 35
   
   # If collision occurs this code block executes
   if collision :
      
      screen.fill((0,0,0))  # Fill screen with black background
      pygame.mixer.music.stop()  # Initially music will not be played

      # score
      initial_time = pygame.time.get_ticks()
      print_score = font.render(f'Score : {score}',True,(255,255,255))
      screen.blit(print_score,(60,100))

      # Guide to play messages
      guide_to_play_messages()

      # opposite vehicle initial details
      opposite_vehicle_position_dictionary = {'vehicle_1_1':[0,-1200],'vehicle_1_2':[0,-100],'vehicle_1_3':[0,-900],'vehicle_2_1':[110,-500],'vehicle_2_2':[110,-300],'vehicle_2_3':[110,-500],'vehicle_3_1':[210,-300],'vehicle_3_2':[210,-200],'vehicle_3_3':[210,-1000]}
      
      # start condition
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            collision = False
            score = 0
            pygame.mixer.music.play(-1)  # music starts when car starts

   # If collision not occured this code block will be executed
   else : 

      screen.fill((63,63,63))  # fill with Black Grey color for road

      # code for score 
      print_score = small_font.render(f'score:{score}',True,(255,255,255))
      score = (pygame.time.get_ticks()-initial_time)//1000
      screen.blit(print_score,(10,10))
      level = score//30  # increase speed level with respect to code 
      
      # code for white lines on road
      lines_on_road()
         
      player_img = pygame.image.load('elements_images/player.png') # Load player image
      
      # jump timer and change image when jumping 
      if jump > 0:
         player_img = pygame.image.load('elements_images/player_jump.png')
         for i in range(1):
            jump -= 1
      
      # player movements 
      player_x_position,player_y_position = player_movements(player_x_position, player_y_position)

      # opposite_vehicle movements and collision
      for vehicle in opposite_vehicle_position_dictionary:
         opposite_vehicle_position_dictionary[vehicle][1] += (5 + level)
         if opposite_vehicle_position_dictionary[vehicle][1] > 1000:
            opposite_vehicle_position_dictionary[vehicle][1] = -random.choice([500,1000,1500,2000,2500,3000])
         opposite_vehicle(opposite_vehicle_position_dictionary[vehicle][0],opposite_vehicle_position_dictionary[vehicle][1])
         player(player_x_position, player_y_position,player_img)
         if check_for_collision({'player_x_position':player_x_position, 'player_y_position':player_y_position,'opposite_vehicle_x_position':opposite_vehicle_position_dictionary[vehicle][0],'opposite_vehicle_y_position':opposite_vehicle_position_dictionary[vehicle][1],'jump':jump}):
            collision = True
                        
   pygame.display.update()  # update display   
   clock.tick(60)
