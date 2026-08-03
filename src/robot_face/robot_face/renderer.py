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

        # =====================
        # FACE BASE
        # =====================

        self.screen.blit(
            self.assets.get_face(),
            (
                Layout.FACE_X,
                Layout.FACE_Y
            )
        )

        # =====================
        # SOBRANCELHA ESQUERDA
        # =====================

        self.screen.blit(
            self.assets.get_eyebrow(
                "left",
                self.state.current_eyebrow
            ),
            (
                Layout.LEFT_EYEBROW_X,
                Layout.LEFT_EYEBROW_Y
                + self.state.left_eyebrow_base_y
                + self.state.eyebrow_anim_y
            )
        )

        # =====================
        # SOBRANCELHA DIREITA
        # =====================

        self.screen.blit(
            self.assets.get_eyebrow(
                "right",
                self.state.current_eyebrow
            ),
            (
                Layout.RIGHT_EYEBROW_X,
                Layout.RIGHT_EYEBROW_Y
                + self.state.right_eyebrow_base_y
                + self.state.eyebrow_anim_y
            )
        )

        # =====================
        # OLHO ESQUERDO
        # =====================

        self.screen.blit(
            self.assets.get_eye(
                "left",
                self.state.current_eye
            ),
            (
                Layout.LEFT_EYE_X,
                Layout.LEFT_EYE_Y
            )
        )

        # =====================
        # OLHO DIREITO
        # =====================

        self.screen.blit(
            self.assets.get_eye(
                "right",
                self.state.current_eye
            ),
            (
                Layout.RIGHT_EYE_X,
                Layout.RIGHT_EYE_Y
            )
        )

        # =====================
        # BOCA
        # =====================

        if self.state.current_mouth in [
            "A",
            "E",
            "I",
            "O",
            "U"
        ]:

            x = Layout.VISEME_X
            y = Layout.VISEME_Y

            if self.state.current_mouth == "I":

                x = Layout.VISEME_I_X
                y = Layout.VISEME_I_Y

            elif self.state.current_mouth == "U":

                x = Layout.VISEME_U_X
                y = Layout.VISEME_U_Y

            self.screen.blit(
                self.assets.get_viseme(
                    self.state.current_mouth
                ),
                (
                    x,
                    y
                )
            )

        else:

            self.screen.blit(
                self.assets.get_mouth(
                    self.state.current_mouth
                ),
                (
                    Layout.MOUTH_X,
                    Layout.MOUTH_Y
                )
            )

        pygame.display.flip()