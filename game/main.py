import direct.directbase.DirectStart
from direct.task import Task
from direct.actor import Actor
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
import math

#Load the first environment model
envirom = loader.loadModel("models/environment")
envirom.reparentTo(render)
envirom.setScale(0.05,0.05,0.05)
envirom.setPos(-8,42,0)

def SpinCameraTask(task):
  angledegrees = task.time * 6.0
  angleradians = angledegrees * (math.pi / 180.0)
  base.camera.setPos(20*math.sin(angleradians),-20.0*math.cos(angleradians),3)
  base.camera.setHpr(angledegrees, 0, 0)
  return Task.cont

taskMgr.add(SpinCameraTask, "SpinCameraTask")

#Import Panda and its animation
panda = Actor.Actor("models/panda-model",{"walk":"models/panda-walk4"})
panda.setScale(0.0025,0.0025,0.0025)
panda.reparentTo(render)
panda.loop("walk")

#Create the four lerp intervals needed to walk back and forth
pandaPosInterval1= panda.posInterval(13,Point3(0,-10,0), startPos=Point3(0,10,0))
pandaPosInterval2= panda.posInterval(13,Point3(0,10,0), startPos=Point3(0,-10,0))
pandaHprInterval1= panda.hprInterval(3,Point3(180,0,0), startHpr=Point3(0,0,0))
pandaHprInterval2= panda.hprInterval(3,Point3(0,0,0), startHpr=Point3(180,0,0))

#Create and play the sequence that coordinates the intervals
pandaPace = Sequence(pandaPosInterval1, pandaHprInterval1,
  pandaPosInterval2, pandaHprInterval2, name = "pandaPace")
pandaPace.loop()

#Run the tutorial
run()
