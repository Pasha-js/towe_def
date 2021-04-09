import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.imgs = []
        self.animation_count = 0
        self.health = 1
        self.path = []


    def draw(self, win):
        """
        Draws the enemy with the give images
        :param win: surface
        :return: None
        """
        
