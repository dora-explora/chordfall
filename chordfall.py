import pygame
import pygame_menu
import notes # type: ignore

import pygame_menu.themes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("playerA.bmp").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, frame: int):
        frames = ["playerA.bmp", "playerB.bmp"]
        self.image = pygame.image.load(frames[frame]).convert_alpha()

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

def construct_notes(list) -> list[Note]:
    notes: list[Note] = []
    for note in list:
        notes.append(Note(note[0], note[1], note[2], note[3]))
    return notes

pygame.init()
screen = pygame.display.set_mode((720, 900))
clock = pygame.time.Clock()
running = True

LEVEL = [0, 0] # level number and frame countdown
level_start_event = pygame.event.Event(pygame.USEREVENT)

player = Player()
position = 330
move_speed = 4
note_speed = 10
player_frame = 0
player_bounce_countdown = 40

def level_1():
    pygame.mixer.music.load("Level 1.mp3")
    pygame.mixer.music.play()
    menu.disable()
    LEVEL[0] = 1
    LEVEL[1] = 860
    pygame.event.post(level_start_event)

def level_2():
    pygame.mixer.music.load("Level 2.mp3")
    pygame.mixer.music.play()
    menu.disable()
    LEVEL[0] = 2
    LEVEL[1] = 4400
    pygame.event.post(level_start_event)

levels_notelists = [notes.level_1_notelist, notes.level_2_notelist] # type: ignore
level_countdown = 0
notes: list[Note] = []

piano = pygame.image.load("piano.bmp")

menu = pygame_menu.Menu("Chordfall", 300, 375, theme=pygame_menu.themes.THEME_DARK)
menu.add.button("Level 1", level_1)
menu.add.button("Level 2", level_2)
menu.add.button("Level 3", level_1)
menu.add.button("Level 4", level_1)

while True:
    # check events to handle quitting and level start
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.USEREVENT:
            notes = construct_notes(levels_notelists[LEVEL[0] - 1])
    if running == False:
        break
    # fill background with sky blue first
    screen.fill((16, 185, 204))
    # handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        position -= move_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        position += move_speed
    # render character and manage bouncing
    player_bounce_countdown -= 1
    if player_bounce_countdown == 0:
        player_bounce_countdown = 40
        player_frame += 1
        player_frame %= 2
        player.update(player_frame)
    screen.blit(player.image, (position, 700), )
    # all the in-level logic
    if LEVEL[0] != 0:
        LEVEL[1] -= 1 # decrement the level length countdown
        for note in notes:
            note.rect = note.rect.move(0, note_speed)
            screen.blit(note.image, note.rect)
        
        if LEVEL[1] == 100:
            pygame.mixer.music.load("golf clap.mp3")
            pygame.mixer.music.play()
        if LEVEL[1] == 0:
            LEVEL[0] = 0
            pygame.mixer.music.fadeout(1500)
            menu.enable()

    screen.blit(piano, (0, 750))

    if menu.is_enabled():
        menu.update(events)
    if menu.is_enabled():
        menu.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently