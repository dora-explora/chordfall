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
screen = pygame.display.set_mode((720, 900))
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
position = 330
move_speed = 4

piano = pygame.image.load("piano.bmp").convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        position -= move_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        position += move_speed

    screen.fill((16, 185, 204))
    screen.blit(player.image, (position, 700), )

    screen.blit(piano, (0, 750))

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently

pygame.quit()