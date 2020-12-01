import pygame

from how_to_think.chapter_14.section_14_4_queen_sprite import QueenSprite


def draw_board(the_board):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255, 0, 0), (0, 0, 0)]   # set up colors, red and black

    n = len(the_board)                  # the board has size n x n
    surface_size = 480                  # the size we'd like to approach (but not exceed)
    square_size = surface_size // n     # each square would be this size
    surface_size = n * square_size      # so this will be the actual size of the board

    surface = pygame.display.set_mode((surface_size, surface_size))

    ball = pygame.image.load("Soccer_ball.png")
    ball = pygame.transform.scale(ball, (square_size, square_size))

    all_sprites = []

    for column, row in enumerate(the_board):
        a_queen = QueenSprite(ball, (column * square_size, row * square_size))
        all_sprites.append(a_queen)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        for sprite in all_sprites:
            sprite.update()

        for row in range(n):
            color_index = row % 2
            for column in range(n):
                the_square = (column * square_size, row * square_size, square_size, square_size)
                surface.fill(colors[color_index], the_square)
                color_index = (color_index + 1) % 2

        for sprite in all_sprites:
            sprite.draw(surface)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])
