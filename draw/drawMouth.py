from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawMouth(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["mouth"][trait]
    if decodedType == "Bone":

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["black"])
        imNew.putpixel((20, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["bone"])
        imNew.putpixel((12, 16), colorsDict["bone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["bone"])
        imNew.putpixel((20, 16), colorsDict["bone"])
        imNew.putpixel((21, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["bone"])
        imNew.putpixel((12, 17), colorsDict["bone"])
        imNew.putpixel((13, 17), colorsDict["bone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["white"])
        imNew.putpixel((19, 17), colorsDict["bone"])
        imNew.putpixel((20, 17), colorsDict["bone"])
        imNew.putpixel((21, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["bone"])
        imNew.putpixel((13, 18), colorsDict["bone"])
        imNew.putpixel((14, 18), colorsDict["bone"])
        imNew.putpixel((15, 18), colorsDict["bone"])
        imNew.putpixel((16, 18), colorsDict["bone"])
        imNew.putpixel((17, 18), colorsDict["bone"])
        imNew.putpixel((18, 18), colorsDict["bone"])
        imNew.putpixel((19, 18), colorsDict["white"])
        imNew.putpixel((20, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["boneShade"])
        imNew.putpixel((12, 19), colorsDict["bone"])
        imNew.putpixel((13, 19), colorsDict["bone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["bone"])
        imNew.putpixel((19, 19), colorsDict["bone"])
        imNew.putpixel((20, 19), colorsDict["bone"])
        imNew.putpixel((21, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["boneShade"])
        imNew.putpixel((12, 20), colorsDict["boneShade"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((19, 20), colorsDict["boneShade"])
        imNew.putpixel((20, 20), colorsDict["bone"])
        imNew.putpixel((21, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((20, 21), colorsDict["black"])

    elif decodedType == "Tongue Out":
        imNew.putpixel((11, 16), colorsDict["tongue"])
        imNew.putpixel((12, 16), colorsDict["tongue"])
        imNew.putpixel((11, 17), colorsDict["tongue"])
        imNew.putpixel((12, 17), colorsDict["tongue"])
        imNew.putpixel((11, 18), colorsDict["tongue"])
        imNew.putpixel((12, 18), colorsDict["tongue"])

    elif decodedType == "Joint":
        imNew.putpixel((20, 11), colorsDict["jointSmoke"])
        imNew.putpixel((21, 11), colorsDict["jointSmoke"])
        imNew.putpixel((22, 11), colorsDict["jointSmoke"])

        imNew.putpixel((8, 12), colorsDict["jointEyes"])
        imNew.putpixel((14, 12), colorsDict["jointEyes"])

        imNew.putpixel((21, 12), colorsDict["jointSmoke"])

        imNew.putpixel((21, 14), colorsDict["jointSmoke"])

        imNew.putpixel((11, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict["joint"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((21, 16), colorsDict["jointSmoke"])

        imNew.putpixel((11, 17), colorsDict["black"])
        imNew.putpixel((12, 17), colorsDict["black"])
        imNew.putpixel((13, 17), colorsDict["joint"])
        imNew.putpixel((14, 17), colorsDict["black"])

        imNew.putpixel((13, 18), colorsDict["black"])
        imNew.putpixel((14, 18), colorsDict["joint"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((16, 18), colorsDict["black"])
        imNew.putpixel((17, 18), colorsDict["black"])
        imNew.putpixel((20, 18), colorsDict["jointSmoke"])

        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["joint"])
        imNew.putpixel((16, 19), colorsDict["jointBurn"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((19, 19), colorsDict["jointSmoke"])

        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
