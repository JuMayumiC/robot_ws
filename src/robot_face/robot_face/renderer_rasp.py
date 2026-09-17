import pygame
import numpy as np

from asset_manager import AssetManager
from layout import Layout
from face_state import FaceState


WIDTH = 480
HEIGHT = 320
FB = "/dev/fb0"


class Renderer:

    def __init__(self):

        pygame.init()

        # Surface do mesmo tamanho do framebuffer
        self.screen = pygame.Surface((WIDTH, HEIGHT))

        self.assets = AssetManager()

        self.state = FaceState()

        # Abre o framebuffer uma única vez
        self.fb = open(FB, "r+b", buffering=0)


    def draw(self):

        # Fundo
        self.screen.fill((30, 30, 30))

        # Face base
        self.screen.blit(
            self.assets.get_face(),
            (
                Layout.FACE_X,
                Layout.FACE_Y
            )
        )

        # Sobrancelha esquerda
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

        # Sobrancelha direita
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

        # Olho esquerdo
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

        # Olho direito
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

        # Boca
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

        # -------------------------------------------------
        # PYGAME SURFACE -> RGB565 -> FRAMEBUFFER
        # -------------------------------------------------

        pixels = pygame.surfarray.array3d(self.screen)

        # Pygame retorna:
        # (largura, altura, RGB)
        #
        # O framebuffer precisa:
        # (altura, largura, RGB)
        pixels = pixels.transpose(1, 0, 2)

        r = pixels[:, :, 0].astype(np.uint16)
        g = pixels[:, :, 1].astype(np.uint16)
        b = pixels[:, :, 2].astype(np.uint16)

        # RGB888 -> RGB565
        rgb565 = (
            ((r >> 3) << 11)
            | ((g >> 2) << 5)
            | (b >> 3)
        )

        # Little-endian
        data = rgb565.astype("<u2").tobytes()

        # Envia para o framebuffer
        self.fb.seek(0)
        self.fb.write(data)


    def close(self):

        self.fb.close()
        pygame.quit()
