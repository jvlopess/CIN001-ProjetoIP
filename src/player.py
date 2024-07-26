import pygame  

# Valores recomendados
LARGURA = 1280          # 1280
ALTURA = 720            # 720
FPS = 60                # 60
ESCALA = 2              # 2
TILESIZE = 16 * ESCALA  # 16 * ESCALA

class Player(pygame.sprite.Sprite):

    # Construtor
    def __init__(self, pos, groups, sprites_obstaculos):
        super().__init__(groups)
        
        # Parâmetros iniciais
        self.current_direction = 'idle_down'
        self.current_frame = 0
        self.full_image = pygame.image.load("../assets/gameplay/Personagem.png").convert_alpha()
        
        # Definir as coordenadas dos sprites
        # Cada ação tem dois frames, um para cada direção
        self.sprite_player_positions = {
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


        self.image = self.get_sprite(self.current_direction, self.current_frame)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)  # Realizar a mudança do hitbox pela img (para não ocorrer bugs)
        self.direction = pygame.math.Vector2()
        
        # Velocidade do jogador
        self.speed = 1.25 * ESCALA
        self.sprites_obstaculos = sprites_obstaculos

        # Timer para animação
        self.animation_time = 1
        self.animation_speed = 0.1
        self.current_time = 0
        
    # Selecionar sprite
    def get_sprite(self, action, frame):
        x, y = self.sprite_player_positions[action][frame]
        sprite = self.full_image.subsurface(pygame.Rect(x, y, 16, 16))
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * ESCALA, sprite.get_height() * ESCALA))
        return sprite
    
    # Receber entrada
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y = -1
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.current_direction = 'run_up_left'
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.current_direction = 'run_up_right'
            else:
                self.current_direction = 'run_up'
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y = 1
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.current_direction = 'run_down_left'
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.current_direction = 'run_down_right'
            else:
                self.current_direction = 'run_down'
        else:
            self.direction.y = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
            if not (keys[pygame.K_w] or keys[pygame.K_UP]) and not (keys[pygame.K_s] or keys[pygame.K_DOWN]):
                self.current_direction = 'run_left'
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
            if not (keys[pygame.K_w] or keys[pygame.K_UP]) and not (keys[pygame.K_s] or keys[pygame.K_DOWN]):
                self.current_direction = 'run_right'
        else:
            self.direction.x = 0

        # Atualizar a animação apenas se a direção mudou ou se estamos nos movendo
        if self.direction.x == 0 and self.direction.y == 0:
            if 'up' in self.current_direction:
                if 'left' in self.current_direction:
                    self.current_direction = 'idle_up_left'
                elif 'right' in self.current_direction:
                    self.current_direction = 'idle_up_right'
                else:
                    self.current_direction = 'idle_up'
            elif 'down' in self.current_direction:
                if 'left' in self.current_direction:
                    self.current_direction = 'idle_down_left'
                elif 'right' in self.current_direction:
                    self.current_direction = 'idle_down_right'
                else:
                    self.current_direction = 'idle_down'
            elif 'left' in self.current_direction:
                self.current_direction = 'idle_left'
            elif 'right' in self.current_direction:
                self.current_direction = 'idle_right'

        self.image = self.get_sprite(self.current_direction, self.current_frame)
    
    # Alternar sprite
    def update_animation(self):
        self.current_time += self.animation_speed
        if self.current_time >= self.animation_time:
            self.current_time = 0
            
            # Alternar entre os dois frames disponíveis
            self.current_frame = (self.current_frame + 1) % 2
            self.image = self.get_sprite(self.current_direction, self.current_frame)
    
    # Movimentar jogador
    def move(self, speed):
        if self.direction.magnitude() != 0: #caso o jogador vá em alguma direção AS, AD, WA ou WD, a velocidade não seja maior do que devia.
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

        # Limites do mapa
        if self.hitbox.left < 0:
            self.hitbox.left = 0
        if self.hitbox.right > LARGURA:
            self.hitbox.right = LARGURA
        if self.hitbox.top < 0:
            self.hitbox.top = 0
        if self.hitbox.bottom > ALTURA:
            self.hitbox.bottom = ALTURA

    # Aplicar colisão
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.sprites_obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left - 1 
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right    
        if direction == 'vertical':
           for sprite in self.sprites_obstaculos:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    # Atualizar jogador
    def update(self):
        self.get_input()
        self.move(self.speed)
        self.update_animation()
