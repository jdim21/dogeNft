from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from drawBowtie import drawBowtie

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

    elif decodedType == "Purple Bowtie":
        drawBowtie(imNew, "purpleBowtie", "purpleBowtieBlue")
    elif decodedType == "Green Bowtie":
        drawBowtie(imNew, "greenBowtie", "greenBowtieShade")
        #imNew.putpixel((8, 17), colorsDict["black"])
        #imNew.putpixel((15, 17), colorsDict["black"])

        #imNew.putpixel((7, 18), colorsDict["black"])
        #imNew.putpixel((8, 18), colorsDict["purpleBowtie"])
        #imNew.putpixel((9, 18), colorsDict["black"])
        #imNew.putpixel((10, 18), colorsDict["black"])
        #imNew.putpixel((13, 18), colorsDict["black"])
        #imNew.putpixel((14, 18), colorsDict["black"])
        #imNew.putpixel((15, 18), colorsDict["purpleBowtie"])
        #imNew.putpixel((16, 18), colorsDict["black"])

        #imNew.putpixel((7, 19), colorsDict["black"])
        #imNew.putpixel((8, 19), colorsDict["purpleBowtieBlue"])
        #imNew.putpixel((9, 19), colorsDict["purpleBowtie"])
        #imNew.putpixel((10, 19), colorsDict["purpleBowtie"])
        #imNew.putpixel((11, 19), colorsDict["black"])
        #imNew.putpixel((12, 19), colorsDict["black"])
        #imNew.putpixel((13, 19), colorsDict["purpleBowtie"])
        #imNew.putpixel((14, 19), colorsDict["purpleBowtie"])
        #imNew.putpixel((15, 19), colorsDict["purpleBowtieBlue"])
        #imNew.putpixel((16, 19), colorsDict["black"])

        #imNew.putpixel((7, 20), colorsDict["black"])
        #imNew.putpixel((8, 20), colorsDict["purpleBowtie"])
        #imNew.putpixel((9, 20), colorsDict["purpleBowtieBlue"])
        #imNew.putpixel((10, 20), colorsDict["black"])
        #imNew.putpixel((11, 20), colorsDict["purpleBowtieBlue"])
        #imNew.putpixel((12, 20), colorsDict["purpleBowtie"])
        #imNew.putpixel((13, 20), colorsDict["black"])
        #imNew.putpixel((14, 20), colorsDict["purpleBowtieBlue"])
        #imNew.putpixel((15, 20), colorsDict["purpleBowtie"])
        #imNew.putpixel((16, 20), colorsDict["black"])

        #imNew.putpixel((7, 21), colorsDict["black"])
        #imNew.putpixel((8, 21), colorsDict["purpleBowtie"])
        #imNew.putpixel((9, 21), colorsDict["black"])
        #imNew.putpixel((11, 21), colorsDict["black"])
        #imNew.putpixel((12, 21), colorsDict["black"])
        #imNew.putpixel((14, 21), colorsDict["black"])
        #imNew.putpixel((15, 21), colorsDict["purpleBowtie"])
        #imNew.putpixel((16, 21), colorsDict["black"])

        #imNew.putpixel((8, 22), colorsDict["black"])
        #imNew.putpixel((15, 22), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
