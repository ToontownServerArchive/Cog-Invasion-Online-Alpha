"""

  Filename: CogGuardGlobals.py
  Created by: blach (31Mar15)

"""

from panda3d.core import *

GuardDialog = {
    'arrest': [
        "Get your hands over your head!",
        "Put your hands over your head!",
        "Put your hands over your head and drop the weapon.",
        "Put your hands over your head and don't move!",
        "Hands behind your back!",
        "Get your hands behind your back!",
        "You're under arrest!",
        "You're arrested!",
        "Put your hands behind your back!",
        "Where did you think you were going?",
        "Don't move!",
        "Place your hands over the top of your head."
    ],
    'disregard': [
        "Hmm, I guess it was nothing.",
        "I swear I saw something.",
        "I swear I heard something.",
        "My mind must be playing tricks on me.",
        "Hmm, nothing there."
    ],
    'somethingInSight': [
        "Who goes there?!",
        "Whoa, what was that?",
        "I think I just saw something.",
        "Did I just see someone?",
        "Did I just see a Toon?"
    ],
    'spot': [
        "It's a Toon! Hey, stop right there!",
        "Stop right there, Toon!",
        "Trespasser!",
        "Get back here!",
        "I've got a 10-76 in sight!",
        "10-43 of a 10-76!",
        "In pursuit of a prowler!"
    ],
    'chase': [
        "Like my face? It's the last thing you'll see.",
        "You can run, but you can't hide.",
        "Stop running!",
        "Running will just make it last longer!",
        "Catching you will just be my uprising.",
        "Let's make this fast, I'm having lunch with Mr. Hollywood."
    ],
    'shot': [
        "I'm hit!",
        "Ow!",
        "Ouch!",
        "Ouch! 10-52!",
        "Ouch! 10-33!",
        "Oof!",
        "Oof! 11-99!"
    ],
    'heard': [
        "What was that noise?",
        "Am I the only one who hears that?",
        "Did you hear that too?",
        "Whoa, what was that?",
        "Whoa, I think I just heard something..."
    ],
    'suspect': [
        "OK, there's gotta be someone around here.",
        "I'm definitely hearing somebody.",
        "This is getting ridiculous. I'm searching for this guy.",
        "Okay come out now!",
        "Okay I know you're there!",
        "Come on out!",
        "Come out wherever you are!",
        "Okay stop hiding and get your hands on top of your head!",
    ]
}

FactoryWalkPoints = {
	'1': Point3(7.02, 102.03, 3.73
	),
	'2': Point3(36.15, 102.0, 3.73
	),
	'3': Point3(21.00, 91.48, 3.73
	),
	'4': Point3(21.00, 34.75, 3.73
	),
	'5': Point3(36.60, 21.79, 3.73
	),
	'6': Point3(6.84, 21.79, 3.73
	),
	'7': Point3(57.42, 113.02, 3.73
	),
	'8': Point3(57.42, 145.53, 3.73
	),
	'9': Point3(39.48, 126.06, 3.73
	),
	'10': Point3(39.48, 158.71, 3.73
	),
	'11': Point3(21.46, 154.05, 3.73
	),
	'12': Point3(20.8298492432, 127.261932373, 3.72601008415
	),
	'13': Point3(-15.8184213638, 107.70401001, 3.72601008415
	),
	'14': Point3(-12.6347436905, 150.498260498, 3.72601008415
	),
	'15': Point3(1.862185359, 127.62688446, 3.72601008415
	),
	'16': Point3(20.7491359711, 181.617355347, 3.72601008415
	),
	'17': Point3(15.9736003876, 195.81703186, 3.72601008415
	),
	'18': Point3(28.177230835, 190.976760864, 3.72601008415
	),
	'19': Point3(-11.136932373, 178.399993896, 3.72601008415
	),
	'20': Point3(20.5021152496, 220.11050415, 3.72601008415
	),
	'21': Point3(20.5021152496, 250.118209839, 3.72601008415
	),
	'22': Point3(20.5021152496, 266.976531982, 3.73070979118
	),
	'23': Point3(-1.70821225643, 266.976531982, 3.72704768181
	),
	'24': Point3(-9.31725215912, 311.727172852, 23.6061973572
	),
	'25': Point3(6.00064468384, 311.727172852, 23.6010684967
	),
	'26': Point3(-2.11948752403, 393.333221436, 58.6142539978
	),
	'27': Point3(45.626335144, 250.790618896, 3.74456477165
	),
	'28': Point3(72.1958084106, 250.790618896, 8.7260093689
	),
	'29': Point3(102.783546448, 236.582550049, 8.68389701843
	),
	'30': Point3(102.783546448, 254.469970703, 8.68389701843
	),
	'31': Point3(182.737991333, 250.998352051, 8.68877983093
	),
	'32': Point3(170.940628052, 274.417785645, 8.71758842468
	),
	'33': Point3(170.940628052, 311.51348877, 18.7258872986
	),
	'34': Point3(155.780151367, 311.51348877, 18.7258872986
	),
	'35': Point3(157.472915649, 338.74230957, 18.7259998322
	),
	'36': Point3(188.975006104, 341.060272217, 18.7259998322
	),
	'37': Point3(155.905532837, 373.534423828, 18.7259998322
	),
	'38': Point3(155.905532837, 466.330718994, 23.7259998322
	),
	'39': Point3(145.229248047, 472.678375244, 23.7259998322
	),
	'40': Point3(145.229248047, 484.490905762, 23.7259998322
	),
	'41': Point3(85.9906768799, 493.035339355, 23.7259998322
	),
	'42': Point3(64.7825775146, 495.028625488, 23.7259998322
	),
	'43': Point3(64.7825775146, 437.651000977, 24.8016834259
	),
	'44': Point3(59.5449943542, 421.77545166, 28.720872879
	),
	'45': Point3(45.8543891907, 420.722930908, 28.7196521759
	),
	'46': Point3(38.069896698, 431.21975708, 28.7245349884
	),
	'47': Point3(38.069896698, 461.540252686, 28.7245349884
	),
	'48': Point3(5.61381816864, 471.174255371, 28.7245349884
	),
	'49': Point3(22.9643363953, 482.653747559, 28.7245349884
	),
	'50': Point3(-12.0776023865, 485.552703857, 28.7245349884
	),
	'51': Point3(5.63659906387, 451.67791748, 28.7245349884
	),
	'52': Point3(5.63659906387, 432.762542725, 28.7245349884
	),
	'53': Point3(19.1862716675, 424.348571777, 28.7235584259
	),
	'54': Point3(22.0231189728, 404.197906494, 33.7259979248
	),
	'55': Point3(-9.55003833771, 405.499603271, 43.7059783936
	),
	'56': Point3(-5.86112260818, 420.435211182, 43.7108612061
	),
	'57': Point3(-34.9273223877, 456.744995117, 28.7250232697
	),
	'58': Point3(-16.2481575012, 460.112060547, 28.7250232697
	),
	'59': Point3(-39.9931030273, 419.621917725, 28.720872879
	),
	'60': Point3(-54.2984924316, 423.636260986, 28.7245349884
	),
	'61': Point3(-54.2984924316, 494.452941895, 23.7259998322
	),
	'62': Point3(-108.340660095, 494.452941895, 23.7259998322
	),
	'63': Point3(-129.677352905, 485.094451904, 23.7259998322
	),
	'64': Point3(-313.463043213, 495.315826416, 23.7259998322
	),
	'65': Point3(-314.154663086, 595.736450195, 23.7376232147
	),
	'66': Point3(-403.777557373, 595.736450195, 23.7376232147
	),
	'67': Point3(-481.709381104, 595.736450195, 8.72601032257
	),
	'68': Point3(-494.487335205, 578.331970215, 8.72601032257
	),
	'69': Point3(-494.144317627, 386.693328857, 8.72601032257
	),
	'70': Point3(-494.144317627, 370.74432373, 8.72601032257
	),
	'71': Point3(-494.144317627, 355.754882812, 8.72601032257
	),
	'72': Point3(-459.184967041, 355.756225586, 18.7259998322
	),
	'73': Point3(-459.184967041, 385.447113037, 18.7259998322
	),
	'74': Point3(-459.184967041, 371.280548096, 18.7259998322
	),
	'75': Point3(-436.206726074, 371.280548096, 18.7259998322
	),
	'76': Point3(-392.863433838, 362.806182861, 18.7259998322
	),
	'77': Point3(-383.311065674, 383.347747803, 18.7259998322
	),
	'78': Point3(-316.622070312, 413.971374512, 18.7259998322
	),
	'79': Point3(-316.622070312, 325.665863037, 18.7259998322
	),
	'80': Point3(-256.322418213, 354.900543213, 18.7259998322
	),
	'81': Point3(-256.322418213, 390.568115234, 18.7259998322
	),
	'82': Point3(-214.715209961, 372.348297119, 18.7259998322
	),
	'83': Point3(-129.384460449, 371.602508545, 18.7259998322
	),
	'84': Point3(-129.384460449, 354.145294189, 18.7259998322
	),
	'85': Point3(-114.271522522, 340.94833374, 18.7259998322
	),
	'86': Point3(-114.271522522, 310.575469971, 18.7259998322
	),
	'87': Point3(-152.82208252, 300.420196533, 18.7259998322
	),
	'88': Point3(-168.71031189, 294.892425537, 18.7259998322
	),
	'89': Point3(-173.580856323, 289.509796143, 18.7259998322
	),
	'90': Point3(-173.580856323, 250.033050537, 8.72601032257
	),
	'91': Point3(-164.228210449, 240.328811646, 8.72601032257
	),
	'92': Point3(-143.334457397, 240.701599121, 8.72601032257
	),
	'93': Point3(-133.640853882, 243.669052124, 8.72601032257
	),
	'94': Point3(-117.203361511, 242.005691528, 8.72601032257
	),
	'95': Point3(-80.3400650024, 244.324478149, 8.72601032257
	),
	'96': Point3(-55.8061103821, 250.527297974, 8.72601032257
	),
	'97': Point3(-2.45391345024, 250.527297974, 3.72601008415
	),
	'98': Point3(4.77302837372, 541.511352539, 38.7259979248
	),
	'99': Point3(-49.9130744934, 540.511962891, 43.7259979248
	),
	'100': Point3(65.2844085693, 541.129455566, 43.7259979248)
}

FactoryGuardPoints = {
	'1': [Point3(50.8605651855, 493.650238037, 28.7250232697),
	Vec3(313.025054932, 0.0, 0.0
	)],
	'2': [Point3(50.5030555725, 479.770721436, 28.7250232697),
	Vec3(270.0, 0.0, 0.0
	)],
	'3': [Point3(-24.8482875824, 498.838745117, 28.7250232697),
	Vec3(0.0, 0.0, 0.0
	)],
	'4': [Point3(-24.8482875824, 446.4090271, 28.7252674103),
	Vec3(180.0, 0.0, 0.0
	)],
	'5': [Point3(-41.4686851501, 446.4090271, 28.7252674103),
	Vec3(90.0, 0.0, 0.0
	)],
	'6': [Point3(-7.23602104187, 434.330535889, 28.7252674103),
	Vec3(90.0, 0.0, 0.0
	)],
	'7': [Point3(17.745639801, 434.330535889, 28.7252674103),
	Vec3(270.0, 0.0, 0.0
	)],
	'8': [Point3(-6.85039520264, 434.566162109, 43.7142791748),
	Vec3(180.0, 0.0, 0.0
	)],
	'9': [Point3(1.79736101627, 434.566162109, 43.7142791748),
	Vec3(180.0, 0.0, 0.0
	)],
	'10': [Point3(10.3381643295, 434.566162109, 43.7142791748),
	Vec3(180.0, 0.0, 0.0
	)],
	'11': [Point3(19.1219005585, 434.566162109, 43.7154998779),
	Vec3(180.0, 0.0, 0.0
	)],
	'12': [Point3(43.9076843262, 449.104980469, 28.724779129),
	Vec3(270.0, 0.0, 0.0
	)],
	'13': [Point3(31.5120067596, 445.849884033, 28.724779129),
	Vec3(90.0, 0.0, 0.0
	)],
	'14': [Point3(76.6376647949, 539.907409668, 43.7259979248),
	Vec3(270.0, 0.0, 0.0
	)],
	'15': [Point3(-64.5058364868, 539.907409668, 43.7259979248),
	Vec3(90.0, 0.0, 0.0
	)],
	'16': [Point3(-19.6063995361, 131.088729858, 3.7260093689),
	Vec3(90.0, 0.0, 0.0
	)],
	'17': [Point3(63.3582801819, 131.088729858, 3.7260093689),
	Vec3(270.0, 0.0, 0.0
	)],
	'18': [Point3(127.58114624, 268.98614502, 8.68414115906),
	Vec3(308.659820557, 0.0, 0.0
	)],
	'19': [Point3(92.5095977783, 232.670257568, 8.68414115906),
	Vec3(152.916442871, 0.0, 0.0
	)],
	'20': [Point3(189.383132935, 233.027069092, 8.68487358093),
	Vec3(180.0, 0.0, 0.0
	)],
	'21': [Point3(205.738693237, 340.856567383, 18.7260017395),
	Vec3(270.0, 0.0, 0.0
	)],
	'22': [Point3(144.820892334, 465.931915283, 23.7259998322),
	Vec3(138.037338257, 0.0, 0.0
	)],
	'23': [Point3(-65.8107452393, 480.288360596, 23.7259998322),
	Vec3(270.0, 0.0, 0.0
	)],
	'24': [Point3(-313.754058838, 528.80090332, 23.7295665741),
	Vec3(0.0, 0.0, 0.0
	)],
	'25': [Point3(-343.322021484, 596.249816895, 23.7386016846),
	Vec3(90.0, 0.0, 0.0
	)],
	'26': [Point3(-404.657501221, 552.570800781, 23.7461681366),
	Vec3(180.0, 0.0, 0.0
	)],
	'27': [Point3(-538.390075684, 595.941772461, 8.72601032257),
	Vec3(90.0, 0.0, 0.0
	)],
	'28': [Point3(-515.727783203, 370.884094238, 8.72601032257),
	Vec3(90.0, 0.0, 0.0
	)],
	'29': [Point3(-184.767532349, 370.884094238, 18.7259998322),
	Vec3(90.0, 0.0, 0.0
	)],
	'30': [Point3(-99.2514801025, 341.364715576, 18.7259998322),
	Vec3(270.0, 0.0, 0.0
	)],
	'31': [Point3(-158.564758301, 295.215332031, 18.7259998322),
	Vec3(270.0, 0.0, 0.0)]
}

FactoryWayPointData = {'24': ['25', '26', '21', '23'], '25': ['24', '26', '23'], '26': ['25', '23'], '27': ['21', '28', '93', '95', '94', '97', '96', '31', '30'], '20': ['21', '22', '11', '12', '17', '16', '18', '9'], '21': ['24', '27', '20', '22', '28', '93', '95', '94', '97', '96', '11', '12', '17', '16', '31', '30'], '22': ['20', '21', '23', '11', '17', '16'], '23': ['24', '25', '26', '22', '98', '48'], '28': ['27', '21', '93', '96', '31', '30'], '29': ['30'], '4': ['6', '5', '3'], '8': ['2', '11', '10', '7', '9', '14'], '59': ['60', '57'], '58': ['57', '51', '50', '48', '49', '47'], '55': ['54', '56'], '54': ['55', '51', '50', '53'], '57': ['59', '58', '50', '48', '49', '47'], '56': ['55'], '51': ['98', '58', '54', '57', '50', '52', '48', '49', '47'], '50': ['58', '54', '57', '51', '52', '48', '49', '47'], '53': ['54', '52'], '52': ['98', '51', '50', '53', '48', '49'], '88': ['90', '89', '86', '87'], '89': ['90', '88'], '82': ['83', '80', '81', '79', '78'], '83': ['82', '84', '85'], '80': ['82', '79'], '81': ['82', '78'], '86': ['88', '87', '85'], '87': ['88', '86'], '84': ['83', '85'], '85': ['83', '86', '84'], '3': ['2', '4', '1'], '7': ['2', '8', '10', '13', '17', '16', '1', '3', '9'], '100': ['99'], '39': ['42', '40', '41', '38'], '38': ['40', '41', '39', '37', '35', '34'], '33': ['32', '34'], '32': ['33', '31'], '31': ['27', '21', '28', '93', '97', '96', '32', '30'], '30': ['27', '21', '28', '29', '93', '95', '94', '97', '96', '31'], '37': ['38', '35', '34'], '36': ['35'], '35': ['38', '37', '36', '34'], '34': ['38', '33', '37', '35'], '60': ['61', '59'], '61': ['60', '62', '63', '64'], '62': ['61', '63', '64'], '63': ['61', '62'], '64': ['61', '62', '65'], '65': ['64', '66', '67'], '66': ['67'], '67': ['66', '68'], '68': ['67', '69', '71', '70'], '69': ['68', '76', '75', '74', '73', '72', '71', '70'], '2': ['8', '10', '13', '1', '3', '7', '9'], '6': ['4', '5', '3'], '99': ['100'], '98': ['23', '51', '52', '48'], '91': ['90', '92', '97'], '90': ['91', '92', '88', '89'], '93': ['27', '21', '28', '92', '95', '94', '97', '96', '31', '30'], '92': ['91', '90', '93'], '95': ['27', '21', '28', '93', '94', '97', '96'], '94': ['27', '21', '93', '95', '97', '96'], '97': ['27', '21', '28', '91', '93', '95', '94', '96', '31', '30'], '96': ['27', '21', '28', '93', '95', '94', '97', '31', '30'], '11': ['20', '21', '22', '8', '10', '12', '17', '16', '18', '14'], '10': ['2', '8', '11', '7', '9', '14'], '13': ['2', '16', '19', '18', '15', '1', '7'], '12': ['20', '21', '22', '11', '16', '18'], '15': ['13', '16', '19', '1', '14'], '14': ['8', '11', '10', '13', '19', '15', '1'], '17': ['20', '21', '22', '11', '16', '18', '7'], '16': ['20', '21', '22', '11', '13', '12', '17', '19', '18', '15', '7'], '19': ['13', '16', '15', '1', '14'], '18': ['13', '12', '16', '20'], '48': ['23', '98', '58', '57', '51', '50', '52', '49', '47'], '49': ['58', '57', '51', '50', '52', '48', '46', '47'], '46': ['23', '49', '47', '44', '45'], '47': ['58', '57', '51', '50', '48', '49', '46'], '44': ['46', '45', '42', '43'], '45': ['46', '44'], '42': ['44', '43', '40', '41', '39'], '43': ['44'], '40': ['42', '41', '39', '38'], '41': ['42', '40', '39', '38'], '1': ['2', '13', '19', '15', '3', '7', '14'], '5': ['4', '6', '3'], '9': ['20', '2', '8', '10', '7'], '77': ['76', '75', '74', '71', '70', '78'], '76': ['69', '77', '75', '74', '70', '79', '78'], '75': ['69', '77', '76', '74', '71', '70', '79'], '74': ['69', '77', '76', '75', '73', '72', '71', '70'], '73': ['69', '74', '72', '71', '70'], '72': ['69', '74', '73', '71', '70'], '71': ['68', '69', '77', '75', '74', '73', '72', '70'], '70': ['68', '69', '77', '76', '75', '74', '73', '72', '71'], '79': ['82', '80', '76', '75'], '78': ['82', '81', '77', '76']}
GuardPointData = {'1': '49', '2': '49', '3': '50', '4': '57', '5': '57', '6': '52',
                  '7': '52', '8': '56', '9': '56', '10': '56', '11': '56', '12': '47',
                  '13': '47', '14': '100', '15': '99', '16': '15', '17': '9', '18': '30',
                  '19': '30', '20': '31', '21': '36', '22': '39', '23': '62', '24': '64',
                  '25': '65', '26': '66', '27': '67', '28': '70', '29': '82', '30': '85',
                  '31': '88'}
JellybeanBarrelPoints = [
    [Point3(-39.7513237, 492.480865479, 28.7250213623), Vec3(45.0, 0.0, 0.0)],
    [Point3(33.1251411438, 499.403594971, 28.7250213623), Vec3(0.0, 0.0, 0.0)],
    [Point3(20.7891941071, 451.0, 28.7250213623), Vec3(0.0, 0.0, 0.0)],
    [Point3(-22.3909473419, 416.06060791, 28.7184333801), Vec3(270.0, 0.0, 0.0)],
    [Point3(-10.0228147507, 451.252868652, 28.7252674103), Vec3(180.0, 0.0, 0.0)],
    [Point3(5.74519491196, 416.444671631, 28.7176990509), Vec3(180.0, 0.0, 0.0)],
    [Point3(19.3000221252, 416.705780029, 43.7093963623), Vec3(180.0, 0.0, 0.0)],
    [Point3(10.1045351028, 416.705780029, 43.7093963623), Vec3(180.0, 0.0, 0.0)],
    [Point3(1.59424114227, 416.705780029, 43.7093963623), Vec3(180.0, 0.0, 0.0)],
    [Point3(158.375442505, 498.157196045, 23.7259998322), Vec3(315.0, 0.0, 0.0)],
    [Point3(212.277908325, 341.0, 18.7259998322), Vec3(270.0, 0.0, 0.0)],
    [Point3(152.493438721, 280.12286377, 18.7259998322), Vec3(180.0, 0.0, 0.0)],
    [Point3(213.100830078, 268.131378174, 8.68511772156), Vec3(0.0, 0.0, 0.0)],
    [Point3(22.4859085083, 339.311187744, 58.6203575134), Vec3(180.0, 0.0, 0.0)],
    [Point3(22.4859085083, 348.359558105, 58.6203575134), Vec3(270.0, 0.0, 0.0)],
    [Point3(22.4859085083, 360.231384277, 58.6215820312), Vec3(270.0, 0.0, 0.0)],
    [Point3(-128.960494995, 328.47164917, 18.7260093689), Vec3(0.0, 0.0, 0.0)],
    [Point3(-263.571563721, 374.413665771, 18.7260093689), Vec3(90.0, 0.0, 0.0)],
    [Point3(-372.620025635, 367.780334473, 18.7260093689), Vec3(270.0, 0.0, 0.0)],
    [Point3(-528.821838379, 370.591156006, 8.72601032257), Vec3(90.0, 0.0, 0.0)],
    [Point3(-477.526855469, 577.470153809, 8.72601032257), Vec3(225.0, 0.0, 0.0)],
    [Point3(-403.55960083, 533.912475586, 23.7383556366), Vec3(180.0, 0.0, 0.0)],
    [Point3(-299.539581299, 490.111419678, 23.7259044647), Vec3(180.0, 0.0, 0.0)],
]

GuardBitmask = BitMask32.bit(6)
