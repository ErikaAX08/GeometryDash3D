"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
24/11/2024

"""

import math

from scripts.utils import *
from scripts.objloader import *


class Enemy:
    def __init__(self, scale, pos, model):
        self.scale = scale
        self.radio = math.sqrt(self.scale * self.scale + self.scale * self.scale)
        self.position = pos.copy()
        self.collision = False
        self.model = model

    def draw(self):
        obj = OBJ(*self.model, swapyz=True)

        glPushMatrix()
        glRotatef(-90.0, 1.0, 0.0, 0.0)
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glScale(self.scale, self.scale, self.scale)
        obj.render()
        glPopMatrix()
