
# Import package
import pygame  

# Initializes all of the imported Pygame 
# modules (returns a tuple indicating success and failure of initializations)
pygame.init()

# Takes a tuple or a list as its parameter to 
# create a surface (tuple preferred)
dis = pygame.display.set_mode((400,300))

# This is the titile
pygame.display.set_caption('This is my Snake Game!')


# Define some colors
blue = (0, 0, 255)
red =  (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Updates the screen
pygame.display.update()
game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

# Helps track time time
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True   
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10            
            
    x1 = x1 + x1_change
    y1 = y1 + y1_change 
    dis.fill(white)
            
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])    
      
    pygame.display.update()  
    
    clock.tick(30) 

pygame.quit()

# Used to uninitialize everything
quit()