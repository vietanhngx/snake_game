import pygame
from settings import WIDTH, HEIGHT, CELL, FPS, BLACK, WHITE
from snake import Snake
from food import Food


def handle_input(snake):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.set_direction((0, -CELL))
    elif keys[pygame.K_DOWN]:
        snake.set_direction((0, CELL))
    elif keys[pygame.K_LEFT]:
        snake.set_direction((-CELL, 0))
    elif keys[pygame.K_RIGHT]:
        snake.set_direction((CELL, 0))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    snake = Snake()
    food = Food()
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input(snake)

        if snake.direction != (0, 0):
            ate = snake.next_head() == food.rect.topleft
            snake.move(grow=ate)
            if ate:
                score += 1
                food.respawn(snake.body)
            if snake.is_dead():
                snake.reset()
                food.respawn(snake.body)
                score = 0

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()