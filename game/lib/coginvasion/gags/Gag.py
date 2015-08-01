"""

  Filename: Gag.py
  Created by: DecodedLogic (07Jul15)

"""


from direct.task.Task import Task
from direct.actor.Actor import Actor
from direct.showbase import Audio3DManager
from lib.coginvasion.gags.GagState import GagState
from lib.coginvasion.gags.GagType import GagType
from lib.coginvasion.gags import GagGlobals
from panda3d.core import Point3
from abc import ABCMeta
import abc

if game.process == 'client':
    audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)
    audio3d.setDistanceFactor(25)
    audio3d.setDropOffFactor(0.025)
else:
    audio3d = None

class Gag(object):

    def __init__(self, name, model, damage, gagType, hitSfx, playRate = 1.0, anim = None, scale = 1, autoRelease = False):
        __metaclass__ = ABCMeta
        self.name = name
        self.model = model
        self.anim = anim
        self.scale = scale
        self.damage = damage
        self.gagType = gagType
        self.playRate = playRate
        self.avatar = None
        self.gag = None
        self.splat = None
        self.splatPos = None
        self.state = GagState.LOADED
        self.woosh = None
        self.handJoint = None
        self.equipped = False
        self.autoRelease = autoRelease
        self.index = None
        self.health = 0
        self.id = GagGlobals.getIDByName(name)
        self.image = None
        self.audio3d = audio3d

        if game.process == 'client':
            if gagType == GagType.THROW:
                self.woosh = self.audio3d.loadSfx(GagGlobals.PIE_WOOSH_SFX)
            self.hitSfx = self.audio3d.loadSfx(hitSfx)

    @abc.abstractmethod
    def start(self):
        if not self.avatar:
            return
        backpack = self.avatar.getBackpack()
        if not backpack:
            return
        elif not self in backpack.getGags():
            return
        elif backpack.getSupply(self.getName()) == 0:
            return
        try:
            self.audio3d.detachSound(self.woosh)
            self.track.pause()
            self.cleanupGag()
        except: pass
        self.state = GagState.START
        self.avatar.getBackpack().setActiveGag(self.getName())

    @abc.abstractmethod
    def reset(self):
        self.state = GagState.LOADED
        if self.avatar:
            backpack = self.avatar.getBackpack()
            if backpack.getActiveGag():
                if backpack.getActiveGag() == self:
                    backpack.setActiveGag(None)

    @abc.abstractmethod
    def throw(self):
        return

    @abc.abstractmethod
    def release(self):
        self.state = GagState.RELEASED
        return

    @abc.abstractmethod
    def buildCollisions(self):
        return

    @abc.abstractmethod
    def onCollision(self):
        pass

    def setAvatar(self, avatar):
        self.avatar = avatar

    def getAvatar(self):
        return self.avatar

    def setState(self, paramState):
        self.state = paramState

    def getState(self):
        return self.state

    def getType(self):
        return self.gagType

    def build(self):
        if self.anim:
            self.gag = Actor(self.model, {'chan' : self.anim})
        else:
            self.gag = loader.loadModel(self.model)
        self.gag.setScale(self.scale)
        self.gag.setName(self.getName())

    def setHandJoint(self):
        self.handJoint = self.avatar.find('**/def_joint_right_hold')

    def equip(self):
        if not self.avatar or not self.avatar.getBackpack() or self.avatar.getBackpack() and self.avatar.getBackpack().getSupply(self.getName()) == 0:
            return
        self.setHandJoint()
        if not self.gag:
            self.build()
        self.gag.reparentTo(self.handJoint)
        self.equipped = True

    @abc.abstractmethod
    def unEquip(self):
        if game.process != 'client':
            return
        if self.equipped and self.handJoint:
            inHand = self.handJoint.getChildren()
            for item in inHand:
                if(item.getName() == self.getName()):
                    item.removeNode()
            self.equipped = False
            self.reset()
            base.localAvatar.enablePieKeys()

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def getDamage(self):
        return self.damage

    def getName(self):
        return self.name

    def delete(self):
        self.unEquip()
        self.handJoint = None
        self.avatar = None
        self.state = None
        self.cleanupGag()
        self.cleanupSplat()
        if self.woosh:
            self.woosh.stop()
            self.woosh = None
        if self.hitSfx:
            self.hitSfx.stop()
            self.hitSfx = None

    def cleanupGag(self):
        try:
            self.track.pause()
        except: pass
        if self.gag and self.state == GagState.LOADED:
            if self.anim:
                self.gag.cleanup()
            self.gag.removeNode()
            self.gag = None

    def getGag(self):
        return self.gag

    def buildSplat(self, scale, color):
        self.cleanupSplat()
        self.splat = Actor(GagGlobals.SPLAT_MDL, {'chan' : GagGlobals.SPLAT_CHAN})
        self.splat.setScale(scale)
        self.splat.setColor(color)
        self.splat.setBillboardPointEye()
        self.splat.play('chan')
        return self.splat

    def setSplatPos(self, x, y, z):
        self.cleanupGag()
        self.splatPos = Point3(x, y, z)
        self.handleSplat()

    def cleanupSplat(self):
        if self.splat:
            self.splat.cleanup()
            self.splat

    def setEndPos(self, x, y, z):
        pass

    def handleSplat(self):
        pass

    def delSplat(self, task):
        self.cleanupSplat()
        return Task.done

    def getAudio3D(self):
        return audio3d

    def doesAutoRelease(self):
        return self.autoRelease

    def isLocal(self):
        return self.avatar.doId == base.localAvatar.doId

    def getID(self):
        return self.id