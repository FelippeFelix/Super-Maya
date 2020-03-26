import entity
import pygame

class Coin(entity.Entity):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

        self.value = 1