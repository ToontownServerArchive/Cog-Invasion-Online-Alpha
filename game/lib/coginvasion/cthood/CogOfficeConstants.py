# Filename: CogOfficeConstants.py
# Created by:  blach (17Dec15)

from panda3d.core import Point3

from lib.coginvasion.cog import Dept

RECEPTION_FLOOR = 0
BREAK_FLOOR = 1
CONFERENCE_FLOOR = 3
EXECUTIVE_FLOOR = 4

# Faceoff: Position of Toons during faceoff
# Guard: Position of a standing Cog before activation
# Chairs: Position of a Cog in a chair

# For chairs and guards, the first item in each list is the floor section they are associated with.

# For chairs, the second item is the in-chair position of the cog, and the last item is the fly-to position.

# For guards, the second item is the guard position (where they stand and face before activation).

# For faceoff, each list is a [x, y, z, h, p, r].

POINTS = {RECEPTION_FLOOR: {'chairs': [[0, (0.91, 16.92, 0, 149.53, 0, 0), (-5.03, 8.69, 0, 331.11, 0, 0)]],
                   'guard': [[0, (-24.8844, 14.6984, 0.025, 270, 0, 0)],
                             [0, (-24.7556, 9.97378, 0.025, 270, 0, 0)],
                             [0, (-24.7342, 4.31459, 0.025, 270, 0, 0)],
                             [0, (-24.717, -0.469944, 0.025, 270, 0, 0)]],
                   'faceoff': [[-0.00392879, -2.6104, 0.025, 72.7151, 0, 0],
                               [-0.0059577, 1.44267, 0.025, 77.4296, 0, 0],
                               [0.0266161, 5.98924, 0.025, 86.452, 0, 0],
                               [0.252626, 10.0329, 0.025, 92.4258, 0, 0]]},
         EXECUTIVE_FLOOR: {'chairs': [
                        # Small room chairs
                        [0, (-48.7442, -0.816753, 0, 112.712, 0, 0), (-36.96, 10.25, 0, 0, 0, 0)],

                        # Large room chairs
                        [1, (12.08, 5.43, 0, 270, 0, 0), (0.16, 5.50, 0, 0, 0, 0)],
                        [1, (12.08, -3.03, 0, 270, 0, 0), (0.16, -2.37, 0, 0, 0, 0)],
                        [1, (18.15, 12.0, 0, 180, 0, 0), (7.02, -14.69, 0, 0, 0, 0)],
                        [1, (18.15, -9.25, 0, 0, 0, 0), (7.02, 15.03, 0, 0, 0, 0)],

                        [2, (-5.66, 43.43, 0, 159.35, 0, 0), (-6.69, 26.24, 0, 0, 0, 0)],
                        [2, (6.38, 56.02, 0, 331.45, 0, 0), (9.25, 71.16, 0, 0, 0, 0)]
                    ],
                    'guard': [
                        # Small room guards
                        [0, (-31.9264, 10.4661, 0, 91.5449, 0, 0)],
                        [0, (-31.8784, 6.01984, 0, 88.9605, 0, 0)],
                        [0, (-31.802, 0.0619547, 0, 86.619, 0, 0)],
                        [0, (-31.7303, -5.69052, 0, 78.1931, 0, 0)],

                        # Large room guards
                        [1, (-13.329, 30.022, 0, 180.862, 0, 0)],
                        [1, (-8.81858, 30.1296, 0, 179.246, 0, 0)],
                        [1, (-3.17527, 30.2092, 0, 176.022, 0, 0)],
                        [1, (0.911327, 30.252, 0, 177.616, 0, 0)],

                        [2, (-13.329, 70.022, 0, 0, 0, 0)],
                        [2, (-8.81858, 70.1296, 0, 0, 0, 0)],
                        [2, (-3.17527, 70.2092, 0, 0, 0, 0)],
                        [2, (0.911327, 70.252, 0, 0, 0, 0)],
                    ],
                    'faceoff': [[-65.9154, 15.2706, 0, -102.464, 0, 0],
                                 [-65.9885, 11.5694, 0, -104.592, 0, 0],
                                 [-65.9267, 7.78086, 0, -97.9578, 0, 0],
                                 [-65.9494, 3.9793, 0, -92.8673, 0, 0]]},
         CONFERENCE_FLOOR: {'chairs': [[0, (17.16, 8.54, 0, 90, 0, 0), (6.42, 8.54, 0, 90, 0, 0)],
                                      [0, (-13.49, 16.70, 0, 180, 0, 0), (-0.95, 19.57, 0, 180, 0, 0)],
                                      [0, (-18.82, 9.99, 0, 270, 0, 0), (-5.61, 29.19, 0, 270, 0, 0)],
                                      [0, (-18.82, 1.08, 0, 270, 0, 0), (1.63, 29.19, 0, 270, 0, 0)]],
                     'guard': [[0, (8.96618, 24.8637, 0.025, 0, 0, 0)],
                               [0, (4.47451, 24.9036, 0.025, 0, 0, 0)],
                               [0, (-0.543322, 24.79, 0.025, 0, 0, 0)],
                               [0, (-6.3705, 24.6147, 0.025, 0, 0, 0)]],
                     'faceoff': [[5.91218, 51.6934, 0.025, 180, 0, 0],
                                 [1.88198, 51.6582, 0.025, 180, 0, 0],
                                 [-2.13479, 51.8396, 0.025, 180, 0, 0],
                                 [-6.00451, 51.9631, 0.025, 180, 0, 0]]}
}
