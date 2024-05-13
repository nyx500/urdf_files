import asyncio
import platform
import os

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


import pybullet as p
p.connect(p.GUI)

# configuration of the engine:
# we tell the engine not to cache files. That is important when working
# iteratively on URDF
p.setPhysicsEngineParameter(enableFileCaching=0)
# We also switch off the GUI panels by default
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)


# create floor
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)

# set gravity
p.setGravity(0, 0, -10)
