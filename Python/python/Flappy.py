import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load assets
BIRD_IMG = pygame.image.load("assets/bird.png").convert_alpha()
BACKGROUND_IMG = pygame.image.load("assets/background.png").convert()
PIPE_IMG = pygame.image.load("assets/pipe.png").convert_alpha()
BASE_IMG = pygame.image.load("assets/base.png").convert()

# Sound effects (optional)
# FLAP_SOUND = pygame.mixer.Sound("assets/flap.wav")
# POINT_SOUND = pygame.mixer.Sound("assets/point.wav")
# HIT_SOUND = pygame.mixer.Sound("assets/hit.wav")

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.gravity = 1
        self.flap_strength = -15
        self.image = BIRD_IMG
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)

    def flap(self):
        self.velocity = self.flap_strength
        # FLAP_SOUND.play()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Pipe class
class Pipe:
    GAP = 200
    SPEED = 4

    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, SCREEN_HEIGHT - Pipe.GAP - 100)
        self.top_pipe = PIPE_IMG
        self.bottom_pipe = pygame.transform.flip(PIPE_IMG, False, True)
        self.top_rect = self.top_pipe.get_rect(topleft=(self.x, self.height - self.top_pipe.get_height()))
        self.bottom_rect = self.bottom_pipe.get_rect(topleft=(self.x, self.height + Pipe.GAP))
        self.passed = False

    def update(self):
        self.x -= Pipe.SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        screen.blit(self.top_pipe, self.top_rect)
        screen.blit(self.bottom_pipe, self.bottom_rect)

# Base class
class Base:
    SPEED = 4
    WIDTH = BASE_IMG.get_width()

    def __init__(self):
        self.x1 = 0
        self.x2 = Base.WIDTH

    def update(self):
        self.x1 -= Base.SPEED
        self.x2 -= Base.SPEED
        if self.x1 + Base.WIDTH < 0:
            self.x1 = self.x2 + Base.WIDTH
        if self.x2 + Base.WIDTH < 0:
            self.x2 = self.x1 + Base.WIDTH

    def draw(self, screen):
        screen.blit(BASE_IMG, (self.x1, SCREEN_HEIGHT - BASE_IMG.get_height()))
        screen.blit(BASE_IMG, (self.x2, SCREEN_HEIGHT - BASE_IMG.get_height()))

# Game variables
bird = Bird()
pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(2)]
base = Base()
score = 0
font = pygame.font.Font(None, 36)
game_over = False

def draw_score(screen, score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def check_collision(bird, pipes):
    if bird.rect.top <= 0 or bird.rect.bottom >= SCREEN_HEIGHT - BASE_IMG.get_height():
        return True
    for pipe in pipes:
        if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
            return True
    return False

def reset_game():
    global bird, pipes, score, game_over
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(2)]
    score = 0
    game_over = False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird.flap()
            elif event.key == pygame.K_SPACE and game_over:
                reset_game()

    if not game_over:
        # Update game elements
        bird.update()
        base.update()

        for pipe in pipes:
            pipe.update()

            # Check if bird passed the pipe for scoring
            if not pipe.passed and pipe.top_rect.right < bird.rect.left:
                score += 1
                pipe.passed = True
                # POINT_SOUND.play()

        # Generate new pipes
        if pipes[-1].top_rect.x < SCREEN_WIDTH - 200:
            pipes.append(Pipe(SCREEN_WIDTH))

        # Remove off-screen pipes
        pipes = [pipe for pipe in pipes if pipe.top_rect.right > 0]

        # Check for collisions
        if check_collision(bird, pipes):
            game_over = True
            # HIT_SOUND.play()

    # Drawing
    screen.blit(BACKGROUND_IMG, (0, 0))
    for pipe in pipes:
        pipe.draw(screen)
    base.draw(screen)
    bird.draw(screen)
    draw_score(screen, score)

    if game_over:
        game_over_text = font.render("Game Over! Press Space to Restart", True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 FPS

pygame.quit()