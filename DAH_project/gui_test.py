import pygame, sys
from pygame.locals import * 
from signal_generator import *
import matplotlib.pyplot as plt

pygame.init()
pygame.display.set_caption('game base')

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
main_clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)
OUTPUT_RATE= 44100
MAX_AMPLITUDE= np.iinfo(np.int16).max
pygame.mixer.init(frequency= OUTPUT_RATE, channels=2, size= -16)
click = False

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                triag523= triangle_wave(523,0.2,1)
                note= pygame.mixer.Sound(buffer= triag523)
                note.play()
                time.sleep(1)
        if button_2.collidepoint((mx, my)):
            if click:
                square523= square_wave(523,0.2,1)
                note= pygame.mixer.Sound(buffer= square523)
                note.play()
                time.sleep(1)                
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        main_clock.tick(60)
 
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        main_clock.tick(60)
 
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        main_clock.tick(60)
 
main_menu()



