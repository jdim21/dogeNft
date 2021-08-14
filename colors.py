colorsDict = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),

    "typeNormal": (224, 167, 33),
    "typeNormalShade": (185, 137, 26),
    "typeNormalLight": (255, 224, 163),
    "typeNormalBrows": (255, 238, 202),

    "typeLight": (255, 211, 121),
    "typeLightShade": (255, 191, 60),
    "typeLightLight": (255, 230, 176),
    "typeLightBrows": (255, 238, 202),

    "typeDark": (185, 137, 26),
    "typeDarkShade": (143, 106, 20),
    "typeDarkLight": (224, 167, 33),
    "typeDarkBrows": (255, 238, 202),

    "typeBrown": (157, 79, 0),
    "typeBrownShade": (119, 60, 0),
    "typeBrownLight": (202, 101, 0),
    "typeBrownBrows": (255, 193, 132),

    "typeDarkBrown": (119, 60, 0),
    "typeDarkBrownShade": (100, 50, 0),
    "typeDarkBrownLight": (157, 79, 0),
    "typeDarkBrownBrows": (255, 192, 130),

    "typeBlack": (64, 64, 64),
    "typeBlackShade": (46, 46, 46),
    "typeBlackLight": (116, 116, 116),
    "typeBlackBrows": (160, 160, 160),

    "typeZombie": (126, 163, 105),
    "typeZombieShade": (104, 140, 85),
    "typeZombieLight": (94, 115, 82),
    "typeZombieEyes": (237, 28, 36),
    "typeZombieBrows": (188, 207, 177),
    "typeZombieMarks": (94, 115, 82),

    "typeDevil": (189, 15, 23),
    "typeDevilShade": (140, 11, 17),
    "typeDevilLight": (140, 11, 17),
    "typeDevilEyes": (255, 127, 39),
    "typeDevilBrows": (251, 179, 182),
    "typeDevilMarks": (136, 0, 21),
    "typeDevilHorns": (136, 0, 21),

    "blueShade": (0, 142, 204),
    "blue": (0, 162, 232),
    "buckleSilver": (167, 167, 167),

    "redCollar": (237, 28, 36),
    "redCollarShade": (215, 17, 27),

    "purpleBowtie": (163, 73, 164),
    "purpleBowtieBlue": (0, 162, 232),

    "greenBowtie": (34, 177, 76),
    "greenBowtieShade": (26, 132, 57),

    "pink": (255, 149, 184),
    "pinkShade": (255, 98, 149),

    "lime": (181, 230, 29),
    "limeShade": (166, 213, 23),

    "orange": (255, 127, 39),
    "orangeShade": (251, 100, 0),
    "gokuBlue": (0, 0, 236),

    "vice": (43, 240, 231),
    "viceShade": (16, 209, 200),
    "viceFlower": (255, 98, 149),

    "clover": (0, 168, 0),
    "cloverSecondary": (181, 230, 29),
    
    "whiteShade": (200, 191, 231),
    "diaperStrap": (83, 117, 255),

    "blackSuit": (46, 46, 46),
    "blackSuitShade": (30, 30, 30),
    "blackSuitTie": (237, 28, 36),

    "navySuit": (0, 0, 145),
    "navySuitShade": (0, 0, 106),
    "navySuitTie": (254, 95, 250),

    "tongue": (255, 174, 201),
    "bone": (223, 223, 223),
    "boneShade": (180, 180, 180),
    "joint": (125, 63, 0),
    "jointSmoke": (64, 64, 64),
    "jointEyes": (255, 159, 159),
    "jointBurn": (255, 127, 39),

    "partyHatRed": (215, 17, 27),
    "partyHatRedShade": (191, 15, 23),
    "partyHatOrange": (255, 127, 39),
    "partyHatOrangeShade": (249, 100, 0),
    "partyHatStreamers": (184, 14, 22),

    "redTophat": (237, 28, 36),
    "redTophatShade": (191, 15, 23),
    "redTophatBuckle": (255, 242, 0),
    "redTophatStrap": (185, 122, 87),
    "redTophatStrapShade": (150, 94, 63),

    "greenTophat": (0, 168, 0),
    "greenTophatShade": (0, 125, 0),
    "greenTophatBuckle": (255, 242, 0),
    "greenTophatStrap": (185, 122, 87),
    "greenTophatStrapShade": (150, 94, 63),

    "whiteTophat": (255, 255, 255),
    "whiteTophatShade": (195, 195, 195),
    "whiteTophatBuckle": (255, 242, 0),
    "whiteTophatStrap": (116, 116, 116),
    "whiteTophatStrapShade": (64, 64, 64),

    "blueBandanaOutline": (0, 71, 102),
    "blueBandana": (0, 101, 145),
    "blueBandanaShade": (0, 90, 130),

    "pinkMohawk": (255, 174, 201),
    "pinkMohawkShade": (255, 149, 184),

    "pvBlue": (0, 162, 232),
    "pvGreen": (181, 230, 29),
    "pvYellow": (255, 242, 0),
    "pvOrange": (255, 127, 39),
    "pvRed": (237, 28, 36),

    "viceBrown": (235, 163, 65),
    "viceBrownLight": (244, 206, 155),

    "solanaBand": [(44, 208, 184),
    (50, 202, 186),
    (56, 197, 189),
    (62, 191, 191),
    (68, 185, 193),
    (75, 179, 196),
    (81, 175, 198),
    (87, 168, 200),
    (93, 161, 204),
    (99, 155, 205),
    (104, 150, 207),
    (111, 144, 210),
    (117, 138, 212),
    (123, 132, 215),
    (128, 126, 218),
    (134, 120, 219),
    (140, 115, 222),
    (147, 107, 225),
    (151, 103, 226),
    (157, 96, 229),
    (163, 90, 232),
    (169, 83, 234),
    (174, 77, 237),
    (180, 71, 239)]
}
