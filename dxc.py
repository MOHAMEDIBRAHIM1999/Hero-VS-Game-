import pygame
import os

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stage Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load Images and Sounds
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
bg_image = pygame.image.load(os.path.join(BASE_DIR, "bg.jpg")).convert()
hero_image = pygame.image.load(os.path.join(BASE_DIR, "hero/standing.png")).convert_alpha()
move_right = [pygame.image.load(os.path.join(BASE_DIR, f"hero/R{i}.png")).convert_alpha() for i in range(1, 10)]
move_left = [pygame.image.load(os.path.join(BASE_DIR, f"hero/L{i}.png")).convert_alpha() for i in range(1, 10)]
bullet_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds/bullet.wav"))
hit_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds/hit.wav"))
font = pygame.font.SysFont("comicsans", 30)

class Player:
    def __init__(self, x, y, width, height, speed=5, jump_power=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.jump_power = jump_power
        self.jump_count = 10
        self.is_jumping = False
        self.direction = "right"
        self.standing = True
        self.move_count = 0
        self.hitbox = (self.x + 20, self.y + 10, self.width - 40, self.height - 10)
        self.score = 0
        self.stage = 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.speed:
            self.x -= self.speed
            self.direction = "left"
            self.standing = False
        elif keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width - self.speed:
            self.x += self.speed
            self.direction = "right"
            self.standing = False
        else:
            self.standing = True
            self.move_count = 0

    class Enemy:
        def __init__(self, x, y, width, height, end, step=3):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [self.x, self.end]
            self.step = step
            self.moves = 0
            self.hitbox = (self.x + 10, self.y + 2, self.width - 20, self.height - 5)
            self.health = 10
            self.visible = True

        def draw(self, screen, move_left=None):
            self.move()
            if self.visible:
                if self.moves >= 33:
                    self.moves = 0
                if self.step > 0:
                    screen.blit(move_right[self.moves // 3], (self.x, self.y))
                    self.moves += 1
                else:
                    screen.blit(move_left[self.moves // 3], (self.x, self.y))
                    self.moves += 1
                # draw health bar
                pygame.draw.rect(screen, RED, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                pygame.draw.rect(screen, GREEN,
                                 (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 10, self.y + 2, self.width - 20, self.height - 5)

    def draw(self, screen, move_left=None):
        self.move()
        if self.visible:
            if self.moves >= 33:
                self.moves = 0
            if self.step > 0:
                screen.blit(move_right[self.moves // 3], (self.x, self.y))
                self.moves += 1
            else:
                screen.blit(move_left[self.moves // 3], (self.x, self.y))
                self.moves += 1
            # draw health bar
            pygame.draw.rect(screen, RED, (self.hitbox[

            def redraw_game_window(self):
                # Draw the background image
                screen.blit(background_image, (0, 0))

                # Render the score text and blit it on the screen
                score_text = self.font.render("Score: " + str(self.score), True, white)
                screen.blit(score_text, (10, 10))

                # Render the stage text and blit it on the screen
                stage_text = self.font.render("Stage: " + str(self.player.stage), True, white)
                screen.blit(stage_text, (screen_width - stage_text.get_width() - 10, 10))

                # Draw the player and bullets
                self.player.draw(screen)
                for bullet in self.bullets:
                    bullet.draw(screen)

                # Draw the enemies
                for enemy in self.enemies:
                    if enemy.step < 0:
                        enemy.draw(screen, move_left)
                    else:
                        enemy.draw(screen, move_right)

                # Update the display
                pygame.display.update()


def wave(self):
    if self.enemyCount == 0:
        self.enemyStep += 0.5
        self.waveLength += 2
        self.enemyCount = self.waveLength
        self.player.stage += 1

    if len(self.enemies) < self.waveLength:
        x = random.randrange(0, screen_width - 64)
        y = random.randrange(-1500, -100)
        self.enemies.append(Enemy(x, y, 64, 64, screen_width))
    else:
        self.enemyCount -= 1

def game_over(self):
    text = self.font.render("Game Over", 1, white)
    screen.blit(text, (screen_width/2 - text.get_width()/2, 250))
    pygame.display.update()
    i = 0
    while i < 200:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 201
                pygame.quit()

def run_game(self):
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in self.bullets:
            for enemy in self.enemies:
                if enemy.visible and bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                    if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        hit_sound.play()
                        enemy.hit()
                        self.score += 1
                        self.bullets.pop(self.bullets.index(bullet))

                if bullet.y < screen_height and bullet.y > 0:
                    bullet.y -= bullet.velocity
                else:
                    self.bullets.pop(self.bullets.index(bullet))

        for enemy in self.enemies:
            if enemy.visible:
                if enemy.hitbox[1] + enemy.hitbox[3] > self.player.hitbox[1]:
                    if enemy.hitbox[0] < self.player.hitbox[0] + self.player.hitbox[2] and enemy.hitbox[0] + enemy.hitbox[2] > self.player.hitbox[0]:
                        self.player.hit()
                        self.score -= 5

                enemy.move()

                if enemy.hitbox[1] > screen_height:
                    enemy.visible = False
                    self.enemies.pop(self.enemies.index(enemy))

        self.wave()

        self.player.move()

        if self.player.hit_points <= 0:
            self.game_over()
            run = False

        self.redraw_game_window()

    pygame.quit()
