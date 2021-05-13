import pygame, random
from pygame.rect import Rect


class Snake():
    def __init__(self, x, y, width, dir):
        self.moved = False
        self.length = 3
        self.width = width
        self.color = (0, 255, 0)
        self.dir = (1, 0)
        self.pos = [[x, y], [x-self.width, y], [x-(self.width*2), y]]


    def draw(self, screen):
        for i in range(self.length):
            pygame.draw.rect(screen, self.color,(self.pos[self.length - 1 - i][0], self.pos[self.length - 1 - i][1], self.width, self.width))


    def move(self, screen):
        prev_move = [self.pos[0][0], self.pos[0][1]]
        self.pos[0][0] += self.dir[0] * self.width
        self.pos[0][1] += self.dir[1] * self.width
        self.moved = True

        if not 0 - self.width < self.pos[0][0] < screen.get_width() or not 0 - self.width < self.pos[0][1] < screen.get_height():
            return True

        for i in range(self.length):
            if self.pos[self.length - 1 - i] != self.pos[1]:
                if self.pos[self.length - 1 - i] != self.pos[0]:
                    self.pos[self.length - 1 - i] = self.pos[self.length - 2 - i]
            else:
                if self.pos[0] != self.pos[1]:
                    self.pos[1] = prev_move
                else:
                    return True
            if self.length - 1 - i != 0 and self.pos[0] == self.pos[self.length - 1 - i]:
                return True
        return False


    def turn(self, dir):
        if self.dir != (-dir[0], -dir[1]) and self.moved:
            self.dir = dir
            self.moved = False


    def eat(self):
        self.pos += [[self.pos[self.length - 1][0] - self.dir[0] * self.width, self.pos[self.length - 1][1] - self.dir[1] * self.width]]
        self.length += 1