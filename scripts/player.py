"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
22/11/2024

"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import pygame

from scripts.objloader import *
from scripts.utils import *


class Player:
    def __init__(self, pos, s, jump_speed):
        # Controllers
        self.current_jump = 0.0
        self.speed = s
        self.jump_speed = jump_speed
        self.jump_height = 30.0
        self.is_falling = False
        self.is_jumping = False

        # Player movement coords
        self.position = pos
        self.scale = 10.0
        self.radio = math.sqrt(self.scale * self.scale + self.scale * self.scale)

        # Rotation control
        self.rotation = 0.0
        self.rotation_speed = 30.0  # Degrees per frame
        self.falling_rotation = 0.0

        # Model
        self.model = Route("modelos", "Cubo_amarillo.obj")

    def update(self, keys):
        # Constant movement in X
        self.position[0] += self.speed

        # Jump handling
        if not self.is_jumping and not self.is_falling and keys[pygame.K_UP]:
            self.is_jumping = True
            self.rotation = 0.0  # Reset rotation at start of jump

        if self.is_jumping:
            self.position[2] += self.jump_speed
            self.current_jump += self.jump_speed
            # Rotate while jumping
            self.rotation += self.rotation_speed

            if self.current_jump >= self.jump_height:
                self.is_jumping = False
                self.is_falling = True
                self.falling_rotation = 0.0  # Reset falling rotation

        if self.is_falling:
            self.position[2] -= self.jump_speed
            # Rotate while falling
            self.falling_rotation += self.rotation_speed

            if self.position[2] <= 5.0:
                self.position[2] = 5.0
                self.is_jumping = False
                self.is_falling = False
                self.current_jump = 0.0
                self.rotation = 0.0  # Reset rotation when landed
                self.falling_rotation = 0.0

    def draw(self):
        obj = OBJ(*self.model, swapyz=True)
        glPushMatrix()
        glRotatef(-90.0, 1.0, 0.0, 0.0)  # Base rotation
        glTranslatef(self.position[0], self.position[1], self.position[2])
        # Apply jump rotation
        if self.is_jumping:
            glRotatef(
                self.rotation, 0.0, 1.0, 0.0
            )  # Rotate around Z axis while jumping

        # Apply falling rotation
        if self.is_falling:
            glRotatef(
                self.falling_rotation, 0.0, -1.0, 0.0
            )  # Rotate opposite direction while falling

        glScale(self.scale, self.scale, self.scale)
        obj.render()
        glPopMatrix()
