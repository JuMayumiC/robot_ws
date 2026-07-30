import pygame
import random


class Animator:


    def __init__(self, state):

        self.state = state


        # =====================
        # FALA
        # =====================

        self.talking = False

        self.talk_timer = 0

        self.talk_speed = 120

        self.viseme_index = 0



        # =====================
        # PISCADA
        # =====================

        self.blinking = False

        self.blink_timer = 0

        self.next_blink = (
            pygame.time.get_ticks()
            + random.randint(2000, 5000)
        )



        # =====================
        # SOBRANCELHA
        # =====================

        self.eyebrow_timer = 0

        self.eyebrow_up = False

        self.eyebrow_speed = 900



    def start_talking(self):

        self.talking = True

        self.viseme_index = 0



    def stop_talking(self):

        self.talking = False

        self.state.stop_talking()



    def update(self):

        self.update_talking()

        self.update_blink()

        self.update_eyebrow()



    # ==================================================
    # BOCA / FALA
    # ==================================================

    def update_talking(self):

        if not self.talking:
            return


        now = pygame.time.get_ticks()


        if now - self.talk_timer >= self.talk_speed:


            sequence = [

                self.state.mouth,

                "A",
                "E",
                "O",
                "U",
                "I"

            ]


            self.state.set_current_mouth(
                sequence[self.viseme_index]
            )


            self.viseme_index += 1


            if self.viseme_index >= len(sequence):

                self.viseme_index = 0


            self.talk_timer = now



    # ==================================================
    # PISCADA
    # ==================================================

    def update_blink(self):

        now = pygame.time.get_ticks()


        if (
            now >= self.next_blink
            and not self.blinking
        ):

            self.state.set_current_eye(
                "blink"
            )


            self.blinking = True

            self.blink_timer = now



        elif self.blinking:


            if now - self.blink_timer >= 150:


                self.state.set_current_eye(
                    self.state.eye
                )


                self.blinking = False


                self.next_blink = (
                    now
                    + random.randint(2000, 5000)
                )



    # ==================================================
    # SOBRANCELHA
    # ==================================================

    def update_eyebrow(self):

        now = pygame.time.get_ticks()


        if now - self.eyebrow_timer >= self.eyebrow_speed:


            if self.eyebrow_up:

                # volta para posição normal
                self.state.set_eyebrow_offset(0)


            else:

                # sobe 5 pixels
                self.state.set_eyebrow_offset(-5)



            self.eyebrow_up = not self.eyebrow_up


            self.eyebrow_timer = now