"""

  Filename: ToonUpGag.py
  Created by: DecodedLogic (17Jul15)

"""

from lib.coginvasion.gags.Gag import Gag
from lib.coginvasion.gags.GagType import GagType
from direct.interval.IntervalGlobal import Sequence, SoundInterval, Wait, Parallel, LerpScaleInterval
from panda3d.core import Point3
import random

class ToonUpGag(Gag):

    def __init__(self, name, model, minHeal, maxHeal, efficiency, healSfx, playRate, anim = None):
        Gag.__init__(self, name, model, 0, GagType.TOON_UP, healSfx, anim = anim, playRate = playRate, scale = 1, autoRelease = False)
        self.minHeal = minHeal
        self.maxHeal = maxHeal
        self.efficiency = efficiency
        self.lHandJoint = None
        self.hips = None
        self.PNTNEARZERO = Point3(0.01, 0.01, 0.01)
        self.PNTNORMAL = Point3(1, 1, 1)
        self.healAmount = None

    def equip(self):
        self.setupHandJoints()

    def setupHandJoints(self):
        if not self.handJoint or not self.lHandJoint:
            self.handJoint = self.avatar.find('**/def_joint_right_hold')
            self.lHandJoint = self.avatar.find('**/def_joint_left_hold')

    def setupHips(self):
        if not self.hips:
            self.hips = self.avatar.find('**/joint_hips')

    def placeProp(self, handJoint, prop, pos = None, hpr = None, scale = None):
        prop.reparentTo(handJoint)
        if pos:
            prop.setPos(pos)
        if hpr:
            prop.setHpr(hpr)
        if scale:
            prop.setScale(scale)

    def getScaleTrack(self, props, duration, startScale, endScale):
        track = Parallel()
        for prop in props:
            track.append(LerpScaleInterval(prop, duration, endScale, startScale = startScale))
        return track

    def getSoundTrack(self, delay, node, duration):
        soundTrack = Sequence()
        soundTrack.append(Wait(delay))
        soundTrack.append(SoundInterval(self.hitSfx, duration = duration, node = node))
        return soundTrack

    def setHealAmount(self):
        if random.randint(0, 100) < self.efficiency:
            healAmount = random.randint(self.minHeal, self.maxHeal)
        else:
            healAmount = random.randint(int(self.minHeal * 0.2), int(self.maxHeal * 0.2))
        self.healAmount = healAmount

    def healNearbyAvatars(self, radius):
        for obj in base.cr.doId2do.values():
            if obj.__class__.__name__ == "DistributedToon":
                if self.avatar.getDistance(obj) <= radius:
                    if obj.getHealth() < obj.getMaxHealth() and not obj.isDead():
                        obj.sendUpdate('toonUp', [self.healAmount, 1, 1])
