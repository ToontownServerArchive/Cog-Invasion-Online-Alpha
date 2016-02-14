# Filename: DistributedCogOfficeSuit.py
# Created by:  blach (17Dec15)

from panda3d.core import Point3

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.ClockDelta import globalClockDelta
from direct.fsm import ClassicFSM, State

from lib.coginvasion.npc.NPCWalker import NPCWalkInterval
from lib.coginvasion.cog.DistributedSuit import DistributedSuit
from CogOfficeConstants import *

class DistributedCogOfficeSuit(DistributedSuit):
    notify = directNotify.newCategory('DistributedCogOfficeSuit')
    
    def __init__(self, cr):
        DistributedSuit.__init__(self, cr)
        self.fsm = ClassicFSM.ClassicFSM('DistributedCogOfficeSuitAI', [State.State('off', self.enterOff, self.exitOff),
         State.State('guard', self.enterGuard, self.exitGuard, ['think']),
         State.State('think', self.enterThink, self.exitThink, ['off']),
         State.State('chair', self.enterChair, self.exitChair, ['chair2battle']),
         State.State('chair2battle', self.enterChair2Battle, self.exitChair2Battle, ['think'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.battleDoId = None
        self.battle = None
        
    def setBattleDoId(self, doId):
        self.battleDoId = doId
        
    def getBattle(self):
        self.battle = self.cr.doId2do.get(self.battleDoId)
        
    def announceGenerate(self):
        self.getBattle()
        DistributedSuit.announceGenerate(self)
        
    def disable(self):
        self.fsm.requestFinalState()
        del self.fsm
        DistributedSuit.disable(self)
        
    def enterWalking(self, startIndex, endIndex, ts = 0.0):
        durationFactor = 0.1
        if startIndex > -1:
            data = self.getPoints('battle')[startIndex]
            startPos = Point3(data[0], data[1], data[2])
        else:
            startPos = self.getPos(render)
        data = self.getPoints('battle')[endIndex]
        endPos = Point3(data[0], data[1], data[2])

        self.stopMoving()

        self.moveIval = NPCWalkInterval(self, endPos, durationFactor, startPos, fluid = 1)
        self.moveIval.start(ts)
        self.animFSM.request('walk')
        
    def getPoints(self, name):
        if self.battle.currentFloor in self.battle.UNIQUE_FLOORS:
            points = POINTS[self.battle.deptClass][self.battle.currentFloor][name]
        else:
            points = POINTS[self.battle.currentFloor][name]
        return points
        
    def enterOff(self, extraArgs = [], ts = 0):
        pass
        
    def exitOff(self):
        pass
        
    def enterGuard(self, extraArgs, ts):
        self.show()
        self.cleanupPropeller()
        points = self.getPoints('guard')
        self.setPosHpr(*points[extraArgs[0]])
        self.setAnimState('neutral')
        
    def exitGuard(self):
        pass
        
    def enterThink(self, extraArgs, ts):
        pass
        
    def exitThink(self):
        pass
        
    def enterChair(self, extraArgs, ts):
        self.show()
        self.cleanupPropeller()
        points = self.getPoints('chairs')
        self.setPosHpr(*points[extraArgs[0]])
        self.setAnimState('sit')
        
    def exitChair(self):
        pass
        
    def enterChair2Battle(self, extraArgs, ts):
        points = self.getPoints('battle')
        pointIndex = extraArgs[0]
        point = points[pointIndex]
        self.startProjInterval(self.getX(), self.getY(), self.getZ(), point[0], point[1], point[2], 5.0, 0.05, ts)
        
    def exitChair2Battle(self):
        if self.moveIval:
            self.ignore(self.moveIval.getDoneEvent())
            self.moveIval.finish()
            self.moveIval = None
        
    def setState(self, state, extraArgs, timestamp):
        self.fsm.request(state, [extraArgs, globalClockDelta.localElapsedTime(timestamp)])