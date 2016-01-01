from lib.coginvasion.globals import CIGlobals

import random

CFSpeech       = 1 << 0
CFThought      = 1 << 1
CFQuicktalker  = 1 << 2
CFTimeout      = 1 << 3
CFPageButton   = 1 << 4
CFQuitButton   = 1 << 5
CFNoQuitButton = 1 << 6
CFReversed     = 1 << 7

WTNormal = 0
WTQuickTalker = 1
WTSystem = 2
WTBattleSOS = 3
WTEmote = 4
WTToontownBoardingGroup = 5

# Foreground, background:
WhisperColors = {
    WTNormal: (
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))   # Disabled
    ),
    WTQuickTalker: (
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))   # Disabled
    ),
    WTSystem: (
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 1.0, 0.8)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))   # Disabled
    ),
    WTBattleSOS: (
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 0.0, 0.8)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))   # Disabled
    ),
    WTEmote: (
        ((0.0, 0.0, 0.0, 1.0), (0.1, 0.7, 0.41, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (0.2, 0.7, 0.41, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.1, 0.6, 0.51, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.1, 0.6, 0.41, 0.6))   # Disabled
    ),
    WTToontownBoardingGroup: (
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.5, 0.1, 0.6)),  # Normal
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),  # Click
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.2, 0.6)),  # Rollover
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.1, 0.6))   # Disabled
    ),
}

WhiteListData = None

def loadWhiteListData():
    global WhiteListData
    if WhiteListData is None:
        whitelistFile = open('phase_3/etc/ciwhitelist.dat', 'r')
        WhiteListData = set()
        for word in whitelistFile.read().split():
            WhiteListData.add(word)
        whitelistFile.close()
        del whitelistFile

def getWhiteListData():
    return WhiteListData
    
garbleData = None

def getGarble(animal):
    global garbleData
    if garbleData is None:
        garbleData = {
            'dog' : CIGlobals.ChatGarblerDog,
            'rabbit' : CIGlobals.ChatGarblerRabbit,
            'cat' : CIGlobals.ChatGarblerCat,
            'mouse' : CIGlobals.ChatGarblerMouse,
            'monkey' : CIGlobals.ChatGarblerMonkey,
            'duck' : CIGlobals.ChatGarblerDuck,
            'bear' : CIGlobals.ChatGarblerBear,
            'horse' : CIGlobals.ChatGarblerHorse,
            'pig' : CIGlobals.ChatGarblerPig
        }
    
    garble = garbleData[animal]
    if garble:
        return garble
    return CIGlobals.ChatGarblerDefault

def filterChat(chat, animal):
    whiteList = getWhiteListData()
    for word in chat.split(" "):
        if len(word) == 0:
            continue
        checkWord = word
        if word and len(word) > 1 and word[len(word) - 1] in ['?', '!', '.']:
            checkWord = word.replace(word[len(word) - 1], '')
        if not (checkWord.lower() in whiteList):
            garble = getGarble(animal)
            chat = chat.replace(checkWord, random.choice(garble))
    return chat
