from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from drawBaseType import drawBaseType

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
        drawBaseType(im, primaryColor, colorShade, colorLight)
    elif decodedType == "Light":
        primaryColor = "typeLight"
        colorShade = "typeLightShade"
        colorLight = "typeLightLight"
        drawBaseType(im, primaryColor, colorShade, colorLight)
    elif decodedType == "Dark":
        primaryColor = "typeDark"
        colorShade = "typeDarkShade"
        colorLight = "typeDarkLight"
        drawBaseType(im, primaryColor, colorShade, colorLight)
    elif decodedType == "Brown":
        primaryColor = "typeBrown"
        colorShade = "typeBrownShade"
        colorLight = "typeBrownLight"
        drawBaseType(im, primaryColor, colorShade, colorLight)
    elif decodedType == "Dark Brown":
        primaryColor = "typeDarkBrown"
        colorShade = "typeDarkBrownShade"
        colorLight = "typeDarkBrownLight"
        drawBaseType(im, primaryColor, colorShade, colorLight)
    elif decodedType == "Black":
        primaryColor = "typeBlack"
        colorShade = "typeBlackShade"
        colorLight = "typeBlackLight"
        drawBaseType(im, primaryColor, colorShade, colorLight)

    im.paste(imNew, (0,0), mask=imNew)
