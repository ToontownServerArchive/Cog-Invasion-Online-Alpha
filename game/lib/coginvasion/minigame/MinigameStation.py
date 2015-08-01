"""

  Filename: MinigameStation.py
  Created by: blach (04Oct14)
  
"""

from panda3d.core import *
from lib.coginvasion.globals import CIGlobals
from direct.gui.DirectGui import *

from GroupStation import GroupStation

class MinigameStation(GroupStation):
	game2maxPlayers = {CIGlobals.UnoGame: 4,
				CIGlobals.RaceGame: 4,
				CIGlobals.GunGame: 8,
				CIGlobals.FactoryGame: 4,
				CIGlobals.CameraShyGame: 4,
				CIGlobals.EagleGame: 4}
	game2dateCreated = {CIGlobals.UnoGame: "October 15, 2014",
		CIGlobals.RaceGame: "October 7, 2014",
		CIGlobals.GunGame: "January 19, 2015",
		CIGlobals.CameraShyGame: "April 26, 2015",
		CIGlobals.EagleGame: "July 4, 2015"}
	
	def __init__(self):
		try:
			self.MinigameStation_initialized
			return
		except:
			self.MinigameStation_initialized = 1
		GroupStation.__init__(self)
		self.game = ""
		self.locations = {"pos": {0: (-100.0, 8.00, 0.00),
								1: (0.00, 100.00, 0.00),
								2: (100.0, -8.00, 0.00),
                                3: (0.00, -100.00, 0.00),
                                4: (-82.85, -71.97, 0.00)},
						"hpr": {0: (255.00, 0.00, 0.00),
								1: (180.00, 0.00, 0.00),
								2: (-255.00, 0.00, 0.00),
                                3: (0.00, 0.00, 0.00),
                                4: (310.00, 0.00, 0.00)}}
		return
		
	def delete(self):
		try:
			self.MinigameStation_deleted
		except:
			self.MinigameStation_deleted = 1
			self.removeStation()
			self.game = None
			GroupStation.delete(self)
		
	def generateStation(self, game):
		self.game = game
		numSlots = self.game2maxPlayers[game]
		GroupStation.generateStation(self, numSlots)
		title = DirectLabel(text=game + "\n" + self.game2dateCreated[game], relief=None, text_fg=(0.7, 0.3, 0.5, 1.0),
							text_decal=True, text_font=CIGlobals.getMickeyFont(), text_pos = (0, 0.1),
							parent=self.sign.find('**/signText_locator'), text_scale=0.3,
							text_wordwrap=7.0)
		title.setBillboardAxis(2)
		