import pygame


def main():
    pygame.init()
    screen_width = 800
    screen_height = screen_width
    screen = pygame.display.set_mode((screen_width, screen_height))

    run = True
    while run:
        pygame.draw.circle(screen, (255, 255, 255), (screen_width // 2, screen_height // 2), 20, 5)
        draw_3_by_3_grid(screen, screen_width, screen_height, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x, y = get_board_index(pos, screen_width, screen_height)
                print(x, y)

        pygame.display.update()

    pygame.quit()


def draw_3_by_3_grid(screen, screen_width, screen_height, line_width):
    x_spacing = screen_width // 3
    y_spacing = screen_height // 3
    for offset in range(1, 3):
        pygame.draw.rect(screen, (255, 255, 255), (0, x_spacing * offset, screen_width, line_width))

    for offset in range(1, 3):
        pygame.draw.rect(screen, (255, 255, 255), (y_spacing * offset, 0, line_width, screen_height))


def get_board_index(pos, screen_width, screen_height):
    y, x = pos
    return 3 * x // screen_width, 3 * y // screen_height


if __name__ == "__main__":
    main()
