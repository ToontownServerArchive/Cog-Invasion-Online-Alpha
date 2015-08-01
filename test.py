from pandac.PandaModules import *

loadPrcFileData('', 'audio-library-name p3fmod_audio')
loadPrcFileData('', 'notify-level info')
loadPrcFileData('', 'default-directnotify-level info')
loadPrcFile('config/config_client.prc')
import __builtin__
class game:
	process = 'client'
__builtin__.game = game
from direct.showbase.ShowBaseWide import ShowBase
base = ShowBase()
from lib.coginvasion.dna.DNAParser import *
from lib.coginvasion.globals import CIGlobals
from direct.controls import ControlManager
from direct.controls.GravityWalker import GravityWalker
from lib.coginvasion.toon.Toon import Toon
from direct.distributed.ClientRepository import ClientRepository
from lib.coginvasion.toon.SmartCamera import SmartCamera
#from lib.toontown.base.ShadowCreator import ShadowCreator

#caster = ShadowCreator()

#from rp.Code.RenderingPipeline import RenderingPipeline

cbm = CullBinManager.getGlobalPtr()
cbm.addBin('ground', CullBinManager.BTUnsorted, 18)
cbm.addBin('shadow', CullBinManager.BTBackToFront, 19)
cbm.addBin('gui-popup', CullBinManager.BTUnsorted, 60)

render.setAntialias(AntialiasAttrib.MMultisample)

base.camLens.setMinFov(54.0 / (4./3.))

cbm = CullBinManager.getGlobalPtr()
cbm.addBin('ground', CullBinManager.BTUnsorted, 18)
cbm.addBin('shadow', CullBinManager.BTBackToFront, 19)
cbm.addBin('gui-popup', CullBinManager.BTUnsorted, 60)

ds = DNAStorage()

loadDNAFile(ds, "phase_4/dna/storage.dna")
loadDNAFile(ds, "phase_4/dna/storage_TT.dna")
loadDNAFile(ds, "phase_4/dna/storage_TT_sz.dna")
loadDNAFile(ds, "phase_5/dna/storage_town.dna")
loadDNAFile(ds, "phase_5/dna/storage_TT_town.dna")
loadDNAFile(ds, "phase_4/dna/storage_new_TT.dna")
node = loadDNAFile(ds, "phase_4/dna/new_ttc_sz.dna")

if node.getNumParents() == 1:
	geom = NodePath(node.getParent(0))
	geom.reparentTo(hidden)
else:
	geom = hidden.attachNewNode(node)
gsg = base.win.getGsg()
if gsg:
	geom.prepareScene(gsg)
geom.setName('toontown_central')
geom.reparentTo(render)
geom.find('**/toontown_central_DNARoot').setTwoSided(1)
for tree in geom.findAllMatches('**/prop_green_tree_large*_DNARoot'):
	print tree.getName()
	tree.setBillboardAxis()
	try:
		tree.find('**/prop_green_tree_large_ur_shadow').removeNode()
	except:
		tree.find('**/prop_green_tree_large_ul_shadow').removeNode()
	newShadow = loader.loadModel("phase_3/models/props/drop_shadow.bam")
	newShadow.reparentTo(tree)
sky = loader.loadModel("phase_3.5/models/props/TT_sky.bam")
sky.reparentTo(render)
sky.setScale(5)
sky.find('**/cloud1').setSz(0.65)
sky.find('**/cloud2').removeNode()


geom.hide(BitMask32.bit(1))
shadowStage = TextureStage("shadowTexStage")
shadowStage.setMode(TextureStage.MBlend)
geom.projectTexture(shadowStage, caster.shadowTexture, caster.shadowCamera)


music = base.loadMusic("phase_4/audio/bgm/TC_nbrhood.ogg")
base.playMusic(music, volume = 0.25, looping = 1, interrupt = 1)

for nodepath in render.findAllMatches('*'):
	try:
		for node in nodepath.findAllMatches('**'):
			try:
				node.findTexture('*').setAnisotropicDegree(10)
			except:
				pass
	except:
		continue


base.cTrav = CollisionTraverser()
cr = ClientRepository(['astron/direct.dc'])
"""
controlManager = ControlManager.ControlManager(True, False)
localAv = Toon(cr)
localAv.setDNAStrand("00/01/07/00/02/00/01/00/00/00/00/00/00/00/00")
localAv.setName("Sneaky Toon")
localAv.initCollisions()
localAv.startBlink()
localAv.startLookAround()
localAv.reparentTo(render)
localAv.animFSM.request("neutral")
avatarMoving = False
base.disableMouse()

animal = localAv.getAnimal()
bodyScale = ToontownGlobals.toonBodyScales[animal]
headScale = ToontownGlobals.toonHeadScales[animal][2]
shoulderHeight = ToontownGlobals.legHeightDict[localAv.legs] * bodyScale + ToontownGlobals.torsoHeightDict[localAv.torso] * bodyScale
height = shoulderHeight + ToontownGlobals.headHeightDict[localAv.head] * headScale
localAv.setHeight(height)
camHeight = max(localAv.getHeight(), 3.0)
heightScaleFactor = camHeight * 0.3333333333
defLookAt = Point3(0.0, 1.5, camHeight)
camPos = (Point3(0.0, -9.0 * heightScaleFactor, camHeight),
	defLookAt,
	Point3(0.0, camHeight, camHeight * 4.0),
	Point3(0.0, camHeight, camHeight * -1.0),
	0)

av = Toon(cr)
av.setDNAStrand("00/00/00/00/00/00/00/00/00/00/00/00/00/00/00")
av.setName("Tom")
av.initCollisions()
av.startBlink()
av.startLookAround()
av.reparentTo(render)
av.animFSM.request("neutral")
av.setX(-20)
"""
av2 = Toon(cr)
av2.setDNAStrand("00/04/01/00/02/00/01/00/00/00/00/00/00/00/00")
av2.setName("Flippy")
av2.initCollisions()
av2.startBlink()
av2.startLookAround()
av2.reparentTo(render)
av2.animFSM.request("neutral")
av2.setX(-23)
av2.setY(5)
av2.setH(77)
"""

ToonStandableGround = 0.707
ToonSpeedFactor = 1.25
ToonForwardSpeed = 16.0 * ToonSpeedFactor
ToonJumpForce = 24.0
ToonReverseSpeed = 8.0 * ToonSpeedFactor
ToonRotateSpeed = 80.0 * ToonSpeedFactor
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0

Y_FACTOR = -0.15

smart_cam = SmartCamera()
smart_cam.set_default_pos(camPos)
smart_cam.set_parent(localAv)
smart_cam.initialize_smartcamera()
smart_cam.initialize_smartcamera_collisions()
smart_cam.start_smartcamera()

walkControls = GravityWalker(legacyLifter=False)
walkControls.setWallBitMask(ToontownGlobals.WallBitmask)
walkControls.setFloorBitMask(ToontownGlobals.FloorBitmask)
walkControls.setWalkSpeed(ToonForwardSpeed, ToonJumpForce, ToonReverseSpeed, ToonRotateSpeed)
walkControls.initializeCollisions(base.cTrav, localAv, avatarRadius=1.4, floorOffset=0.025, reach=4.0)
walkControls.enableAvatarControls()

def crouch():
	walkControls.setWalkSpeed(ToonForwardSpeed, ToonJumpForce, ToonReverseSpeed, ToonRotateSpeed)
	
def uncrouch():
	walkControls.setWalkSpeed(ToonForwardSpeed, ToonJumpForce, ToonReverseSpeed, ToonRotateSpeed)
	
def moving():
	localAv.animFSM.request('run')
	global avatarMoving
	avatarMoving = True
	
def unmoving():
	localAv.animFSM.request('neutral')
	global avatarMoving
	avatarMoving = False

base.accept("control", crouch)
base.accept("control-up", uncrouch)
base.accept("arrow_up", moving)
base.accept("arrow_up-up", unmoving)
"""
"""
amb = AmbientLight('amblight')
amb.setColor(VBase4(0.5, 0.5, 0.5, 1))
ambNp = render.attachNewNode(amb)
render.setLight(ambNp)

spot = Spotlight('slight')
spot.setColor(VBase4(1, 1, 1, 1))
spot.setShadowCaster(True, 2000, 2000)
spot.setExponent(64)
spotNp = render.attachNewNode(spot)
spotNp.setPos(-30, 5, 100)
spotNp.lookAt(0, 0, 0)
#render.setLight(spotNp)

direc = PointLight('dlight')
direc.setColor(VBase4(1, 1, 1, 1))
direcNp = render.attachNewNode(direc)
direcNp.setZ(5)
direcNp.setY(15)
render.setLight(direcNp)

render.setTwoSided(False)
render.setShaderAuto()
"""


# Used for rotating buildings in the outer circle around.
#bldgNode = NodePath()
#bldgNode.attachNewNode(geom.find('**/sz0:random_DNARoot'))
#bldgNode.attachNewNode(geom.find('**/sz0:random_2_DNARoot'))
#bldgNode.attachNewNode(geom.find('**/linktunnel_tt_2132_DNARoot'))
#bldgNode.attachNewNode(geom.find('**/sz18:toon_landmark_TT_library_DNARoot'))
#bldgNode.attachNewNode(geom.find('**/

#geom.find('**/buildings').place()

#geom.find('**/prop_green_tree_large_ur_2_DNARoot').place()

caster.shadowCamera.place()

base.oobe()
run()
