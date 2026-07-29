import pygame


class Animator:

    def __init__(self, state):

        self.state = state

        self.talking = False

        self.timer = 0

        self.speed = 120

        self.index = 0



    def start_talking(self):

        self.talking = True

        self.index = 0



    def stop_talking(self):

        self.talking = False

        self.state.stop_talking()



    def update(self):

        if not self.talking:
            return


        now = pygame.time.get_ticks()


        if now - self.timer >= self.speed:


            sequence = [

                # boca da expressão
                self.state.mouth,

                # visemes
                "A",
                "E",
                "O",
                "U",
                "I"

            ]


            frame = sequence[self.index]


            self.state.set_current_mouth(frame)


            self.index += 1


            if self.index >= len(sequence):

                self.index = 0


            self.timer = now