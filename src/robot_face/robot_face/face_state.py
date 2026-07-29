class FaceState:

    def __init__(self):

        # Partes do rosto
        self.eye = "normal"
        self.eyebrow = "normal"
        self.mouth = "normal"

        # Visema da boca (fala)
        self.viseme = None


    def set_face(self, eye, eyebrow, mouth):

        self.eye = eye
        self.eyebrow = eyebrow
        self.mouth = mouth


    def set_viseme(self, viseme):

        self.viseme = viseme