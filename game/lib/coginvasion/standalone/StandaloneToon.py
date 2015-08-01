# Filename: StandaloneToon.py
# Created by:  blach (02May15)

from panda3d.core import *
loadPrcFile('config/config_client.prc')

from direct.showbase.ShowBase import ShowBase
base = ShowBase()
from direct.distributed.ClientRepository import ClientRepository

import __builtin__
class game:
	process = 'client'
__builtin__.game = game()

from lib.coginvasion.toon import LocalToon
from lib.coginvasion.login.AvChoice import AvChoice

base.cTrav = CollisionTraverser()
base.cr = ClientRepository(['astron/direct.dc', 'astron/toon.dc'])
base.cr.isShowingPlayerIds = False
base.cr.localAvChoice = AvChoice("00/08/00/10/01/12/01/10/18/18/07/00/00/00/00", "Ducky", 0, 0)

dclass = base.cr.dclassesByName['DistributedToon']
base.localAvatar = LocalToon.LocalToon(base.cr)
base.localAvatar.dclass = dclass
base.localAvatar.doId = base.cr.localAvChoice.getAvId()
base.localAvatar.generate()
base.localAvatar.setName(base.cr.localAvChoice.getName())
base.localAvatar.setMaxHealth(137)
base.localAvatar.setHealth(137)
base.localAvatar.setDNAStrand(base.cr.localAvChoice.getDNA())
base.localAvatar.announceGenerate()
base.localAvatar.reparentTo(base.render)
base.localAvatar.enableAvatarControls()