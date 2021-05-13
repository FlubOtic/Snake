import random
import pygame

class Apple():
    def __init__(self, x, y, width):
        self.color = (255, 0, 0)
        self.width = width 
        self.x = x
        self.y = y

        self.set_random_pos([1,1], 1)
    
    
    def set_random_pos(self, avoid_pos, len):
        available = False
        while not available:
            pos = [random.randint(0, self.x-1) * self.width, random.randint(0, self.y-1) * self.width]
            for i in range(len):
                if pos == avoid_pos[i]:
                    available = True
            if available:
                available = False
                continue
            else:
                available = True
        self.pos = pos
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,(self.pos[0], self.pos[1], self.width, self.width))

