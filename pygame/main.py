import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ZELDA")
WHITE = (255, 255, 255)
FPS = 60
PLAYER_SKIN = pygame.image.load(os.path.join('Assets', "user_skin.png"))
NPC_SKIN = pygame.image.load(os.path.join('Assets', "npc_skin.png"))

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(PLAYER_SKIN (450, 250))
    WIN.blit(NPC_SKIN (450, 270))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

if __name__ == "__main__":
    main()