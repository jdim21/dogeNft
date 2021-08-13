from PIL import Image
from colors import colorsDict
from traitEncodings import TR_EN

def drawNeck(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TR_EN["neck"][trait]
    if decodedType == "Blue Collar":

        imNew.putpixel((7, 19), colorsDict["blueShade"])
        imNew.putpixel((8, 19), colorsDict["blue"])

        imNew.putpixel((9, 20), colorsDict["blue"])
        imNew.putpixel((10, 20), colorsDict["blue"])
        imNew.putpixel((11, 20), colorsDict["silver"])
        imNew.putpixel((12, 20), colorsDict["blue"])
        imNew.putpixel((13, 20), colorsDict["blue"])
        imNew.putpixel((14, 20), colorsDict["blue"])

    im.paste(imNew, (0,0), mask=imNew)
