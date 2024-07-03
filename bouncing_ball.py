import pygame
import pyautogui
import random
import time
import threading

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Define ball properties
ball_color = (255, 0, 0)
ball_radius = 20
ball_pos = [random.randint(ball_radius, width - ball_radius), random.randint(ball_radius, height - ball_radius)]
ball_velocity = [5, 5]

# Define function to simulate mouse movements
def move_mouse():
    while True:
        x, y = pyautogui.position()
        new_x = x + random.randint(-10, 10)
        new_y = y + random.randint(-10, 10)
        pyautogui.moveTo(new_x, new_y)
        time.sleep(random.randint(10, 30))  # Move the mouse every 10 to 30 seconds

# Start the mouse movement thread
mouse_thread = threading.Thread(target=move_mouse)
mouse_thread.daemon = True
mouse_thread.start()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Bounce the ball off the walls
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= width:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= height:
        ball_velocity[1] = -ball_velocity[1]

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(window, ball_color, ball_pos, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the fewp6koTieZ
    pygame.time.Clock().tick(60)

pygame.quit()
