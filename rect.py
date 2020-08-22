import pygame
import time
import random


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (self.x-(self.width/2), self.y-(self.height/2), self.width, self.height)
        self.color = (255, 64, 64)
        self.timer = time.time()
        self.enable = False
        self.clicked = False
        self.time_to_active = random.randint(100, 500)
        self.best_time = 10000

    def draw(self, win):
        if self.enable:
            pygame.draw.rect(win, self.color, self.rect, 1)

    def check_click(self, pos):
        if pygame.mouse.get_pressed()[0]:
            if self.rect[0] < pos[0] < self.rect[0] + self.rect[2]:
                if self.rect[1] < pos[1] < self.rect[1] + self.rect[3]:
                    if not self.clicked:
                        self.click()
                        self.clicked = True
                    return True
                self.clicked = False
                return False
            self.clicked = False
            return False
        self.clicked = False
        return False

    def update(self, win, pos):
        if self.enable:
            self.color = (64, 255, 64)
        else:
            self.color = (255, 64, 64)

        # print(self.time_to_active)
        self.time_to_active -= 1
        if self.time_to_active < 0:
            if not self.enable:
                self.enable = True
                self.timer = time.time()
            # print("enable")
        self.check_click(pos)
        self.draw(win)

    def change_color(self, color):
        self.color = color

    def click(self):
        if self.enable:
            self.enable = False
            self.time_to_active = random.randint(100, 1000)
            print(round((time.time() - self.timer)*1000), " | Best: ", self.best_time)
            if self.best_time > round((time.time() - self.timer)*1000):
                self.best_time = round((time.time() - self.timer)*1000)
            self.new_position()

    def new_position(self):
        self.x = random.randint(50, 450)
        self.y = random.randint(50, 450)
        self.rect = (self.x-(self.width/2), self.y-(self.height/2), self.width, self.height)
