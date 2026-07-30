class FaceState:

    def __init__(self):

        # =====================
        # EXPRESSÃO
        # =====================

        self.eye = "normal"
        self.eyebrow = "normal"
        self.mouth = "normal"


        # =====================
        # ESTADOS ANIMADOS
        # =====================

        self.current_eye = "normal"
        self.current_mouth = "normal"
        self.current_eyebrow = "normal"


        # deslocamento da sobrancelha
        # negativo = sobe
        # positivo = desce
        self.eyebrow_offset_y = 0



    def set_face(self, eye, eyebrow, mouth):

        self.eye = eye
        self.eyebrow = eyebrow
        self.mouth = mouth


        self.current_eye = eye
        self.current_eyebrow = eyebrow
        self.current_mouth = mouth



    def set_current_eye(self, eye):

        self.current_eye = eye



    def set_current_mouth(self, mouth):

        self.current_mouth = mouth



    def set_current_eyebrow(self, eyebrow):

        self.current_eyebrow = eyebrow



    def set_eyebrow_offset(self, value):

        self.eyebrow_offset_y = value



    def stop_talking(self):

        self.current_mouth = self.mouth