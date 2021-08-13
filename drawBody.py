from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from drawShirt import drawShirt

def drawBody(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["body"][trait]
    if decodedType == "Pink Shirt":
        drawShirt(im, "pink")
    elif decodedType == "Lime Shirt":
        drawShirt(im, "lime")
    elif decodedType == "White Shirt":
        drawShirt(im, "white")
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

    im.paste(imNew, (0,0), mask=imNew)
