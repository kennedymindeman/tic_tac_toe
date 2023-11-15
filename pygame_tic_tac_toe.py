import pygame


def main():
    pygame.init()
    screen_width = 800
    screen_height = screen_width
    screen = pygame.display.set_mode((screen_width, screen_height))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                square = pygame.Rect(x, y, 10, 10)
                pygame.draw.rect(screen, (255, 0, 0), square)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
