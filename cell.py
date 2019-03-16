#
# cell class definition
#

import math as m
import scipy as sc

class cell_class:
    def __init__(self, name, number, conn_a, conn_T, conn_B):
        self.name = name
        self.number = number
        self.a = conn_a  # pipe connection to acinus parent object
        self.T = conn_T
        self.B = conn_B
        self.p1 = 1.0
        self.run()

    def solve(self, delta_t):
        if self.number == 0: self.B.send(self.name)
        if self.number == 1: self.T.send(self.name)        
        for i in range(10000000):
            k = m.log(i+1)
            l = m.sin(i)
            l = m.cos(i)
        self.a.send([self.name, 1.0])
        if self.number == 0: print(self.name, self.B.recv())
        if self.number == 1: print(self.name, self.T.recv())
        
    def run(self):  # simulation run loop
        step = 0
        while(True):
            print(self.name, "step", step)
            delta_t = self.a.recv()
            if delta_t == 0:
                break
            self.solve(delta_t)
            step += 1
    