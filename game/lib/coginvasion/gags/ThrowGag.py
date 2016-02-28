"""

  Filename: ThrowGag.py
  Created by: DecodedLogic (07Jul15)

"""

from panda3d.core import CollisionSphere, BitMask32, CollisionNode, NodePath, CollisionHandlerEvent
from direct.interval.ProjectileInterval import ProjectileInterval

from lib.coginvasion.gags.Gag import Gag
from lib.coginvasion.gags.GagType import GagType
from lib.coginvasion.globals import CIGlobals
from direct.actor.Actor import Actor
import GagGlobals

class ThrowGag(Gag):

    def __init__(self, name, model, damage, hitSfx, splatColor, anim = None, scale = 1):
        Gag.__init__(self, name, model, damage, GagType.THROW, hitSfx, anim = anim, scale = scale)
        self.splatScale = GagGlobals.splatSizes[self.name]
        self.splatColor = splatColor
        self.entities = []
        self.timeout = 1.0

    def build(self):
        if not self.gag:
            Gag.build(self)
            self.equip()
            if self.anim and self.gag:
                self.gag.loop('chan')
        return self.gag

    def start(self):
        super(ThrowGag, self).start()
        self.build()
        self.avatar.setPlayRate(self.playRate, 'pie')
        self.avatar.play('pie', fromFrame = 0, toFrame = 45)

    def throw(self):
        if self.isLocal():
            self.startTimeout()
        self.avatar.play('pie', fromFrame = 45, toFrame = 90)
        if not self.gag:
            self.build()

    def release(self):
        Gag.release(self)
        base.audio3d.attachSoundToObject(self.woosh, self.gag)
        base.playSfx(self.woosh, node = self.gag)

        throwPath = NodePath('ThrowPath')
        throwPath.reparentTo(self.avatar)
        throwPath.setScale(render, 1)
        throwPath.setPos(0, 160, -90)
        throwPath.setHpr(90, -90, 90)

        entity = self.gag

        if not entity:
            entity = self.build()

        entity.wrtReparentTo(render)
        entity.setHpr(throwPath.getHpr(render))
        self.gag = None

        if not self.handJoint:
            self.handJoint = self.avatar.find('**/joint_Rhold')

        track = ProjectileInterval(entity, startPos = self.handJoint.getPos(render), endPos = throwPath.getPos(render), gravityMult = 0.9, duration = 3)
        event = self.avatar.uniqueName('throwIvalDone') + '-' + str(hash(entity))
        track.setDoneEvent(event)
        base.acceptOnce(event, self.__handlePieIvalDone, [entity])
        track.start()
        self.entities.append([entity, track])
        if self.isLocal():
            self.buildCollisions(entity)
            base.localAvatar.sendUpdate('usedGag', [self.id])
        self.reset()

    def __handlePieIvalDone(self, pie):
        if not pie.isEmpty():
            pie.removeNode()

    def handleSplat(self):
        base.audio3d.detachSound(self.woosh)
        if self.woosh: self.woosh.stop()
        self.buildSplat(self.splatScale, self.splatColor)
        base.audio3d.attachSoundToObject(self.hitSfx, self.splat)
        self.splat.reparentTo(render)
        self.splat.setPos(self.splatPos)
        base.playSfx(self.hitSfx, node = self.splat)
        self.cleanupEntity(self.splatPos)
        self.splatPos = None
        taskMgr.doMethodLater(0.5, self.delSplat, 'Delete Splat')
        return

    def cleanupEntity(self, pos):
        closestPie = None
        trackOfClosestPie = None
        pieHash2range = {}
        for entity, track in self.entities:
            pieHash2range[hash(entity)] = (entity.getPos(render) - pos).length()
        ranges = []
        for distance in pieHash2range.values():
            ranges.append(distance)
        ranges.sort()
        for pieHash in pieHash2range.keys():
            distance = pieHash2range[pieHash]
            if distance == ranges[0]:
                for entity, track in self.entities:
                    if hash(entity) == pieHash:
                        closestPie = entity
                        trackOfClosestPie = track
                        break
            break
        if closestPie != None and trackOfClosestPie != None:
            if [closestPie, trackOfClosestPie] in self.entities:
                self.entities.remove([closestPie, trackOfClosestPie])
            if not closestPie.isEmpty():
                if isinstance(closestPie, Actor):
                    closestPie.cleanup()
                closestPie.removeNode()

    def onCollision(self, entry):
        intoNP = entry.getIntoNodePath()
        avNP = intoNP.getParent()
        fromNP = entry.getFromNodePath().getParent()

        if fromNP.isEmpty():
            return

        for key in base.cr.doId2do.keys():
            obj = base.cr.doId2do[key]
            if obj.__class__.__name__ in CIGlobals.SuitClasses:
                if obj.getKey() == avNP.getKey():
                    obj.sendUpdate('hitByGag', [self.getID()])
            elif obj.__class__.__name__ == "DistributedToon":
                if obj.getKey() == avNP.getKey():
                    if obj.getHealth() < obj.getMaxHealth():
                        if obj != self.avatar:
                            self.avatar.sendUpdate('toonHitByPie', [obj.doId, self.getID()])
                        else:
                            self.avatar.acceptOnce('gagSensor-into', self.onCollision)
                            return
            elif obj.__class__.__name__ == "DistributedPieTurret":
                if obj.getKey() == avNP.getKey():
                    if obj.getHealth() < obj.getMaxHealth():
                        self.avatar.sendUpdate('toonHitByPie', [obj.doId, self.getID()])

        self.splatPos = fromNP.getPos()
        self.avatar.sendUpdate('setSplatPos', [self.getID(), self.splatPos.getX(), self.splatPos.getY(), self.splatPos.getZ()])
        self.handleSplat()

    def buildCollisions(self, entity):
        pieSphere = CollisionSphere(0, 0, 0, 1)
        pieSensor = CollisionNode('gagSensor')
        pieSensor.addSolid(pieSphere)
        pieNP = entity.attachNewNode(pieSensor)
        pieNP.setCollideMask(BitMask32(0))
        pieNP.node().setFromCollideMask(CIGlobals.WallBitmask | CIGlobals.FloorBitmask)

        event = CollisionHandlerEvent()
        event.set_in_pattern("%fn-into")
        event.set_out_pattern("%fn-out")
        base.cTrav.add_collider(pieNP, event)
        self.avatar.acceptOnce('gagSensor-into', self.onCollision)
