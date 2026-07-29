import pygame

from asset_manager import AssetManager
from layout import Layout
from face_state import FaceState


class Renderer:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((520, 309))
        pygame.display.set_caption("Robot Face")

        self.assets = AssetManager()

        self.state = FaceState()


    def draw(self):

        self.screen.fill((30, 30, 30))


        # ---------- FACE BASE ----------
        self.screen.blit(
            self.assets.get_face(),
            (
                Layout.FACE_X,
                Layout.FACE_Y
            )
        )


        # ---------- SOBRANCELHAS ----------
        self.screen.blit(
            self.assets.get_eyebrow(
                "left",
                self.state.eyebrow
            ),
            (
                Layout.LEFT_EYEBROW_X,
                Layout.LEFT_EYEBROW_Y
            )
        )

        self.screen.blit(
            self.assets.get_eyebrow(
                "right",
                self.state.eyebrow
            ),
            (
                Layout.RIGHT_EYEBROW_X,
                Layout.RIGHT_EYEBROW_Y
            )
        )


        # ---------- OLHOS ----------
        self.screen.blit(
            self.assets.get_eye(
                "left",
                self.state.eye
            ),
            (
                Layout.LEFT_EYE_X,
                Layout.LEFT_EYE_Y
            )
        )

        self.screen.blit(
            self.assets.get_eye(
                "right",
                self.state.eye
            ),
            (
                Layout.RIGHT_EYE_X,
                Layout.RIGHT_EYE_Y
            )
        )


        # ---------- BOCA ----------
        self.screen.blit(
            self.assets.get_mouth(
                self.state.mouth
            ),
            (
                Layout.MOUTH_X,
                Layout.MOUTH_Y
            )
        )


        pygame.display.flip()