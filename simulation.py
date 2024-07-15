import pygame

class Simulation():
    def __init__(self):
        pygame.init()
        self.running, self.simming, self.pausing = True, False, False     
        self.winW, self.winH = 800, 800     # Width and height of the screen
        self.screen = pygame.display.set_mode([self.winW, self.winH])
        self.clock = pygame.time.Clock()
        self.frame_rate = 1000
        self.dt = 1 / self.frame_rate
        self.font = pygame.font.get_default_font()
        self.objs = []
        self.obj_count = 0
    
    '''THIS IS WHAT HAPPENS OVER THE ENTIRETY OF THE PROGRAM INCLUDING WHEN WE ARE NOT SIMMING'''
    def run(self):
        self.get_input()
        self.check_collisions()
        self.check_positions()
        self.screen.fill((0, 0, 0))
        for obj in self.objs:   # obj is a Particle class instance
            pygame.draw.circle(self.screen, obj.color, obj.pos, obj.radius)
        pygame.display.flip()
        self.clock.tick(self.frame_rate) # Limit frame rate
    
    '''THIS IS WHAT HAPPENS WHEN WE PRESS START SIM'''
    def sim():
        pass
    
    def pause():
        pass

    def check_collisions(self):
        for obj in self.objs:
            '''OPTIMIZE THIS IF STATEMENT'''
            if (obj.pos[0] - obj.radius <= 0) or (obj.pos[0] + obj.radius >= self.winW) :
                obj.wall_collision('x')
            if (obj.pos[1] - obj.radius <= 0) or (obj.pos[1] + obj.radius >= self.winW):
                obj.wall_collision('y')
            
    
    def check_positions(self):
        for obj in self.objs:
            obj.pos = obj.pos + (obj.vel * self.dt)

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.simming, self.pausing = False, False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused 
        
    def add_obj(self, object):   
        self.obj_count += 1
        self.objs.append(object)
