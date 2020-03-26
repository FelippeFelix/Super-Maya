import pygame
import entity

class Block(entity.Entity):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)