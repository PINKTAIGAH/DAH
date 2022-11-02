import sys, pygame

#setup pygame/window
main_clock= pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen= pygame.display.set_mode((500,500),0,32)

font= pygame.font.SysFont(None, 20)

def draw_text(text, font, colour, surface, x, y):
    textobj= font.render(text, 1, colour)
    textrect= textobj.get_rect()
    textrect.topleft= (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text('main menue', font, (255,255,255), screen, 20, 20)



        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        main_clock.tick(60)

main_menu()



