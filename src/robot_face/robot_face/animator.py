import pygame
import random


class Animator:

    def __init__(self, state):

        self.state = state

        # ==================================================
        # MODO
        # ==================================================

        self.mode = "normal"

        # ==================================================
        # FALA
        # ==================================================

        self.talking = False

        self.talk_timer = 0
        self.talk_speed = 120

        self.viseme_index = 0

        # ==================================================
        # SONO
        # ==================================================

        self.sleep_timer = 0
        self.sleep_speed = 800

        self.sleep_index = 0

        # ==================================================
        # PISCADA
        # ==================================================

        self.blinking = False

        self.blink_timer = 0

        self.next_blink = (
            pygame.time.get_ticks()
            + random.randint(2000, 5000)
        )

        # ==================================================
        # SOBRANCELHAS
        # ==================================================

        self.eyebrow_timer = 0

        self.eyebrow_speed = 120

        self.eyebrow_direction = -1

        self.eyebrow_animation = 0

        self.max_animation = 2


    # ==================================================
    # MODOS
    # ==================================================

    def start_sleep(self):

        self.mode = "sleep"

        self.talking = False

        self.state.set_current_eye("sleepy")

        self.state.set_current_mouth("O")

        self.state.set_eyebrow_pose(2, 2)

        self.sleep_index = 0

        self.sleep_timer = pygame.time.get_ticks()


    def stop_sleep(self):

        self.mode = "normal"

        self.state.set_current_eye(self.state.eye)

        self.state.set_current_mouth(self.state.mouth)

        self.state.reset_eyebrow_pose()

        self.state.reset_eyebrow_animation()


    # ==================================================
    # FALA
    # ==================================================

    def start_talking(self):

        if self.mode == "sleep":
            return

        self.talking = True

        self.viseme_index = 0


    def stop_talking(self):

        self.talking = False

        self.state.stop_talking()


    # ==================================================
    # UPDATE
    # ==================================================

    def update(self):

        if self.mode == "sleep":

            self.update_sleep()

            return


        self.update_talking()

        self.update_blink()

        self.update_eyebrows()


    # ==================================================
    # BOCA (FALA)
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
    # SONO
    # ==================================================

    def update_sleep(self):

        now = pygame.time.get_ticks()

        # Mantém os olhos fechados
        self.state.set_current_eye("sleepy")

        # Respiração da boca (O -> O -> U -> U)
        if now - self.sleep_timer >= self.sleep_speed:

            sequence = [
                "O",
                "O",
                "U",
                "U"
            ]

            self.state.set_current_mouth(
                sequence[self.sleep_index]
            )

            self.sleep_index += 1

            if self.sleep_index >= len(sequence):
                self.sleep_index = 0

            self.sleep_timer = now

        # Movimento suave das sobrancelhas
        self.update_eyebrows()


    # ==================================================
    # PISCADA
    # ==================================================

    def update_blink(self):

        now = pygame.time.get_ticks()

        if (
            now >= self.next_blink
            and not self.blinking
        ):

            self.state.set_current_eye("blink")

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
    # SOBRANCELHAS
    # ==================================================

    def update_eyebrows(self):

        now = pygame.time.get_ticks()

        if now - self.eyebrow_timer < self.eyebrow_speed:
            return

        self.eyebrow_animation += self.eyebrow_direction

        if self.eyebrow_animation <= -self.max_animation:

            self.eyebrow_direction = 1

        elif self.eyebrow_animation >= self.max_animation:

            self.eyebrow_direction = -1

        self.state.set_eyebrow_animation(
            self.eyebrow_animation
        )

        self.eyebrow_timer = now