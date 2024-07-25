import pygame
from player import Player

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Movimentação do Boneco")

# Grupo de sprites e obstaculos
all_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()  # Adicione sprites de obstáculos se necessário

# Criação do jogador
player_pos = (400, 300)
player = Player(pos=player_pos, groups=all_sprites, sprites_obstaculos=obstaculos)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualização dos sprites
    all_sprites.update()

    # Desenho na tela
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Controle de FPS
    clock.tick(60)

pygame.quit()
