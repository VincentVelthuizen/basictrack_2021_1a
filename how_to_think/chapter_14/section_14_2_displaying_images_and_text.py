import pygame


def main():
    pygame.init()
    surface_size = 480

    main_surface = pygame.display.set_mode((surface_size, surface_size))

    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)

    ball = pygame.image.load("Soccer_ball.png")
    # You could argue that I should have made a smaller image instead of scaling this one
    ball = pygame.transform.scale(ball, (50, 50))

    my_font = pygame.font.SysFont("Courier", 16)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        main_surface.fill((0, 200, 255))

        main_surface.fill(some_color, small_rect)

        main_surface.blit(ball, (100, 120))

        the_text = my_font.render("Hello world!", True, (0, 0, 0))
        main_surface.blit(the_text, (10, 10))

        pygame.display.flip()

    pygame.quit()


main()
