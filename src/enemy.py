import pygame

LARGURA = 1280          # 1280
ALTURA = 720            # 720
FPS = 60                # 60
ESCALA = 2              # 2
TILESIZE = 16 * ESCALA  # 16 * ESCALA

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprites_obstaculos, player):
        super().__init__(groups)
        
        # A imagem de todas as possíveis posições do inimigo (spritesheet)
        self.full_image = pygame.image.load("../assets/gameplay/Reitor.png").convert_alpha()
        
        # Definir as coordenadas dos sprites
        # Cada ação tem dois frames, um para cada direção
        self.sprite_enemy_positions = {
            'idle_up': [(16, 0), (144, 0)],
            'idle_down': [(16, 32), (144, 32)],
            'idle_left': [(0, 16), (128, 16)],
            'idle_right': [(32, 16), (160, 16)],
            'idle_up_left': [(0, 0), (128, 0)],
            'idle_up_right': [(32, 0), (160, 0)],
            'idle_down_left': [(0, 32), (128, 32)],
            'idle_down_right': [(32, 32), (160, 32)],
            'run_up': [(80, 0), (208, 0)],
            'run_down': [(80, 32), (208, 32)],
            'run_left': [(64, 16), (192, 16)],
            'run_right': [(96, 16), (224, 16)],
            'run_up_left': [(64, 0), (192, 0)],
            'run_up_right': [(96, 0), (224, 0)],
            'run_down_left': [(64, 32), (192, 32)],
            'run_down_right': [(96, 32), (224, 32)]
        }

        self.current_direction = 'idle_down'
        self.current_frame = 0
        self.image = self.get_sprite(self.current_direction, self.current_frame)

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)  # Realizar a mudança do hitbox pela img (para não ocorrer bugs)

        self.direction = pygame.math.Vector2()
        
        # Velocidade do inimigo
        self.speed = 1.5 * ESCALA

        self.sprites_obstaculos = sprites_obstaculos
        self.player = player

        # Timer para animação
        self.animation_time = 1
        self.animation_speed = 0.1
        self.current_time = 0
        
    # Função para pegar o sprite correto
    def get_sprite(self, action, frame):
        x, y = self.sprite_enemy_positions[action][frame]
        sprite = self.full_image.subsurface(pygame.Rect(x, y, 16, 16))
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * ESCALA, sprite.get_height() * ESCALA))
        return sprite

    def move_towards_player(self):
        player_pos = pygame.math.Vector2(self.player.rect.center)
        enemy_pos = pygame.math.Vector2(self.rect.center)
        
        self.direction = player_pos - enemy_pos

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Atualiza a direção atual para a animação correta
        if abs(self.direction.x) > abs(self.direction.y):
            if self.direction.x > 0:
                if self.direction.y > 0:
                    self.current_direction = 'run_down_right'
                else:
                    self.current_direction = 'run_up_right'
            else:
                if self.direction.y > 0:
                    self.current_direction = 'run_down_left'
                else:
                    self.current_direction = 'run_up_left'
        else:
            if self.direction.y > 0:
                self.current_direction = 'run_down'
            else:
                self.current_direction = 'run_up'

    def move(self, speed):
        if self.direction.magnitude() != 0:  # Caso o inimigo vá em alguma direção AS, AD, WA ou WD, a velocidade não seja maior do que devia.
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.sprites_obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # Moving right
                        self.hitbox.right = sprite.hitbox.left - 1
                        self.direction.x = 0
                    if self.direction.x < 0:  # Moving left
                        self.hitbox.left = sprite.hitbox.right + 1
                        self.direction.x = 0
        if direction == 'vertical':
            for sprite in self.sprites_obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # Moving down
                        self.hitbox.bottom = sprite.hitbox.top - 1
                        self.direction.y = 0
                    if self.direction.y < 0:  # Moving up
                        self.hitbox.top = sprite.hitbox.bottom + 1
                        self.direction.y = 0

    def update(self):
        self.move_towards_player()
        self.move(self.speed)
        self.update_animation()

    def update_animation(self):
        self.current_time += self.animation_speed
        if self.current_time >= self.animation_time:
            self.current_time = 0
            # Alternar entre os dois frames disponíveis
            self.current_frame = (self.current_frame + 1) % 2
            self.image = self.get_sprite(self.current_direction, self.current_frame)
