import pygame
import sys

from renderer import Renderer

from expressions import (
    NORMAL,
    HAPPY,
    HAPPY_BLINK,
    SAD,
    SCARED,
    ANGRY
)


renderer = Renderer()

# Expressão inicial
renderer.state.set_face(*NORMAL)


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:


            # Normal
            if event.key == pygame.K_n:

                renderer.state.set_face(*NORMAL)


            # Feliz
            elif event.key == pygame.K_h:

                renderer.state.set_face(*HAPPY)


            # Feliz piscando
            elif event.key == pygame.K_j:

                renderer.state.set_face(*HAPPY_BLINK)


            # Triste
            elif event.key == pygame.K_s:

                renderer.state.set_face(*SAD)


            # Assustado
            elif event.key == pygame.K_a:

                renderer.state.set_face(*SCARED)


            # Bravo
            elif event.key == pygame.K_b:

                renderer.state.set_face(*ANGRY)


            # -------- VISAMES --------

            # Boca A
            elif event.key == pygame.K_1:

                renderer.state.set_viseme("A")


            # Boca E
            elif event.key == pygame.K_2:

                renderer.state.set_viseme("E")


            # Boca I
            elif event.key == pygame.K_3:

                renderer.state.set_viseme("I")


            # Boca O
            elif event.key == pygame.K_4:

                renderer.state.set_viseme("O")


            # Boca U
            elif event.key == pygame.K_5:

                renderer.state.set_viseme("U")


            # Parar fala
            elif event.key == pygame.K_0:

                renderer.state.stop_talking()


    renderer.draw()


pygame.quit()
sys.exit()