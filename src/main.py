import pygame
import sys
from level import Level
from PIL import Image, ImageFilter

LARGURA = 1280
ALTURA = 720
FPS = 60
ESCALA = 2
TILESIZE = 16 * ESCALA

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
        pygame.display.set_caption('Projeto IP')
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            self.screen.fill('white')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)
    return textrect

def apply_blur(image_path, blur_radius=10):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return pygame.image.fromstring(blurred_image.tobytes(), blurred_image.size, blurred_image.mode)

def main_menu():
    click = False
    game = Game()
    font = pygame.font.Font(None, 74)
    
    # Carregar a imagem de fundo e aplicar desfoque
    background_image = apply_blur('../assets/tilemap/Mapa.png')
    background_image = pygame.transform.scale(background_image, (LARGURA, ALTURA))
    
    options = ["START", "ABOUT", "QUIT"]
    selected_option = 0
    
    while True:
        game.screen.blit(background_image, (0, 0))
        
        mx, my = pygame.mouse.get_pos()

        start_y = ALTURA // 2 - 50
        spacing = 60
        
        for i, option in enumerate(options):
            if i == selected_option:
                draw_text(">", font, WHITE, game.screen, LARGURA // 2 - 150, start_y + i * spacing)
            draw_text(option, font, WHITE, game.screen, LARGURA // 2, start_y + i * spacing)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected_option] == "START":
                        game.run()
                    elif options[selected_option] == "ABOUT":
                        print("About the Game")
                    elif options[selected_option] == "QUIT":
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        game.clock.tick(FPS)

if __name__ == '__main__':
    main_menu()
