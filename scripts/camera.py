"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
22/11/2024

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np


class Camera:
    def __init__(self):
        self._znear = 0.01
        self._zfar = 900
        self._fov_y = 60

        self._eye = np.array([0.0, 60, 150])
        self._center = np.array([0.0, 0.0, 0.0])
        self._up = np.array([0.0, 1.0, 0.0])
        self._position = np.array([0.0, 0.0, 0.0])
        self._offset = self._offset = np.array([10.0, 0.0, 0.0])

    def follow_player(self, player_pos):
        # Follow player in X
        if player_pos[0] != 0.0:
            self._position[0] = (player_pos[0] + self._offset[0]) * (-1)
            self.update_camera()

    def update_camera(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(
            self._eye[0],
            self._eye[1],
            self._eye[2],
            self._center[0],
            self._center[1],
            self._center[2],
            self._up[0],
            self._up[1],
            self._up[2],
        )

        glTranslatef(self._position[0], self._position[1], self._position[2])

    # Getters for other attributes
    def get_znear(self):
        return self._znear

    def get_zfar(self):
        return self._zfar

    def get_fov_y(self):
        return self._fov_y

    # Getter for position
    def get_position_x(self):
        return self._position[0]

    def get_position_y(self):
        return self._position[1]

    def get_position_z(self):
        return self._position[2]

    # Getters for eyes
    def get_eye_x(self):
        return self._eye[0]

    def get_eye_y(self):
        return self._eye[1]

    def get_eye_z(self):
        return self._eye[2]

    # Getters for centers
    def get_center_x(self):
        return self._center[0]

    def get_center_y(self):
        return self._center[1]

    def get_center_z(self):
        return self._center[2]

    # Getters for up
    def get_up_x(self):
        return self._up[0]

    def get_up_y(self):
        return self._up[1]

    def get_up_z(self):
        return self._up[2]
