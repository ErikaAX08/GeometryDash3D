"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
22/11/2024

"""

import os

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Route:
    def __init__(self, folder, name):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.full_path = os.path.join("./", folder, name)

    def __iter__(self):
        return iter([self.full_path])


class RGB:
    def __init__(self, r, g, b):
        self.r = r / 255.0
        self.g = g / 255.0
        self.b = b / 255.0

    def __iter__(self):
        return iter((self.r, self.g, self.b))


class Axis:
    def __init__(self):
        self.X_MIN = -500
        self.X_MAX = 500
        self.Y_MIN = -500
        self.Y_MAX = 500
        self.Z_MIN = -500
        self.Z_MAX = 500

    def draw(self):
        glShadeModel(GL_FLAT)
        glLineWidth(3.0)
        # X axis in red
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(self.X_MIN, 0.0, 0.0)
        glVertex3f(self.X_MAX, 0.0, 0.0)
        glEnd()
        # Y axis in green
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_LINES)
        glVertex3f(0.0, self.Y_MIN, 0.0)
        glVertex3f(0.0, self.Y_MAX, 0.0)
        glEnd()
        # Z axis in blue
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_LINES)
        glVertex3f(0.0, 0.0, self.Z_MIN)
        glVertex3f(0.0, 0.0, self.Z_MAX)
        glEnd()
        glLineWidth(1.0)
