from simulation import Simulation
from particle import Particle
import numpy as np

sim = Simulation()
q = Particle(15, 20, (100, 0, 100), np.array([400, 400]), np.array([-570, 300]))
sim.add_obj(q)
while sim.running:
    sim.run()