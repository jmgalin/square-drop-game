import pygame
import random

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Set title
pygame.display.set_caption('Square Drop')

# Set up clock
clock = pygame.time.Clock()

# Set up colors
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Set up square sizes
square_size = 50
green_square_size = square_size
red_square_size = square_size

# Set up player and enemies
player = pygame.Rect(370, 500, green_square_size, green_square_size)
enemies = [pygame.Rect(random.randint(0, 750), random.randint(-1500, -100), red_square_size, red_square_size) for _ in range(10)]

# Score variables
score = 0
font = pygame.font.SysFont(None, 36)
score_updated = True  # Set it initially to True

# Game loop
running = True
while running:
    # Keep clock speed steady
    clock.tick(60)

    # Draw background
    screen.fill(white)

    # Draw player square
    pygame.draw.rect(screen, green, player)

    # Draw enemy squares
    for enemy in enemies:
        pygame.draw.rect(screen, red, enemy)

    # Check for collision with enemy squares
    collision = False
    for enemy in enemies:
        if player.colliderect(enemy):
            collision = True
            running = False
            


    # Move enemies
    for enemy in enemies:
        enemy.y += 5

    # Delete enemies off screen
    enemies = [enemy for enemy in enemies if enemy.y < 600]

    # Add new enemies if necessary
    while len(enemies) < 10:
        enemies.append(pygame.Rect(random.randint(0, 750), random.randint(-1500, -100), red_square_size, red_square_size))

    # Move player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Keep player on screen
    player.x = max(0, player.x)
    player.x = min(750, player.x)

    # Update and draw score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Draw screen
    pygame.display.flip()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()


