#
# cell class definition
#

import math as m
import scipy as sc

class cell_class:
    def __init__(self, name, conn_a):
        self.name = name
        self.a = conn_a  # pipe connection to acinus parent object
        self.p1 = 1.0
        self.run()

    def solve(self, delta_t):
        for i in range(10000000):
            k = m.log(i+1)
            l = m.sin(i)
            l = m.cos(i)
        self.a.send([self.name, 1.0])
        
    def run(self):  # simulation run loop
        step = 0
        while(True):
            print(self.name, "step", step)
            delta_t = self.a.recv()
            if delta_t == 0:
                break
            self.solve(delta_t)
            step += 1
    