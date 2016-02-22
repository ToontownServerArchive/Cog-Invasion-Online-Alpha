########################################
# Filename: HoodMgr.py
# Created by: blach (15Dec14)
########################################

from direct.showbase.DirectObject import DirectObject
from direct.directnotify.DirectNotifyGlobal import directNotify
from lib.coginvasion.globals import CIGlobals
import random

class HoodMgr(DirectObject):
    notify = directNotify.newCategory("HoodMgr")
    ToontownCentralInitialDropPoints = ([-90.7,
      -60.0,
      0.025,
      102.575,
      0,
      0],
     [-91.4,
      -40.5,
      -3.948,
      125.763,
      0,
      0],
     [-107.8,
      -17.8,
      -1.937,
      149.456,
      0,
      0],
     [-108.7,
      12.8,
      -1.767,
      158.756,
      0,
      0],
     [-42.1,
      -22.8,
      -1.328,
      -248.1,
      0,
      0],
     [-35.2,
      -60.2,
      0.025,
      -265.639,
      0,
      0])
    GagShopClerkPoints = {CIGlobals.CogTropCentral: [-80,
      -85.57,
      0.5,
      -13.5,
      0,
      0],

      CIGlobals.TheBrrrgh: [44.63,
      -80.73,
      6.16,
      62.76,
      0.00,
      0.00
      ],

      CIGlobals.DonaldsDreamland: [-42.99,
      -99.01,
      0.0,
      5.0,
      0.0,
      0.0],

      CIGlobals.DonaldsDock: [-119.38,
      -30.07,
      5.67,
      270.35,
      0.0,
      0.0]}
    BattleShopClerkPoints = {CIGlobals.CogTropCentral: [72.95,
      -152.49,
      2.50,
      180.00,
      0.0,
      0.0],

      CIGlobals.TheBrrrgh: [32.35,
      70.06,
      6.20,
      -135.15,
      0.00,
      0.00],

      CIGlobals.DonaldsDreamland: [93.11,
      38.94,
      -15.94,
      -90.0,
      0.0,
      -3.0],

      CIGlobals.DonaldsDock: [33.63,
      114.46,
      3.25,
      324.46,
      0.0,
      0.0]}
    ToontownCentralHQDropPoints = ([-43.5,
      42.6,
      -0.55,
      -100.454,
      0,
      0],
     [-53.0,
      12.5,
      -2.948,
      281.502,
      0,
      0],
     [-40.3,
      -18.5,
      -0.913,
      -56.674,
      0,
      0],
     [-1.9,
      -37.0,
      0.025,
      -23.43,
      0,
      0],
     [1.9,
      -5.9,
      4.0,
      -37.941,
      0,
      0])
    ToontownCentralTunnelDropPoints = ([-28.3,
      40.1,
      0.25,
      17.25,
      0,
      0],
     [-63.75,
      58.96,
      -0.5,
      -23.75,
      0,
      0],
     [-106.93,
      17.66,
      -2.2,
      99.0,
      0,
      0],
     [-116.0,
      -21.5,
      -0.038,
      50.0,
      0,
      0],
     [74.88,
      -115.0,
      2.53,
      -224.41,
      0,
      0],
     [30.488,
      -101.5,
      2.53,
      -179.23,
      0,
      0])
    dropPoints = {CIGlobals.DonaldsDock: ([-28.0,
                                    -2.5,
                                    5.8,
                                    120.0,
                                    0.0,
                                    0.0],
                                   [-22,
                                    13,
                                    5.8,
                                    155.6,
                                    0.0,
                                    0.0],
                                   [67,
                                    47,
                                    5.7,
                                    134.7,
                                    0.0,
                                    0.0],
                                   [62,
                                    19,
                                    5.7,
                                    97.0,
                                    0.0,
                                    0.0],
                                   [66,
                                    -27,
                                    5.7,
                                    80.5,
                                    0.0,
                                    0.0],
                                   [-114,
                                    -7,
                                    5.7,
                                    -97.0,
                                    -0.0,
                                    0.0],
                                   [-108,
                                    36,
                                    5.7,
                                    -153.8,
                                    -0.0,
                                    0.0],
                                   [-116,
                                    -46,
                                    5.7,
                                    -70.1,
                                    -0.0,
                                    0.0],
                                   [-63,
                                    -79,
                                    5.7,
                                    -41.2,
                                    -0.0,
                                    0.0],
                                   [-2,
                                    -79,
                                    5.7,
                                    57.4,
                                    -0.0,
                                    0.0],
                                   [-38,
                                    -78,
                                    5.7,
                                    9.1,
                                    -0.0,
                                    0.0]),
     CIGlobals.CogTropCentral: ([-60,
                                        -8,
                                        1.3,
                                        -90,
                                        0,
                                        0],
                                       [-66,
                                        -9,
                                        1.3,
                                        -274,
                                        0,
                                        0],
                                       [17,
                                        -28,
                                        4.1,
                                        -44,
                                        0,
                                        0],
                                       [87.7,
                                        -22,
                                        4,
                                        66,
                                        0,
                                        0],
                                       [-9.6,
                                        61.1,
                                        0,
                                        132,
                                        0,
                                        0],
                                       [-109.0,
                                        -2.5,
                                        -1.656,
                                        -90,
                                        0,
                                        0],
                                       [-35.4,
                                        -81.3,
                                        0.5,
                                        -4,
                                        0,
                                        0],
                                       [-103,
                                        72,
                                        0,
                                        -141,
                                        0,
                                        0],
                                       [93.5,
                                        -148.4,
                                        2.5,
                                        43,
                                        0,
                                        0],
                                       [25,
                                        123.4,
                                        2.55,
                                        272,
                                        0,
                                        0],
                                       [48,
                                        39,
                                        4,
                                        201,
                                        0,
                                        0],
                                       [-80,
                                        -61,
                                        0.1,
                                        -265,
                                        0,
                                        0],
                                       [-46.875,
                                        43.68,
                                        -1.05,
                                        124,
                                        0,
                                        0],
                                       [34,
                                        -105,
                                        2.55,
                                        45,
                                        0,
                                        0],
                                       [16,
                                        -75,
                                        2.55,
                                        56,
                                        0,
                                        0],
                                       [-27,
                                        -56,
                                        0.1,
                                        45,
                                        0,
                                        0],
                                       [100,
                                        27,
                                        4.1,
                                        150,
                                        0,
                                        0],
                                       [-70,
                                        4.6,
                                        -1.9,
                                        90,
                                        0,
                                        0],
                                       [-130.7,
                                        50,
                                        0.55,
                                        -111,
                                        0,
                                        0]),
     CIGlobals.ToontownCentral: ([54.1085, -74.5961, 8.03298, 58.8974, 0, 0],
                                 [-80.003, -41.0821, 8.01437, -37.6864, 0, 0],
                                 [-1.15776, 32.0713, 0.00864839, -119.806, 0, 0],
                                 [-36.0105, 77.8885, 7.9839, -111.583, 0, 0],
                                 [0.574271, -46.2154, 0.00862982, -322.394, 0, 0]),
     CIGlobals.TheBrrrgh: ([35,
                                  -32,
                                  6.2,
                                  138,
                                  0.0,
                                  0.0],
                                 [26,
                                  -105,
                                  6.2,
                                  -339,
                                  0.0,
                                  0.0],
                                 [-29,
                                  -139,
                                  6.2,
                                  -385,
                                  0.0,
                                  0.0],
                                 [-79,
                                  -123,
                                  6.2,
                                  -369,
                                  0.0,
                                  0.0],
                                 [-114,
                                  -86,
                                  3,
                                  -54,
                                  0.0,
                                  0.0],
                                 [-136,
                                  9,
                                  6.2,
                                  -125,
                                  0.0,
                                  0.0],
                                 [-75,
                                  92,
                                  6.2,
                                  -187,
                                  0.0,
                                  0.0],
                                 [-7,
                                  75,
                                  6.2,
                                  -187,
                                  0.0,
                                  0.0],
                                 [-106,
                                  -42,
                                  8.6,
                                  -111,
                                  0.0,
                                  0.0],
                                 [-116,
                                  -44,
                                  8.3,
                                  -20,
                                  0.0,
                                  0.0]),
     CIGlobals.MinniesMelodyland: ([86,
                                          44,
                                          -13.5,
                                          121.1,
                                          0.0,
                                          0.0],
                                         [88,
                                          -8,
                                          -13.5,
                                          91,
                                          0,
                                          0],
                                         [92,
                                          -76,
                                          -13.5,
                                          62.5,
                                          0.0,
                                          0.0],
                                         [53,
                                          -112,
                                          6.5,
                                          65.8,
                                          0.0,
                                          0.0],
                                         [-69,
                                          -71,
                                          6.5,
                                          -67.2,
                                          0.0,
                                          0.0],
                                         [-75,
                                          21,
                                          6.5,
                                          -100.9,
                                          0.0,
                                          0.0],
                                         [-21,
                                          72,
                                          6.5,
                                          -129.5,
                                          0.0,
                                          0.0],
                                         [56,
                                          72,
                                          6.5,
                                          138.2,
                                          0.0,
                                          0.0],
                                         [-41,
                                          47,
                                          6.5,
                                          -98.9,
                                          0.0,
                                          0.0]),
     CIGlobals.DaisyGardens: ([0,
                                     0,
                                     0,
                                     -10.5,
                                     0,
                                     0],
                                    [76,
                                     35,
                                     1.1,
                                     -30.2,
                                     0.0,
                                     0.0],
                                    [97,
                                     106,
                                     0.0,
                                     51.4,
                                     0.0,
                                     0.0],
                                    [51,
                                     180,
                                     10.0,
                                     22.6,
                                     0.0,
                                     0.0],
                                    [-14,
                                     203,
                                     10.0,
                                     85.6,
                                     0.0,
                                     0.0],
                                    [-58,
                                     158,
                                     10.0,
                                     -146.9,
                                     0.0,
                                     0.0],
                                    [-86,
                                     128,
                                     0.0,
                                     -178.9,
                                     0.0,
                                     0.0],
                                    [-64,
                                     65,
                                     0.0,
                                     17.7,
                                     0.0,
                                     0.0],
                                    [-13,
                                     39,
                                     0.0,
                                     -15.7,
                                     0.0,
                                     0.0],
                                    [-12,
                                     193,
                                     0.0,
                                     -112.4,
                                     0.0,
                                     0.0],
                                    [87,
                                     128,
                                     0.0,
                                     45.4,
                                     0.0,
                                     0.0]),
     CIGlobals.DonaldsDreamland: ([77,
                                         91,
                                         0.0,
                                         124.4,
                                         0.0,
                                         0.0],
                                        [29,
                                         92,
                                         0.0,
                                         -154.5,
                                         0.0,
                                         0.0],
                                        [-28,
                                         49,
                                         -16.4,
                                         -142.0,
                                         0.0,
                                         0.0],
                                        [21,
                                         40,
                                         -16.0,
                                         -65.1,
                                         0.0,
                                         0.0],
                                        [48,
                                         27,
                                         -15.4,
                                         -161.0,
                                         0.0,
                                         0.0],
                                        [-2,
                                         -22,
                                         -15.2,
                                         -132.1,
                                         0.0,
                                         0.0],
                                        [-92,
                                         -88,
                                         0.0,
                                         -116.3,
                                         0.0,
                                         0.0],
                                        [-56,
                                         -93,
                                         0.0,
                                         -21.5,
                                         0.0,
                                         0.0],
                                        [20,
                                         -88,
                                         0.0,
                                         -123.4,
                                         0.0,
                                         0.0],
                                        [76,
                                         -90,
                                         0.0,
                                         11.0,
                                         0.0,
                                         0.0]),
     CIGlobals.GoofySpeedway: ([-0.7,
                                      62,
                                      0.08,
                                      182,
                                      0,
                                      0],
                                     [-1,
                                      -30,
                                      0.06,
                                      183,
                                      0,
                                      0],
                                     [-13,
                                      -120,
                                      0,
                                      307,
                                      0,
                                      0],
                                     [16.4,
                                      -120,
                                      0,
                                      65,
                                      0,
                                      0],
                                     [-0.5,
                                      -90,
                                      0,
                                      182,
                                      0,
                                      0],
                                     [-30,
                                      -25,
                                      -0.373,
                                      326,
                                      0,
                                      0],
                                     [29,
                                      -17,
                                      -0.373,
                                      32,
                                      0,
                                      0]),
     CIGlobals.GolfZone: ([-49.6,
                                 102,
                                 0,
                                 162,
                                 0,
                                 0],
                                [-22.8,
                                 36.6,
                                 0,
                                 157.5,
                                 0,
                                 0],
                                [40,
                                 51,
                                 0,
                                 185,
                                 0,
                                 0],
                                [48.3,
                                 122.2,
                                 0,
                                 192,
                                 0,
                                 0],
                                [106.3,
                                 69.2,
                                 0,
                                 133,
                                 0,
                                 0],
                                [-81.5,
                                 47.2,
                                 0,
                                 183,
                                 0,
                                 0],
                                [-80.5,
                                 -84.2,
                                 0,
                                 284,
                                 0,
                                 0],
                                [73,
                                 -111,
                                 0,
                                 354,
                                 0,
                                 0]),
     CIGlobals.OutdoorZone: ([-165.8,
                                    108,
                                    0.025,
                                    252,
                                    0,
                                    0],
                                   [21,
                                    130,
                                    0.16,
                                    170,
                                    0,
                                    0],
                                   [93,
                                    78.5,
                                    0.23,
                                    112,
                                    0,
                                    0],
                                   [79,
                                    -1.6,
                                    0.75,
                                    163,
                                    0,
                                    0],
                                   [10,
                                    33,
                                    5.32,
                                    130.379,
                                    0,
                                    0],
                                   [-200,
                                    -42,
                                    0.025,
                                    317.543,
                                    0,
                                    0],
                                   [-21,
                                    -65,
                                    0.335,
                                    -18,
                                    0,
                                    0],
                                   [23,
                                    68.5,
                                    4.51,
                                    -22.808,
                                    0,
                                    0]),
     CIGlobals.SellbotHQ: ([64,
                                  -128,
                                  0.26,
                                  36,
                                  0,
                                  0],
                                 [9,
                                  -140,
                                  0.26,
                                  0,
                                  0,
                                  0],
                                 [-82,
                                  -112,
                                  0.26,
                                  -127,
                                  0,
                                  0],
                                 [-73,
                                  -213,
                                  0.26,
                                  -23,
                                  0,
                                  0],
                                 [-20,
                                  -243,
                                  0.26,
                                  -9,
                                  0,
                                  0],
                                 [79,
                                  -208,
                                  0.26,
                                  43,
                                  0,
                                  0]),
     CIGlobals.CashbotHQ: ([102,
                                  -437,
                                  -23.439,
                                  360,
                                  0,
                                  0],
                                 [124,
                                  -437,
                                  -23.439,
                                  360,
                                  0,
                                  0],
                                 [110,
                                  -446,
                                  -23.439,
                                  360,
                                  0,
                                  0],
                                 [132,
                                  -446,
                                  -23.439,
                                  360,
                                  0,
                                  0]),
     CIGlobals.LawbotHQ: ([77.5,
                                 129.13,
                                 -68.4,
                                 -166.6,
                                 0,
                                 0],
                                [-57.7,
                                 80.75,
                                 -68.4,
                                 -139.2,
                                 0,
                                 0],
                                [203.3,
                                 46.36,
                                 -68.4,
                                 -213.37,
                                 0,
                                 0],
                                [88.2,
                                 -336.52,
                                 -68.4,
                                 -720.4,
                                 0,
                                 0],
                                [232.77,
                                 -305.33,
                                 -68.4,
                                 -651,
                                 0,
                                 0],
                                [-20.16,
                                 -345.76,
                                 -68.4,
                                 -777.98,
                                 0,
                                 0])}
    DefaultDropPoint = [0,
     0,
     0,
     0,
     0,
     0]
    dbgDropMode = 1
    currentDropPoint = 0

    def getDropPoint(self, dropPointList):
        if self.dbgDropMode:
            return random.choice(dropPointList)
        else:
            dropPoint = self.currentDropPoint % len(dropPointList)
            self.currentDropPoint = (self.currentDropPoint + 1) % len(dropPointList)
            return dropPointList[dropPoint]

    def getPlaygroundCenterFromId(self, hood):
        dropPointList = self.dropPoints.get(hood, None)
        if dropPointList:
            return self.getDropPoint(dropPointList)
        else:
            self.notify.warning('Hood %s is not in self.dropPoints!' % hood)
            return self.DefaultDropPoint

    def extractGroupName(self, groupFullName):
        return groupFullName.split(':', 1)[0]
