from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawBandana(im, color):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    if color == "blue":
        imNew.putpixel((5, 4), colorsDict["solanaBand"][4])
        imNew.putpixel((6, 4), colorsDict["solanaBand"][4])
        imNew.putpixel((17, 4), colorsDict["solanaBand"][4])
        imNew.putpixel((18, 4), colorsDict["solanaBand"][4])

        imNew.putpixel((4, 5), colorsDict["solanaBand"][5])
        imNew.putpixel((5, 5), colorsDict["solanaBand"][5])
        imNew.putpixel((6, 5), colorsDict["solanaBand"][5])
        imNew.putpixel((17, 5), colorsDict["solanaBand"][5])
        imNew.putpixel((18, 5), colorsDict["solanaBand"][5])
        imNew.putpixel((19, 5), colorsDict["solanaBand"][5])

        imNew.putpixel((4, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((5, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((6, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((7, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((16, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((17, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((18, 6), colorsDict["solanaBand"][6])
        imNew.putpixel((19, 6), colorsDict["solanaBand"][6])

        imNew.putpixel((4, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((5, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((6, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((7, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((8, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((9, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((10, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((11, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((12, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((13, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((14, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((15, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((16, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((17, 7), colorsDict["blueBandanaOutline"])
        imNew.putpixel((18, 7), colorsDict["solanaBand"][7])
        imNew.putpixel((19, 7), colorsDict["solanaBand"][7])

        imNew.putpixel((5, 8), colorsDict["blueBandanaOutline"])
        imNew.putpixel((6, 8), colorsDict["blueBandanaShade"])
        imNew.putpixel((7, 8), colorsDict["blueBandana"])
        imNew.putpixel((8, 8), colorsDict["blueBandana"])
        imNew.putpixel((9, 8), colorsDict["blueBandana"])
        imNew.putpixel((10, 8), colorsDict["blueBandana"])
        imNew.putpixel((11, 8), colorsDict["blueBandana"])
        imNew.putpixel((12, 8), colorsDict["blueBandana"])
        imNew.putpixel((13, 8), colorsDict["blueBandana"])
        imNew.putpixel((14, 8), colorsDict["blueBandana"])
        imNew.putpixel((15, 8), colorsDict["blueBandana"])
        imNew.putpixel((16, 8), colorsDict["blueBandana"])
        imNew.putpixel((17, 8), colorsDict["blueBandana"])
        imNew.putpixel((18, 8), colorsDict["blueBandanaOutline"])

        imNew.putpixel((4, 9), colorsDict["blueBandanaOutline"])
        imNew.putpixel((5, 9), colorsDict["blueBandanaShade"])
        imNew.putpixel((6, 9), colorsDict["blueBandana"])
        imNew.putpixel((7, 9), colorsDict["blueBandana"])
        imNew.putpixel((8, 9), colorsDict["blueBandana"])
        imNew.putpixel((9, 9), colorsDict["blueBandana"])
        imNew.putpixel((10, 9), colorsDict["blueBandana"])
        imNew.putpixel((11, 9), colorsDict["blueBandana"])
        imNew.putpixel((12, 9), colorsDict["blueBandana"])
        imNew.putpixel((13, 9), colorsDict["blueBandana"])
        imNew.putpixel((14, 9), colorsDict["blueBandana"])
        imNew.putpixel((15, 9), colorsDict["blueBandana"])
        imNew.putpixel((16, 9), colorsDict["blueBandana"])
        imNew.putpixel((17, 9), colorsDict["blueBandana"])
        imNew.putpixel((18, 9), colorsDict["blueBandanaOutline"])

        imNew.putpixel((0, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((1, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((2, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((3, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((4, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((5, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((6, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((7, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((8, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((9, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((10, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((11, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((12, 10), colorsDict["blueBandana"])
        imNew.putpixel((13, 10), colorsDict["blueBandana"])
        imNew.putpixel((14, 10), colorsDict["blueBandana"])
        imNew.putpixel((15, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((16, 10), colorsDict["blueBandanaOutline"])
        imNew.putpixel((17, 10), colorsDict["blueBandanaOutline"])

        imNew.putpixel((1, 11), colorsDict["blueBandanaShade"])
        imNew.putpixel((2, 11), colorsDict["blueBandanaOutline"])
        imNew.putpixel((12, 11), colorsDict["blueBandanaOutline"])
        imNew.putpixel((13, 11), colorsDict["blueBandanaOutline"])
        imNew.putpixel((14, 11), colorsDict["blueBandanaOutline"])

        imNew.putpixel((1, 12), colorsDict["blueBandanaOutline"])

        imNew.putpixel((0, 13), colorsDict["blueBandanaOutline"])


    im.paste(imNew, (0,0), mask=imNew)
