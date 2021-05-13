from Apple import Apple
import pygame
from pygame import draw
from Snake import *

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 750

GRID_SIZE = 50

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

DIFFICULTY = 7


def draw_text(screen, text, size, location):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, text.get_rect(center = location))


def game_loop():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    snake = Snake(450, 350, GRID_SIZE, random.choice([LEFT, RIGHT, UP, DOWN]))
    apple = Apple(SCREEN_WIDTH/GRID_SIZE, SCREEN_HEIGHT/GRID_SIZE, GRID_SIZE)
    
    crash = False
    death = False

    while not crash:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.turn(RIGHT)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.turn(DOWN)
                if event.key == pygame.K_RETURN and death:
                    game_loop()
                    crash = True
    
        if not crash:
            if not death:
                screen.fill((0, 0, 0))
                apple.draw(screen)
                death = snake.move(screen)
                snake.draw(screen)
                if snake.pos[0] == apple.pos:
                    snake.eat()
                    apple.set_random_pos(snake.pos, snake.length)
                if death:
                    screen.fill((0, 0, 0))
                    draw_text(screen, "You Died", GRID_SIZE * 2, [screen.get_width()/2, screen.get_height()/2 - GRID_SIZE])
                    draw_text(screen, "Press Enter To Play Again", GRID_SIZE, [screen.get_width()/2, screen.get_height()/2 + GRID_SIZE])
                    
            pygame.display.update()
            clock.tick(DIFFICULTY)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
