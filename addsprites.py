import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (30, 30, 30)  # dark background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Rectangles Game")

# Clock for FPS control
clock = pygame.time.Clock()
FPS = 60

# Define colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create rectangles (x, y, width, height)
player_rect = pygame.Rect(100, 100, 50, 50)
static_rect = pygame.Rect(500, 300, 100, 100)

# Player speed
speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Keep player within screen bounds
    player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
    player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))

    # Drawing section
    screen.fill(SCREEN_COLOR)
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, BLUE, static_rect)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
