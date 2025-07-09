# note -> x position key:
C4 = 8
Db4 = 45
D4 = 68
Eb4 = 105
E4 = 128
F4 = 188
Gb4 = 225
G4 = 248
Ab4 = 285
A4 = 308
Bb4 = 345
B4 = 368
C5 = 428
Db5 = 465
D5 = 488
Eb5 = 525
E5 = 548
F5 = 608
Gb5 = 645
G5 = 668 

level_1_notelist = [
    # FM7
    [True, 375, F4, -650], 
    [True, 375, A4, -650], 
    [True, 375, C5, -650], 
    [True, 375, E5, -650],
    # Em7
    [True, 375, E4, -375 * (3 + 2/3) -650], 
    [True, 375, G4, -375 * (3 + 2/3) -650],
    [True, 375, B4, -375 * (3 + 2/3) -650],
    [True, 375, D5, -375 * (3 + 2/3) -650],
    [True, 375, E5, -375 * (3 + 2/3) -650],
    # Dm9
    [True, 375, D4, -375 * (8) -650],
    [True, 375, F4, -375 * (8) -650],
    [True, 375, A4, -375 * (8) -650],
    [True, 375, C5, -375 * (8) -650],
    [True, 375, E5, -375 * (8) -650],
    # G7/D
    [True, 375, D4, -375 * (9 + 2/3) -650],
    [True, 375, F4, -375 * (9 + 2/3) -650],
    [True, 375, G4, -375 * (9 + 2/3) -650],
    [True, 375, B4, -375 * (9 + 2/3) -650],
    [True, 375, D5, -375 * (9 + 2/3) -650],
    # CM7
    [True, 375, C4, -375 * (11 + 2/3) -650],
    [True, 375, E4, -375 * (11 + 2/3) -650],
    [True, 375, G4, -375 * (11 + 2/3) -650],
    [True, 375, B4, -375 * (11 + 2/3) -650],
    [True, 375, E5, -375 * (11 + 2/3) -650]
]

level_2_bar_length = -243 # in pixels

level_2_notelist = [
    # GbM7
    [False, 80, Gb4, level_2_bar_length * (2) - 650],
    [False, 80, Bb4, level_2_bar_length * (2) - 650],
    [False, 80, Db5, level_2_bar_length * (2) - 650],
    [True, 80, F5, level_2_bar_length * (2) - 650],
    # the same exact thing
    [False, 80, Gb4, level_2_bar_length * (6) - 650],
    [False, 80, Bb4, level_2_bar_length * (6) - 650],
    [False, 80, Db5, level_2_bar_length * (6) - 650],
    [True, 80, F5, level_2_bar_length * (6) - 650],
    # Fm7
    [True, 80, F4, level_2_bar_length * (10) - 650],
    [False, 80, Ab4, level_2_bar_length * (10) - 650],
    [True, 80, C5, level_2_bar_length * (10) - 650],
    [False, 80, Eb5, level_2_bar_length * (10) - 650],
    [True, 80, F5, level_2_bar_length * (10) - 650],
    # F7!
    [True, 80, F4, level_2_bar_length * (14) - 650],
    [True, 80, A4, level_2_bar_length * (14) - 650],
    [True, 80, C5, level_2_bar_length * (14) - 650],
    [False, 80, Eb5, level_2_bar_length * (14) - 650],
    [True, 80, F5, level_2_bar_length * (14) - 650],
    # Ebm9
    [False, 80, Eb4, level_2_bar_length * (18) - 650],
    [False, 80, Gb4, level_2_bar_length * (18) - 650],
    [False, 80, Bb4, level_2_bar_length * (18) - 650],
    [False, 80, Db5, level_2_bar_length * (18) - 650],
    [True, 80, F5, level_2_bar_length * (18) - 650],
    # Ab6 (no /Eb the first time)
    [False, 80, Ab4, level_2_bar_length * (22) - 650],
    [True, 80, C5, level_2_bar_length * (22) - 650],
    [False, 80, Eb5, level_2_bar_length * (22) - 650],
    [True, 80, F5, level_2_bar_length * (22) - 650],
    # DbM9
    [False, 80 * 3, Db4, level_2_bar_length * (24 + 2/3) - 650],
    [True, 80 * 3, F4, level_2_bar_length * (24 + 2/3) - 650],
    [False, 80 * 3, Ab4, level_2_bar_length * (24 + 2/3) - 650],
    [True, 80 * 3, C5, level_2_bar_length * (24 + 2/3) - 650],
    [False, 80 * 3, Eb5, level_2_bar_length * (24 + 2/3) - 650],
    # C7
    [True, 80 * 4, C4, level_2_bar_length * (26 + 2/3) - 650],
    [True, 80 * 4, E4, level_2_bar_length * (26 + 2/3) - 650],
    [True, 80 * 4, G4, level_2_bar_length * (26 + 2/3) - 650],
    [False, 80 * 4, Bb4, level_2_bar_length * (26 + 2/3) - 650],
    [True, 80 * 4, C5, level_2_bar_length * (26 + 2/3) - 650],
    [True, 80 * 4, E5, level_2_bar_length * (26 + 2/3) - 650],
    [True, 80 * 4, G5, level_2_bar_length * (26 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [False, 80, Eb4, level_2_bar_length * (28 + 2/3) - 650],
    [False, 80, Gb4, level_2_bar_length * (28 + 2/3) - 650],
    [False, 80, Bb4, level_2_bar_length * (28 + 2/3) - 650],
    [False, 80, Db5, level_2_bar_length * (28 + 2/3) - 650],
    [True, 80, F5, level_2_bar_length * (28 + 2/3) - 650],

    # FM7
    [False, 240 * 2, Gb4, level_2_bar_length * (35) - 690],
    [False, 240 * 2, Bb4, level_2_bar_length * (35) - 690],
    [False, 240 * 2, Db5, level_2_bar_length * (35) - 690],
    [True, 240 * 2, F5, level_2_bar_length * (35) - 690],

    [False, 240 * 2, Gb4, level_2_bar_length * (39) - 670],
    [False, 240 * 2, Bb4, level_2_bar_length * (39) - 670],
    [False, 240 * 2, Db5, level_2_bar_length * (39) - 670],
    [True, 240 * 2, F5, level_2_bar_length * (39) - 670],
    # Fm7
    [True, 240 * 2, F4, level_2_bar_length * (43) - 650],
    [False, 240 * 2, Ab4, level_2_bar_length * (43) - 650],
    [True, 240 * 2, C5, level_2_bar_length * (43) - 650],
    [False, 240 * 2, Eb5, level_2_bar_length * (43) - 650],
    [True, 240 * 2, F5, level_2_bar_length * (43) - 650],
    # F7
    [True, 240 * 2, F4, level_2_bar_length * (47) - 650],
    [True, 240 * 2, A4, level_2_bar_length * (47) - 650],
    [True, 240 * 2, C5, level_2_bar_length * (47) - 650],
    [False, 240 * 2, Eb5, level_2_bar_length * (47) - 650],
    [True, 240 * 2, F5, level_2_bar_length * (47) - 650],
    # Ebm9
    [False, 240 * 2, Eb4, level_2_bar_length * (51) - 650],
    [False, 240 * 2, Gb4, level_2_bar_length * (51) - 650],
    [False, 240 * 2, Bb4, level_2_bar_length * (51) - 650],
    [False, 240 * 2, Db5, level_2_bar_length * (51) - 650],
    [True, 240 * 2, F5, level_2_bar_length * (51) - 650],
    # Ab6/Eb
    [False, 240 * 2, Eb4, level_2_bar_length * (55) - 650],
    [False, 240 * 2, Gb4, level_2_bar_length * (55) - 650],
    [False, 240 * 2, Ab4, level_2_bar_length * (55) - 650],
    [True, 240 * 2, C5, level_2_bar_length * (55) - 650],
    [False, 240 * 2, Eb5, level_2_bar_length * (55) - 650],
    [True, 240 * 2, F5, level_2_bar_length * (55) - 650],
    # DbM9
    [False, 80 * 3, Db4, level_2_bar_length * (57 + 2/3) - 650],
    [True, 80 * 3, F4, level_2_bar_length * (57 + 2/3) - 650],
    [False, 80 * 3, Ab4, level_2_bar_length * (57 + 2/3) - 650],
    [True, 80 * 3, C5, level_2_bar_length * (57 + 2/3) - 650],
    [False, 80 * 3, Eb5, level_2_bar_length * (57 + 2/3) - 650],
    # C7
    [True, 80 * 4, C4, level_2_bar_length * (59 + 2/3) - 650],
    [True, 80 * 4, E4, level_2_bar_length * (59 + 2/3) - 650],
    [True, 80 * 4, G4, level_2_bar_length * (59 + 2/3) - 650],
    [False, 80 * 4, Bb4, level_2_bar_length * (59 + 2/3) - 650],
    [True, 80 * 4, C5, level_2_bar_length * (59 + 2/3) - 650],
    [True, 80 * 4, E5, level_2_bar_length * (59 + 2/3) - 650],
    [True, 80 * 4, G5, level_2_bar_length * (59 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [False, 80, Eb4, level_2_bar_length * (61 + 2/3) - 650],
    [False, 80, Gb4, level_2_bar_length * (61 + 2/3) - 650],
    [False, 80, Bb4, level_2_bar_length * (61 + 2/3) - 650],
    [False, 80, Db5, level_2_bar_length * (61 + 2/3) - 650],
    [True, 80, F5, level_2_bar_length * (61 + 2/3) - 650],

    # FM7
    [False, 240 * 2, Gb4, level_2_bar_length * (68) - 570],
    [False, 240 * 2, Bb4, level_2_bar_length * (68) - 570],
    [False, 240 * 2, Db5, level_2_bar_length * (68) - 570],
    [True, 240 * 2, F5, level_2_bar_length * (68) - 570],

    [False, 240 * 2, Gb4, level_2_bar_length * (72) - 590],
    [False, 240 * 2, Bb4, level_2_bar_length * (72) - 590],
    [False, 240 * 2, Db5, level_2_bar_length * (72) - 590],
    [True, 240 * 2, F5, level_2_bar_length * (72) - 590],
    # Fm7
    [True, 240 * 2, F4, level_2_bar_length * (76) - 610],
    [False, 240 * 2, Ab4, level_2_bar_length * (76) - 610],
    [True, 240 * 2, C5, level_2_bar_length * (76) - 610],
    [False, 240 * 2, Eb5, level_2_bar_length * (76) - 610],
    [True, 240 * 2, F5, level_2_bar_length * (76) - 610],
    # F7
    [True, 240 * 2, F4, level_2_bar_length * (80) - 630],
    [True, 240 * 2, A4, level_2_bar_length * (80) - 630],
    [True, 240 * 2, C5, level_2_bar_length * (80) - 630],
    [False, 240 * 2, Eb5, level_2_bar_length * (80) - 630],
    [True, 240 * 2, F5, level_2_bar_length * (80) - 630],
    # Ebm9
    [False, 240 * 2, Eb4, level_2_bar_length * (84) - 650],
    [False, 240 * 2, Gb4, level_2_bar_length * (84) - 650],
    [False, 240 * 2, Bb4, level_2_bar_length * (84) - 650],
    [False, 240 * 2, Db5, level_2_bar_length * (84) - 650],
    [True, 240 * 2, F5, level_2_bar_length * (84) - 650],
    # Ab6/Eb
    [False, 240 * 2, Eb4, level_2_bar_length * (88) - 650],
    [False, 240 * 2, Gb4, level_2_bar_length * (88) - 650],
    [False, 240 * 2, Ab4, level_2_bar_length * (88) - 650],
    [True, 240 * 2, C5, level_2_bar_length * (88) - 650],
    [False, 240 * 2, Eb5, level_2_bar_length * (88) - 650],
    [True, 240 * 2, F5, level_2_bar_length * (88) - 650],
    # DbM9
    [False, 80 * 3, Db4, level_2_bar_length * (90 + 2/3) - 650],
    [True, 80 * 3, F4, level_2_bar_length * (90 + 2/3) - 650],
    [False, 80 * 3, Ab4, level_2_bar_length * (90 + 2/3) - 650],
    [True, 80 * 3, C5, level_2_bar_length * (90 + 2/3) - 650],
    [False, 80 * 3, Eb5, level_2_bar_length * (90 + 2/3) - 650],
    # C7
    [True, 80 * 4, C4, level_2_bar_length * (92 + 2/3) - 650],
    [True, 80 * 4, E4, level_2_bar_length * (92 + 2/3) - 650],
    [True, 80 * 4, G4, level_2_bar_length * (92 + 2/3) - 650],
    [False, 80 * 4, Bb4, level_2_bar_length * (92 + 2/3) - 650],
    [True, 80 * 4, C5, level_2_bar_length * (92 + 2/3) - 650],
    [True, 80 * 4, E5, level_2_bar_length * (92 + 2/3) - 650],
    [True, 80 * 4, G5, level_2_bar_length * (92 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [False, 80, Eb4, level_2_bar_length * (94 + 2/3) - 650],
    [False, 80, Gb4, level_2_bar_length * (94 + 2/3) - 650],
    [False, 80, Bb4, level_2_bar_length * (94 + 2/3) - 650],
    [False, 80, Db5, level_2_bar_length * (94 + 2/3) - 650],
    [True, 80, F5, level_2_bar_length * (94 + 2/3) - 650],
]