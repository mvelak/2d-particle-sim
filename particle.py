import numpy as np

class Particle():
    def __init__(self, radius: float, mass: float, color: tuple, position: np.array, velocity: np.array) -> None:
        self.radius = radius
        self.mass = mass
        self.color =  color
        self.pos = position
        self.vel = velocity
    
    def change_pos(self, input: np.array) -> None:
        self.pos = input
    
    def change_vel(self, input: np.array) -> None:
        self.vel = input
    
    def particle_collision(self, other) -> None:
        up1, uv1, up2, uv2 = np.copy(self.pos), np.copy(self.vel), np.copy(other.pos), np.copy(other.vel)
        self.vel = uv1 - (((2 * other.mass) / (self.mass + other.mass)) * (np.dot(uv1 - uv2, up1 - up2) / (np.linalg.norm(up1 - up2)) ** 2) * (up1 - up2))
        other.vel = uv2 - (((2 * self.mass) / (self.mass + other.mass)) * (np.dot(uv2 - uv1, up2 - up1) / (np.linalg.norm(up2 - up1)) ** 2) * (up2 - up1))

    def wall_collision(self, input: str) -> None:
        if input == 'x':
            self.vel[0] = -self.vel[0]
        if input == 'y':
            self.vel[1] = -self.vel[1]


