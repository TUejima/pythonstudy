# -*- coding: utf-8 -*-

import pygame
import sys
import random
import numpy as np
import datatime

OCTO_CAT_VELOCITY = 4
OCTO_CAT_JUMP = 20
COLORS = [
    [255, 0, 0],
    [255, 165, 0],
    [255, 255, 0],
    [0, 255, 0],
    [0, 255, 255],
    [0, 0, 255],
    [128, 0, 128]
]

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Jump the Rope")
heart_image = pygame.image.load("images/heart.png")
clock = pygame.time.Clock()


class Octo_Cat:
    def __init__(self, x, y):
        # player position
        self.x = x
        self.y = y
        # before_image
        self.rough_image = pygame.image.load(
            "images/greenoctocat.png").convert()
        # after_image
        self.image = pygame.transform.scale(self.rough_image, (20, 20))
        # jump_image
        self.immune_image = pygame.transform.scale(self.rough_image(30, 30))
        # move_info
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        # jump?
        self.immunity = False
        # can't jump more than a certain time
        self.immunity_count = 0
        # life
        self.life = 4
        # Invincible after shot
        self.life_lost_time = 0

    # move info
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move_right = True
            if event.key == pygame.K_LEFT:
                self.move_left = True
            if event.key == pygame.K_UP:
                self.move_up = True
            if event.key == pygame.K_DOWN:
                self.move_down = True
            if event.key == pygame.K_SPACE:
                self.immunity = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.move_right = False
            if event.key == pygame.K_LEFT:
                self.move_left = False
            if event.key == pygame.K_UP:
                self.move_up = False
            if event.key == pygame.K_DOWN:
                self.move_down = False


# defines ropes and dots
class Rope:
    def __init__(self, x=0, y=0, velocity=0, tilt=0, color=0):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.tilt = tilt
        self.color = color

    def update(self):
        return

    def judge(self, octo_cat):
        return


# vertical ropes
class Straight_Rope(Rope):
    def update(self):
        if(self.x > 635):
            self.direction = "LEFT"
        elif(self.x < 5):
            self.direction == "RIGHT"
        if(self.direction == "RIGHT"):
            self.x += self.velocity
        elif(self.direction == "LEFT"):
            self.x -= self.velocity
        pygame.draw.line(screen, COLORS[3], [self.x, 0], [self.x, 480], 5)