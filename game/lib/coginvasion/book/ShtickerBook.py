"""

  Filename: ShtickerBook.py
  Created by: blach (20June14)

"""

from lib.coginvasion.globals import CIGlobals
from panda3d.core import *
from direct.gui.DirectGui import *
from lib.coginvasion.manager.SettingsManager import SettingsManager
from direct.fsm.StateData import StateData
from direct.fsm.State import State
from direct.fsm.ClassicFSM import ClassicFSM
from lib.coginvasion.hood import ZoneUtil
import types

from OptionPage import OptionPage
from AdminPage import AdminPage

qt_btn = loader.loadModel("phase_3/models/gui/quit_button.bam")

class ShtickerBook(StateData):

    def __init__(self, parentFSM, doneEvent):
        self.parentFSM = parentFSM
        StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM('ShtickerBook', [State('off', self.enterOff, self.exitOff),
                State('optionPage', self.enterOptionPage, self.exitOptionPage, ['districtPage', 'off']),
                State('districtPage', self.enterDistrictPage, self.exitDistrictPage, ['optionPage', 'questPage', 'off']),
                State('questPage', self.enterQuestPage, self.exitQuestPage, ['zonePage', 'districtPage', 'off']),
                State('zonePage', self.enterZonePage, self.exitZonePage, ['releaseNotesPage', 'questPage', 'off']),
                State('releaseNotesPage', self.enterReleaseNotesPage, self.exitReleaseNotesPage, ['zonePage', 'off']),
                State('adminPage', self.enterAdminPage, self.exitAdminPage, ['releaseNotesPage', 'off'])],
                'off', 'off')
        if base.localAvatar.getAdminToken() > -1:
            self.fsm.getStateNamed('releaseNotesPage').addTransition('adminPage')
        self.fsm.enterInitialState()
        self.entered = 0
        self.parentFSM.getStateNamed('shtickerBook').addChild(self.fsm)

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def load(self):
        StateData.load(self)
        self.book_contents = loader.loadModel("phase_3.5/models/gui/stickerbook_gui.bam")
        self.book_texture = self.book_contents.find('**/big_book')
        self.book_open = loader.loadSfx("phase_3.5/audio/sfx/GUI_stickerbook_open.mp3")
        self.book_close = loader.loadSfx("phase_3.5/audio/sfx/GUI_stickerbook_delete.mp3")
        self.book_turn = loader.loadSfx("phase_3.5/audio/sfx/GUI_stickerbook_turn.mp3")

    def unload(self):
        self.book_texture.removeNode()
        del self.book_texture
        self.book_contents.removeNode()
        del self.book_contents
        loader.unloadSfx(self.book_open)
        del self.book_open
        loader.unloadSfx(self.book_close)
        del self.book_close
        loader.unloadSfx(self.book_turn)
        del self.book_turn
        del self.fsm
        del self.parentFSM
        del self.entered
        StateData.unload(self)

    def enter(self):
        if self.entered:
            return
        self.entered = 1
        StateData.enter(self)
        render.hide()
        base.setBackgroundColor(0.05, 0.15, 0.4)
        self.book_img = OnscreenImage(image=self.book_texture, scale=(2, 1, 1.5))
        self.book_open.play()
        if base.localAvatar.getAdminToken() > -1:
            self.fsm.request('adminPage')
        else:
            self.fsm.request('zonePage')

    def exit(self):
        if not self.entered:
            return
        self.entered = 0
        base.setBackgroundColor(CIGlobals.DefaultBackgroundColor)
        render.show()
        self.book_img.destroy()
        del self.book_img
        self.book_close.play()
        self.fsm.request('off')
        StateData.exit(self)

    def enterDistrictPage(self):
        self.createPageButtons('optionPage', 'questPage')
        self.setTitle("Districts")

        currDistrictName = base.cr.myDistrict.getDistrictName()
        if not currDistrictName.isalpha():
            currDistrictName = currDistrictName[:-1]
        self.infoLbl = OnscreenText(
            text = 'Each District is a copy of the Cog Invasion world.\n'
                '\n\nYou are currently in the "%s" District' % currDistrictName,
            pos = (0.05, 0.3), align = TextNode.ALeft, wordwrap = 12)
        self.populationLbl = OnscreenText(text = "Population: %d" % base.cr.myDistrict.getPopulation(),
            pos = (0.44, -0.3), align = TextNode.ACenter)

        textRolloverColor = Vec4(1, 1, 0, 1)
        textDownColor = Vec4(0.5, 0.9, 1, 1)
        textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)

        self.shardButtons = []
        for shard in base.cr.activeDistricts.values():
            shardName = shard.getDistrictName()
            shardId = shard.doId
            btn = DirectButton(
                relief=None, text=shardName, text_scale=0.07,
                text_align=TextNode.ALeft, text1_bg=textDownColor, text2_bg=textRolloverColor,
                text3_fg=textDisabledColor, textMayChange=0, command=self.__handleShardButton,
                extraArgs=[shardId], text_pos = (0, 0, 0.0)
            )
            if shardId == base.localAvatar.parentId:
                btn['state'] = DGG.DISABLED
            else:
                btn['state'] = DGG.NORMAL
            self.shardButtons.append(btn)

        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui.bam')
        listXorigin = -0.02
        listFrameSizeX = 0.625
        listZorigin = -0.96
        listFrameSizeZ = 1.04
        arrowButtonScale = 1.3
        itemFrameXorigin = -0.237
        itemFrameZorigin = 0.365
        buttonXstart = itemFrameXorigin + 0.293

        self.districtList = DirectScrolledList(
            relief=None,
            pos=(-0.54, 0, 0.08),
            incButton_image=(gui.find('**/FndsLst_ScrollUp'),
                gui.find('**/FndsLst_ScrollDN'),
                gui.find('**/FndsLst_ScrollUp_Rllvr'),
                gui.find('**/FndsLst_ScrollUp')),
            incButton_relief=None,
            incButton_scale=(arrowButtonScale, arrowButtonScale, -arrowButtonScale),
            incButton_pos=(buttonXstart, 0, itemFrameZorigin - 0.999),
            incButton_image3_color=Vec4(1, 1, 1, 0.2),
            decButton_image=(gui.find('**/FndsLst_ScrollUp'),
                gui.find('**/FndsLst_ScrollDN'),
                gui.find('**/FndsLst_ScrollUp_Rllvr'),
                gui.find('**/FndsLst_ScrollUp')),
            decButton_relief=None,
            decButton_scale=(arrowButtonScale, arrowButtonScale, arrowButtonScale),
            decButton_pos=(buttonXstart, 0, itemFrameZorigin + 0.125),
            decButton_image3_color=Vec4(1, 1, 1, 0.2),
            itemFrame_pos=(itemFrameXorigin, 0, itemFrameZorigin),
            itemFrame_scale=1.0,
            itemFrame_relief=DGG.SUNKEN,
            itemFrame_frameSize=(listXorigin,
                listXorigin + listFrameSizeX,
                listZorigin,
                listZorigin + listFrameSizeZ),
            itemFrame_frameColor=(0.85, 0.95, 1, 1),
            itemFrame_borderWidth=(0.01, 0.01),
            numItemsVisible=15,
            forceHeight=0.075,
            items=self.shardButtons
        )
        base.taskMgr.add(self.__updateDistrictPopTask, "SB.updateDistrictPopTask")

    def __handleShardButton(self, shardId):
        self.finished("switchShard", shardId)

    def __updateDistrictPopTask(self, task):
        population = base.cr.myDistrict.getPopulation()
        self.populationLbl.setText('Population: %d' % population)
        task.delayTime = 5.0
        return task.again

    def exitDistrictPage(self):
        base.taskMgr.remove('SB.updateDistrictPopTask')
        for btn in self.shardButtons:
            btn.destroy()
        del self.shardButtons
        self.districtList.destroy()
        del self.districtList
        self.infoLbl.destroy()
        del self.infoLbl
        self.populationLbl.destroy()
        del self.populationLbl
        self.deletePageButtons(True, True)
        self.clearTitle()

    def enterQuestPage(self):
        self.createPageButtons('districtPage', 'zonePage')
        self.setTitle("Quests")

        self.notes = base.localAvatar.questManager.makeQuestNotes()
        for note in self.notes:
            note.show()

        self.infoText = OnscreenText(text = "Return completed Quests to an HQ Officer at any Toon HQ building.",
            pos = (0, -0.6), scale = 0.045)

    def exitQuestPage(self):
        self.infoText.destroy()
        del self.infoText
        for note in self.notes:
            note.destroy()
        self.deletePageButtons(True, True)
        self.clearTitle()

    def enterZonePage(self):
        self.createPageButtons('questPage', 'releaseNotesPage')
        self.setTitle("Places")
        #self.home_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
        #									qt_btn.find('**/QuitBtn_DN'),
        #									qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.055, text=CIGlobals.Estate, command=self.setHood, extraArgs=[10], pos=(-0.45, 0.55, 0.55))
        self.ttc_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
                                            qt_btn.find('**/QuitBtn_DN'),
                                            qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.045, text=CIGlobals.ToontownCentral, command=self.finished, extraArgs=[CIGlobals.ToontownCentralId], pos=(-0.45, 0.15, 0.5), text_pos = (0, -0.01))
        self.tbr_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
                                            qt_btn.find('**/QuitBtn_DN'),
                                            qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.055, text=CIGlobals.TheBrrrgh, command=self.finished, extraArgs=[CIGlobals.TheBrrrghId], pos=(-0.45, 0.15, 0.38), text_pos = (0, -0.01))
        self.ddl_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
                                            qt_btn.find('**/QuitBtn_DN'),
                                            qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.044, text=CIGlobals.DonaldsDreamland, command=self.finished, extraArgs=[CIGlobals.DonaldsDreamlandId], pos=(-0.45, 0.15, 0.26), text_pos = (0, -0.01))
        self.mml_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
        									qt_btn.find('**/QuitBtn_DN'),
        									qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.0425, text=CIGlobals.MinniesMelodyland, command=self.finished, extraArgs=[CIGlobals.MinniesMelodylandId], pos=(-0.45, 0.35, 0.14), text_pos = (0, -0.01))
        self.dg_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
        									qt_btn.find('**/QuitBtn_DN'),
        									qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.045, text=CIGlobals.DaisyGardens, command=self.finished, extraArgs=[CIGlobals.DaisyGardensId], pos=(-0.45, 0.35, 0.02), text_pos = (0, -0.01))
        self.dd_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
        									qt_btn.find('**/QuitBtn_DN'),
        									qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.045, text=CIGlobals.DonaldsDock, command=self.finished, extraArgs=[CIGlobals.DonaldsDockId], pos=(-0.45, 0.35, -0.1), text_pos = (0, -0.01))
        self.minigame_btn = DirectButton(geom=(qt_btn.find('**/QuitBtn_UP'),
                                            qt_btn.find('**/QuitBtn_DN'),
                                            qt_btn.find('**/QuitBtn_RLVR')), relief=None, scale=1.2, text_scale=0.055, text=CIGlobals.MinigameArea, command=self.finished, extraArgs=[CIGlobals.MinigameAreaId], pos=(-0.45, 0.35, -0.34), text_pos = (0, -0.01))
        #self.populationLbl = OnscreenText(text = "", pos = (0.45, 0.1), align = TextNode.ACenter)
        #self.popRecordLbl = OnscreenText(text = "", pos = (0.45, -0.1), align = TextNode.ACenter, scale = 0.05)
        #taskMgr.add(self.__updateGamePopulation, "ShtickerBook-updateGamePopulation")

    def __updateGamePopulation(self, task):
        population = 0
        for district in base.cr.activeDistricts.values():
            population += district.getPopulation()
        self.populationLbl.setText("Game Population:\n" + str(population))
        recordPopulation = base.cr.myDistrict.getPopRecord()
        self.popRecordLbl.setText("Record Population:\n" + str(recordPopulation))
        task.delayTime = 5.0
        return task.again

    def exitZonePage(self):
        #taskMgr.remove("ShtickerBook-updateGamePopulation")
        #self.popRecordLbl.destroy()
        #del self.popRecordLbl
        #self.populationLbl.destroy()
        #del self.populationLbl
        self.dd_btn.destroy()
        del self.dd_btn
        self.ddl_btn.destroy()
        del self.ddl_btn
        self.ttc_btn.destroy()
        del self.ttc_btn
        self.tbr_btn.destroy()
        del self.tbr_btn
        self.minigame_btn.destroy()
        del self.minigame_btn
        self.mml_btn.destroy()
        del self.mml_btn
        self.dg_btn.destroy()
        del self.dg_btn
        self.deletePageButtons(True, True)
        self.clearTitle()

    def createPageButtons(self, back, fwd):
        if back:
            self.btn_prev = DirectButton(geom=(self.book_contents.find('**/arrow_button'),
                                        self.book_contents.find('**/arrow_down'),
                                        self.book_contents.find('**/arrow_rollover')), relief=None, pos=(-0.838, 0, -0.661), scale=(-0.1, 0.1, 0.1), command=self.pageDone, extraArgs = [back])
        if fwd:
            self.btn_next = DirectButton(geom=(self.book_contents.find('**/arrow_button'),
                                        self.book_contents.find('**/arrow_down'),
                                        self.book_contents.find('**/arrow_rollover')), relief=None, pos=(0.838, 0, -0.661), scale=(0.1, 0.1, 0.1), command=self.pageDone, extraArgs = [fwd])

    def deletePageButtons(self, back, fwd):
        if back:
            self.btn_prev.destroy()
            del self.btn_prev
        if fwd:
            self.btn_next.destroy()
            del self.btn_next

    def setTitle(self, title):
        self.page_title = OnscreenText(text=title, pos=(0, 0.62, 0), scale=0.12)

    def clearTitle(self):
        self.page_title.destroy()
        del self.page_title

    def enterReleaseNotesPage(self):
        if base.localAvatar.getAdminToken() > -1:
            self.createPageButtons('zonePage', 'adminPage')
        else:
            self.createPageButtons('zonePage', None)
        self.setTitle("Release Notes")
        self.frame = DirectScrolledFrame(canvasSize = (-1, 1, -3.5, 1), frameSize = (-1, 1, -0.6, 0.6))
        self.frame.setPos(0, 0, 0)
        self.frame.setScale(0.8)
        self.release_notes = DirectLabel(text=open("release_notes.txt", "r").read(), text_align = TextNode.ALeft, pos=(-0.955, 0, 0.93), relief=None,
            text_fg=(0,0,0,1), text_wordwrap=37.0, text_scale=0.05, parent = self.frame.getCanvas())

    def exitReleaseNotesPage(self):
        self.frame.destroy()
        del self.frame
        self.release_notes.destroy()
        del self.release_notes
        self.clearTitle()
        if base.localAvatar.getAdminToken() > -1:
            self.deletePageButtons(True, True)
        else:
            self.deletePageButtons(True, False)

    def enterAdminPage(self):
        self.adminPageStateData = AdminPage(self, self.fsm)
        self.adminPageStateData.load()
        self.adminPageStateData.enter()

    def exitAdminPage(self):
        self.adminPageStateData.exit()
        self.adminPageStateData.unload()
        del self.adminPageStateData

    def pageDone(self, nextPage):
        self.fsm.request(nextPage)
        self.book_turn.play()

    def enterOptionPage(self):
        self.optionPageStateData = OptionPage(self, self.fsm)
        #self.acceptOnce(self.optionPageStateData.doneEvent, self.pageDone)
        self.optionPageStateData.load()
        self.optionPageStateData.enter()

    def exitOptionPage(self):
        #self.ignore(self.optionPageStateData.doneEvent)
        self.optionPageStateData.exit()
        self.optionPageStateData.unload()
        del self.optionPageStateData

    def prevPage(self, currentPage):
        self.clearCurrentPage()
        if self.currentPage == 2:
            self.optionPage()
        elif self.currentPage == 3:
            self.zonePage()
        elif self.currentPage == 4:
            self.releaseNotesPage()

    def nextPage(self, currentPage):
        self.clearCurrentPage()
        if self.currentPage == 1:
            self.zonePage()
        elif self.currentPage == 2:
            self.releaseNotesPage()
        elif self.currentPage == 3:
            self.adminPage()

    def clearCurrentPage(self):
        self.book_turn.play()
        for m in base.bookpgnode.getChildren():
            m.removeNode()

    def finished(self, zone, shardId = None):
        if base.localAvatar.getHealth() < 1 and type(zone) == type(1):
            return
        doneStatus = {}
        if zone in [CIGlobals.ToontownCentralId, CIGlobals.MinigameAreaId,
        CIGlobals.TheBrrrghId, CIGlobals.DonaldsDreamlandId, CIGlobals.MinniesMelodylandId,
        CIGlobals.DaisyGardensId, CIGlobals.DonaldsDockId]:
            doneStatus["mode"] = 'teleport'
            doneStatus["zoneId"] = zone
            doneStatus["hoodId"] = ZoneUtil.getHoodId(zone)
            doneStatus["where"] = ZoneUtil.getWhereName(zone)
            doneStatus["how"] = 'teleportIn'
            doneStatus["avId"] = base.localAvatar.doId
            doneStatus["shardId"] = None
            doneStatus["loader"] = ZoneUtil.getLoaderName(zone)
        else:
            doneStatus["mode"] = zone
            if zone == "switchShard":
                doneStatus["shardId"] = shardId
        self.doneStatus = doneStatus
        messenger.send(self.doneEvent)

    def closeBook(self):
        self.book_close.play()
        base.bookpgnode.removeNode()
        base.booknode.removeNode()