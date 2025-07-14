from os import environ, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import pygame_menu
import notes # type: ignore

import pygame_menu.themes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path.join("assets", "images", "playerA.bmp")).convert_alpha()

    def update(self, frame: int):
        frames = [path.join("assets", "images", "playerA.bmp"), path.join("assets", "images", "playerB.bmp")]
        self.image = pygame.image.load(frames[frame]).convert_alpha()

class Note(pygame.sprite.Sprite):
    def __init__(self, note_type: int, height: int, x: float, y: float):
        super().__init__()
        if note_type == 0:
            self.image = pygame.Surface([35, height])
            self.image.fill("white")
        elif note_type == 1:
            self.image = pygame.Surface([20, height])
            self.image.fill("black")
        elif note_type == 2:
            self.image = pygame.Surface([35, height])
            self.image.fill("orange")
        elif note_type == 3:
            self.image = pygame.Surface([20, height])
            self.image.fill("orange")
        elif note_type == 4:
            self.image = pygame.Surface([35, height])
            self.image.fill("dark blue")
        elif note_type == 5:
            self.image = pygame.Surface([20, height])
            self.image.fill("dark blue")
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
position = 350
move_speed = 4
note_speed = 10
player_frame = 0
player_bounce_countdown = 40

def level_1():
    pygame.mixer.music.load(path.join("assets", "sounds", "Level 1.mp3"))
    pygame.mixer.music.play()
    main_menu.disable()
    main_menu.full_reset()
    LEVEL[0] = 1
    LEVEL[1] = 860
    pygame.event.post(level_start_event)

def level_2():
    pygame.mixer.music.load(path.join("assets", "sounds", "Level 2.mp3"))
    pygame.mixer.music.play()
    main_menu.disable()
    main_menu.full_reset()
    LEVEL[0] = 2
    LEVEL[1] = 4400
    pygame.event.post(level_start_event)

def level_3():
    pygame.mixer.music.load(path.join("assets", "sounds", "Level 3.mp3"))
    pygame.mixer.music.play()
    main_menu.disable()
    main_menu.full_reset()
    LEVEL[0] = 3
    LEVEL[1] = 4000
    pygame.event.post(level_start_event)

levels_notelists = [notes.level_1_notelist, notes.level_2_notelist, notes.level_3_notelist] # type: ignore
level_countdown = 0
notes: list[Note] = []

left_key = pygame.image.load(path.join("assets", "images", "left_key.bmp")).convert_alpha()
middle_key = pygame.image.load(path.join("assets", "images", "middle_key.bmp")).convert_alpha()
right_key = pygame.image.load(path.join("assets", "images", "right_key.bmp")).convert_alpha()
black_key = pygame.Surface((30, 75))
black_key.fill((99, 198, 77))

def check_lit_key(rect: pygame.rect.Rect) -> tuple[pygame.surface.Surface, tuple[int, int]]: # type: ignore
    if rect.collidepoint(30, 750):
        return (left_key, (8, 758))
    elif rect.collidepoint(60, 750):
        return (black_key, (45, 758))
    elif rect.collidepoint(90, 750):
        return (middle_key, (68, 758))
    elif rect.collidepoint(120, 750):
        return (black_key, (105, 758))
    elif rect.collidepoint(150, 750):
        return (right_key, (128, 758))
    elif rect.collidepoint(210, 750):
        return (left_key, (188, 758))
    elif rect.collidepoint(240, 750):
        return (black_key, (225, 758))
    elif rect.collidepoint(270, 750):
        return (middle_key, (248, 758))
    elif rect.collidepoint(300, 750):
        return (black_key, (285, 758))
    elif rect.collidepoint(330, 750):
        return (middle_key, (308, 758))
    elif rect.collidepoint(360, 750):
        return (black_key, (345, 758))
    elif rect.collidepoint(390, 750):
        return (right_key, (368, 758))
    elif rect.collidepoint(450, 750):
        return (left_key, (428, 758))
    elif rect.collidepoint(480, 750):
        return (black_key, (465, 758))
    elif rect.collidepoint(510, 750):
        return (middle_key, (488, 758))
    elif rect.collidepoint(540, 750):
        return (black_key, (525, 758))
    elif rect.collidepoint(570, 750):
        return (right_key, (548, 758))
    elif rect.collidepoint(630, 750):
        return (left_key, (608, 758))
    elif rect.collidepoint(660, 750):
        return (black_key, (645, 758))
    elif rect.collidepoint(690, 750):
        return (right_key, (668, 758))

background = pygame.image.load(path.join("assets", "images", "background.bmp"))
piano = pygame.image.load(path.join("assets", "images", "piano.bmp")).convert_alpha()
render_keys: list[tuple[pygame.Surface, tuple[int, int]]] = []

main_menu = pygame_menu.Menu("Chordfall", 300, 375, theme=pygame_menu.themes.THEME_DARK)
main_menu.add.button("Level 1", level_1)
main_menu.add.button("Level 2", level_2)
main_menu.add.button("Level 3", level_3)

def open_main_menu():
    main_menu.enable()
    win_menu.disable()
    loss_menu.disable()

win_menu = pygame_menu.Menu("Level Won!", 300, 375, theme=pygame_menu.themes.THEME_DARK)
win_level_label = win_menu.add.label("")
win_score_label = win_menu.add.label("")
win_score_label.set_margin(0, 30) # type: ignore
win_back_button = win_menu.add.button("Go Back", open_main_menu)
win_menu.disable()

def open_level():
    loss_menu.disable()
    match level:
        case 1:
            level_1()
        case 2:
            level_2()
        case 3:
            level_3()

loss_menu = pygame_menu.Menu("Level Lost", 300, 375, theme=pygame_menu.themes.THEME_DARK)
loss_level_label = loss_menu.add.label("")
loss_score_label = loss_menu.add.label("")
loss_score_label.set_margin(0, 30) # type: ignore
loss_back_button = loss_menu.add.button("Go Back", open_main_menu) # type: ignore
loss_retry_button = loss_menu.add.button("Try Again", open_level)
loss_menu.disable()

game_over = False
score = 0
level = 0

while True:
    # check events to handle quitting and level start
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.USEREVENT:
            score = 0
            level = LEVEL[0]
            main_menu.disable()
            win_menu.disable()
            loss_menu.disable()
            notes = construct_notes(levels_notelists[LEVEL[0] - 1])
    if running == False:
        break
    # render
    screen.blit(background, (0, 0))
    # handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if position > 0:
            position -= move_speed
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if position < 700:
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
        if not game_over:
            render_keys = []
            for note in notes:
                note.rect = note.rect.move(0, note_speed)
                screen.blit(note.image, note.rect)
                if pygame.Rect(position, 720, 20, 45).colliderect(note.rect):
                    game_over = True
                elif pygame.Rect(position + 20, 720, 20, 45).colliderect(note.rect) or pygame.Rect(position - 20, 720, 20, 45).colliderect(note.rect):
                    score += 20 + (20 * (LEVEL[0] == 3))
                elif pygame.Rect(position + 40, 720, 20, 45).colliderect(note.rect) or pygame.Rect(position - 40, 720, 20, 45).colliderect(note.rect):
                    score += 10 + (10 * (LEVEL[0] == 3))
                elif pygame.Rect(position + 60, 720, 20, 45).colliderect(note.rect) or pygame.Rect(position - 60, 720, 20, 45).colliderect(note.rect):
                    score += 5 + (5 * (LEVEL[0] == 3))
                
                if note.rect.bottom > 750 and note.rect.top <= 750:
                    render_keys.append(check_lit_key(note.rect))
                
        if game_over:
            render_keys = []
            LEVEL[1] = 0

        if LEVEL[1] == 100:
            pygame.mixer.music.load(path.join("assets", "sounds", "golf clap.mp3"))
            pygame.mixer.music.play()
        if LEVEL[1] == 0:
            pygame.mixer.music.fadeout(1500)
            if game_over:
                game_over = False
                loss_level_label.set_title(f"Level {LEVEL[0]} lost...") # type: ignore
                loss_score_label.set_title(f"Score: {score}") # type: ignore
                loss_menu.enable()
            else: 
                win_level_label.set_title(f"Level {LEVEL[0]} completed!") # type: ignore
                win_score_label.set_title(f"Score: {score}") # type: ignore
                win_menu.enable()
            LEVEL[0] = 0
                

    screen.blit(piano, (0, 750))
    for key in render_keys:
        screen.blit(key[0], key[1])
    score_text = pygame.font.Font(None, 32).render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    if main_menu.is_enabled():
        main_menu.update(events)
    if win_menu.is_enabled():
        win_menu.update(events)
    if loss_menu.is_enabled():
        loss_menu.update(events)
    if main_menu.is_enabled():
        main_menu.draw(screen)
    if win_menu.is_enabled():
        win_menu.draw(screen)
    if loss_menu.is_enabled():
        loss_menu.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently