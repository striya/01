import time
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("Countdown Timer")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Font for displaying time
font = pygame.font.Font(None, 100)

# Timer settings
start_time = time.time()
countdown_time = 120  # Seconds

# Function to draw the countdown timer
def draw_timer(time_left):
    # Calculate remaining time
    minutes = int(time_left // 60)
    seconds = int(time_left % 60)

    # Display the time
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, white)
    text_rect = time_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(time_text, text_rect)

    # Draw the circle
    pygame.draw.circle(screen, blue, (screen_width // 2, screen_height // 2), 150, 5)

    # Check if time is up and draw additional indication if needed
    if time_left <= 0:
        # You can add a different color or text to indicate time is up
        pygame.draw.circle(screen, red, (screen_width // 2, screen_height // 2), 150, 5)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate remaining time
    time_elapsed = time.time() - start_time
    time_left = countdown_time - time_elapsed

    # Check if timer is up
    if time_left <= 0:
        time_left = 0  # Ensure time_left is zero when time is up
        # Optional: display a message or perform an action when the timer ends

    # Clear the screen
    screen.fill(black)

    # Draw the timer
    draw_timer(time_left)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(30)  # 30 frames per second

# Quit Pygame
pygame.quit()