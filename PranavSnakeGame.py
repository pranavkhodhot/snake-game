# PRANAV KHODHOT
# OCTOBER 15, 2019
# BASIC AND SIMPLE SNAKE GAME

import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Screen variables for size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colour variables used
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CADETBLUE = (100, 149, 237)
SPRINGGREEN = (0, 255, 127)
PURPLE = (186, 85, 211)

# Food variables
FOOD_SIZE = 15

# Snake variables
SNAKE_SIZE = 30
SNAKE_SPEED = 30

# Timer for the game and frames per second
FPS = 10
clock = pygame.time.Clock()

# Font for rendering text
font = pygame.font.SysFont("arial", 28)

def draw_text(text, font, color, surface, x, y):
    """Function to draw text on the screen"""
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main():
    # Main game loop variables
    running = True
    intro = True
    gameover = False

    # Snake variables
    snake_pos = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]]
    dx = 0
    dy = 0

    # Food variables
    food_x = random.randint(50, SCREEN_WIDTH - 50)
    food_y = random.randint(50, SCREEN_HEIGHT - 50)

    # Game variables
    score = 0
    start_time = time.perf_counter()

    while running:
        # Intro loop
        while intro:
            screen.fill(CADETBLUE)
            draw_text("Introducing the Snake Game", font, BLACK, screen, 250, 210)
            draw_text("Press (1) for easy, (2) for medium, (3) for hard", font, BLACK, screen, 150, 260)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        FPS = 10
                        intro = False
                    elif event.key == pygame.K_2:
                        FPS = 15
                        intro = False
                    elif event.key == pygame.K_3:
                        FPS = 20
                        intro = False

        # Main game loop
        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and dx == 0:
                        dx = -SNAKE_SPEED
                        dy = 0
                    elif event.key == pygame.K_d and dx == 0:
                        dx = SNAKE_SPEED
                        dy = 0
                    elif event.key == pygame.K_w and dy == 0:
                        dy = -SNAKE_SPEED
                        dx = 0
                    elif event.key == pygame.K_s and dy == 0:
                        dy = SNAKE_SPEED
                        dx = 0
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            # Move the snake
            new_head = [snake_pos[0][0] + dx, snake_pos[0][1] + dy]
            snake_pos = [new_head] + snake_pos[:-1]

            # Check for collisions with walls
            if new_head[0] < 0 or new_head[0] + SNAKE_SIZE > SCREEN_WIDTH or new_head[1] < 0 or new_head[1] + SNAKE_SIZE > SCREEN_HEIGHT:
                gameover = True

            # Check for collisions with itself
            if new_head in snake_pos[1:]:
                gameover = True

            # Check for collision with food
            if new_head[0] < food_x + FOOD_SIZE and new_head[0] + SNAKE_SIZE > food_x and new_head[1] < food_y + FOOD_SIZE and new_head[1] + SNAKE_SIZE > food_y:
                food_x = random.randint(50, SCREEN_WIDTH - 50)
                food_y = random.randint(50, SCREEN_HEIGHT - 50)
                score += 1
                snake_pos.append(snake_pos[-1])  # Grow the snake

            # Clear the screen and draw everything
            screen.fill(SPRINGGREEN)
            for pos in snake_pos:
                pygame.draw.rect(screen, BLUE, (pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))
            pygame.draw.rect(screen, YELLOW, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))
            draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)
            pygame.display.update()
            clock.tick(FPS)

        # Game over loop
        screen.fill(CADETBLUE)
        draw_text(f"You lasted {int(time.perf_counter() - start_time)} seconds", font, RED, screen, 30, 200)
        draw_text(f"and scored {score} points. Press 'p' to play again.", font, RED, screen, 30, 240)
        pygame.display.update()
        
        while gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameover = False
                        intro = True
                        snake_pos = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]]
                        dx = 0
                        dy = 0
                        score = 0
                        start_time = time.perf_counter()
                        food_x = random.randint(50, SCREEN_WIDTH - 50)
                        food_y = random.randint(50, SCREEN_HEIGHT - 50)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
