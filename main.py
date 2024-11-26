"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
12/11/2024

"""

import pygame
from pygame.locals import *

# Load OpenGL libraries
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np

# Import obj loader
from scripts.objloader import *

# from shaders.shader import *
from scripts.player import Player
from scripts.camera import Camera
from scripts.utils import *
from scripts.wall import *
from scripts.enemy import *

# Screen size
screen_width = 800
screen_height = 600

# Dimension del plano
DimBoard = 800

# Player settings

player_pos = np.array([0.0, 0.0, 5.0])
player_jump_speed = 5.0
player_speed = 5.0
player_scale = 10.0

player = Player(player_pos, player_speed, player_jump_speed)

# Scenario settings

conos = [[80, 0.0, 0.0], [90, 0, 0], [100, 0, 0]]
cono_scale = 10.0

cubes = [[80, 5.0, 0.0], [90, 5, 0], [100, 5, 0]]
cube_scale = 10.0

# Camera
camera = Camera()

pygame.init()


def Init():
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Geometry Dash 3D")

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(
        camera.get_fov_y(),
        (screen_width / screen_height),
        camera.get_znear(),
        camera.get_zfar(),
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        camera.get_eye_x(),
        camera.get_eye_y(),
        camera.get_eye_z(),
        camera.get_center_x(),
        camera.get_center_y(),
        camera.get_center_z(),
        camera.get_up_x(),
        camera.get_up_y(),
        camera.get_up_z(),
    )
    glTranslatef(
        camera.get_position_x(), camera.get_position_y(), camera.get_position_z()
    )
    glClearColor(*RGB(58, 88, 256), 1.0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 200, 0, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)  # most obj files expect to be smooth-shaded


# Dibuja el escenario
def dibujar_escenario():
    global conos, cono_scale, cubes, cube_scale
    for cono in conos:
        Enemy(cono_scale, cono, Route("modelos", "Cono_negro.obj")).draw()

    for cube in cubes:
        Wall(cube_scale, cube).draw()


def render_floor():
    glColor3f(*RGB(51, 82, 246))
    glBegin(GL_QUADS)
    glVertex3d(-DimBoard, 0, -DimBoard)
    glVertex3d(-DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, DimBoard)
    glVertex3d(DimBoard, 0, -DimBoard)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)


done = False
Init()

while not done:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Axis().draw()

    dibujar_escenario()
    render_floor()
    player.draw()
    player.update(keys)
    camera.follow_player(player_pos)

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
