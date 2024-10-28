import pygame
import webview 
import threading

# Initialize pygame
pygame.init()

# Set up screen dimensions
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Pygame with pywebview")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create a button (rectangle)
button_rect = pygame.Rect(200, 150, 100, 50)

# Function to open the pywebview window in a new thread
def open_webview():
    webview_window = webview.create_window('Webview', 'https://www.python.org')
    webview.start()

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
                # Open pywebview in a new thread to avoid blocking pygame's main loop
                threading.Thread(target=open_webview).start()
    
    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()

