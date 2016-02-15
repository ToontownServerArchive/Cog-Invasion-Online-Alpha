########################################
# Filename: ToonGlobals.py
# Created by: DecodedLogic (14Feb16)
########################################

# First argument is phase, next is type, body part, pant type, and finally model detail.
# Pant type is either: Shorts, Skirt, or Naked.
# Type is either: SS, MM, or LL.

BASE_MODEL = "phase_%s/models/char/dog%s_%s-%s-%s.bam"

# These are the animations
# Key is the code name of the animation,
# Value starts with phase number, second
# is the actual file name of the animation.
# If you aren't using the base model, you must
# specify the path of the animation after the file name.

ANIMATIONS = {
    "neutral" : [3, "neutral"],
    "run" : [3, "run"],
    "walk" : [3.5, "walk"],
    "pie" : [3.5, "pie-throw"],
    "fallb" : [4, "slip-backward"],
    "fallf" : [4, "slip-forward"],
    "lose" : [5, "lose"],
    "win" : [3.5, "victory-dance"],
    "squirt" : [5, "water-gun"],
    "zend" : [3.5, "jump-zend"],
    "tele" : [3.5, "teleport"],
    "book" : [3.5, "book"],
    "leap": [3.5, "leap_zhang"],
    "jump": [3.5, "jump-zhang"],
    "happy": [3.5, "jump"],
    "shrug": [3.5, "shrug"],
    "hdance": [5, "happy-dance"],
    "wave": [3.5, "wave"],
    "swim": [4, "swim"],
    "toss": [5, "toss"],
    "cringe": [3.5, "cringe"],
    "conked": [3.5, "conked"],
    "catchneutral": [4, "gameneutral"],
    "catchrun": [4, "gamerun"],
    "hold-bottle": [5, "hold-bottle"],
    "push-button" : [3.5, "press-button"],
    "happy-dance" : [5, "happy-dance"],
    "juggle" : [5, "juggle"],
    "shout": [5, "shout"],
    "dneutral": [4, "sad-neutral"],
    "dwalk": [4, "losewalk"],
    "smooch" : [5, "smooch"],
    "conked" : [3.5, "conked"],
    "sound" : [5, "shout"],
    "sprinkle-dust" : [5, "sprinkle-dust"],
    "start-sit" : [4, "intoSit"],
    "sit" : [4, "sit"],
    "water": [3.5, "water"],
    "spit": [5, "spit"],
    "firehose": [5, "firehose"]
}

# These are the admin tokens
# Key is token id, value is the actual model id.
STAFF_TOKENS = {0 : 500, 2 : 300}

