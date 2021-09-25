import pygame as pg


class BaseShape:
    def __init__(self, relative_pos: pg.math.Vector2 = pg.math.Vector2(0, 0)):
        self.relative_pos = relative_pos
        self.body = None

    def get_absolute_pos(self):
        return self.relative_pos + self.body.get_position()

    def collide_reflect_velocity(self, shape, velocity):
        pass

    def collide_with(self, shape, velocity):
        pass


class PlaneShape(BaseShape):
    def __init__(self, normal: pg.math.Vector2, relative_pos: pg.math.Vector2 = pg.math.Vector2(0, 0)):
        super().__init__(relative_pos)
        self.normal = normal

    def collide_width(self, shape, velocity):
        pass


class CircleShape(BaseShape):
    def __init__(self, radius, relative_pos: pg.math.Vector2 = pg.math.Vector2(0, 0)):
        super().__init__(relative_pos)
        self.radius = radius

    def collide_reflect_velocity(self, shape, velocity):
        if isinstance(shape, CircleShape):
            pass
        if isinstance(shape, PlaneShape):
            return shape.normal * (velocity * shape.normal) * (-2)

    def collide_with(self, shape, velocity):
        if isinstance(shape, CircleShape):
            pass
        elif isinstance(shape, PlaneShape):
            dc = (-1) * self.get_absolute_pos() * shape.normal
            d = (-1) * shape.get_absolute_pos() * shape.normal
            if abs(d - dc) < self.radius:
                if shape.normal * velocity > 0:
                    return True, False
                else:
                    return True, True
            else:
                return False, False

