from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from draw.drawBandana import drawBandana
from draw.drawTophat import drawTophat

def drawHat(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["hat"][trait]
    if decodedType == "Party Hat":

        imNew.putpixel((7, 1), colorsDict["partyHatStreamers"])
        imNew.putpixel((8, 1), colorsDict["partyHatStreamers"])
        imNew.putpixel((10, 1), colorsDict["partyHatStreamers"])
        imNew.putpixel((11, 1), colorsDict["partyHatStreamers"])
        imNew.putpixel((12, 1), colorsDict["partyHatStreamers"])

        imNew.putpixel((6, 2), colorsDict["partyHatStreamers"])
        imNew.putpixel((9, 2), colorsDict["partyHatStreamers"])
        imNew.putpixel((10, 2), colorsDict["partyHatStreamers"])

        imNew.putpixel((8, 3), colorsDict["partyHatStreamers"])
        imNew.putpixel((9, 3), colorsDict["partyHatStreamers"])
        imNew.putpixel((10, 3), colorsDict["partyHatOrange"])

        imNew.putpixel((7, 4), colorsDict["partyHatStreamers"])
        imNew.putpixel((9, 4), colorsDict["partyHatOrangeShade"])
        imNew.putpixel((10, 4), colorsDict["partyHatOrange"])
        imNew.putpixel((11, 4), colorsDict["partyHatOrange"])

        imNew.putpixel((9, 5), colorsDict["partyHatRedShade"])
        imNew.putpixel((10, 5), colorsDict["partyHatRed"])
        imNew.putpixel((11, 5), colorsDict["partyHatRed"])
        imNew.putpixel((12, 5), colorsDict["partyHatRed"])

        imNew.putpixel((9, 6), colorsDict["partyHatOrangeShade"])
        imNew.putpixel((10, 6), colorsDict["partyHatOrange"])
        imNew.putpixel((11, 6), colorsDict["partyHatOrange"])
        imNew.putpixel((12, 6), colorsDict["partyHatOrange"])
        imNew.putpixel((13, 6), colorsDict["partyHatOrange"])

        imNew.putpixel((9, 7), colorsDict["partyHatOrangeShade"])
        imNew.putpixel((10, 7), colorsDict["partyHatOrange"])
        imNew.putpixel((11, 7), colorsDict["partyHatOrange"])
        imNew.putpixel((12, 7), colorsDict["partyHatOrange"])
        imNew.putpixel((13, 7), colorsDict["partyHatRed"])
        imNew.putpixel((14, 7), colorsDict["partyHatRed"])

        imNew.putpixel((9, 8), colorsDict["partyHatRedShade"])
        imNew.putpixel((10, 8), colorsDict["partyHatRed"])
        imNew.putpixel((11, 8), colorsDict["partyHatRed"])
        imNew.putpixel((12, 8), colorsDict["partyHatRed"])
        imNew.putpixel((13, 8), colorsDict["partyHatRed"])
        imNew.putpixel((14, 8), colorsDict["partyHatRed"])

        imNew.putpixel((9, 9), colorsDict["partyHatRedShade"])
        imNew.putpixel((10, 9), colorsDict["partyHatRed"])
        imNew.putpixel((11, 9), colorsDict["partyHatRed"])
        imNew.putpixel((12, 9), colorsDict["partyHatRed"])
    elif decodedType == "Blue Bandana":
        drawBandana(imNew, "blue")
    elif decodedType == "Red Tophat":
        drawTophat(imNew, "redTophat", "redTophatShade", "redTophatStrap", "redTophatStrapShade", "redTophatBuckle")
    elif decodedType == "Green Tophat":
        drawTophat(imNew, "greenTophat", "greenTophatShade", "greenTophatStrap", "greenTophatStrapShade", "greenTophatBuckle")
    elif decodedType == "White Tophat":
        drawTophat(imNew, "whiteTophat", "whiteTophatShade", "whiteTophatStrap", "whiteTophatStrapShade", "whiteTophatBuckle")
    elif decodedType == "Pink Mohawk":
        imNew.putpixel((13, 4), colorsDict["black"])

        imNew.putpixel((12, 5), colorsDict["black"])
        imNew.putpixel((13, 5), colorsDict["pinkMohawk"])
        imNew.putpixel((14, 5), colorsDict["black"])

        imNew.putpixel((11, 6), colorsDict["black"])
        imNew.putpixel((12, 6), colorsDict["pinkMohawk"])
        imNew.putpixel((13, 6), colorsDict["pinkMohawk"])
        imNew.putpixel((14, 6), colorsDict["black"])

        imNew.putpixel((10, 7), colorsDict["black"])
        imNew.putpixel((11, 7), colorsDict["pinkMohawkShade"])
        imNew.putpixel((12, 7), colorsDict["pinkMohawk"])
        imNew.putpixel((13, 7), colorsDict["pinkMohawk"])
        imNew.putpixel((14, 7), colorsDict["black"])

        imNew.putpixel((9, 8), colorsDict["black"])
        imNew.putpixel((10, 8), colorsDict["pinkMohawkShade"])
        imNew.putpixel((11, 8), colorsDict["pinkMohawk"])
        imNew.putpixel((12, 8), colorsDict["pinkMohawk"])
        imNew.putpixel((13, 8), colorsDict["pinkMohawk"])
        imNew.putpixel((14, 8), colorsDict["black"])

        imNew.putpixel((12, 9), colorsDict["pinkMohawk"])
        imNew.putpixel((13, 9), colorsDict["pinkMohawk"])

        imNew.putpixel((13, 10), colorsDict["pinkMohawk"])

    im.paste(imNew, (0,0), mask=imNew)