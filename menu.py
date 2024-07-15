import pygame
class Menu:
    def __init__(self) -> None:
        pas
 

class Slider:
    def __init__(self, position: tuple, size: tuple, val: float, min: int, max: int) -> None:
        self.position = position  #tuple of form (left, top)
        self.size = size   #tuple of form (width, height)
        self.val = val
        self.min = min
        self.max = max
        self.container = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        self.button = pygame.Rect(self.position[0] + (self.size[0] // 2) - self.size[0] // 20, self.position[1], self.size[0] // 10, self.size[1])
    
class Checkbox:
    def __init__(self):
        self.state = False
    
    def get_input(self, input) -> None:
        self.state = not self.state