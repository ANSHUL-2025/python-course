import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Two Sprites with Custom Color Change")

# Custom event for changing color
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Sprite Class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        # Change to a random color
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite(200, 200, (255, 0, 0))  # Red
sprite2 = ColorSprite(400, 200, (0, 0, 255))  # Blue

# Sprite Group
sprites = pygame.sprite.Group(sprite1, sprite2)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Trigger custom event when SPACE is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

        # Handle custom event
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in sprites:
                sprite.change_color()

    # Clear screen
    screen.fill((30, 30, 30))
    # Draw sprites
    sprites.draw(screen)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
