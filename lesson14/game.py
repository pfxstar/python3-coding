import pygame
import sys
import random


# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_HALF = 720 / 2
PLAYER_WIDTH = 80
PLAYER_HEIGHT = 100
PLAYER_DUCKING_WIDTH = 110
PLAYER_DUCKING_HEIGHT = 60
PLAYER_GROUND_DIFF = 40
PLAYER_GROUND_DIFF = 40
OSTACLE_WIDTH = 50
OSTACLE_HEIGHT = 50
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
CLOUD_WIDTH = 200
CLOUD_HEIGHT = 80
CLOUD_EVENT_INTERVAL = 3000
VELOCITY = 50
GRAVITY = 4.5
GROUND_HEIGHT = 50
GROUND_TOP_Y = SCREEN_HALF - GROUND_HEIGHT
GROUND_BOTTOM_Y = SCREEN_HALF + GROUND_HEIGHT
GAME_SPEED_INIT = 5
GAME_SPEED_INCREMENT = 0.000001 
FONT_SIZE = 24

# Initial game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Sisi's Super Sparkle Adventure Minigame")
game_font = pygame.font.Font("../assets/SunnyspellsRegular-MV9ze.otf", FONT_SIZE)

# Classes
class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.x -= 1


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.running_sprites = []
        self.ducking_sprites = []

        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("../assets/player1.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("../assets/player2.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)))

        self.ducking_sprites.append(pygame.transform.scale(
            # pygame.image.load(f"../assets/PlayerDucking1.png"), (110, 60)))
            pygame.image.load("../assets/player1.png"), (PLAYER_DUCKING_WIDTH, PLAYER_DUCKING_HEIGHT)))
        self.ducking_sprites.append(pygame.transform.scale(
            # pygame.image.load(f"../assets/PlayerDucking2.png"), (110, 60)))
            pygame.image.load("../assets/player2.png"), (PLAYER_DUCKING_WIDTH, PLAYER_DUCKING_HEIGHT)))

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = VELOCITY
        self.gravity = GRAVITY
        self.ducking = False

    def jump(self):
        jump_sfx.play()
        if self.rect.centery >= SCREEN_HALF:
            while self.rect.centery - self.velocity > PLAYER_GROUND_DIFF:
                self.rect.centery -= 1

    def duck(self):
        self.ducking = True
        self.rect.centery = SCREEN_HALF + GROUND_HEIGHT

    def unduck(self):
        self.ducking = False
        self.rect.centery = SCREEN_HALF

    def apply_gravity(self):
        if self.rect.centery <= SCREEN_HALF:
            self.rect.centery += self.gravity

    def update(self):
        self.animate()
        self.apply_gravity()

    def animate(self):
        self.current_image += 0.05
        if self.current_image >= 2:
            self.current_image = 0

        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]
        else:
            self.image = self.running_sprites[int(self.current_image)]


class Ostacle(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        for i in range(1, 7):
            current_sprite = pygame.transform.scale(
                pygame.image.load(f"../assets/obstacle.png"), (OSTACLE_WIDTH, OSTACLE_HEIGHT))
            self.sprites.append(current_sprite)
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 1300
        self.y_pos = random.choice([280, 295, 350])
        self.sprites = []
        self.sprites.append(
            pygame.transform.scale(
                pygame.image.load("../assets/avocado1.png"), (BIRD_WIDTH, BIRD_HEIGHT)))
        self.sprites.append(
            pygame.transform.scale(
                pygame.image.load("../assets/avocado2.png"), (BIRD_WIDTH, BIRD_HEIGHT)))
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.animate()
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def animate(self):
        self.current_image += 0.025
        if self.current_image >= 2:
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]

# Initial States
game_speed = GAME_SPEED_INIT
jump_count = 10
player_score = 0
game_over = False
obstacle_timer = 0
obstacle_spawn = False
obstacle_cooldown = 1000

# Surfaces
ground = pygame.image.load("../assets/ground.png")
ground = pygame.transform.scale(ground, (SCREEN_WIDTH, GROUND_HEIGHT))
ground_x = 0
ground_rect = ground.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT + PLAYER_GROUND_DIFF))
cloud = pygame.image.load("../assets/cloud.png")
cloud = pygame.transform.scale(cloud, (CLOUD_WIDTH, CLOUD_HEIGHT))

# Groups
cloud_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()
bird_group = pygame.sprite.Group()

# Objects
player = Player(50, SCREEN_HALF)
player_group.add(player)

# Sounds
bg_sfx = pygame.mixer.Sound("../assets/bg-sound.mp3")
death_sfx = pygame.mixer.Sound("../assets/game-over.mp3")
points_sfx = pygame.mixer.Sound("../assets/winning.mp3")
jump_sfx = pygame.mixer.Sound("../assets/jump.mp3")

# Events
CLOUD_EVENT = pygame.USEREVENT
pygame.time.set_timer(CLOUD_EVENT, CLOUD_EVENT_INTERVAL)

# Functions
def end_game():
    global player_score, game_speed
    game_over_text = game_font.render("Game Over!", True, "black")
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HALF - 60))
    score_text = game_font.render(f"Score: {int(player_score)}", True, "black")
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HALF))
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    game_speed = GAME_SPEED_INIT
    cloud_group.empty()
    obstacle_group.empty()


while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player.duck()
    else:
        if player.ducking:
            player.unduck()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLOUD_EVENT:
            current_cloud_y = random.randint(50, 300)
            current_cloud = Cloud(cloud, SCREEN_WIDTH + 100, current_cloud_y)
            cloud_group.add(current_cloud)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                player.jump()
                if game_over:
                    game_over = False
                    game_speed = GAME_SPEED_INIT
                    player_score = 0

    screen.fill("white")

    # Collisions
    if pygame.sprite.spritecollide(player_group.sprite, obstacle_group, False):
        game_over = True
        death_sfx.play()
    if game_over:
        end_game()

    if not game_over:
        game_speed += GAME_SPEED_INCREMENT
        if round(player_score, 1) % 100 == 0 and int(player_score) > 0:
            points_sfx.play()

        if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
            obstacle_spawn = True

        if obstacle_spawn:
            obstacle_random = random.randint(1, 50)
            if obstacle_random in range(1, 7):
                new_obstacle = Ostacle(SCREEN_WIDTH, SCREEN_HALF + GROUND_HEIGHT/2)
                obstacle_group.add(new_obstacle)
                obstacle_timer = pygame.time.get_ticks()
                obstacle_spawn = False
            elif obstacle_random in range(7, 10):
                new_obstacle = Bird()
                obstacle_group.add(new_obstacle)
                obstacle_timer = pygame.time.get_ticks()
                obstacle_spawn = False
        
        screen.fill((143, 212, 255), (0, 0, SCREEN_WIDTH, GROUND_BOTTOM_Y))
        screen.fill((112, 69, 0), (0, GROUND_BOTTOM_Y, SCREEN_WIDTH, GROUND_TOP_Y))
        bg_sfx.play()

        player_score += 0.1
        player_score_surface = game_font.render(
            str(int(player_score)), True, ("black"))
        screen.blit(player_score_surface, (1150, 10))

        cloud_group.update()
        cloud_group.draw(screen)

        bird_group.update()
        bird_group.draw(screen)

        ground_x -= game_speed
        screen.blit(ground, (ground_x, SCREEN_HALF))
        screen.blit(ground, (ground_x + SCREEN_WIDTH, SCREEN_HALF))
        if ground_x <= -SCREEN_WIDTH:
            ground_x = 0

        obstacle_group.update()
        obstacle_group.draw(screen)

        player_group.update()
        player_group.draw(screen)

    clock.tick(120)
    pygame.display.update()