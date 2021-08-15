from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from draw.drawBowtie import drawBowtie
from draw.drawNecklace import drawNecklace
from draw.drawScarf import drawScarf

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
    elif decodedType == "Red Collar":
        imNew.putpixel((7, 19), colorsDict["redCollarShade"])
        imNew.putpixel((8, 19), colorsDict["redCollar"])

        imNew.putpixel((9, 20), colorsDict["redCollar"])
        imNew.putpixel((10, 20), colorsDict["redCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["redCollar"])
        imNew.putpixel((13, 20), colorsDict["redCollar"])
        imNew.putpixel((14, 20), colorsDict["redCollar"])
    elif decodedType == "Pink Collar":
        imNew.putpixel((7, 19), colorsDict["pinkCollarShade"])
        imNew.putpixel((8, 19), colorsDict["pinkCollar"])

        imNew.putpixel((9, 20), colorsDict["pinkCollar"])
        imNew.putpixel((10, 20), colorsDict["pinkCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["pinkCollar"])
        imNew.putpixel((13, 20), colorsDict["pinkCollar"])
        imNew.putpixel((14, 20), colorsDict["pinkCollar"])

    elif decodedType == "Purple Bowtie":
        drawBowtie(imNew, "purpleBowtie", "purpleBowtieBlue")
    elif decodedType == "Green Bowtie":
        drawBowtie(imNew, "greenBowtie", "greenBowtieShade")
    elif decodedType == "Yellow Bowtie":
        drawBowtie(imNew, "yellowBowtie", "yellowBowtieShade")
    elif decodedType == "Orange Bowtie":
        drawBowtie(imNew, "orangeBowtie", "orangeBowtieShade")
    elif decodedType == "Emerald Necklace":
        gemColor = "necklaceEmerald"
        drawNecklace(imNew, gemColor)
    elif decodedType == "Sapphire Necklace":
        gemColor = "necklaceSapphire"
        drawNecklace(imNew, gemColor)
    elif decodedType == "Ruby Necklace":
        gemColor = "necklaceRuby"
        drawNecklace(imNew, gemColor)
    elif decodedType == "Diamond Necklace":
        gemColor = "necklaceDiamond"
        drawNecklace(imNew, gemColor)
    elif decodedType == "Red Scarf":
        primaryColor = "scarfRed"
        primaryColorShade = "scarfRedShade"
        drawScarf(imNew, primaryColor, primaryColorShade)
    elif decodedType == "Green Scarf":
        primaryColor = "scarfGreen"
        primaryColorShade = "scarfGreenShade"
        drawScarf(imNew, primaryColor, primaryColorShade)
    elif decodedType == "Cape":
        imNew.putpixel((0, 15), colorsDict["black"])
        imNew.putpixel((1, 15), colorsDict["black"])

        imNew.putpixel((0, 16), colorsDict["capeShade"])
        imNew.putpixel((1, 16), colorsDict["capeShade"])
        imNew.putpixel((2, 16), colorsDict["black"])
        imNew.putpixel((3, 16), colorsDict["black"])

        imNew.putpixel((0, 17), colorsDict["cape"])
        imNew.putpixel((1, 17), colorsDict["cape"])
        imNew.putpixel((2, 17), colorsDict["capeShade"])
        imNew.putpixel((3, 17), colorsDict["black"])
        imNew.putpixel((4, 17), colorsDict["black"])

        imNew.putpixel((0, 18), colorsDict["cape"])
        imNew.putpixel((1, 18), colorsDict["cape"])
        imNew.putpixel((2, 18), colorsDict["cape"])
        imNew.putpixel((3, 18), colorsDict["capeShade"])
        imNew.putpixel((4, 18), colorsDict["capeShade"])
        imNew.putpixel((5, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["cape"])
        imNew.putpixel((1, 19), colorsDict["cape"])
        imNew.putpixel((2, 19), colorsDict["cape"])
        imNew.putpixel((3, 19), colorsDict["cape"])
        imNew.putpixel((4, 19), colorsDict["cape"])
        imNew.putpixel((5, 19), colorsDict["capeShade"])
        imNew.putpixel((6, 19), colorsDict["black"])
        imNew.putpixel((7, 19), colorsDict["capeShade"])
        imNew.putpixel((8, 19), colorsDict["capeShade"])
        imNew.putpixel((9, 19), colorsDict["cape"])
        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["black"])
        imNew.putpixel((12, 19), colorsDict["black"])
        imNew.putpixel((13, 19), colorsDict["black"])

        imNew.putpixel((0, 20), colorsDict["cape"])
        imNew.putpixel((1, 20), colorsDict["cape"])
        imNew.putpixel((2, 20), colorsDict["cape"])
        imNew.putpixel((3, 20), colorsDict["black"])
        imNew.putpixel((4, 20), colorsDict["cape"])
        imNew.putpixel((5, 20), colorsDict["cape"])
        imNew.putpixel((6, 20), colorsDict["cape"])
        imNew.putpixel((7, 20), colorsDict["capeShade"])
        imNew.putpixel((8, 20), colorsDict["black"])
        imNew.putpixel((9, 20), colorsDict["black"])
        imNew.putpixel((10, 20), colorsDict["cape"])
        imNew.putpixel((11, 20), colorsDict["cape"])
        imNew.putpixel((12, 20), colorsDict["cape"])
        imNew.putpixel((13, 20), colorsDict["capeShade"])
        imNew.putpixel((14, 20), colorsDict["black"])

        imNew.putpixel((0, 21), colorsDict["capeShade"])
        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["black"])
        imNew.putpixel((4, 21), colorsDict["black"])
        imNew.putpixel((5, 21), colorsDict["black"])
        imNew.putpixel((6, 21), colorsDict["black"])
        imNew.putpixel((7, 21), colorsDict["black"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
