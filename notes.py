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
    [0, 375, F4, -650], 
    [0, 375, A4, -650], 
    [0, 375, C5, -650], 
    [0, 375, E5, -650],
    # Em7
    [0, 375, E4, -375 * (3 + 2/3) -650], 
    [0, 375, G4, -375 * (3 + 2/3) -650],
    [0, 375, B4, -375 * (3 + 2/3) -650],
    [0, 375, D5, -375 * (3 + 2/3) -650],
    [0, 375, E5, -375 * (3 + 2/3) -650],
    # Dm9
    [0, 375, D4, -375 * (8) -650],
    [0, 375, F4, -375 * (8) -650],
    [0, 375, A4, -375 * (8) -650],
    [0, 375, C5, -375 * (8) -650],
    [0, 375, E5, -375 * (8) -650],
    # G7/D
    [0, 375, D4, -375 * (9 + 2/3) -650],
    [0, 375, F4, -375 * (9 + 2/3) -650],
    [0, 375, G4, -375 * (9 + 2/3) -650],
    [0, 375, B4, -375 * (9 + 2/3) -650],
    [0, 375, D5, -375 * (9 + 2/3) -650],
    # CM7
    [0, 375, C4, -375 * (11 + 2/3) -650],
    [0, 375, E4, -375 * (11 + 2/3) -650],
    [0, 375, G4, -375 * (11 + 2/3) -650],
    [0, 375, B4, -375 * (11 + 2/3) -650],
    [0, 375, E5, -375 * (11 + 2/3) -650]
]

level_2_bar_length = -248 # in pixels

level_2_notelist = [
    # GbM7
    [1, 80, Gb4, level_2_bar_length * (2) - 650],
    [1, 80, Bb4, level_2_bar_length * (2) - 650],
    [1, 80, Db5, level_2_bar_length * (2) - 650],
    [0, 80, F5, level_2_bar_length * (2) - 650],
    # the same exact thing
    [1, 80, Gb4, level_2_bar_length * (6) - 650],
    [1, 80, Bb4, level_2_bar_length * (6) - 650],
    [1, 80, Db5, level_2_bar_length * (6) - 650],
    [0, 80, F5, level_2_bar_length * (6) - 650],
    # Fm7
    [0, 80, F4, level_2_bar_length * (10) - 650],
    [1, 80, Ab4, level_2_bar_length * (10) - 650],
    [0, 80, C5, level_2_bar_length * (10) - 650],
    [1, 80, Eb5, level_2_bar_length * (10) - 650],
    [0, 80, F5, level_2_bar_length * (10) - 650],
    # F7!
    [0, 80, F4, level_2_bar_length * (14) - 650],
    [0, 80, A4, level_2_bar_length * (14) - 650],
    [0, 80, C5, level_2_bar_length * (14) - 650],
    [1, 80, Eb5, level_2_bar_length * (14) - 650],
    [0, 80, F5, level_2_bar_length * (14) - 650],
    # Ebm9
    [1, 80, Eb4, level_2_bar_length * (18) - 650],
    [1, 80, Gb4, level_2_bar_length * (18) - 650],
    [1, 80, Bb4, level_2_bar_length * (18) - 650],
    [1, 80, Db5, level_2_bar_length * (18) - 650],
    [0, 80, F5, level_2_bar_length * (18) - 650],
    # Ab6 (no /Eb the first time)
    [1, 80, Ab4, level_2_bar_length * (22) - 650],
    [0, 80, C5, level_2_bar_length * (22) - 650],
    [1, 80, Eb5, level_2_bar_length * (22) - 650],
    [0, 80, F5, level_2_bar_length * (22) - 650],
    # DbM9
    [1, 80 * 3, Db4, level_2_bar_length * (24 + 2/3) - 650],
    [0, 80 * 3, F4, level_2_bar_length * (24 + 2/3) - 650],
    [1, 80 * 3, Ab4, level_2_bar_length * (24 + 2/3) - 650],
    [0, 80 * 3, C5, level_2_bar_length * (24 + 2/3) - 650],
    [1, 80 * 3, Eb5, level_2_bar_length * (24 + 2/3) - 650],
    # C7
    [0, 80 * 4, C4, level_2_bar_length * (26 + 2/3) - 650],
    [0, 80 * 4, E4, level_2_bar_length * (26 + 2/3) - 650],
    [0, 80 * 4, G4, level_2_bar_length * (26 + 2/3) - 650],
    [1, 80 * 4, Bb4, level_2_bar_length * (26 + 2/3) - 650],
    [0, 80 * 4, C5, level_2_bar_length * (26 + 2/3) - 650],
    [0, 80 * 4, E5, level_2_bar_length * (26 + 2/3) - 650],
    [0, 80 * 4, G5, level_2_bar_length * (26 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [1, 80, Eb4, level_2_bar_length * (28 + 2/3) - 650],
    [1, 80, Gb4, level_2_bar_length * (28 + 2/3) - 650],
    [1, 80, Bb4, level_2_bar_length * (28 + 2/3) - 650],
    [1, 80, Db5, level_2_bar_length * (28 + 2/3) - 650],
    [0, 80, F5, level_2_bar_length * (28 + 2/3) - 650],

    # FM7
    [1, 240 * 2, Gb4, level_2_bar_length * (34) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (34) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (34) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (34) - 650],

    [1, 240 * 2, Gb4, level_2_bar_length * (38) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (38) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (38) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (38) - 650],
    # Fm7
    [0, 240 * 2, F4, level_2_bar_length * (42) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (42) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (42) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (42) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (42) - 650],
    # F7
    [0, 240 * 2, F4, level_2_bar_length * (46) - 650],
    [0, 240 * 2, A4, level_2_bar_length * (46) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (46) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (46) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (46) - 650],
    # Ebm9
    [1, 240 * 2, Eb4, level_2_bar_length * (50) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (50) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (50) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (50) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (50) - 650],
    # Ab6/Eb
    [1, 240 * 2, Eb4, level_2_bar_length * (54) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (54) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (54) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (54) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (54) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (54) - 650],
    # DbM9
    [1, 80 * 3, Db4, level_2_bar_length * (56 + 2/3) - 650],
    [0, 80 * 3, F4, level_2_bar_length * (56 + 2/3) - 650],
    [1, 80 * 3, Ab4, level_2_bar_length * (56 + 2/3) - 650],
    [0, 80 * 3, C5, level_2_bar_length * (56 + 2/3) - 650],
    [1, 80 * 3, Eb5, level_2_bar_length * (56 + 2/3) - 650],
    # C7
    [0, 80 * 4, C4, level_2_bar_length * (58 + 2/3) - 650],
    [0, 80 * 4, E4, level_2_bar_length * (58 + 2/3) - 650],
    [0, 80 * 4, G4, level_2_bar_length * (58 + 2/3) - 650],
    [1, 80 * 4, Bb4, level_2_bar_length * (58 + 2/3) - 650],
    [0, 80 * 4, C5, level_2_bar_length * (58 + 2/3) - 650],
    [0, 80 * 4, E5, level_2_bar_length * (58 + 2/3) - 650],
    [0, 80 * 4, G5, level_2_bar_length * (58 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [1, 80, Eb4, level_2_bar_length * (60 + 2/3) - 650],
    [1, 80, Gb4, level_2_bar_length * (60 + 2/3) - 650],
    [1, 80, Bb4, level_2_bar_length * (60 + 2/3) - 650],
    [1, 80, Db5, level_2_bar_length * (60 + 2/3) - 650],
    [0, 80, F5, level_2_bar_length * (60 + 2/3) - 650],

    # FM7
    [1, 240 * 2, Gb4, level_2_bar_length * (66) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (66) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (66) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (66) - 650],

    [1, 240 * 2, Gb4, level_2_bar_length * (70) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (70) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (70) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (70) - 650],
    # Fm7
    [0, 240 * 2, F4, level_2_bar_length * (74) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (74) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (74) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (74) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (74) - 650],
    # F7
    [0, 240 * 2, F4, level_2_bar_length * (78) - 650],
    [0, 240 * 2, A4, level_2_bar_length * (78) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (78) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (78) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (78) - 650],
    # Ebm9
    [1, 240 * 2, Eb4, level_2_bar_length * (82) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (82) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (82) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (82) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (82) - 650],
    # Ab6/Eb
    [1, 240 * 2, Eb4, level_2_bar_length * (86) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (86) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (86) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (86) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (86) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (86) - 650],
    # DbM9
    [1, 80 * 3, Db4, level_2_bar_length * (88 + 2/3) - 650],
    [0, 80 * 3, F4, level_2_bar_length * (88 + 2/3) - 650],
    [1, 80 * 3, Ab4, level_2_bar_length * (88 + 2/3) - 650],
    [0, 80 * 3, C5, level_2_bar_length * (88 + 2/3) - 650],
    [1, 80 * 3, Eb5, level_2_bar_length * (88 + 2/3) - 650],
    # C7
    [0, 80 * 4, C4, level_2_bar_length * (90 + 2/3) - 650],
    [0, 80 * 4, E4, level_2_bar_length * (90 + 2/3) - 650],
    [0, 80 * 4, G4, level_2_bar_length * (90 + 2/3) - 650],
    [1, 80 * 4, Bb4, level_2_bar_length * (90 + 2/3) - 650],
    [0, 80 * 4, C5, level_2_bar_length * (90 + 2/3) - 650],
    [0, 80 * 4, E5, level_2_bar_length * (90 + 2/3) - 650],
    [0, 80 * 4, G5, level_2_bar_length * (90 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [1, 80, Eb4, level_2_bar_length * (92 + 2/3) - 650],
    [1, 80, Gb4, level_2_bar_length * (92 + 2/3) - 650],
    [1, 80, Bb4, level_2_bar_length * (92 + 2/3) - 650],
    [1, 80, Db5, level_2_bar_length * (92 + 2/3) - 650],
    [0, 80, F5, level_2_bar_length * (92 + 2/3) - 650],
        
    # FM7
    [1, 240 * 2, Gb4, level_2_bar_length * (98) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (98) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (98) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (98) - 650],

    [1, 240 * 2, Gb4, level_2_bar_length * (102) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (102) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (102) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (102) - 650],
    # Fm7
    [0, 240 * 2, F4, level_2_bar_length * (106) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (106) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (106) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (106) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (106) - 650],
    # F7
    [0, 240 * 2, F4, level_2_bar_length * (110) - 650],
    [0, 240 * 2, A4, level_2_bar_length * (110) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (110) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (110) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (110) - 650],
    # Ebm9
    [1, 240 * 2, Eb4, level_2_bar_length * (114) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (114) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (114) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (114) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (114) - 650],
    # Ab6/Eb
    [1, 240 * 2, Eb4, level_2_bar_length * (118) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (118) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (118) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (118) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (118) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (118) - 650],
    # DbM9
    [1, 80 * 3, Db4, level_2_bar_length * (120 + 2/3) - 650],
    [0, 80 * 3, F4, level_2_bar_length * (120 + 2/3) - 650],
    [1, 80 * 3, Ab4, level_2_bar_length * (120 + 2/3) - 650],
    [0, 80 * 3, C5, level_2_bar_length * (120 + 2/3) - 650],
    [1, 80 * 3, Eb5, level_2_bar_length * (120 + 2/3) - 650],
    # C7
    [0, 80 * 4, C4, level_2_bar_length * (122 + 2/3) - 650],
    [0, 80 * 4, E4, level_2_bar_length * (122 + 2/3) - 650],
    [0, 80 * 4, G4, level_2_bar_length * (122 + 2/3) - 650],
    [1, 80 * 4, Bb4, level_2_bar_length * (122 + 2/3) - 650],
    [0, 80 * 4, C5, level_2_bar_length * (122 + 2/3) - 650],
    [0, 80 * 4, E5, level_2_bar_length * (122 + 2/3) - 650],
    [0, 80 * 4, G5, level_2_bar_length * (122 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [1, 80, Eb4, level_2_bar_length * (124 + 2/3) - 650],
    [1, 80, Gb4, level_2_bar_length * (124 + 2/3) - 650],
    [1, 80, Bb4, level_2_bar_length * (124 + 2/3) - 650],
    [1, 80, Db5, level_2_bar_length * (124 + 2/3) - 650],
    [0, 80, F5, level_2_bar_length * (124 + 2/3) - 650],

    # FM7
    [1, 240 * 2, Gb4, level_2_bar_length * (130) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (130) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (130) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (130) - 650],

    [1, 240 * 2, Gb4, level_2_bar_length * (134) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (134) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (134) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (134) - 650],
    # Fm7
    [0, 240 * 2, F4, level_2_bar_length * (138) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (138) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (138) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (138) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (138) - 650],
    # F7
    [0, 240 * 2, F4, level_2_bar_length * (142) - 650],
    [0, 240 * 2, A4, level_2_bar_length * (142) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (142) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (142) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (142) - 650],
    # Ebm9
    [1, 240 * 2, Eb4, level_2_bar_length * (146) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (146) - 650],
    [1, 240 * 2, Bb4, level_2_bar_length * (146) - 650],
    [1, 240 * 2, Db5, level_2_bar_length * (146) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (146) - 650],
    # Ab6/Eb
    [1, 240 * 2, Eb4, level_2_bar_length * (150) - 650],
    [1, 240 * 2, Gb4, level_2_bar_length * (150) - 650],
    [1, 240 * 2, Ab4, level_2_bar_length * (150) - 650],
    [0, 240 * 2, C5, level_2_bar_length * (150) - 650],
    [1, 240 * 2, Eb5, level_2_bar_length * (150) - 650],
    [0, 240 * 2, F5, level_2_bar_length * (150) - 650],
    # DbM9
    [1, 80 * 3, Db4, level_2_bar_length * (152 + 2/3) - 650],
    [0, 80 * 3, F4, level_2_bar_length * (152 + 2/3) - 650],
    [1, 80 * 3, Ab4, level_2_bar_length * (152 + 2/3) - 650],
    [0, 80 * 3, C5, level_2_bar_length * (152 + 2/3) - 650],
    [1, 80 * 3, Eb5, level_2_bar_length * (152 + 2/3) - 650],
    # C7
    [0, 80 * 4, C4, level_2_bar_length * (154 + 2/3) - 650],
    [0, 80 * 4, E4, level_2_bar_length * (154 + 2/3) - 650],
    [0, 80 * 4, G4, level_2_bar_length * (154 + 2/3) - 650],
    [1, 80 * 4, Bb4, level_2_bar_length * (154 + 2/3) - 650],
    [0, 80 * 4, C5, level_2_bar_length * (154 + 2/3) - 650],
    [0, 80 * 4, E5, level_2_bar_length * (154 + 2/3) - 650],
    [0, 80 * 4, G5, level_2_bar_length * (154 + 2/3) - 650],
    # BM9 (but both sides are cut off)
    [1, 80, Eb4, level_2_bar_length * (156 + 2/3) - 650],
    [1, 80, Gb4, level_2_bar_length * (156 + 2/3) - 650],
    [1, 80, Bb4, level_2_bar_length * (156 + 2/3) - 650],
    [1, 80, Db5, level_2_bar_length * (156 + 2/3) - 650],
    [0, 80, F5, level_2_bar_length * (156 + 2/3) - 650],
    # ending
    [1, 80, Gb5, level_2_bar_length * 160 - 690],
    [1, 80, Db5, level_2_bar_length * 160 - 690],
    [1, 80, Db5, level_2_bar_length * 162 - 680],
    [1, 80, Gb4, level_2_bar_length * 162 - 680],
    [1, 80, Gb4, level_2_bar_length * 164 - 670],
    [1, 80, Db4, level_2_bar_length * 164 - 670],

    # the lead 
    [3, 80, Eb4, level_2_bar_length * (30 + 2/3) - 650],
    [3, 80, Db4, level_2_bar_length * (31) - 650],

    [3, 80, Eb4, level_2_bar_length * (34 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (35 + 0/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (35 + 1/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (35 + 2/3) - 650],
    [3, 400, Eb4, level_2_bar_length * (36) - 650],
    [3, 80, Db4, level_2_bar_length * (38) - 650],
    [2, 160, F4, level_2_bar_length * (38 + 2/3) - 650],
    [2, 80, E4, level_2_bar_length * (39 + 2/3) - 650],
    [3, 400, Eb4, level_2_bar_length * (40) - 650],
    [2, 320, F4, level_2_bar_length * (42) - 650],
    [3, 20, Gb4, level_2_bar_length * (42 + 0.04) - 650],
    [2, 300, F4, level_2_bar_length * (43 + 2/3) - 650],
    [3, 40, Ab4, level_2_bar_length * (43 + 5/6) - 650],
    [2, 40, A4, level_2_bar_length * (46 + 1/6) - 650],
    [3, 880, Bb4, level_2_bar_length * (46 + 1/3) - 650],
    [2, 80, C5, level_2_bar_length * (50 + 0/3) - 650],
    [3, 80, Bb4, level_2_bar_length * (50 + 1/3) - 650],
    [2, 80, A4, level_2_bar_length * (50 + 2/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (51 + 0/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (51 + 1/3) - 650],
    [2, 480, F4, level_2_bar_length * (51 + 2/3) - 650],
    [3, 320, Eb4, level_2_bar_length * (54) - 650],
    [3, 80, Db4, level_2_bar_length * (55 + 2/3) - 650],
    [2, 400, F4, level_2_bar_length * (56 + 2/3) - 650],
    [2, 400, G4, level_2_bar_length * (58 + 2/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (60 + 2/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (62 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (63) - 650],

    [3, 80, Db4, level_2_bar_length * (67 + 2/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (68 + 0/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (68 + 1/3) - 650],
    [2, 80, F4, level_2_bar_length * (68 + 2/3) - 650],
    [3, 240, Eb4, level_2_bar_length * (69) - 650],
    [3, 80, Db4, level_2_bar_length * (71) - 650],
    [2, 80, F4, level_2_bar_length * (71 + 0.7) - 650],
    [3, 80, Eb4, level_2_bar_length * (72 + 0.5) - 650],
    [3, 80, Db4, level_2_bar_length * (73 + 0.4) - 650],
    [2, 560, C4, level_2_bar_length * (74 + 1/3) - 650],
    [3, 160, Eb4, level_2_bar_length * (76 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (77 + 2/3) - 650],
    [3, 720, Gb4, level_2_bar_length * (78) - 650],
    [3, 80, Bb4, level_2_bar_length * (82 + 0/3) - 650],
    [2, 80, C5, level_2_bar_length * (82 + 1/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (82 + 2/3) - 650],
    [2, 640, F4, level_2_bar_length * (83) - 650],
    [3, 80, Gb4, level_2_bar_length * (86 + 0/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (86 + 1/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (86 + 2/3) - 650],
    [2, 240, F4, level_2_bar_length * (87) - 650],
    [3, 400, Eb4, level_2_bar_length * (88 + 2/3) - 650],
    [2, 400, E4, level_2_bar_length * (90 + 2/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (92 + 2/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (94 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (95) - 650],
    [3, 80, Eb4, level_2_bar_length * (94 + 2/3) - 650],
    [3, 80, Db4, level_2_bar_length * (95) - 650],

    [3, 40, Gb4, level_2_bar_length * (101 + 5/6) - 650],
    [3, 80, Ab4, level_2_bar_length * (102) - 650],
    [3, 80, Gb4, level_2_bar_length * (102 + 2/3) - 650],
    [2, 160, F4, level_2_bar_length * (103) - 650],
    [2, 80, F4, level_2_bar_length * (106) - 650],
    [3, 80, Gb4, level_2_bar_length * (106 + 5/6) - 650],
    [2, 80, F4, level_2_bar_length * (107 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (110) - 650],
    [2, 80, A4, level_2_bar_length * (110 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (111 + 1/2) - 650],
    [2, 80, F4, level_2_bar_length * (114) - 650],
    [3, 80, Bb4, level_2_bar_length * (114 + 7/8) - 650],
    [2, 80, F4, level_2_bar_length * (115 + 2/3) - 650],    
    [3, 40, Gb4, level_2_bar_length * (117 + 5/6) - 650],
    [3, 80, Ab4, level_2_bar_length * (118) - 650],
    [3, 80, Gb4, level_2_bar_length * (118 + 2/3) - 650],
    [2, 160, F4, level_2_bar_length * (119) - 650],
    [3, 400, Eb4, level_2_bar_length * (120 + 2/3) - 650],
    [2, 400, G4, level_2_bar_length * (122 + 2/3) - 650],
    [3, 80, Ab4, level_2_bar_length * (124 + 2/3) - 650],
    [3, 80, Gb4, level_2_bar_length * (126 + 2/3) - 650],
    [2, 80, F4, level_2_bar_length * (127) - 650],
]