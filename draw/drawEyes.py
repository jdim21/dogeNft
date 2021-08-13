from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawEyes(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["eyes"][trait]
    if decodedType == "Pit Vipers":

        imNew.putpixel((8, 10), colorsDict["black"])
        imNew.putpixel((9, 10), colorsDict["black"])
        imNew.putpixel((10, 10), colorsDict["black"])
        imNew.putpixel((11, 10), colorsDict["black"])
        imNew.putpixel((12, 10), colorsDict["black"])
        imNew.putpixel((13, 10), colorsDict["black"])
        imNew.putpixel((14, 10), colorsDict["black"])
        imNew.putpixel((15, 10), colorsDict["black"])
        imNew.putpixel((16, 10), colorsDict["black"])
        imNew.putpixel((17, 10), colorsDict["black"])

        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["pvGreen"])
        imNew.putpixel((9, 11), colorsDict["pvYellow"])
        imNew.putpixel((10, 11), colorsDict["pvOrange"])
        imNew.putpixel((11, 11), colorsDict["pvRed"])
        imNew.putpixel((12, 11), colorsDict["pvRed"])
        imNew.putpixel((13, 11), colorsDict["pvRed"])
        imNew.putpixel((14, 11), colorsDict["pvOrange"])
        imNew.putpixel((15, 11), colorsDict["pvYellow"])
        imNew.putpixel((16, 11), colorsDict["pvGreen"])
        imNew.putpixel((17, 11), colorsDict["pvBlue"])

        imNew.putpixel((5, 12), colorsDict["black"])
        imNew.putpixel((6, 12), colorsDict["black"])
        imNew.putpixel((7, 12), colorsDict["pvBlue"])
        imNew.putpixel((8, 12), colorsDict["pvGreen"])
        imNew.putpixel((9, 12), colorsDict["pvYellow"])
        imNew.putpixel((10, 12), colorsDict["pvOrange"])
        imNew.putpixel((11, 12), colorsDict["pvRed"])
        imNew.putpixel((13, 12), colorsDict["pvRed"])
        imNew.putpixel((14, 12), colorsDict["pvOrange"])
        imNew.putpixel((15, 12), colorsDict["pvYellow"])
        imNew.putpixel((16, 12), colorsDict["pvGreen"])
        imNew.putpixel((17, 12), colorsDict["pvBlue"])

        imNew.putpixel((8, 13), colorsDict["pvGreen"])
        imNew.putpixel((9, 13), colorsDict["pvYellow"])
        imNew.putpixel((10, 13), colorsDict["pvOrange"])
        imNew.putpixel((11, 13), colorsDict["pvRed"])
        imNew.putpixel((13, 13), colorsDict["pvRed"])
        imNew.putpixel((14, 13), colorsDict["pvOrange"])
        imNew.putpixel((15, 13), colorsDict["pvYellow"])
        imNew.putpixel((16, 13), colorsDict["pvGreen"])

    elif decodedType == "Vice Shades":

        imNew.putpixel((5, 10), colorsDict["black"])
        imNew.putpixel((6, 10), colorsDict["black"])
        imNew.putpixel((7, 10), colorsDict["black"])
        imNew.putpixel((8, 10), colorsDict["black"])
        imNew.putpixel((9, 10), colorsDict["black"])
        imNew.putpixel((10, 10), colorsDict["black"])
        imNew.putpixel((11, 10), colorsDict["black"])
        imNew.putpixel((12, 10), colorsDict["black"])
        imNew.putpixel((13, 10), colorsDict["black"])
        imNew.putpixel((14, 10), colorsDict["black"])
        imNew.putpixel((15, 10), colorsDict["black"])
        imNew.putpixel((16, 10), colorsDict["black"])
        imNew.putpixel((17, 10), colorsDict["black"])

        imNew.putpixel((7, 11), colorsDict["black"])
        imNew.putpixel((8, 11), colorsDict["viceBrown"])
        imNew.putpixel((9, 11), colorsDict["viceBrown"])
        imNew.putpixel((10, 11), colorsDict["viceBrown"])
        imNew.putpixel((11, 11), colorsDict["viceBrown"])
        imNew.putpixel((12, 11), colorsDict["black"])
        imNew.putpixel((13, 11), colorsDict["viceBrown"])
        imNew.putpixel((14, 11), colorsDict["viceBrown"])
        imNew.putpixel((15, 11), colorsDict["viceBrown"])
        imNew.putpixel((16, 11), colorsDict["viceBrown"])
        imNew.putpixel((17, 11), colorsDict["black"])

        imNew.putpixel((7, 12), colorsDict["black"])
        imNew.putpixel((8, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((9, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((10, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((11, 12), colorsDict["black"])
        imNew.putpixel((13, 12), colorsDict["black"])
        imNew.putpixel((14, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((15, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((16, 12), colorsDict["viceBrownLight"])
        imNew.putpixel((17, 12), colorsDict["black"])

        imNew.putpixel((7, 13), colorsDict["black"])
        imNew.putpixel((8, 13), colorsDict["black"])
        imNew.putpixel((9, 13), colorsDict["black"])
        imNew.putpixel((10, 13), colorsDict["black"])
        imNew.putpixel((14, 13), colorsDict["black"])
        imNew.putpixel((15, 13), colorsDict["black"])
        imNew.putpixel((16, 13), colorsDict["black"])
        imNew.putpixel((17, 13), colorsDict["black"])

    elif decodedType == "Angry Eyebrows":

        imNew.putpixel((9, 10), colorsDict["black"])
        imNew.putpixel((14, 10), colorsDict["black"])

        imNew.putpixel((10, 11), colorsDict["black"])
        imNew.putpixel((13, 11), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
