# Filename: DistributedCogStation.py
# Created by:  blach (11Jun15)

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import Sequence, Wait, Func

from lib.coginvasion.minigame.DistributedGroupStation import DistributedGroupStation
from CogStation import CogStation

class DistributedCogStation(DistributedGroupStation, CogStation):
	notify = directNotify.newCategory("DistributedCogStation")

	def __init__(self, cr):
		try:
			self.DistributedCogStation_initialized
			return
		except:
			self.DistributedCogStation_initialized = 1
		DistributedGroupStation.__init__(self, cr)
		CogStation.__init__(self)

	def headOff(self, zone, hoodIndex):
		self.deleteStationAbortGui()
		requestStatus = {'zoneId': zone,
					'hoodId': self.cr.playGame.hood.hoodId,
					'where': 'playground',
					'avId': base.localAvatar.doId,
					'loader': 'safeZoneLoader',
					'shardId': None,
					'wantLaffMeter': 1,
					'how': 'teleportIn'}
		self.cr.playGame.getPlace().fsm.request('teleportOut', [requestStatus])
		Sequence(Wait(5.0), Func(self.d_leaving)).start()

	def generate(self):
		DistributedGroupStation.generate(self)
		self.generateStation()

	def announceGenerate(self):
		DistributedGroupStation.announceGenerate(self)
		self.reparentTo(render)

	def disable(self):
		self.reparentTo(hidden)
		DistributedGroupStation.disable(self)

	def delete(self):
		CogStation.delete(self)
		DistributedGroupStation.delete(self)