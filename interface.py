import pygame

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

def main ():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        WIN.fill((255,255,0))
                  #  R   G  B
        pygame.display.update()
    pygame.quit()
        
if __name__ == "__main__":
    main()