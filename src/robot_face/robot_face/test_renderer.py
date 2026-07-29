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

from animator import Animator


renderer = Renderer()

# Expressão inicial
renderer.state.set_face(*NORMAL)

# Controle da fala
animator = Animator(
    renderer.state
)


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:


            # ---------- EXPRESSÕES ----------

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



            # ---------- TESTE MANUAL DE VISEMES ----------

            # A
            elif event.key == pygame.K_1:

                renderer.state.set_viseme("A")


            # E
            elif event.key == pygame.K_2:

                renderer.state.set_viseme("E")


            # I
            elif event.key == pygame.K_3:

                renderer.state.set_viseme("I")


            # O
            elif event.key == pygame.K_4:

                renderer.state.set_viseme("O")


            # U
            elif event.key == pygame.K_5:

                renderer.state.set_viseme("U")



            # ---------- ANIMAÇÃO DE FALA ----------

            # Iniciar fala automática
            elif event.key == pygame.K_t:

                animator.start_talking()


            # Parar fala
            elif event.key == pygame.K_SPACE:

                animator.stop_talking()



    # Atualiza animação da boca
    animator.update()


    # Desenha rosto
    renderer.draw()



pygame.quit()
sys.exit()