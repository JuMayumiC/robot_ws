class FaceState:

    def __init__(self):

        # Expressão atual
        self.eye = "normal"
        self.eyebrow = "normal"
        self.mouth = "normal"


        # Boca atualmente desenhada
        self.current_mouth = "normal"


    def set_face(self, eye, eyebrow, mouth):

        self.eye = eye
        self.eyebrow = eyebrow
        self.mouth = mouth

        # quando troca expressão, muda a boca de repouso
        self.current_mouth = mouth



    def set_current_mouth(self, mouth):

        self.current_mouth = mouth



    def stop_talking(self):

        # volta para a boca da expressão
        self.current_mouth = self.mouth