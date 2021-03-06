import pygame as pg

from src.surface.base_surface import BaseSurface
from src.surface.surfaces import FieldSurface
from src.surface.surfaces import TextSurface
from src.common.config import SCREEN_WIDTH
from src.common.config import SCREEN_HEIGHT


class BaseSprite(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.surface: BaseSurface = None
        self.priority = 0

    def set_rotation(self, rotation):
        self.surface.rotate(rotation)

    def get_image(self):
        return self.surface.get_surface()

    def get_rect(self):
        pass

    def update(self, now):
        self.surface.update(now)

    # passing get_image and get_rect alone doesn't work with inheritance
    image = property(fget=lambda self: self.get_image())
    rect = property(fget=lambda self: self.get_rect())


class Field(BaseSprite):
    def __init__(self, game):
        super().__init__(game)
        self.surface = FieldSurface()

    def get_rect(self):
        return self.surface.get_surface().get_rect(topleft=(0, 0))


class CountDownText(BaseSprite):
    def __init__(self, game, count_to):
        super().__init__(game)
        self.surface = TextSurface()
        self.current = count_to
        self.prev = None
        self.surface.set_text(str(self.current))

    def update(self, now):
        if self.prev is None:
            self.prev = now
            return

        if (now - self.prev) > 1000:
            self.current = self.current - 1
            self.surface.set_text(str(self.current))
            if self.current == 0:
                self.game.done = True
            self.prev = now

    def get_rect(self):
        return self.surface.get_surface().get_rect(midtop=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


class Score(BaseSprite):
    def __init__(self, game):
        super().__init__(game)
        self.team0 = 0
        self.team1 = 0
        self.surface = TextSurface()
        self.surface.set_text("Score: " + str(self.team0) + " | " + str(self.team1))

    def update_score(self, team0=None, team1=None):
        if team0 is not None:
            self.team0 = team0
        if team1 is not None:
            self.team1 = team1
        self.surface.set_text("Score: " + str(self.team0) + " | " + str(self.team1))

    def get_rect(self):
        return self.surface.get_surface().get_rect(midtop=(SCREEN_WIDTH/2, 100))
