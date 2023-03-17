import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("Welcome to Tic-Tac-Toe")

global playerFalg, noResult
global markedBox, markedPlayer1, markedPlayer2
noResult,  playerFalg = True, False
markedBox, markedPlayer1, markedPlayer2 = [], [], []
winnerArray = [((100, 100),(200, 200),(300, 300)),
((100, 100),(200, 100),(300, 100)),
((100, 100),(100, 200),(100, 300)),
((200, 100),(200, 200),(200, 300)),
((300, 100),(200, 200),(100, 300)),
((300, 100),(300, 200),(300, 300)),
((100, 200),(200, 200),(300, 200)),
((100, 300),(200, 300),(300, 300))]

def drawCircle(w, h):
    w += 50
    h += 50
    pygame.draw.circle(screen, (0, 0, 255), (w, h), 30, 5)

def drawCross(w, h):
    w1, w2 = w + 25, w + 75
    h1, h2 = h + 25, h + 75

    pygame.draw.lines(screen, (0, 255, 0), False, 
                      [(w1, h1), (w2, h2)], 5)
    
    pygame.draw.lines(screen, (0, 255, 0), False, 
                      [(w1, h2), (w2, h1)], 5)

def background():
    pygame.draw.lines(screen, (0, 0, 0), True, 
                      [(100, 100), (400, 100), (400, 400), (100, 400)],3)
    
    pygame.draw.lines(screen, (0, 0, 0), False, 
                      [(200, 100), (200, 400), (300, 400), (300, 100)],3)
    
    pygame.draw.lines(screen, (0, 0, 0), False, 
                      [(100, 200), (400, 200), (400, 300), (100, 300)],3)
    
    pygame.display.flip()

def scoreCard(player1, player2, draw):
    text = str(f"Player 1: {player1} | Draw: {draw} | Player 2: {player2}")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 20))
    screen.blit(text, text_rect)

def playerTurn(player):
    text = str(f"It is {player} turn...")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 80))
    screen.blit(text, text_rect)

def result(text):
    text = str(f"{text}")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 80))
    screen.blit(text, text_rect)

def checkWinner(markedPlayer):
    global noResult

    for i in range (8):
        count = 0
        for j in range (3):
            if winnerArray[i][j] in markedPlayer:
                count += 1
        if count == 3:
            result("Here, we have a winner...!")
            noResult = False
            break
        elif ((len(markedPlayer1)+len(markedPlayer2)) == 9):
            result("It's a draw, comeon guys...!")
            noResult = False
            break

def play(w, h):
    global playerFalg, noResult
    global markedBox, markedPlayer1, markedPlayer2

    w = ((w // 100) * 100)
    h = ((h // 100) * 100)

    if (w, h) not in markedBox and noResult == True:
        markedBox.append((w,h))
        if playerFalg == False:
            drawCircle(w, h)
            markedPlayer1.append((w,h))
            checkWinner(markedPlayer1)
            playerFalg = True
        else:
            drawCross(w, h)
            markedPlayer2.append((w,h))
            checkWinner(markedPlayer2)
            playerFalg = False

def main():
    player1 = 0
    player2 = 0
    draw = 0

    running = True

    while running:
        background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONUP:
                w, h = pygame.mouse.get_pos()
                print(w, h)
                if w in range(100, 400) and h in range(100, 400):
                    play(w, h)
        
        # playerTurn("P")
        # scoreCard(player1, player2, draw)
        
main()
pygame.quit()