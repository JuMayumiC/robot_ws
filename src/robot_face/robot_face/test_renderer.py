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

# Controle das animações
animator = Animator(renderer.state)


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:


            # ==========================================
            # EXPRESSÕES
            # ==========================================

            # Normal
            if event.key == pygame.K_n:

                animator.stop_sleep()

                renderer.state.set_face(*NORMAL)


            # Feliz
            elif event.key == pygame.K_h:

                animator.stop_sleep()

                renderer.state.set_face(*HAPPY)


            # Feliz piscando
            elif event.key == pygame.K_j:

                animator.stop_sleep()

                renderer.state.set_face(*HAPPY_BLINK)


            # Triste
            elif event.key == pygame.K_s:

                animator.stop_sleep()

                renderer.state.set_face(*SAD)


            # Assustado
            elif event.key == pygame.K_a:

                animator.stop_sleep()

                renderer.state.set_face(*SCARED)


            # Bravo
            elif event.key == pygame.K_b:

                animator.stop_sleep()

                renderer.state.set_face(*ANGRY)



            # ==========================================
            # MODO DORMIR
            # ==========================================

            # Dormir
            elif event.key == pygame.K_d:

                animator.start_sleep()


            # Acordar
            elif event.key == pygame.K_w:

                animator.stop_sleep()



            # ==========================================
            # TESTE DOS VISEMES
            # ==========================================

            elif event.key == pygame.K_1:

                renderer.state.set_current_mouth("A")


            elif event.key == pygame.K_2:

                renderer.state.set_current_mouth("E")


            elif event.key == pygame.K_3:

                renderer.state.set_current_mouth("I")


            elif event.key == pygame.K_4:

                renderer.state.set_current_mouth("O")


            elif event.key == pygame.K_5:

                renderer.state.set_current_mouth("U")



            # ==========================================
            # FALA
            # ==========================================

            elif event.key == pygame.K_t:

                animator.start_talking()


            elif event.key == pygame.K_SPACE:

                animator.stop_talking()



    # Atualiza animações
    animator.update()

    # Desenha o rosto
    renderer.draw()


pygame.quit()
sys.exit()