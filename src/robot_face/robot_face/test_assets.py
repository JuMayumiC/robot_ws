from pathlib import Path
import pygame
import sys

# Inicializa o pygame
pygame.init()

# Caminho da pasta onde este arquivo está
BASE_DIR = Path(__file__).parent

# Caminho da imagem de fundo
FACE_PATH = BASE_DIR / "assets" / "face" / "base.png"

# Carrega a imagem
face = pygame.image.load(str(FACE_PATH))

# Obtém a resolução da imagem
width, height = face.get_size()

# Cria a janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Robot Face")

# Loop principal
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenha a face
    screen.blit(face, (0, 0))

    # Atualiza a tela
    pygame.display.flip()

# Fecha o pygame
pygame.quit()
sys.exit()
