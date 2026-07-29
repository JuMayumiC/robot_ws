import pygame
import sys

from renderer import Renderer


renderer = Renderer()

renderer.state.set_face(
    "normal",
    "normal",
    "normal"
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:


            # Normal
            if event.key == pygame.K_n:

                renderer.state.set_face(
                    "normal",
                    "normal",
                    "normal"
                )


            # Feliz Normal
            elif event.key == pygame.K_h:

                renderer.state.set_face(
                    "normal",
                    "normal",
                    "happy"
                )

            #Feliz Blink
            elif event.key == pygame.K_j:

                renderer.state.set_face(
                    "blink",
                    "normal",
                    "happy"
                )

            # Triste Normal
            elif event.key == pygame.K_s:

                renderer.state.set_face(
                    "normal",
                    "sad",
                    "sad"
                )


            # Assustado
            elif event.key == pygame.K_a:

                renderer.state.set_face(
                    "scary",
                    "serious",
                    "scary"
                )

            # Bravo Normal
            elif event.key == pygame.K_b:

                renderer.state.set_face(
                    "normal",
                    "angry",
                    "angry"
                )

    renderer.draw()


pygame.quit()
sys.exit()