"""

  Filename: DistributedToonAI.py
  Created by: blach (12Oct14)

"""

from lib.coginvasion.globals import CIGlobals
from direct.distributed.DistributedSmoothNodeAI import DistributedSmoothNodeAI
from direct.directnotify.DirectNotify import DirectNotify
from panda3d.core import *
from pandac.PandaModules import *
from lib.coginvasion.avatar.DistributedAvatarAI import DistributedAvatarAI
from lib.coginvasion.gags import GagGlobals
from lib.coginvasion.gags.GagManager import GagManager
from lib.coginvasion.gags.GagType import GagType
from lib.coginvasion.gags.backpack import BackpackManager
from lib.coginvasion.quests.QuestManagerAI import QuestManagerAI
from lib.coginvasion.quests import Quests
from direct.interval.IntervalGlobal import Sequence, Wait, Func
import ToonDNA
import json

class DistributedToonAI(DistributedAvatarAI, DistributedSmoothNodeAI, ToonDNA.ToonDNA):
    notify = DirectNotify().newCategory("DistributedToonAI")

    def __init__(self, air):
        try:
            self.DistributedToonAI_initialized
            return
        except:
            self.DistributedToonAI_initialized = 1
        DistributedAvatarAI.__init__(self, air)
        DistributedSmoothNodeAI.__init__(self, air)
        ToonDNA.ToonDNA.__init__(self)
        self.questManager = QuestManagerAI(self)
        self.avatarType = CIGlobals.Toon
        self.money = 0
        self.name = ""
        self.anim = "neutral"
        self.chat = ""
        self.health = 50
        self.damage = 0
        self.height = 3
        self.gender = "boy"
        self.headtype = "dgm_skirt"
        self.head = "dog"
        self.legtype = "dgm"
        self.torsotype = "dgm_shorts"
        self.hr = 1
        self.hg = 1
        self.hb = 1
        self.tr = 1
        self.tg = 1
        self.tb = 1
        self.lr = 1
        self.lg = 1
        self.lb = 1
        self.shir = 1
        self.shig = 1
        self.shib = 1
        self.shor = 1
        self.shog = 1
        self.shob = 1
        self.ammo = []
        self.shirt = "phase_3/maps/desat_shirt_1.jpg"
        self.short = "phase_3/maps/desat_shorts_1.jpg"
        self.sleeve = "phase_3/maps/desat_sleeve_1.jpg"
        self.isdying = False
        self.isdead = False
        self.toon_legs = None
        self.toon_torso = None
        self.toon_head = None
        self.portal = None
        self.book = None
        self.token = -1
        self.ghost = 0
        self.attackers = []
        self.puInventory = []
        self.equippedPU = -1
        self.backpack = -1
        self.gagMgr = GagManager()
        self.setupGags = False
        self.makeTopToons()
        self.quests = [[], [], []]
        self.questHistory = []
        self.tier = -1
        self.friends = []
        return

    def requestAddFriend(self, avId):
        av = self.air.doId2do.get(avId)
        if av:
            if av.zoneId == self.zoneId and not avId in self.friends:
                fl = list(self.friends)
                fl.append(avId)
                self.b_setFriendsList(fl)

    def setFriendsList(self, friends):
        self.friends = friends

    def d_setFriendsList(self, friends):
        self.sendUpdate('setFriendsList', [friends])

    def b_setFriendsList(self, friends):
        self.d_setFriendsList(friends)
        self.setFriendsList(friends)

    def getFriendsList(self):
        return self.friends

    def setTier(self, tier):
        self.tier = tier

    def d_setTier(self, tier):
        self.sendUpdate('setTier', [tier])

    def b_setTier(self, tier):
        self.d_setTier(tier)
        self.setTier(tier)

    def getTier(self):
        return self.tier

    def setQuestHistory(self, history):
        self.questHistory = history

    def d_setQuestHistory(self, history):
        self.sendUpdate('setQuestHistory', [history])

    def b_setQuestHistory(self, history):
        self.d_setQuestHistory(history)
        self.setQuestHistory(history)

    def getQuestHistory(self):
        return self.questHistory

    def d_setChat(self, chat):
        self.sendUpdate('setChat', [chat])

    def setQuests(self, questIds, currentObjectives, currentObjectivesProgress):
        self.quests = [questIds, currentObjectives, currentObjectivesProgress]
        self.questManager.makeQuestsFromData()

    def d_setQuests(self, questIds, currentObjectives, currentObjectivesProgress):
        self.sendUpdate('setQuests', [questIds, currentObjectives, currentObjectivesProgress])

    def b_setQuests(self, questData):
        self.d_setQuests(questData[0], questData[1], questData[2])
        self.setQuests(questData[0], questData[1], questData[2])

    def getQuests(self):
        return self.quests

    def makeTopToons(self):
        data = {'mostJellybeans' : [0, None], 'mostCogsDefeated' : [0, None]}
        with open('astron/top_toons.json', 'w') as toptoons:
            json.dump(data, toptoons)

    def setBackpack(self, backpack):
        self.backpack = BackpackManager.getBackpack(backpack)

    def d_setBackpack(self, backpack):
        self.sendUpdate('setBackpack', [backpack])

    def b_setBackpack(self, backpack):
        self.setBackpack(backpack)
        self.d_setBackpack(backpack)

    def getBackpack(self):
        index = BackpackManager.getIndex(self.backpack)
        # This is a required field and this sometimes returns None.
        # We can't send none out on the wire.
        if index == None:
            return 0
        else:
            return index

    def usedPU(self, index):
        self.puInventory[index] = 0
        self.b_setPUInventory(self.puInventory)

    def requestEquipPU(self, index):
        if len(self.puInventory) > index and self.puInventory[index] > 0:
            self.b_setEquippedPU(index)

    def setEquippedPU(self, index):
        self.equippedPU = index

    def d_setEquippedPU(self, index):
        self.sendUpdate('setEquippedPU', [index])

    def b_setEquippedPU(self, index):
        self.d_setEquippedPU(index)
        self.setEquippedPU(index)

    def getEquippedPU(self):
        return self.equippedPU

    def setPUInventory(self, array):
        self.puInventory = array

    def d_setPUInventory(self, array):
        self.sendUpdate("setPUInventory", [array])

    def b_setPUInventory(self, array):
        self.d_setPUInventory(array)
        self.setPUInventory(array)

    def getPUInventory(self):
        return self.puInventory

    def addNewAttacker(self, suitId, length = 5):
        if not suitId in self.attackers:
            self.attackers.append(suitId)
            Sequence(Wait(length), Func(self.removeAttacker, suitId)).start()

    def removeAttacker(self, suitId):
        if self.attackers:
            self.attackers.remove(suitId)
        else:
            self.attackers = []

    def getNumAttackers(self):
        return len(self.attackers)

    def getAttackers(self):
        return self.attackers

    def ejectSelf(self, reason = ""):
        self.air.eject(self.doId, 0, reason)

    def requestEject(self, avId, andBan = 0):
        clientChannel = self.GetPuppetConnectionChannel(avId)

        def getToonDone(dclass, fields):
            if dclass != self.air.dclassesByName['DistributedToonAI']:
                return
            accId = fields['ACCOUNT']
            self.air.dbInterface.updateObject(
                self.air.dbId,
                accId,
                self.air.dclassesByName['AccountAI'],
                {"BANNED": 1}
            )

        if self.getAdminToken() > -1:
            if andBan:
                self.air.dbInterface.queryObject(
                    self.air.dbId,
                    avId,
                    getToonDone
                )
            self.air.eject(clientChannel, 0, "Ejected by an administrator.")
        else:
            # Oh ok, a non-admin is trying to eject someone.
            # Let's eject them instead.
            self.ejectSelf("This player did not have administrator rights, but was trying to eject someone.")

    def setGhost(self, value):
        if not self.getAdminToken() > -1:
            self.ejectSelf()
            return
        self.ghost = value

    def getGhost(self):
        return self.ghost

    def toonUp(self, hp, announce = 1, sound = 1):
        amt = hp
        originalHealth = self.getHealth()
        hp = self.getHealth() + hp
        if hp > self.getMaxHealth():
            amt = self.getMaxHealth() - originalHealth
            hp = self.getMaxHealth()
        self.b_setHealth(hp)
        if announce and sound:
            self.d_announceHealthAndPlaySound(1, amt)
        elif announce and not sound:
            self.d_announceHealth(1, amt)

    def d_announceHealthAndPlaySound(self, level, hp):
        self.sendUpdate("announceHealthAndPlaySound", [level, hp])

    def setMoney(self, money):
        self.money = money

    def d_setMoney(self, money):
        self.sendUpdate('setMoney', [money])

    def b_setMoney(self, money):
        self.d_setMoney(money)
        self.setMoney(money)

    def getMoney(self):
        return self.money

    def setAnimState(self, anim, timestamp = 0):
        self.anim = anim

    def getAnimState(self):
        return self.anim

    def setAdminToken(self, token):
        self.token = token

    def getAdminToken(self):
        return self.token

    def gagRelease(self, gag_id):
        gagIds = []
        ammoList = []
        for gag in self.backpack.getGags():
            if gag:
                gagIds.append(gag.getID())
        for index in range(len(gagIds)):
            gagId = gagIds[index]
            supply = self.backpack.getSupply(GagGlobals.getGagByID(gagId))
            if gagId == gag_id:
                amt = supply - 1
                if amt < 0:
                    self.ejectSelf()
                    return
            else:
                amt = supply
                if not amt: amt = 0
            ammoList.append(amt)
        self.b_setBackpackAmmo(gagIds, ammoList)

    def equip(self, index):
        if not self.setupGags: self.setupGags = True
        self.backpack.setCurrentGag(index)

    def buildAmmoList(self, gagIds):
        ammoList = []
        for index in range(len(gagIds)):
            gagId = gagIds[index]
            amt = self.backpack.getSupply(GagGlobals.getGagByID(gagId))
            ammoList.append(amt)
        return ammoList

    def setBackpackAmmo(self, gagIds, ammoList):
        if self.ammo == ammoList: return
        if len(self.backpack.gags.keys()) > 0:
            for index in range(len(gagIds)):
                gagId = gagIds[index]
                numOfThisGag = 0
                for gag in self.backpack.gags.keys():
                    if type(self.backpack.gagMgr.getGagByName(GagGlobals.getGagByID(gagId))) == type(gag):
                        numOfThisGag += 1
                if numOfThisGag < 1:
                    # We must have been given a new backpack. Clear the current gag dictionary.
                    self.backpack.resetGags()
                    break
        for index in range(len(ammoList)):
            amt = ammoList[index]
            gagId = gagIds[index]
            if amt < 0:
                amt = 0
            self.backpack.setSupply(amt, GagGlobals.getGagByID(gagId))
        self.ammo = ammoList
        if self.setupGags == False: self.d_setBackpackAmmo(gagIds, ammoList)

    def d_setBackpackAmmo(self, gagIds, ammoList):
        for amt in ammoList:
            if amt < 0: amt = 0
        self.sendUpdate('setBackpackAmmo', [gagIds, ammoList])

    def b_setBackpackAmmo(self, gagIds, ammoList):
        self.setBackpackAmmo(gagIds, ammoList)
        self.d_setBackpackAmmo(gagIds, ammoList)

    def getBackpackAmmo(self):
        return self.ammo

    def died(self):
        self.b_setHealth(self.getMaxHealth())

    def suitHitByPie(self, avId, gag_id):
        # The id of the weapon must be provided so the player
        # can't cheat and switch weapons while it is in mid-air
        # to do a different damage amount.
        obj = self.air.doId2do.get(avId, None)
        gag = self.gagMgr.getGagByName(GagGlobals.getGagByID(gag_id))
        dmg = gag.getDamage()
        if obj:
            if not obj.isDead():
                obj.b_setHealth(obj.getHealth() - dmg)
                obj.d_announceHealth(0, dmg)
                if obj.getHealth() <= 0:
                    if gag.getType() == GagType.THROW or gag.getType() == GagType.TRAP:
                        obj.b_setAnimState('pie')
                    elif gag.getType() == GagType.DROP:
                        obj.b_setAnimState('drop')
                    elif gag.getType() == GagType.SQUIRT:
                        obj.b_setAnimState('squirt-small')

                    self.questManager.cogDefeated(obj)

    def suitKilled(self, avId):
        obj = self.air.doId2do.get(avId, None)
        if obj:
            money = int(obj.maxHealth / CIGlobals.SuitAttackDamageFactors['clipontie'])
            self.b_setMoney(self.getMoney() + money)

    def toonHitByPie(self, avId, gag_id):
        obj = self.air.doId2do.get(avId, None)
        hp = self.gagMgr.getGagByName(GagGlobals.getGagByID(gag_id)).getHealth()
        if obj:
            if obj.getHealth() < obj.getMaxHealth() and not obj.isDead():
                obj.toonUp(hp)

    def announceGenerate(self):
        DistributedAvatarAI.announceGenerate(self)
        DistributedSmoothNodeAI.announceGenerate(self)

    def delete(self):
        try:
            self.DistributedToonAI_deleted
        except:
            self.DistributedToonAI_deleted = 1
            DistributedAvatarAI.delete(self)
            DistributedSmoothNodeAI.delete(self)
            self.questManager.cleanup()
            self.questManager = None
            self.token = None
            self.name = None
            self.anim = None
            self.chat = None
            self.health = None
            self.damage = None
            self.height = None
            self.gender = None
            self.headtype = None
            self.head = None
            self.legtype = None
            self.torsotype = None
            self.hr = None
            self.hg = None
            self.hb = None
            self.tr = None
            self.tg = None
            self.tb = None
            self.lr = None
            self.lg = None
            self.lb = None
            self.shir = None
            self.shig = None
            self.shib = None
            self.shor = None
            self.shog = None
            self.shob = None
            self.shirt = None
            self.short = None
            self.sleeve = None
            self.isdying = None
            self.isdead = None
            self.toon_legs = None
            self.toon_torso = None
            self.toon_head = None
            self.portal = None
            self.book = None
            self.place = None
            self.attackers = None
        return
