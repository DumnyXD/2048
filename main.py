# main.py
import pygame
from Entities.game import Game
from Entities.ui import GameUI

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('2048')

    game = Game()
    ui = GameUI(screen)

    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and not game_over:
                direction_map = {
                    pygame.K_LEFT: 'left',
                    pygame.K_a: 'left',
                    pygame.K_RIGHT: 'right',
                    pygame.K_d: 'right',
                    pygame.K_UP: 'up',
                    pygame.K_w: 'up',
                    pygame.K_DOWN: 'down',
                    pygame.K_s: 'down'
                }

                if event.key in direction_map:
                    game.move(direction_map[event.key])

                if game.is_game_over():
                    game_over = True

        ui.render(game.get_board(), game_over=game_over)
        pygame.display.update()

        clock.tick(30)  # 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
