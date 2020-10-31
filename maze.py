import pygame

pygame.init()

#global constants
GAME_WIDTH = 1000
GAME_HEIGHT = 1000
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 100
PLAYER_VELOCITY = 10
PLAYER_X_START = 100
PLAYER_Y_START = 100
#end global constants

window = pygame.display.set_mode((GAME_WIDTH,GAME_HEIGHT))
pygame.display.set_caption("Maze Runner")


class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
    
    def draw(self):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y,self.width, self.height))
        pygame.display.update()


andy = Player(PLAYER_X_START,PLAYER_Y_START,PLAYER_WIDTH,PLAYER_HEIGHT)

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if andy.x < 0 - 100:
            andy.x = GAME_WIDTH
        andy.x -= PLAYER_VELOCITY

    if keys[pygame.K_RIGHT]:
        if andy.x > GAME_WIDTH:
            andy.x = -100
        andy.x += PLAYER_VELOCITY

    if keys[pygame.K_DOWN] and andy.y < GAME_HEIGHT - andy.height:
        andy.y += PLAYER_VELOCITY

    if keys[pygame.K_UP] and andy.y > 0:
        andy.y -= PLAYER_VELOCITY

    window.fill((0,0,0))
    andy.draw()
    pygame.display.update()

pygame.quit()




