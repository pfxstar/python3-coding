import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((143, 212, 255), (0, 0, 1280, 360))
screen.fill((112, 69, 0), (0, 360, 1280, 360))

player = pygame.image.load("../assets/sisi.png")
game_font = pygame.font.Font("../assets/SunnyspellsRegular-MV9ze.otf")
pygame.display.set_caption("Sisi's Super Sparkle Adventure Minigame")

class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    def update(self):
        self.rect.x -= 1

game_speed = 5

ground = pygame.image.load("../assets/Ground.png")
ground = pygame.transform.scale(ground, (1280, 20))
ground_x = 0
cloud = pygame.image.load("../assets/cloud.png")
cloud = pygame.transform.scale(cloud, (200, 80))

cloud_group = pygame.sprite.Group()

CLOUD_EVENT = pygame.USEREVENT
pygame.time.set_timer(CLOUD_EVENT, 3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == CLOUD_EVENT:
            current_cloud_y = random.randint(50, 300)
            current_cloud = Cloud(cloud, 1380, current_cloud_y)
            cloud_group.add(current_cloud)

    cloud_group.update()
    cloud_group.draw(screen)

    ground_x -= game_speed

    screen.blit(ground, (ground_x, 360))
    screen.blit(ground, (ground_x + 1280, 360))

    if ground_x <= - 1280:
        ground_x = 0

    clock.tick(120)
    pygame.display.update()