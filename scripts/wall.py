"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
23/11/2024

"""

import math

from scripts.utils import *
from scripts.objloader import *


class Wall:
    def __init__(self, scale, pos):
        self.scale = scale
        self.radio = math.sqrt(self.scale * self.scale + self.scale * self.scale)
        self.position = pos.copy()
        self.collision = False
        self.model = Route("modelos", "black_cube.obj")

    def draw(self):
        obj = OBJ(*self.model, swapyz=True)

        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glScale(self.scale, self.scale, self.scale)
        obj.render()
        glPopMatrix()
