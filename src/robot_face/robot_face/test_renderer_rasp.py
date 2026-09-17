import pygame
import sys
import termios
import tty
import select

from renderer_rasp import Renderer

from expressions import (
    NORMAL,
    HAPPY,
    HAPPY_BLINK,
    SAD,
    SCARED,
    ANGRY
)

from animator import Animator


# ==========================================
# TECLADO DO TERMINAL
# ==========================================

old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())


def key_pressed():
    return select.select([sys.stdin], [], [], 0)[0]


renderer = Renderer()

# Expressão inicial
renderer.state.set_face(*NORMAL)

# Controle das animações
animator = Animator(renderer.state)


running = True


try:

    while running:

        # ==========================================
        # TECLADO
        # ==========================================

        if key_pressed():

            key = sys.stdin.read(1)


            # ==========================================
            # EXPRESSÕES
            # ==========================================

            # Normal
            if key == "n":

                animator.stop_sleep()

                renderer.state.set_face(*NORMAL)


            # Feliz
            elif key == "h":

                animator.stop_sleep()

                renderer.state.set_face(*HAPPY)


            # Feliz piscando
            elif key == "j":

                animator.stop_sleep()

                renderer.state.set_face(*HAPPY_BLINK)


            # Triste
            elif key == "s":

                animator.stop_sleep()

                renderer.state.set_face(*SAD)


            # Assustado
            elif key == "a":

                animator.stop_sleep()

                renderer.state.set_face(*SCARED)


            # Bravo
            elif key == "b":

                animator.stop_sleep()

                renderer.state.set_face(*ANGRY)


            # ==========================================
            # MODO DORMIR
            # ==========================================

            elif key == "d":

                animator.start_sleep()


            elif key == "w":

                animator.stop_sleep()


            # ==========================================
            # TESTE DOS VISEMES
            # ==========================================

            elif key == "1":

                renderer.state.set_current_mouth("A")


            elif key == "2":

                renderer.state.set_current_mouth("E")


            elif key == "3":

                renderer.state.set_current_mouth("I")


            elif key == "4":

                renderer.state.set_current_mouth("O")


            elif key == "5":

                renderer.state.set_current_mouth("U")


            # ==========================================
            # FALA
            # ==========================================

            elif key == "t":

                animator.start_talking()


            elif key == " ":

                animator.stop_talking()


            # ESC para sair
            elif key == "\x1b":

                running = False


        # ==========================================
        # ATUALIZA ANIMAÇÕES
        # ==========================================

        animator.update()


        # ==========================================
        # DESENHA O ROSTO
        # ==========================================

        renderer.draw()


finally:

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    renderer.close()

    pygame.quit()
