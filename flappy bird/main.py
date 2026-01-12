import sys

from objects import *
from menu import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((W, H))


def main_game():
    dt = 1

    menu_manager = MenuManager()

    while True:

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return

        screen.fill('black')

        menu_manager.update(events, dt)
        menu_manager.draw(screen)


        pygame.display.update()
        dt = TARGET_FPS * clock.tick(FPS) / 1000
        print(clock.get_fps())

        if dt == 0:
            dt = 1


if __name__ == '__main__':
    main_game()
    pygame.quit()
    sys.exit(0)
