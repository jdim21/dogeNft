from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from draw.drawBaseType import drawBaseType

def drawSolanaBackground(im):
    for i in range(24):
        for j in range(24):
            im.putpixel((i, j), colorsDict["solanaBand"][j])

def drawType(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["type"][trait]
    if decodedType == "Normal":
        primaryColor = "typeNormal"
        colorShade = "typeNormalShade"
        colorLight = "typeNormalLight"
        colorBrow = "typeNormalBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Light":
        primaryColor = "typeLight"
        colorShade = "typeLightShade"
        colorLight = "typeLightLight"
        colorBrow = "typeLightBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Dark":
        primaryColor = "typeDark"
        colorShade = "typeDarkShade"
        colorLight = "typeDarkLight"
        colorBrow = "typeDarkBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Brown":
        primaryColor = "typeBrown"
        colorShade = "typeBrownShade"
        colorLight = "typeBrownLight"
        colorBrow = "typeBrownBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Dark Brown":
        primaryColor = "typeDarkBrown"
        colorShade = "typeDarkBrownShade"
        colorLight = "typeDarkBrownLight"
        colorBrow = "typeDarkBrownBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Black":
        primaryColor = "typeBlack"
        colorShade = "typeBlackShade"
        colorLight = "typeBlackLight"
        colorBrow = "typeBlackBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
    elif decodedType == "Zombie":
        primaryColor = "typeZombie"
        colorShade = "typeZombieShade"
        colorLight = "typeZombieLight"
        colorBrow = "typeZombieBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)

        imNew.putpixel((10, 9), colorsDict["typeZombieMarks"])
        imNew.putpixel((13, 9), colorsDict["typeZombieMarks"])

        imNew.putpixel((8, 12), colorsDict["typeZombieEyes"])
        imNew.putpixel((14, 12), colorsDict["typeZombieEyes"])

        imNew.putpixel((9, 21), colorsDict["typeZombieMarks"])

        imNew.putpixel((6, 22), colorsDict["typeZombieMarks"])

    elif decodedType == "Devil":
        primaryColor = "typeDevil"
        colorShade = "typeDevilShade"
        colorLight = "typeDevilLight"
        colorBrow = "typeDevilBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)

        imNew.putpixel((5, 4), colorsDict["black"])
        imNew.putpixel((6, 4), colorsDict["black"])
        imNew.putpixel((17, 4), colorsDict["black"])
        imNew.putpixel((18, 4), colorsDict["black"])

        imNew.putpixel((4, 5), colorsDict["black"])
        imNew.putpixel((5, 5), colorsDict["typeDevilHorns"])
        imNew.putpixel((6, 5), colorsDict["black"])
        imNew.putpixel((17, 5), colorsDict["black"])
        imNew.putpixel((18, 5), colorsDict["typeDevilHorns"])
        imNew.putpixel((19, 5), colorsDict["black"])

        imNew.putpixel((4, 6), colorsDict["black"])
        imNew.putpixel((5, 6), colorsDict["typeDevilHorns"])
        imNew.putpixel((6, 6), colorsDict["black"])
        imNew.putpixel((7, 6), colorsDict["black"])
        imNew.putpixel((16, 6), colorsDict["black"])
        imNew.putpixel((17, 6), colorsDict["black"])
        imNew.putpixel((18, 6), colorsDict["typeDevilHorns"])
        imNew.putpixel((19, 6), colorsDict["black"])

        imNew.putpixel((4, 7), colorsDict["black"])
        imNew.putpixel((5, 7), colorsDict["typeDevilHorns"])
        imNew.putpixel((6, 7), colorsDict["typeDevilHorns"])
        imNew.putpixel((7, 7), colorsDict["black"])
        imNew.putpixel((8, 7), colorsDict["black"])
        imNew.putpixel((10, 7), colorsDict["black"])
        imNew.putpixel((11, 7), colorsDict["black"])
        imNew.putpixel((12, 7), colorsDict["black"])
        imNew.putpixel((13, 7), colorsDict["black"])
        imNew.putpixel((15, 7), colorsDict["black"])
        imNew.putpixel((16, 7), colorsDict["black"])
        imNew.putpixel((17, 7), colorsDict["typeDevilHorns"])
        imNew.putpixel((18, 7), colorsDict["typeDevilHorns"])
        imNew.putpixel((19, 7), colorsDict["black"])

        imNew.putpixel((5, 8), colorsDict["black"])
        imNew.putpixel((6, 8), colorsDict["typeDevilHorns"])
        imNew.putpixel((7, 8), colorsDict["typeDevilHorns"])
        imNew.putpixel((8, 8), colorsDict["black"])
        imNew.putpixel((15, 8), colorsDict["black"])
        imNew.putpixel((16, 8), colorsDict["typeDevilHorns"])
        imNew.putpixel((17, 8), colorsDict["typeDevilHorns"])
        imNew.putpixel((18, 8), colorsDict["black"])

        imNew.putpixel((5, 9), colorsDict["solanaBand"][9])
        imNew.putpixel((6, 9), colorsDict["black"])
        imNew.putpixel((17, 9), colorsDict["black"])
        imNew.putpixel((18, 9), colorsDict["solanaBand"][9])

        imNew.putpixel((10, 11), colorsDict["typeDevilMarks"])
        imNew.putpixel((13, 11), colorsDict["typeDevilMarks"])

        imNew.putpixel((8, 12), colorsDict["typeDevilEyes"])
        imNew.putpixel((14, 12), colorsDict["typeDevilEyes"])

        # Overwrite tail

        imNew.putpixel((0, 17), colorsDict["black"])
        imNew.putpixel((1, 17), colorsDict["black"])
        imNew.putpixel((2, 17), colorsDict["black"])
        imNew.putpixel((3, 17), colorsDict["black"])

        imNew.putpixel((0, 18), colorsDict["typeDevil"])
        imNew.putpixel((1, 18), colorsDict["typeDevil"])
        imNew.putpixel((2, 18), colorsDict["typeDevilShade"])
        imNew.putpixel((3, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["black"])
        imNew.putpixel((1, 19), colorsDict["typeDevilShade"])
        imNew.putpixel((2, 19), colorsDict["typeDevil"])
        imNew.putpixel((3, 19), colorsDict["black"])

        imNew.putpixel((1, 20), colorsDict["black"])
        imNew.putpixel((2, 20), colorsDict["typeDevil"])
        imNew.putpixel((3, 20), colorsDict["black"])

        imNew.putpixel((2, 21), colorsDict["black"])
        imNew.putpixel((3, 21), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
