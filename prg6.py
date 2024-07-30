import pygame
import sys


def main():
    pygame.init()

    screen_width = 800
    screen_height = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    ball_pos = [screen_width // 2, screen_height // 2]
    ball_radius = 20
    ball_speed = [2, 2]

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simple Ball Animation")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > screen_width:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > screen_height:
            ball_speed[1] = -ball_speed[1]

        screen.fill(white)

        pygame.draw.circle(screen, red, ball_pos, ball_radius)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()