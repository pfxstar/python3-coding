import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((375, 275, 50, 50))

pygame.display.set_caption("Jumpy")

run = True
while run:

  screen.fill((0, 0, 0))
    
  pygame.draw.rect(screen, (209, 135, 255), player)

  key = pygame.key.get_pressed()
  if key[pygame.K_a] == True:
    player.move_ip(-1, 0)
  elif key[pygame.K_d] == True:
    player.move_ip(1, 0)
  elif key[pygame.K_w] == True:
    player.move_ip(0, -1)
  elif key[pygame.K_s] == True:
    player.move_ip(0, 1)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  pygame.display.update()

pygame.quit()