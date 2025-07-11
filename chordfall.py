import pygame
import pygame_menu
import notes # type: ignore

import pygame_menu.themes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("playerA.bmp").convert_alpha()

    def update(self, frame: int):
        frames = ["playerA.bmp", "playerB.bmp"]
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

background = pygame.image.load("background.bmp")
piano = pygame.image.load("piano.bmp").convert_alpha()
left_key = pygame.image.load("left_key.bmp").convert_alpha()
middle_key = pygame.image.load("middle_key.bmp").convert_alpha()
right_key = pygame.image.load("right_key.bmp").convert_alpha()
black_key = pygame.Surface((30, 75))
black_key.fill((99, 198, 77))
render_keys: list[tuple[pygame.Surface, tuple[int, int]]] = []

menu = pygame_menu.Menu("Chordfall", 300, 375, theme=pygame_menu.themes.THEME_DARK)
menu.add.button("Level 1", level_1)
menu.add.button("Level 2", level_2)
menu.add.button("Level 3", level_1)
menu.add.button("Level 4", level_1)

game_over = False

score = 0

while True:
    # check events to handle quitting and level start
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.USEREVENT:
            score = 0
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
                    score += 20
                    # print(f"near miss! score = {score}")
                elif pygame.Rect(position + 40, 720, 20, 45).colliderect(note.rect) or pygame.Rect(position - 40, 720, 20, 45).colliderect(note.rect):
                    score += 10
                    # print(f"close! score = {score}")
                elif pygame.Rect(position + 60, 720, 20, 45).colliderect(note.rect) or pygame.Rect(position - 60, 720, 20, 45).colliderect(note.rect):
                    score += 5
                    # print(f"about, score = {score}")
                
                if note.rect.collidepoint(30, 750):
                    render_keys.append((left_key, (8, 758)))
                elif note.rect.collidepoint(60, 750):
                    render_keys.append((black_key, (45, 758)))
                elif note.rect.collidepoint(90, 750):
                    render_keys.append((middle_key, (68, 758)))
                elif note.rect.collidepoint(120, 750):
                    render_keys.append((black_key, (105, 758)))
                elif note.rect.collidepoint(150, 750):
                    render_keys.append((right_key, (128, 758)))
                elif note.rect.collidepoint(210, 750):
                    render_keys.append((left_key, (188, 758)))
                elif note.rect.collidepoint(240, 750):
                    render_keys.append((black_key, (225, 758)))
                elif note.rect.collidepoint(270, 750):
                    render_keys.append((middle_key, (248, 758)))
                elif note.rect.collidepoint(300, 750):
                    render_keys.append((black_key, (285, 758)))
                elif note.rect.collidepoint(330, 750):
                    render_keys.append((middle_key, (308, 758)))
                elif note.rect.collidepoint(360, 750):
                    render_keys.append((black_key, (345, 758)))
                elif note.rect.collidepoint(390, 750):
                    render_keys.append((right_key, (368, 758)))
                elif note.rect.collidepoint(450, 750):
                    render_keys.append((left_key, (428, 758)))
                elif note.rect.collidepoint(480, 750):
                    render_keys.append((black_key, (465, 758)))
                elif note.rect.collidepoint(510, 750):
                    render_keys.append((middle_key, (488, 758)))
                elif note.rect.collidepoint(540, 750):
                    render_keys.append((black_key, (525, 758)))
                elif note.rect.collidepoint(570, 750):
                    render_keys.append((right_key, (548, 758)))
                elif note.rect.collidepoint(630, 750):
                    render_keys.append((left_key, (608, 758)))
                elif note.rect.collidepoint(660, 750):
                    render_keys.append((black_key, (645, 758)))
                elif note.rect.collidepoint(690, 750):
                    render_keys.append((right_key, (668, 758)))
        if game_over:
            render_keys = []
            LEVEL[1] = 0
            print("game over!")

        if LEVEL[1] == 100:
            pygame.mixer.music.load("golf clap.mp3")
            pygame.mixer.music.play()
        if LEVEL[1] == 0:
            LEVEL[0] = 0
            pygame.mixer.music.fadeout(1500)
            if game_over:
                game_over = False
                # show loss menu
                score = 0
            # else: 
                # show win menu
            menu.enable()

    screen.blit(piano, (0, 750))
    for key in render_keys:
        screen.blit(key[0], key[1])
    score_text = pygame.font.Font(None, 32).render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    if menu.is_enabled():
        menu.update(events)
    if menu.is_enabled():
        menu.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60, apparently