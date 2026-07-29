class FaceState:

    def __init__(self):

        # Expressão atual
        self.eye = "normal"
        self.eyebrow = "normal"
        self.mouth = "normal"


        # Estado de animação
        self.current_eye = "normal"
        self.current_mouth = "normal"



    def set_face(self, eye, eyebrow, mouth):

        self.eye = eye
        self.eyebrow = eyebrow
        self.mouth = mouth

        # Atualiza o estado visual
        self.current_eye = eye
        self.current_mouth = mouth



    def set_current_eye(self, eye):

        self.current_eye = eye



    def set_current_mouth(self, mouth):

        self.current_mouth = mouth



    def stop_talking(self):

        # volta para a boca da emoção
        self.current_mouth = self.mouth