from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawBaseType(im, colorPrimary, colorShade, colorLight):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    imNew.putpixel((6, 5), colorsDict["black"])
    imNew.putpixel((17, 5), colorsDict["black"])

    imNew.putpixel((5, 6), colorsDict["black"])
    imNew.putpixel((6, 6), colorsDict[colorPrimary])
    imNew.putpixel((7, 6), colorsDict["black"])
    imNew.putpixel((16, 6), colorsDict["black"])
    imNew.putpixel((17, 6), colorsDict[colorPrimary])
    imNew.putpixel((18, 6), colorsDict["black"])

    imNew.putpixel((5, 7), colorsDict["black"])
    imNew.putpixel((6, 7), colorsDict[colorLight])
    imNew.putpixel((7, 7), colorsDict[colorPrimary])
    imNew.putpixel((8, 7), colorsDict["black"])
    imNew.putpixel((10, 7), colorsDict["black"])
    imNew.putpixel((11, 7), colorsDict["black"])
    imNew.putpixel((12, 7), colorsDict["black"])
    imNew.putpixel((13, 7), colorsDict["black"])
    imNew.putpixel((15, 7), colorsDict["black"])
    imNew.putpixel((16, 7), colorsDict[colorPrimary])
    imNew.putpixel((17, 7), colorsDict[colorLight])
    imNew.putpixel((18, 7), colorsDict["black"])

    imNew.putpixel((5, 8), colorsDict["black"])
    imNew.putpixel((6, 8), colorsDict[colorLight])
    imNew.putpixel((7, 8), colorsDict[colorPrimary])
    imNew.putpixel((8, 8), colorsDict["black"])
    imNew.putpixel((9, 8), colorsDict["black"])
    imNew.putpixel((10, 8), colorsDict[colorPrimary])
    imNew.putpixel((11, 8), colorsDict[colorPrimary])
    imNew.putpixel((12, 8), colorsDict[colorPrimary])
    imNew.putpixel((13, 8), colorsDict[colorPrimary])
    imNew.putpixel((14, 8), colorsDict["black"])
    imNew.putpixel((15, 8), colorsDict["black"])
    imNew.putpixel((16, 8), colorsDict[colorPrimary])
    imNew.putpixel((17, 8), colorsDict[colorLight])
    imNew.putpixel((18, 8), colorsDict["black"])

    imNew.putpixel((5, 9), colorsDict["black"])
    imNew.putpixel((6, 9), colorsDict[colorPrimary])
    imNew.putpixel((7, 9), colorsDict["black"])
    imNew.putpixel((8, 9), colorsDict[colorPrimary])
    imNew.putpixel((9, 9), colorsDict[colorPrimary])
    imNew.putpixel((10, 9), colorsDict[colorPrimary])
    imNew.putpixel((11, 9), colorsDict[colorPrimary])
    imNew.putpixel((12, 9), colorsDict[colorPrimary])
    imNew.putpixel((13, 9), colorsDict[colorPrimary])
    imNew.putpixel((14, 9), colorsDict[colorPrimary])
    imNew.putpixel((15, 9), colorsDict[colorPrimary])
    imNew.putpixel((16, 9), colorsDict["black"])
    imNew.putpixel((17, 9), colorsDict[colorPrimary])
    imNew.putpixel((18, 9), colorsDict["black"])

    imNew.putpixel((5, 10), colorsDict["black"])
    imNew.putpixel((6, 10), colorsDict["black"])
    imNew.putpixel((7, 10), colorsDict[colorPrimary])
    imNew.putpixel((8, 10), colorsDict["white"])
    imNew.putpixel((9, 10), colorsDict[colorPrimary])
    imNew.putpixel((10, 10), colorsDict[colorPrimary])
    imNew.putpixel((11, 10), colorsDict[colorPrimary])
    imNew.putpixel((12, 10), colorsDict[colorPrimary])
    imNew.putpixel((13, 10), colorsDict[colorPrimary])
    imNew.putpixel((14, 10), colorsDict[colorPrimary])
    imNew.putpixel((15, 10), colorsDict["white"])
    imNew.putpixel((16, 10), colorsDict[colorPrimary])
    imNew.putpixel((17, 10), colorsDict["black"])
    imNew.putpixel((18, 10), colorsDict["black"])

    imNew.putpixel((5, 11), colorsDict["black"])
    imNew.putpixel((6, 11), colorsDict[colorPrimary])
    imNew.putpixel((7, 11), colorsDict[colorPrimary])
    imNew.putpixel((8, 11), colorsDict[colorPrimary])
    imNew.putpixel((9, 11), colorsDict[colorPrimary])
    imNew.putpixel((10, 11), colorsDict[colorPrimary])
    imNew.putpixel((11, 11), colorsDict[colorPrimary])
    imNew.putpixel((12, 11), colorsDict[colorPrimary])
    imNew.putpixel((13, 11), colorsDict[colorPrimary])
    imNew.putpixel((14, 11), colorsDict[colorPrimary])
    imNew.putpixel((15, 11), colorsDict[colorPrimary])
    imNew.putpixel((16, 11), colorsDict[colorPrimary])
    imNew.putpixel((17, 11), colorsDict[colorPrimary])
    imNew.putpixel((18, 11), colorsDict["black"])

    imNew.putpixel((5, 12), colorsDict["black"])
    imNew.putpixel((6, 12), colorsDict[colorPrimary])
    imNew.putpixel((7, 12), colorsDict[colorPrimary])
    imNew.putpixel((8, 12), colorsDict["white"])
    imNew.putpixel((9, 12), colorsDict["black"])
    imNew.putpixel((10, 12), colorsDict[colorPrimary])
    imNew.putpixel((11, 12), colorsDict[colorPrimary])
    imNew.putpixel((12, 12), colorsDict[colorPrimary])
    imNew.putpixel((13, 12), colorsDict[colorPrimary])
    imNew.putpixel((14, 12), colorsDict["white"])
    imNew.putpixel((15, 12), colorsDict["black"])
    imNew.putpixel((16, 12), colorsDict[colorPrimary])
    imNew.putpixel((17, 12), colorsDict[colorPrimary])
    imNew.putpixel((18, 12), colorsDict["black"])

    imNew.putpixel((4, 13), colorsDict["black"])
    imNew.putpixel((5, 13), colorsDict["white"])
    imNew.putpixel((6, 13), colorsDict["white"])
    imNew.putpixel((7, 13), colorsDict[colorPrimary])
    imNew.putpixel((8, 13), colorsDict["black"])
    imNew.putpixel((9, 13), colorsDict["black"])
    imNew.putpixel((10, 13), colorsDict[colorPrimary])
    imNew.putpixel((11, 13), colorsDict[colorPrimary])
    imNew.putpixel((12, 13), colorsDict[colorPrimary])
    imNew.putpixel((13, 13), colorsDict[colorPrimary])
    imNew.putpixel((14, 13), colorsDict["black"])
    imNew.putpixel((15, 13), colorsDict["black"])
    imNew.putpixel((16, 13), colorsDict[colorPrimary])
    imNew.putpixel((17, 13), colorsDict["white"])
    imNew.putpixel((18, 13), colorsDict["white"])
    imNew.putpixel((19, 13), colorsDict["black"])

    imNew.putpixel((4, 14), colorsDict["black"])
    imNew.putpixel((5, 14), colorsDict["white"])
    imNew.putpixel((6, 14), colorsDict["white"])
    imNew.putpixel((7, 14), colorsDict["white"])
    imNew.putpixel((8, 14), colorsDict["white"])
    imNew.putpixel((9, 14), colorsDict["white"])
    imNew.putpixel((10, 14), colorsDict["white"])
    imNew.putpixel((11, 14), colorsDict["black"])
    imNew.putpixel((12, 14), colorsDict["black"])
    imNew.putpixel((13, 14), colorsDict["white"])
    imNew.putpixel((14, 14), colorsDict["white"])
    imNew.putpixel((15, 14), colorsDict["white"])
    imNew.putpixel((16, 14), colorsDict["white"])
    imNew.putpixel((17, 14), colorsDict["white"])
    imNew.putpixel((18, 14), colorsDict["white"])
    imNew.putpixel((19, 14), colorsDict["black"])

    imNew.putpixel((4, 15), colorsDict["black"])
    imNew.putpixel((5, 15), colorsDict["white"])
    imNew.putpixel((6, 15), colorsDict["white"])
    imNew.putpixel((7, 15), colorsDict["white"])
    imNew.putpixel((8, 15), colorsDict["white"])
    imNew.putpixel((9, 15), colorsDict["black"])
    imNew.putpixel((10, 15), colorsDict["white"])
    imNew.putpixel((11, 15), colorsDict["black"])
    imNew.putpixel((12, 15), colorsDict["black"])
    imNew.putpixel((13, 15), colorsDict["white"])
    imNew.putpixel((14, 15), colorsDict["black"])
    imNew.putpixel((15, 15), colorsDict["white"])
    imNew.putpixel((16, 15), colorsDict["white"])
    imNew.putpixel((17, 15), colorsDict["white"])
    imNew.putpixel((18, 15), colorsDict["white"])
    imNew.putpixel((19, 15), colorsDict["black"])

    imNew.putpixel((5, 16), colorsDict["black"])
    imNew.putpixel((6, 16), colorsDict["white"])
    imNew.putpixel((7, 16), colorsDict["white"])
    imNew.putpixel((8, 16), colorsDict["white"])
    imNew.putpixel((9, 16), colorsDict["white"])
    imNew.putpixel((10, 16), colorsDict["black"])
    imNew.putpixel((11, 16), colorsDict["tongue"])
    imNew.putpixel((12, 16), colorsDict["tongue"])
    imNew.putpixel((13, 16), colorsDict["black"])
    imNew.putpixel((14, 16), colorsDict["white"])
    imNew.putpixel((15, 16), colorsDict["white"])
    imNew.putpixel((16, 16), colorsDict["white"])
    imNew.putpixel((17, 16), colorsDict["white"])
    imNew.putpixel((18, 16), colorsDict["black"])

    imNew.putpixel((6, 17), colorsDict["black"])
    imNew.putpixel((7, 17), colorsDict["white"])
    imNew.putpixel((8, 17), colorsDict["white"])
    imNew.putpixel((9, 17), colorsDict["white"])
    imNew.putpixel((10, 17), colorsDict["white"])
    imNew.putpixel((11, 17), colorsDict["black"])
    imNew.putpixel((12, 17), colorsDict["black"])
    imNew.putpixel((13, 17), colorsDict["white"])
    imNew.putpixel((14, 17), colorsDict["white"])
    imNew.putpixel((15, 17), colorsDict["white"])
    imNew.putpixel((16, 17), colorsDict["white"])
    imNew.putpixel((17, 17), colorsDict["black"])

    imNew.putpixel((7, 18), colorsDict["black"])
    imNew.putpixel((8, 18), colorsDict["black"])
    imNew.putpixel((9, 18), colorsDict["white"])
    imNew.putpixel((10, 18), colorsDict["white"])
    imNew.putpixel((11, 18), colorsDict["white"])
    imNew.putpixel((12, 18), colorsDict["white"])
    imNew.putpixel((13, 18), colorsDict["white"])
    imNew.putpixel((14, 18), colorsDict["white"])
    imNew.putpixel((15, 18), colorsDict["black"])
    imNew.putpixel((16, 18), colorsDict["black"])

    imNew.putpixel((1, 19), colorsDict["black"])
    imNew.putpixel((6, 19), colorsDict["black"])
    imNew.putpixel((7, 19), colorsDict[colorShade])
    imNew.putpixel((8, 19), colorsDict[colorPrimary])
    imNew.putpixel((9, 19), colorsDict["black"])
    imNew.putpixel((10, 19), colorsDict["black"])
    imNew.putpixel((11, 19), colorsDict["black"])
    imNew.putpixel((12, 19), colorsDict["black"])
    imNew.putpixel((13, 19), colorsDict["black"])
    imNew.putpixel((14, 19), colorsDict["black"])

    imNew.putpixel((0, 20), colorsDict["black"])
    imNew.putpixel((1, 20), colorsDict[colorPrimary])
    imNew.putpixel((2, 20), colorsDict["black"])
    imNew.putpixel((5, 20), colorsDict["black"])
    imNew.putpixel((6, 20), colorsDict[colorShade])
    imNew.putpixel((7, 20), colorsDict[colorPrimary])
    imNew.putpixel((8, 20), colorsDict[colorPrimary])
    imNew.putpixel((9, 20), colorsDict[colorPrimary])
    imNew.putpixel((10, 20), colorsDict[colorPrimary])
    imNew.putpixel((11, 20), colorsDict[colorPrimary])
    imNew.putpixel((12, 20), colorsDict[colorPrimary])
    imNew.putpixel((13, 20), colorsDict[colorPrimary])
    imNew.putpixel((14, 20), colorsDict[colorPrimary])
    imNew.putpixel((15, 20), colorsDict["black"])

    imNew.putpixel((0, 21), colorsDict[colorPrimary])
    imNew.putpixel((1, 21), colorsDict["black"])
    imNew.putpixel((4, 21), colorsDict["black"])
    imNew.putpixel((5, 21), colorsDict[colorShade])
    imNew.putpixel((6, 21), colorsDict[colorPrimary])
    imNew.putpixel((7, 21), colorsDict[colorPrimary])
    imNew.putpixel((8, 21), colorsDict[colorPrimary])
    imNew.putpixel((9, 21), colorsDict[colorPrimary])
    imNew.putpixel((10, 21), colorsDict[colorPrimary])
    imNew.putpixel((11, 21), colorsDict[colorPrimary])
    imNew.putpixel((12, 21), colorsDict[colorPrimary])
    imNew.putpixel((13, 21), colorsDict[colorPrimary])
    imNew.putpixel((14, 21), colorsDict[colorPrimary])
    imNew.putpixel((15, 21), colorsDict["black"])

    imNew.putpixel((0, 22), colorsDict[colorPrimary])
    imNew.putpixel((1, 22), colorsDict["black"])
    imNew.putpixel((3, 22), colorsDict["black"])
    imNew.putpixel((4, 22), colorsDict[colorShade])
    imNew.putpixel((5, 22), colorsDict[colorPrimary])
    imNew.putpixel((6, 22), colorsDict[colorPrimary])
    imNew.putpixel((7, 22), colorsDict[colorPrimary])
    imNew.putpixel((8, 22), colorsDict[colorPrimary])
    imNew.putpixel((9, 22), colorsDict[colorPrimary])
    imNew.putpixel((10, 22), colorsDict[colorPrimary])
    imNew.putpixel((11, 22), colorsDict[colorPrimary])
    imNew.putpixel((12, 22), colorsDict[colorPrimary])
    imNew.putpixel((13, 22), colorsDict[colorPrimary])
    imNew.putpixel((14, 22), colorsDict[colorPrimary])
    imNew.putpixel((15, 22), colorsDict["black"])

    imNew.putpixel((0, 23), colorsDict[colorPrimary])
    imNew.putpixel((1, 23), colorsDict["black"])
    imNew.putpixel((2, 23), colorsDict["black"])
    imNew.putpixel((3, 23), colorsDict[colorShade])
    imNew.putpixel((4, 23), colorsDict[colorPrimary])
    imNew.putpixel((5, 23), colorsDict[colorPrimary])
    imNew.putpixel((6, 23), colorsDict[colorPrimary])
    imNew.putpixel((7, 23), colorsDict[colorPrimary])
    imNew.putpixel((8, 23), colorsDict[colorPrimary])
    imNew.putpixel((9, 23), colorsDict["black"])
    imNew.putpixel((10, 23), colorsDict[colorShade])
    imNew.putpixel((11, 23), colorsDict[colorShade])
    imNew.putpixel((12, 23), colorsDict["black"])
    imNew.putpixel((13, 23), colorsDict[colorShade])
    imNew.putpixel((14, 23), colorsDict[colorShade])
    imNew.putpixel((15, 23), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
