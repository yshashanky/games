import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("Welcome to Tic-Tac-Toe")

def drawCircle():
    pygame.draw.circle(screen, (0, 0, 255), (150, 150), 30, 5)

def drawCross():
    pygame.draw.lines(screen, (0, 255, 0), False, 
                      [(125, 125), (175, 175)], 5)
    
    pygame.draw.lines(screen, (0, 255, 0), False, 
                      [(175, 125), (125, 175)], 5)
    
def screenText(player1, player2):
    text = str(f"Player 1: {player1} | Draw: 10 | Player 2: {player2}")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 20))
    screen.blit(text, text_rect)

def background():
    pygame.draw.lines(screen, (0, 0, 0), True, 
                      [(100, 100), (400, 100), (400, 400), (100, 400)],3)
    
    pygame.draw.lines(screen, (0, 0, 0), False, 
                      [(200, 100), (200, 400), (300, 400), (300, 100)],3)
    
    pygame.draw.lines(screen, (0, 0, 0), False, 
                      [(100, 200), (400, 200), (400, 300), (100, 300)],3)

def main():
    player1 = 0
    player2 = 0
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONUP:
                w, h = pygame.mouse.get_pos()
                print(w, h)
        
        background()
        drawCross()
        drawCircle()
        screenText(player1, player2)
        pygame.display.flip()
        

main()
pygame.quit()