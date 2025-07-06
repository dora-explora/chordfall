import pygame # type: ignore
from time import sleep
import threading

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("playerA.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, frame: int):
        if frame == 0:
            self.image = pygame.image.load("playerA.bmp").convert_alpha()
        if frame == 1:
            self.image = pygame.image.load("playerB.bmp").convert_alpha()

pygame.init()
screen = pygame.display.set_mode((480, 720))
clock = pygame.time.Clock()
running = True

def bounce_character(player: pygame.sprite.Sprite):
    frame = 0
    while True:
        player.update(frame)
        frame += 1
        frame %= 2
        sleep(0.5)

player = Player()
bouncer = threading.Thread(target=bounce_character, args=[player])
bouncer.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.blit(player.image, (210, 670), )

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently

pygame.quit()