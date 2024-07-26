import pygame
from player import Player

# Inicializar tela
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("nome-do-jogo")
running = True
clock = pygame.time.Clock()

# Sprites e obstáculos
all_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()  # Adicione sprites de obstáculos se necessário

# Jogador
player_pos = (400, 300)
player = Player(pos=player_pos, groups=all_sprites, sprites_obstaculos=obstaculos)

# Inicializar Jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

    # Atualizar sprites
    all_sprites.update()

    # Desenhar sprites
    screen.fill("white")
    all_sprites.draw(screen)
    pygame.display.flip()

    # FPS
    clock.tick(60)

pygame.quit()
