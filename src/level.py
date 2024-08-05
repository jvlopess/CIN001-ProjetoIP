import pygame
from tile import Tile
from player import Player
from csv import reader

def import_csv_layout(path):
    mapa = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            mapa.append(list(row))
        return mapa
    

# Valores recomendados
LARGURA = 1280          # 1280
ALTURA = 720            # 720
FPS = 60                # 60
ESCALA = 2              # 2
TILESIZE = 16 * ESCALA  # 16 * ESCALA

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.sprites_acima_do_player = pygame.sprite.Group()
        self.sprites_visiveis = CameraGroup(self.sprites_acima_do_player)
        self.sprites_obstaculos = pygame.sprite.Group()
        self.sprites_abaixo_do_player = pygame.sprite.Group()
        self.player = Player((600 * ESCALA, 1520 * ESCALA), [self.sprites_visiveis], self.sprites_obstaculos)

        self.create_map()

    def get_sprite(self, action):
        x, y = self.sprite_positions[action]
        sprite = self.image.subsurface(pygame.Rect(x, y, 16, 16))
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * ESCALA, sprite.get_height() * ESCALA))
        return sprite
    
    def run(self):
        # Atualiza e desenha o jogo
        self.sprites_visiveis.drawn(self.player)
        self.sprites_visiveis.update()

    def create_map(self):

        self.sprite_positions = {
            'parede_preta': (16, 208),
            'parede_preta_vermelho': (32, 32),
            'parede_preta_vermelho_meio': (32, 48),
            'parede_preta_vermelho_esquerda': (16, 48),
            'parede_preta_vermelho_direita': (48, 48),
            'parede_preta_branca': (48, 208),
            'parede_preta_branca_meio': (32, 224),
            'parede_preta_branca_direita': (48, 224),
            'parede_preta_branca_esquerda': (16, 224),
            'parede_preta_roxo': (32, 80),
            'parede_preta_verde_esquerda': (16, 16),
            'parede_preta_verde_meio': (32, 16),
            'parede_preta_verde_direita': (48, 16),
            'parede_preta_azul_meio': (32, 112),
            'parede_preta_azul_direita': (48, 112),
            'parede_verde_listrado_esquerda': (16, 144),
            'parede_verde_listrado_meio': (32, 144),
            'parede_laranja_listrado': (32, 176),
            
            'porta_de_vidro_cima': (32, 58),
            'porta_de_vidro_cima_esquerda': (16, 58),
            'porta_de_vidro_baixo': (16, 80),

            'porta_de_vidro': (64, 144),
            'porta_de_vidro_esquerda': (80, 144),
            'porta_de_vidro_direita': (96, 144),
            'vidro_direita': (160, 160),
            'vidro_meio': (144, 160),
            'vidro_esquerda': (128, 160),
            'vidro_meio_direita': (128, 144),
            'vidro_meio_esquerda': (112, 144),
            'vidro_quina': (144, 144),

            'cadeira_auditorio': (64, 336),

            'armario_esquerda_cima' : (64, 288),
            'armario_direita_cima' : (80 , 288),
            'armario_esquerda_baixo' : (64, 304),
            'armario_direita_baixo' : (80, 304),

            'porta_azul_baixo': (112, 80),
            'porta_azul_cima_direita': (128, 58),
            'porta_azul_cima_esquerda': (112, 58),

            'porta_branca_cima_direita': (176, 58),
            'porta_branca_direita': (176, 112),
            'porta_branca_esquerda': (160, 112),
            
            'mesa_quina_baixo_esquerda': (16, 256),
            'mesa_meio_baixo': (32, 256),
            'mesa_quina_baixo_direita': (48, 256),
            'mesa_meio_esquerda':  (16, 240),
            'mesa_meio_direita':  (48, 240),
            'mesa_quina_cima_esquerda': (16, 224),
            'mesa_quina_cima_direita': (48, 224),
            'mesa_meio_cima': (32, 224),

            'escada_esquerda_1': (80, 256),
            'escada_esquerda_2': (96, 256),
            'escada_esquerda_3': (112, 256),
            'escada_esquerda_4': (128, 256),
            'escada_esquerda_5': (144, 256),
            'escada_direita_1': (80, 224),
            'escada_direita_2': (96, 224),
            'escada_direita_3': (112, 224),
            'escada_direita_4': (128, 224),
            'escada_direita_5': (144, 224),
            'meio_escada_direita': (112, 240),
            'meio_escada': (128, 240),
            'meio_escada_2': (80, 240),
            'meio_escada_esquerda': (96, 240),

            'sofa_1_pe': (176, 304),
            'sofa_1_pe_2': (192, 304),
            'sofa_1_meio': (192, 288),
            'sofa_1_meio_2': (176, 288),
            'sofa_1_canto_1': (176, 272),
            'sofa_1_canto_2': (192, 272),

            'porta_madeira_cima': (64, 58),
            'porta_madeira_baixo': (64, 80),
            'porta_madeira_esquerda_cima':(64,16),
            'porta_madeira_direita_cima':(80,16),
            'porta_madeira_esquerda_baixo':(64,32),
            'porta_madeira_direita_baixo':(80,32),

            'porta_branca_baixo': (160, 80),
            
            'arquivo_parte_cima': (32, 336),
            'arquivo_parte_baixo': (32, 352),

            'tv_direita': (32, 368),
            'tv_esquerda': (16, 368),
            'tv_direita_baixo': (32, 384),
            'tv_esquerda_baixo': (16, 384),

            'tv_2_direita': (64, 368),
            'tv_2_esquerda': (48, 368),
            'tv_2_direita_baixo': (64, 384),
            'tv_2_esquerda_baixo': (48, 384),

            'mesa_madeira_baixo_esquerda': (128, 304),
            'mesa_madeira_baixo_direita': (144, 304),
            'mesa_madeira_cima_esquerda': (128, 288),
            'mesa_madeira_cima_direita': (144, 288),

            'banco_de_ferro_cima': (160, 288),
            'banco_de_ferro_baixo':(160, 304),
            'banco_de_ferro_2_baixo_esquerda': (96, 336),
            'banco_de_ferro_2_baixo_direita': (112, 336),
            'banco_de_ferro_2_cima_esquerda': (96, 320),
            'banco_de_ferro_2_cima_direita': (112, 320),

            'geladeira_baixo': (16, 180),
            'geladeira_cima': (16, 164),
            'mesa_pia_baixo': (128, 192),
            'cima_pia': (64, 192),
            'microondas': (80, 192),
            'pia': (144, 192),

            'banheiro_cima':(160, 336),
            'banheiro_baixo':(160, 352),
            'pc_1': (192, 208),
            'pc_lab': (176, 240),
            'pc_lab_2':(176, 224),
            'mesa_lab': (192, 240),
            'mesa_pc_1': (192, 192),

            'mesa_ping_pong_esquerda_cima': (16, 288),
            'mesa_ping_pong_direita_cima': (32, 288),
            'mesa_ping_pong_esquerda_meio': (16, 304),
            'mesa_ping_pong_direita_meio': (32, 304),
            'mesa_ping_pong_esquerda_baixo': (16, 320),
            'mesa_ping_pong_direita_baixo': (32, 320),
        }

        layout = {
            'paredes': import_csv_layout('../assets/map/PAREDES.csv'),
            'piso': import_csv_layout('../assets/map/PISO.csv'),
            'sombras' : import_csv_layout('../assets/map/SOMBRAS.csv'),
            'objetos' : import_csv_layout('../assets/map/OBJETOS.csv'),
            'objetos_acima_do_player' : import_csv_layout('../assets/map/OBJETOS_ACIMA_DO_PLAYER.csv'),
            'objetos_Gameplay' : import_csv_layout('../assets/map/OBJETOS_Gameplay.csv'),
        }
        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'paredes':
                            self.image = pygame.image.load("../assets/gameplay/Piso.png").convert_alpha()
                            if col == '144' or col == '-2147483504':
                                piso_sprite = self.get_sprite('parede_preta')
                            elif col == '35':
                                piso_sprite = self.get_sprite('parede_preta_vermelho_meio')
                            elif col == '24':
                                piso_sprite = self.get_sprite('parede_preta_vermelho')
                            elif col == '34':
                                piso_sprite = self.get_sprite('parede_preta_vermelho_esquerda')
                            elif col == '36':
                                piso_sprite = self.get_sprite('parede_preta_vermelho_direita')
                            elif col == '156':
                                piso_sprite = self.get_sprite('parede_preta_branca_meio')
                            elif col == '146':
                                piso_sprite = self.get_sprite('parede_preta_branca')
                            elif col == '157':
                                piso_sprite = self.get_sprite('parede_preta_branca_direita')
                            elif col == '155':
                                piso_sprite = self.get_sprite('parede_preta_branca_esquerda')
                            elif col == '57':
                                piso_sprite = self.get_sprite('parede_preta_roxo')
                            elif col == '12':
                                piso_sprite = self.get_sprite('parede_preta_verde_esquerda')
                            elif col == '13':
                                piso_sprite = self.get_sprite('parede_preta_verde_meio')
                            elif col == '14':
                                piso_sprite = self.get_sprite('parede_preta_verde_direita')
                            elif col == '79':
                                piso_sprite = self.get_sprite('parede_preta_azul_meio')
                            elif col == '80':
                                piso_sprite = self.get_sprite('parede_preta_azul_direita')
                            elif col == '100':
                                piso_sprite = self.get_sprite('parede_verde_listrado_esquerda')
                            elif col == '101':
                                piso_sprite = self.get_sprite('parede_verde_listrado_meio')
                            elif col == '123':
                                piso_sprite = self.get_sprite('parede_laranja_listrado')
                            else:
                                print('parede não encontrada col:', col)
                            Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], piso_sprite)
                        elif style == 'objetos' or style == 'objetos_acima_do_player':
                            # Reajuste feito, devido a erro de leitura do csv
                            x  += 16 * ESCALA
                            y  += 80 * ESCALA
                            self.image = pygame.image.load("../assets/gameplay/Objetos.png").convert_alpha()
                            if col == '277':
                                objeto_sprite = self.get_sprite('cadeira_auditorio')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '238':
                                objeto_sprite = self.get_sprite('armario_esquerda_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '239':
                                objeto_sprite = self.get_sprite('armario_direita_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '140': # 240 é nada ???
                                objeto_sprite = self.get_sprite('vidro_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '139':
                                objeto_sprite = self.get_sprite('vidro_meio')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '138':
                                objeto_sprite = self.get_sprite('vidro_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '-1073741699':
                                objeto_sprite = self.get_sprite('vidro_meio_direita')
                                objeto_sprite = pygame.transform.rotate(objeto_sprite, 180)
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '125':
                                objeto_sprite = self.get_sprite('vidro_meio_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '124':
                                objeto_sprite = self.get_sprite('vidro_meio_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '121':
                                objeto_sprite = self.get_sprite('porta_de_vidro')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '126':
                                objeto_sprite = self.get_sprite('vidro_quina')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '122':
                                objeto_sprite = self.get_sprite('porta_de_vidro_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '72': #264 é nada ???
                                objeto_sprite = self.get_sprite('porta_azul_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '-2147483522':
                                objeto_sprite = self.get_sprite('vidro_quina')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '60':
                                objeto_sprite = self.get_sprite('porta_azul_cima_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '101':
                                objeto_sprite = self.get_sprite('porta_branca_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '102':
                                objeto_sprite = self.get_sprite('porta_branca_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '209':
                                objeto_sprite = self.get_sprite('mesa_quina_baixo_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '210':
                                objeto_sprite = self.get_sprite('mesa_meio_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '211':
                                objeto_sprite = self.get_sprite('mesa_quina_baixo_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '202':
                                objeto_sprite = self.get_sprite('meio_escada_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '203':
                                objeto_sprite = self.get_sprite('meio_escada')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '201':
                                objeto_sprite = self.get_sprite('meio_escada_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '-2147483390':
                                objeto_sprite = self.get_sprite('sofa_1_pe')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis], objeto_sprite)
                            elif col == '-2147483389':
                                objeto_sprite = self.get_sprite('sofa_1_pe_2')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '-2147483402':
                                objeto_sprite = self.get_sprite('sofa_1_meio')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, -10, 8, 8)
                            elif col == '-2147483416':
                                objeto_sprite = self.get_sprite('sofa_1_canto_1')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis], objeto_sprite)
                            elif col == '-2147483415':
                                objeto_sprite = self.get_sprite('sofa_1_canto_2')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis], objeto_sprite)
                            elif col == '-2147483403':
                                objeto_sprite = self.get_sprite('sofa_1_meio_2')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis], objeto_sprite)
                            elif col == '196':
                                objeto_sprite = self.get_sprite('mesa_meio_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '198':
                                objeto_sprite = self.get_sprite('mesa_meio_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '54' or col == '92':
                                objeto_sprite = self.get_sprite('porta_de_vidro_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '93':
                                objeto_sprite = self.get_sprite('porta_de_vidro_cima_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '66':
                                objeto_sprite = self.get_sprite('porta_de_vidro_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '56':
                                objeto_sprite = self.get_sprite('porta_madeira_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '75':
                                objeto_sprite = self.get_sprite('porta_branca_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '288': # 47 é nada ???
                                objeto_sprite = self.get_sprite('arquivo_parte_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '275':
                                objeto_sprite = self.get_sprite('arquivo_parte_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '123':
                                objeto_sprite = self.get_sprite('porta_de_vidro_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '301':
                                objeto_sprite = self.get_sprite('tv_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '300':
                                objeto_sprite = self.get_sprite('tv_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '314':
                                objeto_sprite = self.get_sprite('tv_direita_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, 0, -15.9, 0)
                            elif col == '313':
                                objeto_sprite = self.get_sprite('tv_esquerda_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, 0, -15.9, 0)
                            elif col == '303':
                                objeto_sprite = self.get_sprite('tv_2_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '302':
                                objeto_sprite = self.get_sprite('tv_2_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '316':
                                objeto_sprite = self.get_sprite('tv_2_direita_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, 0, -15.9, 0)
                            elif col == '315':
                                objeto_sprite = self.get_sprite('tv_2_esquerda_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, 0, -15.9, 0)
                            elif col == '183':
                                objeto_sprite = self.get_sprite('mesa_quina_cima_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '185':
                                objeto_sprite = self.get_sprite('mesa_quina_cima_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '184':
                                objeto_sprite = self.get_sprite('mesa_meio_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '251':
                                objeto_sprite = self.get_sprite('armario_esquerda_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '252':
                                objeto_sprite = self.get_sprite('armario_direita_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '255':
                                objeto_sprite = self.get_sprite('mesa_madeira_baixo_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '256':
                                objeto_sprite = self.get_sprite('mesa_madeira_baixo_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '242':
                                objeto_sprite = self.get_sprite('mesa_madeira_cima_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '243':
                                objeto_sprite = self.get_sprite('mesa_madeira_cima_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '244':
                                objeto_sprite = self.get_sprite('banco_de_ferro_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '257':
                                objeto_sprite = self.get_sprite('banco_de_ferro_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '-2147483391':
                                objeto_sprite = self.get_sprite('banco_de_ferro_baixo')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '-2147483404':
                                objeto_sprite = self.get_sprite('banco_de_ferro_cima')
                                objeto_sprite = pygame.transform.flip(objeto_sprite, True, False)
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '279':
                                objeto_sprite = self.get_sprite('banco_de_ferro_2_baixo_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '280':
                                objeto_sprite = self.get_sprite('banco_de_ferro_2_baixo_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '266':
                                objeto_sprite = self.get_sprite('banco_de_ferro_2_cima_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '267':
                                objeto_sprite = self.get_sprite('banco_de_ferro_2_cima_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '213':
                                objeto_sprite = self.get_sprite('escada_esquerda_1')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '214':
                                objeto_sprite = self.get_sprite('escada_esquerda_2')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '215':
                                objeto_sprite = self.get_sprite('escada_esquerda_3')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '216':
                                objeto_sprite = self.get_sprite('escada_esquerda_4')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '217':
                                objeto_sprite = self.get_sprite('escada_esquerda_5')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '187':
                                objeto_sprite = self.get_sprite('escada_direita_1')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '188':
                                objeto_sprite = self.get_sprite('escada_direita_2')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '189':
                                objeto_sprite = self.get_sprite('escada_direita_3')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '190':
                                objeto_sprite = self.get_sprite('escada_direita_4')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '191':
                                objeto_sprite = self.get_sprite('escada_direita_5')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '200':
                                objeto_sprite = self.get_sprite('meio_escada_2')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '131':
                                y = y + (4 * ESCALA)
                                objeto_sprite = self.get_sprite('geladeira_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '144':
                                y = y + (4 * ESCALA)
                                objeto_sprite = self.get_sprite('geladeira_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '164' or col == '166':
                                objeto_sprite = self.get_sprite('mesa_pia_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '165':
                                objeto_sprite = self.get_sprite('pia')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '160':
                                objeto_sprite = self.get_sprite('cima_pia')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '161':
                                objeto_sprite = self.get_sprite('microondas')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '283':
                                objeto_sprite = self.get_sprite('banheiro_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '296':
                                objeto_sprite = self.get_sprite('banheiro_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '59':
                                objeto_sprite = self.get_sprite('porta_azul_cima_esquerda')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '63':
                                objeto_sprite = self.get_sprite('porta_branca_cima_direita')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '181':
                                objeto_sprite = self.get_sprite('pc_1')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '168':
                                y = y + (4 * ESCALA)
                                objeto_sprite = self.get_sprite('mesa_pc_1')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '69':
                                objeto_sprite = self.get_sprite('porta_madeira_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '207':
                                objeto_sprite = self.get_sprite('mesa_lab')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '206':
                                objeto_sprite = self.get_sprite('pc_lab')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '193':
                                y = y + (32 * ESCALA)
                                objeto_sprite = self.get_sprite('pc_lab_2')
                                Tile((x, y), [self.sprites_acima_do_player], objeto_sprite)
                            elif col == '235':
                                objeto_sprite = self.get_sprite('mesa_ping_pong_esquerda_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '236':
                                objeto_sprite = self.get_sprite('mesa_ping_pong_direita_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '248':
                                objeto_sprite = self.get_sprite('mesa_ping_pong_esquerda_meio')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '249':
                                objeto_sprite = self.get_sprite('mesa_ping_pong_direita_meio')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '261':
                                objeto_sprite = self.get_sprite('mesa_ping_pong_esquerda_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '262':
                                objeto_sprite = self.get_sprite('mesa_ping_pong_direita_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '259':
                                objeto_sprite = self.get_sprite('sofa_1_pe_2')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, 6)
                            elif col == '258':
                                objeto_sprite = self.get_sprite('sofa_1_pe')
                                Tile((x, y), [self.sprites_visiveis], objeto_sprite)
                            elif col == '246':
                                objeto_sprite = self.get_sprite('sofa_1_meio')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite, 6)
                            elif col == '245':
                                objeto_sprite = self.get_sprite('sofa_1_meio_2')
                                Tile((x, y), [self.sprites_visiveis], objeto_sprite)
                            elif col == '233':
                                objeto_sprite = self.get_sprite('sofa_1_canto_2')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '232':
                                objeto_sprite = self.get_sprite('sofa_1_canto_1')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '17':
                                objeto_sprite = self.get_sprite('porta_madeira_esquerda_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '18':
                                objeto_sprite = self.get_sprite('porta_madeira_direita_cima')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '30':
                                objeto_sprite = self.get_sprite('porta_madeira_esquerda_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)
                            elif col == '31':
                                objeto_sprite = self.get_sprite('porta_madeira_direita_baixo')
                                Tile((x, y), [self.sprites_visiveis, self.sprites_obstaculos], objeto_sprite)

class CameraGroup(pygame.sprite.Group):
    def __init__(self, sprites_acima_do_player):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.sprites_acima_do_player = sprites_acima_do_player

        # criando o Piso utilizando a imagem do tilemap
        self.floor_surf = pygame.image.load('../assets/tilemap/Piso.png').convert()
        self.floor_surf = pygame.transform.scale(self.floor_surf, (self.floor_surf.get_width() * ESCALA, self.floor_surf.get_height() * ESCALA))
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))
    
    def drawn(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Desenhando o Piso z
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # Desenhando todos os sprites na ordem de sua posição Y
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        # Desenhando os sprites acima do player
        for sprite in self.sprites_acima_do_player:
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)