"""
ERIKA AMASTAL XOCHIMITL
GRAFICACION
23/11/2024

"""

import math


class Collisions:
    def detect(self, main_obj, objs):
        for obj in objs:
            d_x = main_obj.position[0] - objs.position[0]
            d_y = main_obj.position[1] - objs.position[1]
            d_c = math.sqrt(d_x * d_x + d_y * d_y)
            if d_c - (main_obj.radio + obj.radio) < 0.0:
                self.collision = True
