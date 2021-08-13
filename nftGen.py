import os, sys
import random
from PIL import Image
from drawType import drawSolanaBackground, drawType
from drawBody import drawBody
from drawNeck import drawNeck

def main():
    traitsDict = buildTraitsDict()
    random.seed(5333)

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
    #drawLetterAtPosition(l2, 1, im)
    #drawLetterAtPosition(l3, 2, im)
    #smallFileName = "images/" + str(iter) + "." + l1 + l2 + l3 + ".png"
    #im.save(smallFileName, "PNG")
    
    # Make a larger version which looks nicer
    im2 = im.resize((256, 256), resample=Image.NEAREST)
    #im2.show()
    largeFileName = "images/" + str(iter) + "." + traits + ".256.png"
    im2.save(largeFileName, "PNG")

def buildTraitsDict():
    traitsDict = {
        "type": ["n", "n"], 
        "body": ["p", "l"], 
        "neck": ["b", "_"], 
        "mouth": ["_", "_"], 
        "eyes": ["_", "_"], 
        "hat": ["_", "_"]
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
    for trait in ["type", "body", "neck", "mouth", "eyes", "hat"]:
        roll = random.choice(traitsDict[trait])
        traitsDict[trait].remove(roll)
        traitStr = traitStr + roll
    return traitStr

# Entry point
main()
