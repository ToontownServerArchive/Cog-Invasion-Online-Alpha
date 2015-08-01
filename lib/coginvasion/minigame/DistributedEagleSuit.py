# Filename: DistributedEagleSuit.py
# Created by:  blach (08Jul15)

from panda3d.core import CollisionSphere, CollisionNode
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from direct.actor.Actor import Actor
from direct.fsm.State import State
from direct.interval.IntervalGlobal import LerpPosInterval

from FlightProjectileInterval import FlightProjectileInterval
from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.suit.DistributedSuit import DistributedSuit
from lib.coginvasion.npc.NPCWalker import NPCWalkInterval
from DistributedEagleGame import DistributedEagleGame
import EagleGameGlobals as EGG

import random

class DistributedEagleSuit(DistributedSuit):
    notify = directNotify.newCategory("DistributedEagleSuit")

    def __init__(self, cr):
        DistributedSuit.__init__(self, cr)
        self.suitFSM.addState(State('eagleFly', self.enterEagleFly, self.exitEagleFly))
        self.suitFSM.addState(State('eagleFall', self.enterEagleFall, self.exitEagleFall))
        self.makeStateDict()
        self.eagleCry = self.audio3d.loadSfx('phase_5/audio/sfx/tt_s_ara_cfg_eagleCry.mp3')
        self.audio3d.attachSoundToObject(self.eagleCry, self)
        self.fallWhistle = self.audio3d.loadSfx('phase_5/audio/sfx/incoming_whistleALT.mp3')
        self.audio3d.attachSoundToObject(self.fallWhistle, self)
        self.explode = self.audio3d.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.mp3')
        self.audio3d.attachSoundToObject(self.explode, self)
        self.eventSphereNodePath = None
        self.fallingPropeller = None
        self.fallingPropProjectile = None
        self.mg = None
        self.flySpeed = 0.0

    def setFlySpeed(self, value):
        self.flySpeed = value

    def getFlySpeed(self):
        return self.flySpeed

    def enterEagleFly(self, startIndex, endIndex, ts = 0.0):
        durationFactor = self.getFlySpeed()
        if startIndex > -1:
            startPos = EGG.EAGLE_FLY_POINTS[startIndex]
        else:
            startPos = self.getPos(render)
        endPos = EGG.EAGLE_FLY_POINTS[endIndex]

        if self.moveIval:
            self.moveIval.pause()
            self.moveIval = None

        self.moveIval = NPCWalkInterval(self, endPos,
            durationFactor = durationFactor, startPos = startPos, fluid = 1)
        self.moveIval.start(ts)

    def exitEagleFly(self):
        if self.moveIval:
            self.moveIval.pause()
            self.moveIval = None

    def enterEagleFall(self, startIndex, endIndex, ts = 0.0):
        self.moveIval = LerpPosInterval(
            self,
            duration = 4.0,
            pos = self.getPos(render) - (0, 0, 75),
            startPos = self.getPos(render),
            blendType = 'easeIn'
        )
        self.moveIval.start(ts)

    def exitEagleFall(self):
        if self.moveIval:
            self.moveIval.finish()
            self.moveIval = None

    def fallAndExplode(self):
        self.fallingPropeller = Actor("phase_4/models/props/propeller-mod.bam",
                        {"chan": "phase_4/models/props/propeller-chan.bam"})
        self.fallingPropeller.reparentTo(render)
        self.fallingPropeller.loop('chan', fromFrame = 0, toFrame = 3)

        parentNode = self.attachNewNode('fallingPropParentNode')
        h = random.randint(0, 359)
        parentNode.setH(h)

        dummyNode = parentNode.attachNewNode('dummyNode')
        dummyNode.setPos(0, 10, -50)

        self.fallingPropProjectile = FlightProjectileInterval(
            self.fallingPropeller,
            startPos = self.find('**/joint_head').getPos(render),
            endPos = dummyNode.getPos(render),
            duration = 5.0,
            gravityMult = .25
        )
        self.fallingPropProjectile.start()

        dummyNode.removeNode()
        del dummyNode
        parentNode.removeNode()
        del parentNode

        self.updateHealthBar(0)
        self.ignoreHit()
        self.fallWhistle.play()
        taskMgr.doMethodLater(4.0, self.doExplodeSound, self.uniqueName("DEagleSuit-doExplodeSound"))

    def doExplodeSound(self, task):
        self.explode.play()
        return Task.done

    def __initializeEventSphere(self):
        sphere = CollisionSphere(0, 0, 0, 2)
        sphere.setTangible(0)
        node = CollisionNode(self.uniqueName("DEagleSuit-eventSphere"))
        node.addSolid(sphere)
        node.setCollideMask(CIGlobals.WallBitmask)
        np = self.attachNewNode(node)
        np.setSz(2.5)
        np.setZ(5.5)
        #np.show()
        self.eventSphereNodePath = np

    def removeEventSphere(self):
        if self.eventSphereNodePath:
            self.eventSphereNodePath.removeNode()
            self.eventSphereNodePath = None

    def acceptHit(self):
        self.acceptOnce('enter' + self.eventSphereNodePath.node().getName(), self.__handleHit)

    def ignoreHit(self):
        self.ignore('enter' + self.eventSphereNodePath.node().getName())

    def __handleHit(self, entry):
        messenger.send(EGG.EAGLE_HIT_EVENT, [self.doId])

    def setSuit(self, suitType, head, team, skeleton):
        DistributedSuit.setSuit(self, suitType, head, team, skeleton)
        self.deleteShadow()
        self.disableBodyCollisions()
        self.disableRay()
        self.__initializeEventSphere()

    def __doEagleCry(self, task):
        self.eagleCry.play()
        task.delayTime = random.uniform(3, 30)
        return Task.again

    def announceGenerate(self):
        DistributedSuit.announceGenerate(self)
        taskMgr.doMethodLater(random.uniform(0, 20), self.__doEagleCry, self.uniqueName("DEagleSuit-doEagleCry"))
        self.acceptHit()

    def disable(self):
        self.ignoreHit()
        self.removeEventSphere()
        taskMgr.remove(self.uniqueName("DEagleSuit-doExplodeSound"))
        taskMgr.remove(self.uniqueName("DEagleSuit-doEagleCry"))
        if self.fallingPropProjectile:
            self.fallingPropProjectile.finish()
            self.fallingPropProjectile = None
        if self.fallingPropeller:
            self.fallingPropeller.cleanup()
            self.fallingPropeller = None
        self.audio3d.detachSound(self.fallWhistle)
        del self.fallWhistle
        self.audio3d.detachSound(self.explode)
        del self.explode
        self.audio3d.detachSound(self.eagleCry)
        del self.eagleCry
        self.mg = None
        DistributedSuit.disable(self)
