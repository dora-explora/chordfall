import pygame
import pygame_menu
from time import sleep
# import threading

import pygame_menu.themes

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
            self.image = pygame.Surface([35, height])
            self.image.fill("white")
        else:
            self.image = pygame.Surface([20, height])
            self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x + 5, y - height)

pygame.init()
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()
running = True

LEVEL = [0, 0] # level number and frame countdown
level_start_event = pygame.event.Event(pygame.USEREVENT)

player = Player()
# bouncer = threading.Thread(target=bounce_character, args=[player])
# bouncer.start()
position = 330
move_speed = 4
note_speed = 10

# note -> x position key:
C4 = 8
D4 = 68
E4 = 128
F4 = 188
G4 = 248
A4 = 308
B4 = 368
C5 = 428
D5 = 488
E5 = 548
F5 = 608
G5 = 668 

level_1_bar_length = 375  # in pixels
level_1_offset = -650
level_1_notes = [
                # Fmaj7
                Note(True, level_1_bar_length, F4, level_1_offset), 
                Note(True, level_1_bar_length, A4, level_1_offset), 
                Note(True, level_1_bar_length, C5, level_1_offset), 
                Note(True, level_1_bar_length, E5, level_1_offset),
                # Em7
                Note(True, level_1_bar_length, E4, -level_1_bar_length * (3 + 2/3) + level_1_offset), 
                Note(True, level_1_bar_length, G4, -level_1_bar_length * (3 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, B4, -level_1_bar_length * (3 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, D5, -level_1_bar_length * (3 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, E5, -level_1_bar_length * (3 + 2/3) + level_1_offset),
                # Dm9
                Note(True, level_1_bar_length, D4, -level_1_bar_length * (8) + level_1_offset),
                Note(True, level_1_bar_length, F4, -level_1_bar_length * (8) + level_1_offset),
                Note(True, level_1_bar_length, A4, -level_1_bar_length * (8) + level_1_offset),
                Note(True, level_1_bar_length, C5, -level_1_bar_length * (8) + level_1_offset),
                Note(True, level_1_bar_length, E5, -level_1_bar_length * (8) + level_1_offset),
                # G7/D
                Note(True, level_1_bar_length, D4, -level_1_bar_length * (9 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, F4, -level_1_bar_length * (9 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, G4, -level_1_bar_length * (9 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, B4, -level_1_bar_length * (9 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, D5, -level_1_bar_length * (9 + 2/3) + level_1_offset),
                # Cmaj7
                Note(True, level_1_bar_length, C4, -level_1_bar_length * (11 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, E4, -level_1_bar_length * (11 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, G4, -level_1_bar_length * (11 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, B4, -level_1_bar_length * (11 + 2/3) + level_1_offset),
                Note(True, level_1_bar_length, E5, -level_1_bar_length * (11 + 2/3) + level_1_offset)
                ]

def level_1():
    pygame.mixer.music.load("Level 1.mp3")
    pygame.mixer.music.play()
    menu.disable()
    LEVEL[0] = 1
    LEVEL[1] = 860
    pygame.event.post(level_start_event)

levels = [level_1_notes]
level_countdown = 0
notes: list[Note] = []

piano = pygame.image.load("piano.bmp")

menu = pygame_menu.Menu("Chordfall", 400, 500, theme=pygame_menu.themes.THEME_DARK)
menu.add.button("Level 1", level_1)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            notes = levels[LEVEL[0] - 1].copy()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        position -= move_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        position += move_speed

    screen.fill((16, 185, 204))
    screen.blit(player.image, (position, 700), )

    if LEVEL[0] != 0:
        LEVEL[1] -= 1
        for note in notes:
            note.rect = note.rect.move(0, note_speed)
            screen.blit(note.image, note.rect)
        
        if LEVEL[1] == 100:
            pygame.mixer.music.load("golf clap.mp3")
            pygame.mixer.music.play()
        if LEVEL[1] == 0:
            LEVEL[0] = 0
            menu.enable()


    screen.blit(piano, (0, 750))

    if menu.is_enabled():
        menu.update(events)
    if menu.is_enabled():
        menu.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently


pygame.quit()