import pygame
import os

# Initialize pygame
pygame.init()

# Set up screen dimensions
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Pygame with Webview Launcher")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create a button (rectangle)
button_rect = pygame.Rect(200, 150, 100, 50)

# Function to execute the webview script
def launch_webview():
    os.system("python open_webview.py")

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Draw the button
    pygame.draw.rect(screen, BLUE, button_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button was clicked
            if button_rect.collidepoint(event.pos):
                # Launch the webview script
                launch_webview()
    
    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()

