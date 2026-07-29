from pathlib import Path
import pygame


class AssetManager:

    def __init__(self):

        self.base_path = Path(__file__).parent / "assets"

        self.face = None

        self.eyes = {
            "left": {},
            "right": {}
        }

        self.eyebrows = {
            "left": {},
            "right": {}
        }

        self.mouth = {
            "emotions": {},
            "visemes": {}
        }

        self.load_assets()

    def load_assets(self):

        # ---------- FACE ----------
        self.face = pygame.image.load(
            str(self.base_path / "face" / "base.png")
        )

        # ---------- EYES ----------
        for side in ["left", "right"]:

            folder = self.base_path / "eyes" / side

            for image in folder.glob("*.png"):

                self.eyes[side][image.stem] = pygame.image.load(str(image))


        # ---------- EYEBROWS ----------
        for side in ["left", "right"]:

            folder = self.base_path / "eyebrows" / side

            for image in folder.glob("*.png"):

                self.eyebrows[side][image.stem] = pygame.image.load(str(image))


        # ---------- MOUTH (EMOTIONS) ----------
        folder = self.base_path / "mouth" / "emotions"

        for image in folder.glob("*.png"):

            self.mouth["emotions"][image.stem] = pygame.image.load(str(image))


        # ---------- MOUTH (VISEMES) ----------
        folder = self.base_path / "mouth" / "visemes"

        for image in folder.glob("*.png"):

            self.mouth["visemes"][image.stem] = pygame.image.load(str(image))


        # ---------- DEBUG TAMANHOS ----------
        print("FACE:", self.face.get_size())

        print("LEFT EYE:", self.eyes["left"]["normal"].get_size())
        print("RIGHT EYE:", self.eyes["right"]["normal"].get_size())

        print("LEFT EYEBROW:", self.eyebrows["left"]["normal"].get_size())
        print("RIGHT EYEBROW:", self.eyebrows["right"]["normal"].get_size())

        print("MOUTH:", self.mouth["emotions"]["normal"].get_size())


    def get_face(self):
        return self.face


    def get_eye(self, side, expression):
        return self.eyes[side][expression]


    def get_eyebrow(self, side, expression):
        return self.eyebrows[side][expression]


    def get_mouth(self, expression):
        return self.mouth["emotions"][expression]


    def get_viseme(self, viseme):
        return self.mouth["visemes"][viseme]
