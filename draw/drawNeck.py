from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from draw.drawBowtie import drawBowtie

def drawNeck(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["neck"][trait]
    if decodedType == "Blue Collar":
        imNew.putpixel((7, 19), colorsDict["blueShade"])
        imNew.putpixel((8, 19), colorsDict["blue"])

        imNew.putpixel((9, 20), colorsDict["blue"])
        imNew.putpixel((10, 20), colorsDict["blue"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["blue"])
        imNew.putpixel((13, 20), colorsDict["blue"])
        imNew.putpixel((14, 20), colorsDict["blue"])
    if decodedType == "Red Collar":
        imNew.putpixel((7, 19), colorsDict["redCollarShade"])
        imNew.putpixel((8, 19), colorsDict["redCollar"])

        imNew.putpixel((9, 20), colorsDict["redCollar"])
        imNew.putpixel((10, 20), colorsDict["redCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["redCollar"])
        imNew.putpixel((13, 20), colorsDict["redCollar"])
        imNew.putpixel((14, 20), colorsDict["redCollar"])

    elif decodedType == "Purple Bowtie":
        drawBowtie(imNew, "purpleBowtie", "purpleBowtieBlue")
    elif decodedType == "Green Bowtie":
        drawBowtie(imNew, "greenBowtie", "greenBowtieShade")

    im.paste(imNew, (0,0), mask=imNew)
