import pygame
import sys
from level import Level
from PIL import Image, ImageFilter
from settings import *

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
        pygame.display.set_caption('FRAGM')
        self.clock = pygame.time.Clock()
        self.level = Level()

        # Carregar e tocar música de fundo
        pygame.mixer.music.load("../assets/gameplay/sounds/fundo.mp3")
        pygame.mixer.music.set_volume(0.5)  # Ajustar o volume se necessário
        pygame.mixer.music.play(-1)  # Tocar em loop
    
    def draw_text(self, text, font, color, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect(topleft=(x, y))
        self.screen.blit(textobj, textrect)
    
    def run(self):
        font = pygame.font.Font(None, 36)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_p:
                        take_screenshot(self.screen)
            
            self.screen.fill('white')
            self.level.run()
            
            # Desenhar a quantidade de itens coletados
            x_offset = LARGURA - 120
            y_offset = 10
            spacing = 40
            for item, count in self.level.collected_items.items():
                self.draw_text(f"{item.capitalize()}: {count}", font, YELLOW, x_offset, y_offset)
                y_offset += spacing
            
            # Desenhar o temporizador
            timer_text = f"Time: {int(self.level.timer)}"
            self.draw_text(timer_text, font, YELLOW, x_offset, y_offset + spacing)
            
            pygame.display.update()
            self.clock.tick(FPS)

def take_screenshot(screen):
    screenshot = pygame.Surface(screen.get_size())
    screenshot.blit(screen, (0, 0))
    pygame.image.save(screenshot, f"screenshot_{pygame.time.get_ticks()}.png")

def apply_blur(image_path, blur_radius=10):
    image = Image.open(image_path)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
    return pygame.image.fromstring(blurred_image.tobytes(), blurred_image.size, blurred_image.mode)

def about_screen(game):
    font = pygame.font.Font(None, 74)
    
    # Carregar a imagem de fundo para a tela "ABOUT"
    about_image = pygame.image.load("../assets/gameplay/about.png").convert_alpha()
    about_image = pygame.transform.scale(about_image, (LARGURA, ALTURA))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Volta ao menu principal

        game.screen.blit(about_image, (0, 0))
        game.draw_text("Pressione ESC para voltar", font, WHITE, LARGURA // 2 - 200, ALTURA - 100)
        
        pygame.display.update()
        game.clock.tick(FPS)

def main_menu():
    click = False
    game = Game()
    font = pygame.font.Font(None, 74)
    
    # Carregar a imagem de fundo e aplicar desfoque
    background_image = pygame.image.load("../assets/gameplay/FRAGMENTADO.png").convert_alpha()
    background_image = pygame.transform.scale(background_image, (LARGURA, ALTURA))
    
    options = ["START", "ABOUT", "QUIT"]
    selected_option = 0
    
    while True:
        game.screen.blit(background_image, (0, 0))
        
        mx, my = pygame.mouse.get_pos()

        start_y = ALTURA // 2 + 50  # Reposiciona o menu mais para baixo
        spacing = 60
        
        for i, option in enumerate(options):
            if i == selected_option:
                game.draw_text(">", font, WHITE, LARGURA // 2 - 130, start_y + i * spacing)  # Aproxima a setinha dos textos
            game.draw_text(option, font, WHITE, LARGURA // 2 - 100, start_y + i * spacing)  # Ajusta a posição dos textos

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
                        about_screen(game)
                    elif options[selected_option] == "QUIT":
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_p:
                    take_screenshot(game.screen)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        game.clock.tick(FPS)

if __name__ == '__main__':
    main_menu()
