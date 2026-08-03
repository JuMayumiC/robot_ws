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

        # =====================
        # SOBRANCELHAS
        # =====================

        # Posição definida pela expressão
        self.left_eyebrow_base_y = 0
        self.right_eyebrow_base_y = 0

        # Movimento aplicado pela animação
        # Movimento aplicado pela animação
        self.eyebrow_anim_y = 0


    def set_face(self, eye, eyebrow, mouth):

        self.eye = eye
        self.eyebrow = eyebrow
        self.mouth = mouth

        self.current_eye = eye
        self.current_eyebrow = eyebrow
        self.current_mouth = mouth


    # =====================
    # OLHOS
    # =====================

    def set_current_eye(self, eye):

        self.current_eye = eye


    # =====================
    # BOCA
    # =====================

    def set_current_mouth(self, mouth):

        self.current_mouth = mouth


    # =====================
    # SOBRANCELHAS
    # =====================

    def set_current_eyebrow(self, eyebrow):

        self.current_eyebrow = eyebrow


    # ---------- Pose ----------

    def set_eyebrow_pose(self, left, right):

        self.left_eyebrow_base_y = left
        self.right_eyebrow_base_y = right


    def reset_eyebrow_pose(self):

        self.left_eyebrow_base_y = 0
        self.right_eyebrow_base_y = 0


    # ---------- Animação ----------

    def set_eyebrow_animation(self, offset):

        self.eyebrow_anim_y = offset


    def reset_eyebrow_animation(self):

        self.eyebrow_anim_y = 0

    # =====================
    # FALA
    # =====================

    def stop_talking(self):

        self.current_mouth = self.mouth