import os, sys
import random
from PIL import Image
from draw.drawType import drawSolanaBackground, drawType
from draw.drawBody import drawBody
from draw.drawNeck import drawNeck
from draw.drawHat import drawHat
from draw.drawEyes import drawEyes
from draw.drawMouth import drawMouth

def main():
    traitsDict = buildTraitsDict()
    random.seed(53330)

    makeNewImage(13370, "v___f_")

    dogeId = 1
    while len(traitsDict["type"]) > 0:
        roll = makeTraitsRoll(traitsDict)
        makeNewImage(dogeId, roll)
        dogeId = dogeId + 1

def makeNewImage(iter, traits):

    # Draw the tiny version
    im = Image.new('RGBA', (24, 24))
    drawSolanaBackground(im)
    drawType(im, traits[0])
    drawBody(im, traits[1])
    drawNeck(im, traits[2])
    drawMouth(im, traits[3])
    drawHat(im, traits[4])
    drawEyes(im, traits[5])
    #smallFileName = "images/" + str(iter) + "." + l1 + l2 + l3 + ".png"
    #im.save(smallFileName, "PNG")
    
    # Make a larger version which looks nicer
    im2 = im.resize((256, 256), resample=Image.NEAREST)
    #im2.show()
    largeFileName = "images/" + str(iter) + "." + traits + ".256.png"
    im2.save(largeFileName, "PNG")

def buildTraitsDict():
    traitsDict = {
        "type": ["n", "l", "d", "b", "r", "k", "n", "v", "z", "a", "n", "n", "n", "n", "n", "n", "n"], 
        "body": ["p", "w", "l", "c", "i", "k", "o", "s", "n", "y", "_", "_", "_", "_", "_", "_", "_"], 
        "neck": ["b", "r", "g", "c", "y", "o", "e", "s", "u", "d", "f", "n", "p", "_", "_", "_", "_"], 
        "mouth": ["b", "t", "j", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], 
        "hat": ["p", "b", "r", "g", "w", "m", "z", "c", "f", "j", "k", "o", "n", "f", "_", "_", "_"],
        "eyes": ["p", "c", "a", "h", "y", "g", "s", "t", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    }

    # Check that all entries are equal, else fail
    expectedLen = len(traitsDict["type"])
    for key in traitsDict.keys():
        if len(traitsDict[key]) != expectedLen:
            print("Error in buildTraitsDict(). " + str(key) + " does not match expectedLen: " + str(expectedLen))
            exit(-1)

    return traitsDict

def makeTraitsRoll(traitsDict):
    traitStr = ""
    for trait in ["type", "body", "neck", "mouth", "hat", "eyes"]:
        roll = random.choice(traitsDict[trait])
        traitsDict[trait].remove(roll)
        traitStr = traitStr + roll
    return traitStr

# Entry point
main()
