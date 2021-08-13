from PIL import Image
from colors import colorsDict
from traitEncodings import TR_EN
from drawShirt import drawShirt

def drawBody(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TR_EN["body"][trait]
    if decodedType == "Pink Shirt":
        drawShirt(im, "pink")
    elif decodedType == "Lime Shirt":
        drawShirt(im, "lime")

    im.paste(imNew, (0,0), mask=imNew)
