"""

  Filename: RemoteToonBattleAvatar.py
  Created by: blach (20Jan15)

"""

from panda3d.core import VBase4, TextNode
from lib.coginvasion.globals import CIGlobals
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.interval.IntervalGlobal import *
from direct.fsm.ClassicFSM import ClassicFSM
from direct.fsm.State import State
from Bullet import Bullet
from RemoteAvatar import RemoteAvatar
import GunGameGlobals as GGG

class RemoteToonBattleAvatar(RemoteAvatar):
    notify = directNotify.newCategory("RemoteToonBattleAvatar")

    def __init__(self, mg, cr, avId, gunName = "pistol"):
        RemoteAvatar.__init__(self, mg, cr, avId)
        self.track = None
        self.gunName = gunName
        self.team = None
        self.teamText = None
        self.fsm = ClassicFSM(
            'RemoteToonBattleAvatar',
            [
                State(
                    'off',
                    self.enterOff,
                    self.exitOff
                ),
                State(
                    'shoot',
                    self.enterShoot,
                    self.exitShoot
                ),
                State(
                    'die',
                    self.enterDie,
                    self.exitDie
                ),
                State(
                    'dead',
                    self.enterDead,
                    self.exitDead
                )
            ],
            'off',
            'off'
        )
        self.fsm.enterInitialState()
        self.soundGrunt = None
        self.retrieveAvatar()

    def setTeam(self, team):
        self.team = team
        if self.teamText:
            self.teamText.removeNode()
            self.teamText = None
        textNode = TextNode('teamText')
        textNode.setText(GGG.TeamNameById[team][0])
        textNode.setTextColor(GGG.TeamColorById[team])
        textNode.setAlign(TextNode.ACenter)
        textNode.setFont(CIGlobals.getMickeyFont())
        self.teamText = self.avatar.attachNewNode(textNode)
        self.teamText.setBillboardAxis()
        self.teamText.setZ(self.avatar.getNameTag().getZ() + 1.0)
        self.teamText.setScale(5.0)

    def getTeam(self):
        return self.team

    def setGunName(self, gunName):
        self.gunName = gunName
        self.avatar.attachGun(gunName)
        if self.gunName == 'shotgun':
            color = GGG.TeamColorById[self.team]
            self.avatar.gun.setColorScale(color)

    def getGunName(self):
        return self.gunName

    def retrieveAvatar(self):
        RemoteAvatar.retrieveAvatar(self)
        if self.avatar:
            self.soundGrunt = base.loadSfx('phase_4/audio/sfx/target_impact_grunt1.mp3')

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def grunt(self):
        base.playSfx(self.soundGrunt, node = self.avatar)

    def enterDead(self):
        if self.avatar:
            self.avatar.stash()

    def exitDead(self):
        if self.avatar:
            self.avatar.unstash()
            self.avatar.clearColorScale()
            self.avatar.getGeomNode().clearColorScale()
            self.avatar.clearTransparency()
            self.avatar.getGeomNode().clearTransparency()
            self.avatar.getNameTag().clearColorScale()

    def enterDie(self, ts):
        if self.avatar:
            dieSound = base.audio3d.loadSfx(self.avatar.getToonAnimalNoise('exclaim'))
            base.audio3d.attachSoundToObject(dieSound, self.avatar)
            self.avatar.setTransparency(1)
            self.avatar.getGeomNode().setTransparency(1)
            self.track = Sequence(
                Func(dieSound.play),
                Parallel(
                    LerpColorScaleInterval(
                        self.avatar.getGeomNode(),
                        colorScale = VBase4(1, 1, 1, 0),
                        startColorScale = VBase4(1, 1, 1, 1),
                        duration = 0.5
                    ),
                    LerpColorScaleInterval(
                        self.avatar.getNameTag(),
                        colorScale = VBase4(1, 1, 1, 0),
                        startColorScale = VBase4(1, 1, 1, 1),
                        duration = 0.5
                    ),
                    ActorInterval(
                        self.avatar,
                        'fallb'
                    )
                ),
                Func(self.fsm.request, 'dead')
            )
            self.track.start()
            del dieSound

    def exitDie(self):
        self.resetTrack()

    def resetTrack(self):
        if self.track:
            self.track.pause()
            self.track = None
        #self.avatar.stop()

    def run(self):
        if self.avatar:
            if self.track and self.track.isPlaying():
                self.avatar.loop('run', partName = 'legs')
            else:
                self.avatar.loop('run')

    def stand(self):
        if self.avatar:
            if self.track and self.track.isPlaying():
                self.avatar.loop('neutral', partName = 'legs')
            else:
                self.avatar.loop('neutral')

    def jump(self):
        if self.avatar:
            if self.track and self.track.isPlaying():
                self.avatar.loop('jump', partName = 'legs')
            else:
                self.avatar.loop('jump')

    def enterShoot(self, ts):
        if self.avatar:

            def createBullet():
                if not self.avatar or not self.avatar.gun:
                    return
                if self.gunName == "pistol":
                    Bullet(self.mg, self.avatar.gun.find('**/joint_nozzle'), 0, self.gunName)
                elif self.gunName == "shotgun":
                    b1 = Bullet(self.mg, self.avatar.gun.find('**/joint_nozzle'), 0, self.gunName)
                    b2 = Bullet(self.mg, self.avatar.gun.find('**/joint_nozzle'), 0, self.gunName)

            def changeToLegAnim():
                if not self.avatar:
                    return
                self.avatar.loop(self.avatar.getCurrentAnim(partName = 'legs'))

            if self.gunName == "pistol":
                gunSound = base.audio3d.loadSfx("phase_4/audio/sfx/pistol_shoot.wav")
            elif self.gunName == "shotgun":
                gunSound = base.audio3d.loadSfx("phase_4/audio/sfx/shotgun_shoot.wav")
            base.audio3d.attachSoundToObject(gunSound, self.avatar)
            self.track = Sequence(
                Func(createBullet),
                Func(gunSound.play),
                ActorInterval(
                    self.avatar,
                    "squirt",
                    partName = 'torso',
                    startFrame = 48,
                    endFrame = 58
                ),
                ActorInterval(
                    self.avatar,
                    "squirt",
                    partName = 'torso',
                    startFrame = 107,
                    endFrame = 126,
                    playRate = 3
                ),
                Func(changeToLegAnim)
            )
            self.track.start()
            del gunSound

            self.mg.makeSmokeEffect(self.avatar.gun.find('**/joint_nozzle').getPos(render))

    def exitShoot(self):
        self.resetTrack()

    def cleanup(self):
        if self.teamText:
            self.teamText.removeNode()
            self.teamText = None
        if self.avatar:
            self.avatar.detachGun()
        self.soundGrunt = None
        if self.track:
            self.track.pause()
        del self.track
        RemoteAvatar.cleanup(self)
