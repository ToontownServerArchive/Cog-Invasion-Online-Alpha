# Filename: DistributedDodgeballGame.py
# Created by:  blach (18Apr16)
#
# OMG FINALLY THE DODGEBALL GAME!!

from panda3d.core import Fog, Point3, Vec3

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.fsm.State import State
from direct.interval.IntervalGlobal import Sequence, Wait, Func, LerpPosInterval

from lib.coginvasion.globals import CIGlobals
from lib.coginvasion.toon import ParticleLoader

from DistributedToonFPSGame import DistributedToonFPSGame
from DodgeballFirstPerson import DodgeballFirstPerson
from TeamMinigame import TeamMinigame, TEAM1, TEAM2

BLUE = TEAM1
RED = TEAM2

TEAM_COLOR_BY_ID = {RED: (1, 0, 0, 1), BLUE: (0.2, 0.2, 1, 1)}

from RemoteDodgeballAvatar import RemoteDodgeballAvatar

class DistributedDodgeballGame(DistributedToonFPSGame, TeamMinigame):
    """The winter dodgeball minigame (client side)"""

    notify = directNotify.newCategory("DistributedDodgeballGame")

    TreeData = [['prop_snow_tree_small_ur', Point3(23.23, 66.52, 7.46)],
	            ['prop_snow_tree_small_ul', Point3(-34.03, 88.02, 24.17)],
	            ['prop_snow_tree_small_ur', Point3(-54.80, 0, 4.19)],
	            ['prop_snow_tree_small_ul', Point3(54.80, -5, 4.19)],
	            ['prop_snow_tree_small_ur', Point3(62.71, 62.66, 16.80)],
	            ['prop_snow_tree_small_ul', Point3(-23.23, -66.52, 6)],
	            ['prop_snow_tree_small_ur', Point3(34.03, -88.02, 23)],
	            ['prop_snow_tree_small_ul', Point3(-62.71, -62.66, 16)]]

    GameSong = "phase_4/audio/bgm/MG_Dodgeball.mp3"
    GameDesc = ("Welcome to the north! You have been invited to play dodgeball with the penguins!\n\n"
                "How To Play\nWASD to Move and use the mouse to aim.\nLeft click to Throw!\nRight click"
                " to Catch!\n\nObjective\nThe first team to get everyone out wins!")

    InitCamTrans = [Point3(25, 45, 19.5317), Vec3(154.001, -15, 0)]

    def __init__(self, cr):
        try:
            self.DistributedDodgeballGame_initialized
            return
        except:
            self.DistributedDodgeballGame_initialized = 1

        DistributedToonFPSGame.__init__(self, cr)

        TeamMinigame.__init__(self, "BlueSnow", ('phase_4/maps/db_blue_neutral.png',
                                               'phase_4/maps/db_blue_hover.png',
                                               'phase_4/maps/db_blue_hover.png'),
                                    "RedIce", ('phase_4/maps/db_red_neutral.png',
                                               'phase_4/maps/db_red_hover.png',
                                               'phase_4/maps/db_red_hover.png'))

        self.fsm.addState(State('chooseTeam', self.enterChooseTeam, self.exitChooseTeam, ['waitForOthers']))
        self.fsm.addState(State('scrollBy', self.enterScrollBy, self.exitScrollBy, ['countdown']))
        self.fsm.addState(State('countdown', self.enterCountdown, self.exitCountdown, ['play']))
        self.fsm.getStateNamed('waitForOthers').addTransition('chooseTeam')
        self.fsm.getStateNamed('waitForOthers').addTransition('scrollBy')

        self.firstPerson = DodgeballFirstPerson(self)

        self.scrollBySeq = None

        self.spawnPointsByTeam = {
            BLUE: [
                [Point3(5, 15, 0), Vec3(180, 0, 0)],
                [Point3(15, 15, 0), Vec3(180, 0, 0)],
                [Point3(-5, 15, 0), Vec3(180, 0, 0)],
                [Point3(-15, 15, 0), Vec3(180, 0, 0)]],
            RED: [
                [Point3(5, -15, 0), Vec3(0, 0, 0)],
                [Point3(15, -15, 0), Vec3(0, 0, 0)],
                [Point3(-5, -15, 0), Vec3(0, 0, 0)],
                [Point3(-15, -15, 0), Vec3(0, 0, 0)]]}

        # Environment vars
        self.sky = None
        self.arena = None
        self.fog = None
        self.snow = None
        self.snowRender = None
        self.trees = []

    def setupRemoteAvatar(self, avId):
        av = RemoteDodgeballAvatar(self, self.cr, avId)
        if avId == self.cr.localAvId:
            self.myRemoteAvatar = av
        self.remoteAvatars.append(av)

    def __getSnowTree(self, path):
        trees = loader.loadModel('phase_8/models/props/snow_trees.bam')
        tree = trees.find('**/' + path)
        tree.find('**/*shadow*').removeNode()
        return tree

    def load(self):
        self.setMinigameMusic(DistributedDodgeballGame.GameSong)
        self.setDescription(DistributedDodgeballGame.GameDesc)
        self.createWorld()

        trans = DistributedDodgeballGame.InitCamTrans
        camera.setPos(trans[0])
        camera.setHpr(trans[1])

        DistributedToonFPSGame.load(self)

    def createWorld(self):
        self.deleteWorld()

        self.sky = loader.loadModel("phase_3.5/models/props/BR_sky.bam")
        self.sky.reparentTo(render)
        self.sky.setZ(-40)
        self.sky.setFogOff()

        self.arena = loader.loadModel("phase_4/models/minigames/dodgeball_arena.egg")
        self.arena.reparentTo(render)
        self.arena.setScale(0.5)
        self.arena.find('**/team_divider').setBin('ground', 18)
        self.arena.find('**/floor').setBin('ground', 18)
        self.arena.find('**/team_divider_coll').setCollideMask(CIGlobals.FloorBitmask)

        for data in DistributedDodgeballGame.TreeData:
            code = data[0]
            pos = data[1]
            tree = self.__getSnowTree(code)
            tree.reparentTo(self.arena)
            tree.setPos(pos)
            self.trees.append(tree)

        self.snow = ParticleLoader.loadParticleEffect('phase_8/etc/snowdisk.ptf')
        self.snow.setPos(0, 0, 5)
        self.snowRender = self.arena.attachNewNode('snowRender')
        self.snowRender.setDepthWrite(0)
        self.snowRender.setBin('fixed', 1)
        self.snow.start(camera, self.snowRender)

        self.fog = Fog('snowFog')
        self.fog.setColor(0.486, 0.784, 1)
        self.fog.setExpDensity(0.003)
        render.setFog(self.fog)

    def deleteWorld(self):
        for tree in self.trees:
            tree.removeNode()
        self.trees = []
        if self.snow:
            self.snow.cleanup()
            self.snow = None
        if self.snowRender:
            self.snowRender.removeNode()
            self.snowRender = None
        self.fog = None
        if self.sky:
            self.sky.removeNode()
            self.sky = None
        if self.arena:
            self.arena.removeNode()
            self.arena = None
        render.clearFog()

    def enterCountdown(self):
        pass

    def exitCountdown(self):
        pass

    def enterScrollBy(self):
        BLUE_START_POS = Point3(-20, 0, 4)
        BLUE_END_POS = Point3(20, 0, 4)
        BLUE_HPR = Vec3(0, 0, 0)

        RED_START_POS = Point3(20, 0, 4)
        RED_END_POS = Point3(-20, 0, 4)
        RED_HPR = Vec3(180, 0, 0)

        self.playMinigameMusic()

        self.scrollBySeq = Sequence(
            Func(camera.setHpr, BLUE_HPR),
            LerpPosInterval(
                camera, duration = 5.0, pos = BLUE_END_POS, startPos = BLUE_START_POS, blendType = 'easeOut'),
            Func(base.transitions.fadeOut, 0.4),
            Wait(0.5),
            Func(base.transitions.fadeIn, 0.4),
            Func(camera.setHpr, RED_HPR),
            LerpPosInterval(
                camera, duration = 5.0, pos = RED_END_POS, startPos = RED_START_POS, blendType = 'easeOut'),
            name = "SCROLLBYSEQ")
        self.scrollBySeq.setDoneEvent(self.scrollBySeq.getName())
        self.acceptOnce(self.scrollBySeq.getDoneEvent(), self.__handleScrollByDone)
        self.scrollBySeq.start()

    def __handleScrollByDone(self):
        self.fsm.request('countdown')

    def exitScrollBy(self):
        if self.scrollBySeq:
            self.ignore(self.scrollBySeq.getDoneEvent())
            self.scrollBySeq.finish()
            self.scrollBySeq = None

    def allPlayersReady(self):
        self.fsm.request('scrollBy')

    def chooseUrTeam(self):
        # The AI has told us it's time to choose our team.
        self.fsm.request('chooseTeam')

    def enterChooseTeam(self):
        self.makeSelectionGUI()

    def acceptedIntoTeam(self, spawnPoint):
        TeamMinigame.acceptedIntoTeam(self)

        self.sendUpdate('readyToStart')
        self.fsm.request('waitForOthers')

        pos, hpr = self.spawnPointsByTeam[self.team][spawnPoint]
        base.localAvatar.setPos(pos)
        base.localAvatar.setHpr(hpr)

    def exitChooseTeam(self):
        self.destroySelectionGUI()

    def announceGenerate(self):
        DistributedToonFPSGame.announceGenerate(self)
        self.load()

    def disable(self):
        self.deleteWorld()
        self.trees = None
        self.spawnPointsByTeam = None
        if self.firstPerson:
            self.firstPerson.cleanup()
            self.firstPerson = None
        DistributedToonFPSGame.disable(self)
