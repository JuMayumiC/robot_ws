import pygame

from asset_manager import AssetManager
from layout import Layout


class Renderer:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((520, 309))
        pygame.display.set_caption("Robot Face")

        self.assets = AssetManager()

    def draw(self):

        self.screen.fill((30, 30, 30))

        # Face
        self.screen.blit(
            self.assets.get_face(),
            (Layout.FACE_X, Layout.FACE_Y)
        )

        # Sobrancelhas
        self.screen.blit(
            self.assets.get_eyebrow("left", "normal"),
            (Layout.LEFT_EYEBROW_X, Layout.LEFT_EYEBROW_Y)
        )

        self.screen.blit(
            self.assets.get_eyebrow("right", "normal"),
            (Layout.RIGHT_EYEBROW_X, Layout.RIGHT_EYEBROW_Y)
        )

        # Olhos
        self.screen.blit(
            self.assets.get_eye("left", "normal"),
            (Layout.LEFT_EYE_X, Layout.LEFT_EYE_Y)
        )

        self.screen.blit(
            self.assets.get_eye("right", "normal"),
            (Layout.RIGHT_EYE_X, Layout.RIGHT_EYE_Y)
        )

        # Boca
        self.screen.blit(
            self.assets.get_mouth("normal"),
            (Layout.MOUTH_X, Layout.MOUTH_Y)
        )

        pygame.display.flip()
