import pygame
import webbrowser

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("Welcome to Tic-Tac-Toe")

global playerFalg, noResult
global markedBox, markedPlayer1, markedPlayer2
global player1, player2, draw
player1, player2, draw = 0, 0, 0
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

def startingText():
    text = str("Let's play tic-tac-toe...")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 500/2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.draw.rect(screen, (255, 255, 255),(80,98,410,312))
    pygame.display.update()

def restartText():
    text = str("Next round is on...")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 500/2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(1000)
    pygame.draw.rect(screen, (255, 255, 255),(80,98,410,312))
    pygame.display.update()

def background():
    pygame.draw.lines(screen, (0, 0, 0), True, 
                      [(100, 100), (400, 100), (400, 400), (100, 400)],3)
    
    pygame.draw.lines(screen, (0, 0, 0), False, 
                      [(200, 100), (200, 400), (300, 400), (300, 100)],3)
    
    pygame.draw.lines(screen, (0, 0, 0), False, 
                      [(100, 200), (400, 200), (400, 300), (100, 300)],3)

def scorecard():
    text = str("Player 1: 0 | Draw: 0 | Player 2: 0")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 20))
    screen.blit(text, text_rect)

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

def updateScoreCard(player1, player2, draw):
    pygame.draw.rect(screen, (255, 255, 255),(0,0,500,50))
    text = str(f"Player 1: {player1} | Draw: {draw} | Player 2: {player2}")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 20))
    screen.blit(text, text_rect)

def initialTurn():
    pygame.draw.rect(screen, (255, 255, 255),(0,50,500,48))
    text = str("It is Player 1 turn...")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 70))
    screen.blit(text, text_rect)

def playerTurn(player):
    pygame.draw.rect(screen, (255, 255, 255),(0,50,500,48))
    text = str(f"It is {player} turn...")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 70))
    screen.blit(text, text_rect)

def result(text):
    pygame.draw.rect(screen, (255, 255, 255),(0,50,500,48))
    text = str(f"{text}")
    text = my_font.render(text, True, (200, 000, 000))
    text_rect = text.get_rect(center=(500/2, 70))
    screen.blit(text, text_rect)

def checkWinner(markedPlayer, playerNumber):
    global noResult, player1, player2, draw

    for i in range (8):
        count = 0
        for j in range (3):
            if winnerArray[i][j] in markedPlayer:
                count += 1
        if count == 3:
            result("Here, we have a winner...!")
            if playerNumber == 1: player1 += 1
            else: player2 += 1
            updateScoreCard(player1, player2, draw)
            noResult = False
            break
        elif ((len(markedPlayer1)+len(markedPlayer2)) == 9):
            result("It's a draw, c'mon guys...!")
            draw += 1
            updateScoreCard(player1, player2, draw)
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
            playerFalg = True
            playerTurn("Player 2")
            checkWinner(markedPlayer1, 1)
        else:
            drawCross(w, h)
            markedPlayer2.append((w,h))
            playerFalg = False
            playerTurn("Player 1")
            checkWinner(markedPlayer2, 2)

def resetGame():
    global markedBox, markedPlayer1, markedPlayer2, playerFalg, noResult
    pygame.draw.rect(screen, (255, 255, 255),(98,98,410,312))
    markedBox, markedPlayer1, markedPlayer2 = [], [], []
    playerFalg = False
    noResult = True
    restartText() 
    initialTurn()
    background()

def footer():
    global linkden, code
    footerFont = pygame.font.SysFont('Comic Sans MS', 15)
    text = str("To restart the game or for the next round, press enter.")
    text = footerFont.render(text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(500/2, 420))
    screen.blit(text, text_rect)
    text = str("Developed by Shashank Yadav!")
    text = footerFont.render(text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(500/2, 450))
    linkden = screen.blit(text, text_rect)
    text = str("Source Code: @tic-tac-toe")
    text = footerFont.render(text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(500/2, 470))
    code = screen.blit(text, text_rect)

def main():
    running = True

    startingText()    
    background()
    scorecard()
    initialTurn()
    footer()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONUP:
                w, h = pygame.mouse.get_pos()
                if w in range(100, 400) and h in range(100, 400):
                    play(w, h)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    resetGame()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if linkden.collidepoint(pos):
                    webbrowser.open(r"https://stackoverflow.com/")
                
                if code.collidepoint(pos):
                    webbrowser.open(r"https://stackoverflow.com/")

        pygame.display.update()
        
main()
pygame.quit()