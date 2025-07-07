import pygame
from time import sleep
import threading

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("playerA.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, frame: int):
        frames = ["playerA.bmp", "playerB.bmp"]
        self.image = pygame.image.load(frames[frame]).convert_alpha()

def bounce_character(player: pygame.sprite.Sprite):
    frame = 0
    while True:
        player.update(frame)
        frame += 1
        frame %= 2
        sleep(0.5)

class Note(pygame.sprite.Sprite):
    def __init__(self, white_note: bool, height: int, x: float, y: float):
        super().__init__()
        if white_note:
            self.image = pygame.Surface([45, height])
            self.image.fill("white")
        else:
            self.image = pygame.Surface([30, height])
            self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

pygame.init()
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()
running = True

player = Player()
bouncer = threading.Thread(target=bounce_character, args=[player])
bouncer.start()
position = 330
move_speed = 4
note_speed = 10

# note -> x position key:
# C4: 8
# D4: 68
# E4: 128
# F4: 188
# G4: 268
# A4: 348
# B4: 428
# C5: 508
# D5: 588
# E5: 668
# F5: 748
# G5: 828
level_0_notes = [Note(True, 128, 8, -1200)]
pygame.mixer.music.load("Level 0.mp3")
pygame.mixer.music.play()

piano = pygame.image.load("piano.bmp")

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

    for note in level_0_notes:
        note.rect = note.rect.move(0, note_speed)
        screen.blit(note.image, note.rect)

    screen.blit(piano, (0, 750))

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently

pygame.quit()