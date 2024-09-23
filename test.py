import pygame

# Initialize Pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set the width and height of the screen (window)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Move the Square")

# Define the square
square_size = 50
square_x = screen_width // 2 - square_size // 2
square_y = screen_height // 2 - square_size // 2
square_speed = 5

# Run the game loop
running = True
while running:
    # Event handling (keyboard inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of the keys
    keys = pygame.key.get_pressed()

    # Move the square
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed

    # Fill the screen with white color (background)
    screen.fill(WHITE)

    # Draw the square (rectangle)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
