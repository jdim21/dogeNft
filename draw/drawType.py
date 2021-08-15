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
    elif decodedType == "Skeleton":
        primaryColor = "typeSkeleton"
        colorShade = "typeSkeletonShade"
        colorLight = "typeSkeletonLight"
        colorBrow = "typeSkeletonBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((6, 5), colorsDict["solanaBand"][5])
        imNew.putpixel((17, 5), colorsDict["solanaBand"][5])

        imNew.putpixel((5, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((6, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((7, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((16, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((17, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((18, 6), colorsDict["solanaBand"][6])

        imNew.putpixel((5, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((6, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((7, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((8, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((15, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((16, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((17, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((18, 7), colorsDict["solanaBand"][7])

        imNew.putpixel((5, 8), colorsDict["solanaBand"][8])
        imNew.putpixel((6, 8), colorsDict["solanaBand"][8])
        imNew.putpixel((7, 8), colorsDict["solanaBand"][8])
        imNew.putpixel((10, 8), colorsDict["typeSkeletonShade"])
        imNew.putpixel((11, 8), colorsDict["typeSkeletonShade"])
        imNew.putpixel((16, 8), colorsDict["solanaBand"][8])
        imNew.putpixel((17, 8), colorsDict["solanaBand"][8])
        imNew.putpixel((18, 8), colorsDict["solanaBand"][8])

        imNew.putpixel((5, 9), colorsDict["solanaBand"][9])
        imNew.putpixel((6, 9), colorsDict["solanaBand"][9])
        imNew.putpixel((8, 9), colorsDict["typeSkeletonShade"])
        imNew.putpixel((9, 9), colorsDict["typeSkeletonShade"])
        imNew.putpixel((17, 9), colorsDict["solanaBand"][9])
        imNew.putpixel((18, 9), colorsDict["solanaBand"][9])

        imNew.putpixel((5, 10), colorsDict["solanaBand"][10])
        imNew.putpixel((7, 10), colorsDict["typeSkeletonShade"])
        imNew.putpixel((11, 10), colorsDict["typeSkeletonShade"])
        imNew.putpixel((18, 10), colorsDict["solanaBand"][10])

        imNew.putpixel((6, 11), colorsDict["typeSkeletonShade"])
        imNew.putpixel((10, 11), colorsDict["typeSkeletonShade"])

        imNew.putpixel((6, 12), colorsDict["typeSkeletonShade"])
        imNew.putpixel((8, 12), colorsDict["black"])
        imNew.putpixel((9, 12), colorsDict["black"])
        imNew.putpixel((14, 12), colorsDict["black"])
        imNew.putpixel((15, 12), colorsDict["black"])

        imNew.putpixel((5, 13), colorsDict["typeSkeletonLight"])
        imNew.putpixel((6, 13), colorsDict["typeSkeletonLight"])
        imNew.putpixel((8, 13), colorsDict["black"])
        imNew.putpixel((9, 13), colorsDict["typeSkeleton"])
        imNew.putpixel((14, 13), colorsDict["black"])
        imNew.putpixel((15, 13), colorsDict["typeSkeleton"])
        imNew.putpixel((17, 13), colorsDict["typeSkeletonLight"])
        imNew.putpixel((18, 13), colorsDict["typeSkeletonLight"])

        imNew.putpixel((5, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((6, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((7, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((8, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((9, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((10, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((13, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((14, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((15, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((16, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((17, 14), colorsDict["typeSkeletonLight"])
        imNew.putpixel((18, 14), colorsDict["typeSkeletonLight"])

        imNew.putpixel((5, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((6, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((7, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((8, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((9, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((10, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((13, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((14, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((15, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((16, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((17, 15), colorsDict["typeSkeletonLight"])
        imNew.putpixel((18, 15), colorsDict["typeSkeletonLight"])

        imNew.putpixel((6, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((7, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((8, 16), colorsDict["black"])
        imNew.putpixel((9, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((12, 16), colorsDict["black"])
        imNew.putpixel((13, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((14, 16), colorsDict["black"])
        imNew.putpixel((15, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((16, 16), colorsDict["typeSkeletonLight"])
        imNew.putpixel((17, 16), colorsDict["typeSkeletonLight"])

        imNew.putpixel((7, 17), colorsDict["typeSkeletonLight"])
        imNew.putpixel((8, 17), colorsDict["typeSkeletonLight"])
        imNew.putpixel((9, 17), colorsDict["black"])
        imNew.putpixel((10, 17), colorsDict["typeSkeletonLight"])
        imNew.putpixel((11, 17), colorsDict["black"])
        imNew.putpixel((12, 17), colorsDict["typeSkeletonLight"])
        imNew.putpixel((13, 17), colorsDict["black"])
        imNew.putpixel((14, 17), colorsDict["typeSkeletonLight"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["typeSkeletonLight"])

        imNew.putpixel((9, 18), colorsDict["typeSkeletonLight"])
        imNew.putpixel((10, 18), colorsDict["typeSkeletonLight"])
        imNew.putpixel((11, 18), colorsDict["typeSkeletonLight"])
        imNew.putpixel((12, 18), colorsDict["typeSkeletonLight"])
        imNew.putpixel((13, 18), colorsDict["typeSkeletonLight"])
        imNew.putpixel((14, 18), colorsDict["typeSkeletonLight"])

        imNew.putpixel((9, 20), colorsDict["typeSkeletonLight"])
        imNew.putpixel((11, 20), colorsDict["typeSkeletonLight"])
        imNew.putpixel((13, 20), colorsDict["typeSkeletonLight"])

        imNew.putpixel((10, 21), colorsDict["typeSkeletonLight"])
        imNew.putpixel((11, 21), colorsDict["typeSkeletonLight"])
        imNew.putpixel((12, 21), colorsDict["typeSkeletonLight"])

        imNew.putpixel((9, 22), colorsDict["typeSkeletonLight"])
        imNew.putpixel((11, 22), colorsDict["typeSkeletonLight"])
        imNew.putpixel((13, 22), colorsDict["typeSkeletonLight"])
    elif decodedType == "Alien":
        primaryColor = "typeAlien"
        colorShade = "typeAlienShade"
        colorLight = "typeAlienLight"
        colorBrow = "typeAlienBrows"
        drawBaseType(im, primaryColor, colorShade, colorLight, colorBrow)
        imNew.putpixel((8, 12), colorsDict["typeAlienEyes2"])
        imNew.putpixel((9, 12), colorsDict["black"])
        imNew.putpixel((14, 12), colorsDict["typeAlienEyes2"])
        imNew.putpixel((15, 12), colorsDict["black"])

        imNew.putpixel((8, 13), colorsDict["black"])
        imNew.putpixel((9, 13), colorsDict["typeAlienEyes1"])
        imNew.putpixel((14, 13), colorsDict["black"])
        imNew.putpixel((15, 13), colorsDict["typeAlienEyes1"])
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
