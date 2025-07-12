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
    [3, 80, Gb4, level_2_bar_length * (30 + 2/3) - 650],
    [3, 80, F4, level_2_bar_length * (31) - 650],

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

level_4_bar_length = -144

level_4_notelist = [
    # Piano Chords
    [1, 144, Gb5, level_4_bar_length * (60) - 650],
    [1, 144, Db5, level_4_bar_length * (60) - 650],
    [0, 144, B4, level_4_bar_length * (60) - 650],
    [1, 144, Ab4, level_4_bar_length * (60) - 650],
    [0, 144, E4, level_4_bar_length * (60) - 650],

    [1, 144, Gb5, level_4_bar_length * (61 + 2/3) - 650],
    [1, 144, Eb5, level_4_bar_length * (61 + 2/3) - 650],
    [1, 144, Bb4, level_4_bar_length * (61 + 2/3) - 650],
    [1, 144, Ab4, level_4_bar_length * (61 + 2/3) - 650],
    [0, 144, E4, level_4_bar_length * (61 + 2/3) - 650],

    [1, 240, Gb5, level_4_bar_length * (64) - 650],
    [1, 240, Eb5, level_4_bar_length * (64) - 650],
    [1, 240, Db5, level_4_bar_length * (64) - 650],
    [1, 240, Bb4, level_4_bar_length * (64) - 650],
    [1, 240, Gb4, level_4_bar_length * (64) - 650],

    [0, 240, D5, level_4_bar_length * (66) - 650],
    [0, 240, B4, level_4_bar_length * (66) - 650],
    [1, 240, Gb4, level_4_bar_length * (66) - 650],
    [0, 240, E4, level_4_bar_length * (66) - 650],
    [0, 240, C4, level_4_bar_length * (66) - 650],

    [0, 240, B4, level_4_bar_length * (68) - 650],
    [0, 240, G4, level_4_bar_length * (68) - 650],
    [1, 240, Gb4, level_4_bar_length * (68) - 650],
    [0, 240, D4, level_4_bar_length * (68) - 650],

    [0, 144, G4, level_4_bar_length * (70) - 650],
    [0, 144, D4, level_4_bar_length * (70) - 650],
    [0, 144, C4, level_4_bar_length * (70) - 650],

    [1, 576, Bb4, level_4_bar_length * (71 + 2/3) - 650],
    [0, 576, G4, level_4_bar_length * (71 + 2/3) - 650],
    [0, 576, F4, level_4_bar_length * (71 + 2/3) - 650],
    [1, 576, Eb4, level_4_bar_length * (71 + 2/3) - 650],
    [1, 576, D4, level_4_bar_length * (71 + 2/3) - 650],

    [0, 144, B4, level_4_bar_length * (76) - 650],
    [0, 144, G4, level_4_bar_length * (76) - 650],
    [0, 144, D4, level_4_bar_length * (76) - 650],
    [0, 144, C4, level_4_bar_length * (76) - 650],

    [0, 240, A4, level_4_bar_length * (77 + 2/3) - 650],
    [1, 240, Gb4, level_4_bar_length * (77 + 2/3) - 650],
    [0, 240, E4, level_4_bar_length * (77 + 2/3) - 650],
    [0, 240, C4, level_4_bar_length * (77 + 2/3) - 650],

    [0, 240, D5, level_4_bar_length * (80) - 650],
    [0, 240, B4, level_4_bar_length * (80) - 650],
    [1, 240, Gb4, level_4_bar_length * (80) - 650],
    [0, 240, D4, level_4_bar_length * (80) - 650],

    [1, 240, Bb4, level_4_bar_length * (82) - 650],
    [0, 240, G4, level_4_bar_length * (82) - 650],
    [0, 240, D4, level_4_bar_length * (82) - 650],
    [0, 240, C4, level_4_bar_length * (82) - 650],

    [0, 240, G5, level_4_bar_length * (84) - 650],
    [0, 240, D5, level_4_bar_length * (84) - 650],
    [1, 240, Bb4, level_4_bar_length * (84) - 650],
    [0, 240, G4, level_4_bar_length * (84) - 650],
    [1, 240, Eb4, level_4_bar_length * (84) - 650],

    [1, 144, Eb5, level_4_bar_length * (86) - 650],
    [1, 144, Bb4, level_4_bar_length * (86) - 650],
    [1, 144, Ab4, level_4_bar_length * (86) - 650],
    [0, 144, E4, level_4_bar_length * (86) - 650],

    [1, 576, Gb5, level_4_bar_length * (87 + 2/3) - 650],
    [1, 576, Eb5, level_4_bar_length * (87 + 2/3) - 650],
    [1, 576, Db5, level_4_bar_length * (87 + 2/3) - 650],
    [1, 576, Bb4, level_4_bar_length * (87 + 2/3) - 650],
    [1, 576, Gb4, level_4_bar_length * (87 + 2/3) - 650],

    [0, 240, G5, level_4_bar_length * (92) - 650],
    [1, 240, Eb5, level_4_bar_length * (92) - 650],
    [0, 240, C5, level_4_bar_length * (92) - 650],
    [1, 240, Ab4, level_4_bar_length * (92) - 650],
    [0, 240, F4, level_4_bar_length * (92) - 650],

    [0, 144, F5, level_4_bar_length * (94) - 650],
    [0, 144, D5, level_4_bar_length * (94) - 650],
    [0, 144, C5, level_4_bar_length * (94) - 650],
    [1, 144, Ab4, level_4_bar_length * (94) - 650],
    [0, 144, F4, level_4_bar_length * (94) - 650],

    [1, 576, Bb4, level_4_bar_length * (95 + 2/3) - 650],
    [0, 576, G4, level_4_bar_length * (95 + 2/3) - 650],
    [0, 576, F4, level_4_bar_length * (95 + 2/3) - 650],
    [0, 576, D4, level_4_bar_length * (95 + 2/3) - 650],

    [0, 240, B4, level_4_bar_length * (100) - 650],
    [0, 240, G4, level_4_bar_length * (100) - 650],
    [0, 240, D4, level_4_bar_length * (100) - 650],
    [0, 240, C4, level_4_bar_length * (100) - 650],

    [0, 144, A4, level_4_bar_length * (102) - 650],
    [1, 144, Gb4, level_4_bar_length * (102) - 650],
    [0, 144, E4, level_4_bar_length * (102) - 650],
    [0, 144, C4, level_4_bar_length * (102) - 650],

    [0, 576, D5, level_4_bar_length * (103 + 2/3) - 650],
    [0, 576, A4, level_4_bar_length * (103 + 2/3) - 650],
    [1, 576, Gb4, level_4_bar_length * (103 + 2/3) - 650],
    [0, 576, D4, level_4_bar_length * (103 + 2/3) - 650],

    [1, 240, Eb5, level_4_bar_length * (108) - 650],
    [0, 240, B4, level_4_bar_length * (108) - 650],
    [1, 240, Ab4, level_4_bar_length * (108) - 650],
    [1, 240, Gb4, level_4_bar_length * (108) - 650],
    [0, 240, E4, level_4_bar_length * (108) - 650],

    [1, 144, Eb5, level_4_bar_length * (110) - 650],
    [1, 144, Bb4, level_4_bar_length * (110) - 650],
    [1, 144, Ab4, level_4_bar_length * (110) - 650],
    [0, 144, E4, level_4_bar_length * (110) - 650],

    [1, 576, Gb5, level_4_bar_length * (111 + 2/3) - 650],
    [1, 576, Eb5, level_4_bar_length * (111 + 2/3) - 650],
    [1, 576, Db5, level_4_bar_length * (111 + 2/3) - 650],
    [1, 576, Bb4, level_4_bar_length * (111 + 2/3) - 650],
    [1, 576, Gb4, level_4_bar_length * (111 + 2/3) - 650],

    [0, 240, G5, level_4_bar_length * (116) - 650],
    [1, 240, Eb5, level_4_bar_length * (116) - 650],
    [1, 240, Bb4, level_4_bar_length * (116) - 650],
    [1, 240, Ab4, level_4_bar_length * (116) - 650],
    [0, 240, F4, level_4_bar_length * (116) - 650],

    [0, 144, G5, level_4_bar_length * (118) - 650],
    [0, 144, D5, level_4_bar_length * (118) - 650],
    [0, 144, C5, level_4_bar_length * (118) - 650],
    [1, 144, Ab4, level_4_bar_length * (118) - 650],

    [0, 576, G5, level_4_bar_length * (119 + 2/3) - 650],
    [0, 576, F5, level_4_bar_length * (119 + 2/3) - 650],
    [0, 576, D5, level_4_bar_length * (119 + 2/3) - 650],
    [1, 576, Bb4, level_4_bar_length * (119 + 2/3) - 650],
    [1, 576, Eb4, level_4_bar_length * (119 + 2/3) - 650],

    [1, 144, Gb5, level_4_bar_length * (124) - 650],
    [1, 144, Db5, level_4_bar_length * (124) - 650],
    [0, 144, B4, level_4_bar_length * (124) - 650],
    [1, 144, Ab4, level_4_bar_length * (124) - 650],
    [0, 144, E4, level_4_bar_length * (124) - 650],

    [1, 144, Gb5, level_4_bar_length * (125 + 2/3) - 650],
    [1, 144, Eb5, level_4_bar_length * (125 + 2/3) - 650],
    [1, 144, Bb4, level_4_bar_length * (125 + 2/3) - 650],
    [1, 144, Ab4, level_4_bar_length * (125 + 2/3) - 650],
    [0, 144, E4, level_4_bar_length * (125 + 2/3) - 650],

    # these notes are the exact same as the piano chords, but shifted by 64 bars and 128 bars respectively by another python program
    [1, 144, 645, -18506], [1, 144, 465, -18506], [0, 144, 368, -18506], [1, 144, 285, -18506], [0, 144, 128, -18506], [1, 144, 645, -18746.0], [1, 144, 525, -18746.0], [1, 144, 345, -18746.0], [1, 144, 285, -18746.0], [0, 144, 128, -18746.0], [1, 240, 645, -19082], [1, 240, 525, -19082], [1, 240, 465, -19082], [1, 240, 345, -19082], [1, 240, 225, -19082], [0, 240, 488, -19370], [0, 240, 368, -19370], [1, 240, 225, -19370], [0, 240, 128, -19370], [0, 240, 8, -19370], [0, 240, 368, -19658], [0, 240, 248, -19658], [1, 240, 225, -19658], [0, 240, 68, -19658], [0, 144, 248, -19946], [0, 144, 68, -19946], [0, 144, 8, -19946], [1, 576, 345, -20186.0], [0, 576, 248, -20186.0], [0, 576, 188, -20186.0], [1, 576, 105, -20186.0], [1, 576, 68, -20186.0], [0, 144, 368, -20810], [0, 144, 248, -20810], [0, 144, 68, -20810], [0, 144, 8, -20810], [0, 240, 308, -21050.0], [1, 240, 225, -21050.0], [0, 240, 128, -21050.0], [0, 240, 8, -21050.0], [0, 240, 488, -21386], [0, 240, 368, -21386], [1, 240, 225, -21386], [0, 240, 68, -21386], [1, 240, 345, -21674], [0, 240, 248, -21674], [0, 240, 68, -21674], [0, 240, 8, -21674], [0, 240, 668, -21962], [0, 240, 488, -21962], [1, 240, 345, -21962], [0, 240, 248, -21962], [1, 240, 105, -21962], [1, 144, 525, -22250], [1, 144, 345, -22250], [1, 144, 285, -22250], [0, 144, 128, -22250], [1, 576, 645, -22490.0], [1, 576, 525, -22490.0], [1, 576, 465, -22490.0], [1, 576, 345, -22490.0], [1, 576, 225, -22490.0], [0, 240, 668, -23114], [1, 240, 525, -23114], [0, 240, 428, -23114], [1, 240, 285, -23114], [0, 240, 188, -23114], [0, 144, 608, -23402], [0, 144, 488, -23402], [0, 144, 428, -23402], [1, 144, 285, -23402], [0, 144, 188, -23402], [1, 576, 345, -23642.0], [0, 576, 248, -23642.0], [0, 576, 188, -23642.0], [0, 576, 68, -23642.0], [0, 240, 368, -24266], [0, 240, 248, -24266], [0, 240, 68, -24266], [0, 240, 8, -24266], [0, 144, 308, -24554], [1, 144, 225, -24554], [0, 144, 128, -24554], [0, 144, 8, -24554], [0, 576, 488, -24794.0], [0, 576, 308, -24794.0], [1, 576, 225, -24794.0], [0, 576, 68, -24794.0], [1, 240, 525, -25418], [0, 240, 368, -25418], [1, 240, 285, -25418], [1, 240, 225, -25418], [0, 240, 128, -25418], [1, 144, 525, -25706], [1, 144, 345, -25706], [1, 144, 285, -25706], [0, 144, 128, -25706], [1, 576, 645, -25946.0], [1, 576, 525, -25946.0], [1, 576, 465, -25946.0], [1, 576, 345, -25946.0], [1, 576, 225, -25946.0], [0, 240, 668, -26570], [1, 240, 525, -26570], [1, 240, 345, -26570], [1, 240, 285, -26570], [0, 240, 188, -26570], [0, 144, 668, -26858], [0, 144, 488, -26858], [0, 144, 428, -26858], [1, 144, 285, -26858], [0, 576, 668, -27098.0], [0, 576, 608, -27098.0], [0, 576, 488, -27098.0], [1, 576, 345, -27098.0], [1, 576, 105, -27098.0], [1, 144, 645, -27722], [1, 144, 465, -27722], [0, 144, 368, -27722], [1, 144, 285, -27722], [0, 144, 128, -27722], [1, 144, 645, -27962.0], [1, 144, 525, -27962.0], [1, 144, 345, -27962.0], [1, 144, 285, -27962.0], [0, 144, 128, -27962.0],
    [1, 144, 645, -27722], [1, 144, 465, -27722], [0, 144, 368, -27722], [1, 144, 285, -27722], [0, 144, 128, -27722], [1, 144, 645, -27962.0], [1, 144, 525, -27962.0], [1, 144, 345, -27962.0], [1, 144, 285, -27962.0], [0, 144, 128, -27962.0], [1, 240, 645, -28298], [1, 240, 525, -28298], [1, 240, 465, -28298], [1, 240, 345, -28298], [1, 240, 225, -28298], [0, 240, 488, -28586], [0, 240, 368, -28586], [1, 240, 225, -28586], [0, 240, 128, -28586], [0, 240, 8, -28586], [0, 240, 368, -28874], [0, 240, 248, -28874], [1, 240, 225, -28874], [0, 240, 68, -28874], [0, 144, 248, -29162], [0, 144, 68, -29162], [0, 144, 8, -29162], [1, 576, 345, -29402.0], [0, 576, 248, -29402.0], [0, 576, 188, -29402.0], [1, 576, 105, -29402.0], [1, 576, 68, -29402.0], [0, 144, 368, -30026], [0, 144, 248, -30026], [0, 144, 68, -30026], [0, 144, 8, -30026], [0, 240, 308, -30266.0], [1, 240, 225, -30266.0], [0, 240, 128, -30266.0], [0, 240, 8, -30266.0], [0, 240, 488, -30602], [0, 240, 368, -30602], [1, 240, 225, -30602], [0, 240, 68, -30602], [1, 240, 345, -30890], [0, 240, 248, -30890], [0, 240, 68, -30890], [0, 240, 8, -30890], [0, 240, 668, -31178], [0, 240, 488, -31178], [1, 240, 345, -31178], [0, 240, 248, -31178], [1, 240, 105, -31178], [1, 144, 525, -31466], [1, 144, 345, -31466], [1, 144, 285, -31466], [0, 144, 128, -31466], [1, 576, 645, -31706.0], [1, 576, 525, -31706.0], [1, 576, 465, -31706.0], [1, 576, 345, -31706.0], [1, 576, 225, -31706.0], [0, 240, 668, -32330], [1, 240, 525, -32330], [0, 240, 428, -32330], [1, 240, 285, -32330], [0, 240, 188, -32330], [0, 144, 608, -32618], [0, 144, 488, -32618], [0, 144, 428, -32618], [1, 144, 285, -32618], [0, 144, 188, -32618], [1, 576, 345, -32858.0], [0, 576, 248, -32858.0], [0, 576, 188, -32858.0], [0, 576, 68, -32858.0], [0, 240, 368, -33482], [0, 240, 248, -33482], [0, 240, 68, -33482], [0, 240, 8, -33482], [0, 144, 308, -33770], [1, 144, 225, -33770], [0, 144, 128, -33770], [0, 144, 8, -33770], [0, 576, 488, -34010.0], [0, 576, 308, -34010.0], [1, 576, 225, -34010.0], [0, 576, 68, -34010.0], [1, 240, 525, -34634], [0, 240, 368, -34634], [1, 240, 285, -34634], [1, 240, 225, -34634], [0, 240, 128, -34634], [1, 144, 525, -34922], [1, 144, 345, -34922], [1, 144, 285, -34922], [0, 144, 128, -34922], [1, 576, 645, -35162.0], [1, 576, 525, -35162.0], [1, 576, 465, -35162.0], [1, 576, 345, -35162.0], [1, 576, 225, -35162.0], [0, 240, 668, -35786], [1, 240, 525, -35786], [1, 240, 345, -35786], [1, 240, 285, -35786], [0, 240, 188, -35786], [0, 144, 668, -36074], [0, 144, 488, -36074], [0, 144, 428, -36074], [1, 144, 285, -36074], [0, 576, 668, -36314.0], [0, 576, 608, -36314.0], [0, 576, 488, -36314.0], [1, 576, 345, -36314.0], [1, 576, 105, -36314.0], [1, 144, 645, -36938], [1, 144, 465, -36938], [0, 144, 368, -36938], [1, 144, 285, -36938], [0, 144, 128, -36938], [1, 144, 645, -37178.0], [1, 144, 525, -37178.0], [1, 144, 345, -37178.0], [1, 144, 285, -37178.0], [0, 144, 128, -37178.0],
    

    # Bass
    [4, 96, B4, level_4_bar_length * (0) - 650],
    [5, 96, Db5, level_4_bar_length * (1) - 650],
    [4, 96, D5, level_4_bar_length * (2) - 650],
    [5, 96, Gb4, level_4_bar_length * (3) - 650],

    [4, 96, G4, level_4_bar_length * (4) - 650],
    [4, 96, A4, level_4_bar_length * (5) - 650],
    [5, 96, Bb4, level_4_bar_length * (6) - 650],
    [4, 96, D4, level_4_bar_length * (7) - 650],

    [5, 96, Eb4, level_4_bar_length * (8) - 650],
    [5, 96, Bb4, level_4_bar_length * (9) - 650],
    [5, 96, Eb5, level_4_bar_length * (10) - 650],
    [5, 96, Bb4, level_4_bar_length * (11) - 650],

    [4, 96, A4, level_4_bar_length * (12) - 650],
    [5, 96, Db4, level_4_bar_length * (13) - 650],
    [4, 96, D4, level_4_bar_length * (14) - 650],
    [5, 96, Gb4, level_4_bar_length * (15) - 650],

    [4, 96, G4, level_4_bar_length * (16) - 650],
    [4, 96, A4, level_4_bar_length * (17) - 650],
    [5, 96, Bb4, level_4_bar_length * (18) - 650],
    [4, 96, D4, level_4_bar_length * (19) - 650],

    [5, 96, Eb4, level_4_bar_length * (20) - 650],
    [4, 96, F4, level_4_bar_length * (21) - 650],
    [5, 96, Gb4, level_4_bar_length * (22) - 650],
    [5, 96, Bb4, level_4_bar_length * (23) - 650],

    [4, 96, B4, level_4_bar_length * (24) - 650],
    [5, 96, Gb5, level_4_bar_length * (25) - 650], 
    # [4, 96, B5, level_4_bar_length * (26) - 650],
    [5, 96, Gb5, level_4_bar_length * (27) - 650],

    [4, 96, F4, level_4_bar_length * (28) - 650],
    [4, 96, A4, level_4_bar_length * (29) - 650],
    [5, 96, Bb4, level_4_bar_length * (30) - 650],
    [4, 96, D5, level_4_bar_length * (31) - 650],

    [5, 96, Eb5, level_4_bar_length * (32) - 650],
    [5, 96, Bb4, level_4_bar_length * (33) - 650],
    [4, 96, G4, level_4_bar_length * (34) - 650],
    [5, 96, Eb4, level_4_bar_length * (35) - 650],

    [4, 96, A4, level_4_bar_length * (36) - 650],
    [5, 96, Db4, level_4_bar_length * (37) - 650],
    [4, 96, D4, level_4_bar_length * (38) - 650],
    [5, 96, Gb4, level_4_bar_length * (39) - 650],

    [4, 96, G4, level_4_bar_length * (40) - 650],
    [4, 96, D5, level_4_bar_length * (41) - 650],
    [4, 96, G5, level_4_bar_length * (42) - 650],
    [4, 96, D5, level_4_bar_length * (43) - 650],

    [5, 96, Db4, level_4_bar_length * (44) - 650],
    [4, 96, F4, level_4_bar_length * (45) - 650],
    [5, 96, Gb4, level_4_bar_length * (46) - 650],
    [5, 96, Bb4, level_4_bar_length * (47) - 650],

    [4, 96, B4, level_4_bar_length * (48) - 650],
    [5, 96, Gb5, level_4_bar_length * (49) - 650],
    # [4, 96, B5, level_4_bar_length * (50) - 650],
    [5, 96, Gb5, level_4_bar_length * (51) - 650],

    [4, 96, F4, level_4_bar_length * (52) - 650],
    [4, 96, A4, level_4_bar_length * (53) - 650],
    [5, 96, Bb4, level_4_bar_length * (54) - 650],
    [4, 96, D5, level_4_bar_length * (55) - 650],

    [5, 96, Eb5, level_4_bar_length * (56) - 650],
    [5, 96, Bb4, level_4_bar_length * (57) - 650],
    [4, 96, G4, level_4_bar_length * (58) - 650],
    [5, 96, Eb4, level_4_bar_length * (59) - 650],

    [5, 144, Db4, level_4_bar_length * (60) - 650],
    [5, 144, Db4, level_4_bar_length * (61 + 2/3) - 650],
    
    # these notes are the exact same as the bass, but shifted by 192
    [4, 96, 368, -28298], [5, 96, 465, -28442], [4, 96, 488, -28586], [5, 96, 225, -28730], [4, 96, 248, -28874], [4, 96, 308, -29018], [5, 96, 345, -29162], [4, 96, 68, -29306], [5, 96, 105, -29450], [5, 96, 345, -29594], [5, 96, 525, -29738], [5, 96, 345, -29882], [4, 96, 308, -30026], [5, 96, 45, -30170], [4, 96, 68, -30314], [5, 96, 225, -30458], [4, 96, 248, -30602], [4, 96, 308, -30746], [5, 96, 345, -30890], [4, 96, 68, -31034], [5, 96, 105, -31178], [4, 96, 188, -31322], [5, 96, 225, -31466], [5, 96, 345, -31610], [4, 96, 368, -31754], [5, 96, 645, -31898], [5, 96, 645, -32186], [4, 96, 188, -32330], [4, 96, 308, -32474], [5, 96, 345, -32618], [4, 96, 488, -32762], [5, 96, 525, -32906], [5, 96, 345, -33050], [4, 96, 248, -33194], [5, 96, 105, -33338], [4, 96, 308, -33482], [5, 96, 45, -33626], [4, 96, 68, -33770], [5, 96, 225, -33914], [4, 96, 248, -34058], [4, 96, 488, -34202], [4, 96, 668, -34346], [4, 96, 488, -34490], [5, 96, 45, -34634], [4, 96, 188, -34778], [5, 96, 225, -34922], [5, 96, 345, -35066], [4, 96, 368, -35210], [5, 96, 645, -35354], [5, 96, 645, -35642], [4, 96, 188, -35786], [4, 96, 308, -35930], [5, 96, 345, -36074], [4, 96, 488, -36218], [5, 96, 525, -36362], [5, 96, 345, -36506], [4, 96, 248, -36650], [5, 96, 105, -36794], [5, 144, 45, -36938], [5, 144, 45, -37178.0],

    # Piano Solo
    [3, 48, Gb5, level_4_bar_length * (128 + 0/3) - 650],
    [2, 48, F5, level_4_bar_length * (128 + 2/3) - 650],
    [2, 48, E5, level_4_bar_length * (129 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (129 + 2/3) - 650],
    [2, 48, D5, level_4_bar_length * (130 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (130 + 2/3) - 650],
    [2, 48, G4, level_4_bar_length * (131 + 0/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (131 + 2/3) - 650],
    [2, 48, D5, level_4_bar_length * (132 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (132 + 2/3) - 650],
    [2, 48, G4, level_4_bar_length * (133 + 0/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (133 + 2/3) - 650],
    [3, 48, Db5, level_4_bar_length * (134 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (134 + 2/3) - 650],
    [2, 48, B4, level_4_bar_length * (135 + 0/3) - 650],
    [2, 48, G4, level_4_bar_length * (135 + 2/3) - 650],
    [3, 576, Bb4, level_4_bar_length * (136 + 0/3) - 650],

    [2, 48, A4, level_4_bar_length * (140 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (140 + 2/3) - 650],
    [2, 48, E5, level_4_bar_length * (141 + 0/3) - 650],
    [2, 48, G5, level_4_bar_length * (141 + 2/3) - 650],
    [3, 48, Gb5, level_4_bar_length * (142 + 0/3) - 650],
    [2, 48, D5, level_4_bar_length * (142 + 2/3) - 650],
    [2, 48, C5, level_4_bar_length * (143 + 0/3) - 650],
    [2, 48, A4, level_4_bar_length * (143 + 2/3) - 650],
    [2, 48, D5, level_4_bar_length * (144 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (144 + 2/3) - 650],
    [2, 48, B4, level_4_bar_length * (145 + 0/3) - 650],
    [2, 48, A4, level_4_bar_length * (145 + 2/3) - 650],
    [2, 48, G4, level_4_bar_length * (146 + 0/3) - 650],
    [2, 48, A4, level_4_bar_length * (146 + 2/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (147 + 0/3) - 650],
    [2, 48, B4, level_4_bar_length * (147 + 2/3) - 650],
    [2, 48, C5, level_4_bar_length * (148 + 0/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (148 + 2/3) - 650],
    [3, 48, Ab4, level_4_bar_length * (149 + 0/3) - 650],
    [2, 48, G4, level_4_bar_length * (149 + 2/3) - 650],
    [3, 48, Gb4, level_4_bar_length * (150 + 0/3) - 650],
    [3, 48, Ab4, level_4_bar_length * (150 + 2/3) - 650],
    [2, 48, A4, level_4_bar_length * (151 + 0/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (151 + 2/3) - 650],
    [2, 48, B4, level_4_bar_length * (152 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (152 + 2/3) - 650],
    [3, 48, Gb5, level_4_bar_length * (153 + 0/3) - 650],
    #   576, too high

    [2, 48, F5, level_4_bar_length * (156 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (156 + 2/3) - 650],
    [2, 48, C5, level_4_bar_length * (157 + 0/3) - 650],
    [2, 48, B4, level_4_bar_length * (157 + 2/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (158 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (158 + 2/3) - 650],
    [3, 48, Db5, level_4_bar_length * (159 + 0/3) - 650],
    [2, 48, D5, level_4_bar_length * (159 + 2/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (160 + 0/3) - 650],
    [2, 48, G5, level_4_bar_length * (160 + 2/3) - 650],
    #   48, too high
    #   576, too high

    [2, 48, A4, level_4_bar_length * (164 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (164 + 2/3) - 650],
    [2, 48, E5, level_4_bar_length * (165 + 0/3) - 650],
    [2, 48, G5, level_4_bar_length * (165 + 2/3) - 650],
    [3, 48, Gb5, level_4_bar_length * (166 + 0/3) - 650],
    [2, 48, D5, level_4_bar_length * (166 + 2/3) - 650],
    [2, 48, C5, level_4_bar_length * (167 + 0/3) - 650],
    [2, 48, A4, level_4_bar_length * (167 + 2/3) - 650],
    [2, 48, G4, level_4_bar_length * (168 + 0/3) - 650],
    [2, 48, A4, level_4_bar_length * (168 + 2/3) - 650],
    [2, 48, B4, level_4_bar_length * (169 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (169 + 2/3) - 650],
    [3, 48, Db5, level_4_bar_length * (170 + 0/3) - 650],
    [2, 48, D5, level_4_bar_length * (170 + 2/3) - 650],
    [2, 48, E5, level_4_bar_length * (171 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (171 + 2/3) - 650],
    [3, 48, Db5, level_4_bar_length * (172 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (172 + 2/3) - 650],
    [2, 48, E5, level_4_bar_length * (173 + 0/3) - 650],
    [2, 48, F5, level_4_bar_length * (173 + 2/3) - 650],
    [3, 48, Gb5, level_4_bar_length * (174 + 0/3) - 650],
    [2, 48, E5, level_4_bar_length * (174 + 2/3) - 650],
    [3, 48, Db5, level_4_bar_length * (175 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (175 + 2/3) - 650],
    [2, 48, B4, level_4_bar_length * (176 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (176 + 2/3) - 650],
    [3, 48, Gb5, level_4_bar_length * (177 + 0/3) - 650],
    #   576, too high

    [2, 48, F5, level_4_bar_length * (180 + 0/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (180 + 2/3) - 650],
    [2, 48, C5, level_4_bar_length * (181 + 0/3) - 650],
    [2, 48, B4, level_4_bar_length * (181 + 2/3) - 650],
    [3, 48, Bb4, level_4_bar_length * (182 + 0/3) - 650],
    [2, 48, C5, level_4_bar_length * (182 + 2/3) - 650],
    [3, 48, Db5, level_4_bar_length * (183 + 0/3) - 650],
    [2, 48, D5, level_4_bar_length * (183 + 2/3) - 650],
    [3, 48, Eb5, level_4_bar_length * (184 + 0/3) - 650],
    [2, 48, G5, level_4_bar_length * (184 + 2/3) - 650],
    #   48, too high
    #   576, too high

    [3, 48, Db5, level_4_bar_length * (187 + 2/3) - 650],
    [2, 48, E5, level_4_bar_length * (188 + 0/3) - 650],
    #   48, too high
    #   48, too high
    #   48, too high
    [3, 48, Gb5, level_4_bar_length * (190 + 0/3) - 650],

]