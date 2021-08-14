from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from draw.drawShirt import drawShirt
from draw.drawSuit import drawSuit

def drawBody(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["body"][trait]
    if decodedType == "Pink Shirt":
        drawShirt(im, "pink")
    elif decodedType == "Lime Shirt":
        drawShirt(im, "lime")
    elif decodedType == "White Shirt":
        drawShirt(im, "white")
    elif decodedType == "Lucky Shirt":
        drawShirt(im, "white")
        imNew.putpixel((6, 20), colorsDict["clover"])
        imNew.putpixel((8, 20), colorsDict["clover"])

        imNew.putpixel((5, 21), colorsDict["clover"])
        imNew.putpixel((6, 21), colorsDict["clover"])
        imNew.putpixel((7, 21), colorsDict["cloverSecondary"])
        imNew.putpixel((8, 21), colorsDict["clover"])
        imNew.putpixel((9, 21), colorsDict["clover"])

        imNew.putpixel((6, 22), colorsDict["cloverSecondary"])
        imNew.putpixel((7, 22), colorsDict["clover"])
        imNew.putpixel((8, 22), colorsDict["cloverSecondary"])

        imNew.putpixel((5, 23), colorsDict["clover"])
        imNew.putpixel((6, 23), colorsDict["clover"])
        imNew.putpixel((7, 23), colorsDict["cloverSecondary"])
        imNew.putpixel((8, 23), colorsDict["clover"])
        imNew.putpixel((9, 23), colorsDict["clover"])
    elif decodedType == "Goku Shirt":
        drawShirt(im, "goku")
        imNew.putpixel((9, 20), colorsDict["gokuBlue"])
        imNew.putpixel((13, 20), colorsDict["gokuBlue"])
        imNew.putpixel((14, 20), colorsDict["gokuBlue"])
        imNew.putpixel((15, 20), colorsDict["black"])

        imNew.putpixel((10, 21), colorsDict["gokuBlue"])
        imNew.putpixel((11, 21), colorsDict["gokuBlue"])
        imNew.putpixel((12, 21), colorsDict["gokuBlue"])
        imNew.putpixel((13, 21), colorsDict["white"])

        imNew.putpixel((10, 23), colorsDict["gokuBlue"])
        imNew.putpixel((11, 23), colorsDict["gokuBlue"])
        imNew.putpixel((13, 23), colorsDict["gokuBlue"])
        imNew.putpixel((14, 23), colorsDict["gokuBlue"])
    elif decodedType == "Vice Shirt":
        drawShirt(im, "vice")
        imNew.putpixel((6, 20), colorsDict["viceFlower"])
        imNew.putpixel((8, 20), colorsDict["viceFlower"])

        imNew.putpixel((7, 21), colorsDict["viceFlower"])
        imNew.putpixel((14, 21), colorsDict["viceFlower"])

        imNew.putpixel((6, 22), colorsDict["viceFlower"])
        imNew.putpixel((8, 22), colorsDict["viceFlower"])
        imNew.putpixel((13, 22), colorsDict["viceFlower"])

        imNew.putpixel((14, 23), colorsDict["viceFlower"])
    elif decodedType == "Diaper":
        imNew.putpixel((5, 20), colorsDict["black"])
        
        imNew.putpixel((4, 21), colorsDict["black"])
        imNew.putpixel((5, 21), colorsDict["white"])
        imNew.putpixel((6, 21), colorsDict["black"])
        imNew.putpixel((7, 21), colorsDict["black"])
    
        imNew.putpixel((3, 22), colorsDict["black"])
        imNew.putpixel((4, 22), colorsDict["whiteShade"])
        imNew.putpixel((5, 22), colorsDict["white"])
        imNew.putpixel((6, 22), colorsDict["white"])
        imNew.putpixel((7, 22), colorsDict["diaperStrap"])
        imNew.putpixel((8, 22), colorsDict["black"])

        imNew.putpixel((2, 23), colorsDict["black"])
        imNew.putpixel((3, 23), colorsDict["whiteShade"])
        imNew.putpixel((4, 23), colorsDict["white"])
        imNew.putpixel((5, 23), colorsDict["white"])
        imNew.putpixel((6, 23), colorsDict["white"])
        imNew.putpixel((7, 23), colorsDict["white"])
        imNew.putpixel((8, 23), colorsDict["white"])
        imNew.putpixel((9, 23), colorsDict["black"])
    elif decodedType == "Black Suit":
        primaryColor = colorsDict["blackSuit"]
        primaryColorShade = colorsDict["blackSuitShade"]
        tieColor = colorsDict["blackSuitTie"]
        drawSuit(imNew, primaryColor, primaryColorShade, tieColor)
    elif decodedType == "Navy Suit":
        primaryColor = colorsDict["navySuit"]
        primaryColorShade = colorsDict["navySuitShade"]
        tieColor = colorsDict["navySuitTie"]
        drawSuit(imNew, primaryColor, primaryColorShade, tieColor)
    elif decodedType == "Nyan Doge":
        imNew.putpixel((0, 18), colorsDict["nyanDogeRed"])
        imNew.putpixel((1, 18), colorsDict["nyanDogeRed"])
        imNew.putpixel((2, 18), colorsDict["nyanDogeRed"])
        imNew.putpixel((3, 18), colorsDict["black"])
        imNew.putpixel((4, 18), colorsDict["black"])
        imNew.putpixel((5, 18), colorsDict["black"])
        imNew.putpixel((6, 18), colorsDict["black"])
        imNew.putpixel((7, 18), colorsDict["black"])
        imNew.putpixel((8, 18), colorsDict["black"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((16, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["nyanDogeOrange"])
        imNew.putpixel((1, 19), colorsDict["nyanDogeOrange"])
        imNew.putpixel((2, 19), colorsDict["black"])
        imNew.putpixel((3, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((4, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((5, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((6, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((7, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((8, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((9, 19), colorsDict["black"])
        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["black"])
        imNew.putpixel((12, 19), colorsDict["black"])
        imNew.putpixel((13, 19), colorsDict["black"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((16, 19), colorsDict["nyanDogeEdge"])
        imNew.putpixel((17, 19), colorsDict["black"])

        imNew.putpixel((0, 20), colorsDict["nyanDogeYellow"])
        imNew.putpixel((1, 20), colorsDict["black"])
        imNew.putpixel((2, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((4, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((6, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((8, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 20), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((10, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((12, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 20), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((14, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((15, 20), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((16, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((17, 20), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 20), colorsDict["black"])

        imNew.putpixel((0, 21), colorsDict["nyanDogeGreen"])
        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((4, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 21), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((6, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((8, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((10, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((12, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((14, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((15, 21), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((16, 21), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((17, 21), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["nyanDogeBlue"])
        imNew.putpixel((1, 22), colorsDict["black"])
        imNew.putpixel((2, 22), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((4, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((6, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 22), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((8, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((10, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 22), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((12, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((14, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((15, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((16, 22), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((17, 22), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 22), colorsDict["black"])

        imNew.putpixel((0, 23), colorsDict["nyanDogePurple"])
        imNew.putpixel((1, 23), colorsDict["black"])
        imNew.putpixel((2, 23), colorsDict["nyanDogeEdge"])
        imNew.putpixel((3, 23), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((4, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((5, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((6, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((7, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((8, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((9, 23), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((10, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((11, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((12, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((13, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((14, 23), colorsDict["nyanDogeSprinkle"])
        imNew.putpixel((15, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((16, 23), colorsDict["nyanDogeFrosting"])
        imNew.putpixel((17, 23), colorsDict["nyanDogeEdge"])
        imNew.putpixel((18, 23), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
