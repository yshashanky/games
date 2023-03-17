import pygame
import webbrowser

pygame.init()

screen = pygame.display.set_mode((1000, 800))

link_font = pygame.font.SysFont('Consolas', 50)
link_color = (0, 0, 0)

running = True

while running:

    screen.fill((255, 255, 255))
    
    rect = screen.blit(link_font.render("Sample Link", True, link_color), (50, 50))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if rect.collidepoint(pos):
                webbrowser.open(r"https://stackoverflow.com/")
    pygame.display.update()