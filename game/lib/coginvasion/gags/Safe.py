"""

  Filename: Safe.py
  Created by: DecodedLogic (16Jul15)

"""

from lib.coginvasion.gags.DropGag import DropGag
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.globals import CIGlobals
from direct.interval.IntervalGlobal import Sequence, LerpPosInterval, LerpScaleInterval, Func, Wait, Parallel
from direct.showutil import Effects
from panda3d.core import OmniBoundingVolume, Point3

class Safe(DropGag):

    def __init__(self):
        DropGag.__init__(self, CIGlobals.Safe, 'phase_5/models/props/safe-mod.bam', 'phase_5/models/props/safe-chan.bam',
                         60, GagGlobals.SAFE_DROP_SFX, GagGlobals.SAFE_MISS_SFX, 1, 1)
        self.setImage('phase_3.5/maps/safe.png')

    def startDrop(self):
        if self.gag and self.dropLoc:
            endPos = self.dropLoc
            startPos = Point3(endPos.getX(), endPos.getY(), endPos.getZ() + 20)
            self.gag.setPos(startPos.getX(), startPos.getY() + 2, startPos.getZ())
            self.gag.setScale(5 * 0.85)
            #self.gag.setP(90)
            #self.gag.headsUp(self.avatar)
            self.gag.node().setBounds(OmniBoundingVolume())
            self.gag.node().setFinal(1)
            self.buildCollisions()
            objectTrack = Sequence()
            animProp = LerpPosInterval(self.gag, self.fallDuration, endPos, startPos = startPos)
            bounceProp = Effects.createZBounce(self.gag, 2, endPos, 0.5, 1.5)
            objAnimShrink = Sequence(Func(self.gag.setScale, 5), Func(self.gag.setP, 90), Wait(0.5), Func(self.gag.reparentTo, render), animProp, bounceProp)
            objectTrack.append(objAnimShrink)
            dropShadow = loader.loadModel('phase_3/models/props/drop_shadow.bam')
            dropShadow.reparentTo(render)
            dropShadow.setPos(endPos)
            shadowTrack = Sequence(LerpScaleInterval(dropShadow, self.fallDuration + 0.1, dropShadow.getScale()*3,
                                startScale=Point3(0.01, 0.01, 0.01)), Wait(0.3), Func(dropShadow.removeNode))
            Parallel(Sequence(Wait(self.fallDuration), Func(self.completeDrop)), objectTrack, shadowTrack).start()
            self.dropLoc = None