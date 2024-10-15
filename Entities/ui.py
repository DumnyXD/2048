import pygame

class GameUI:
    """
    Class responsible for managing the graphical interface of the 2048 game.
    Renders the game board and displays the "Game Over" message when applicable.
    """

    def __init__(self, screen):
        """
        Initializes the game interface, setting colors, font, and the screen.

        :param screen: Pygame display surface where the game will be rendered.
        """
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.bg_color = (30, 30, 30)
        self.tile_border_color = (40, 40, 40)

        self.colors = {
            0: (50, 50, 50),
            2: (60, 60, 60),
            4: (70, 70, 70),
            8: (120, 85, 70),
            16: (140, 90, 70),
            32: (160, 100, 80),
            64: (180, 110, 90),
            128: (200, 130, 100),
            256: (210, 140, 110),
            512: (220, 150, 120),
            1024: (230, 160, 130),
            2048: (240, 170, 140)
        }
        self.text_color = (255, 255, 255)

    def render(self, board, game_over=False):
        """
        Renders the game board, and if applicable, displays the "Game Over" screen.

        :param board: The current state of the board as a 2D matrix.
        :param game_over: Boolean indicating if the game has ended.
        """
        self.screen.fill(self.bg_color)
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                self.draw_tile(i, j, value)

        if game_over:
            self.render_game_over()

    def draw_tile(self, row, col, value):
        """
        Draws an individual tile on the board according to its value.

        :param row: The row index of the tile.
        :param col: The column index of the tile.
        :param value: The value of the tile (e.g., 2, 4, 8, etc.).
        """
        color = self.colors.get(value, (50, 50, 50))
        pygame.draw.rect(self.screen, color, pygame.Rect(col * 100, row * 100, 100, 100))
        pygame.draw.rect(self.screen, self.tile_border_color, pygame.Rect(col * 100, row * 100, 100, 100), 5)

        if value != 0:
            text = self.font.render(str(value), True, self.text_color)
            text_rect = text.get_rect(center=(col * 100 + 50, row * 100 + 50))
            self.screen.blit(text, text_rect)

    def render_game_over(self):
        """
        Displays the "Game Over" screen with a rounded background and a centered message.
        """
        overlay_rect = pygame.Rect(50, 150, 300, 100)
        self.draw_rounded_rect(self.screen, (30, 30, 30, 180), overlay_rect, 20)

        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)

    def draw_rounded_rect(self, surface, color, rect, radius=20):
        """
        Draws a rectangle with rounded corners and applies transparency.

        :param surface: The surface where the rectangle will be drawn.
        :param color: The color of the rectangle with an alpha channel for transparency.
        :param rect: The area of the rectangle.
        :param radius: The corner radius for rounded edges.
        """
        temp_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(temp_surface, color, temp_surface.get_rect(), border_radius=radius)
        surface.blit(temp_surface, rect.topleft)
