#
# cell class definition
#

import numpy as np

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
        x = np.arange(start=0.1, stop=100000.0, step=0.01, dtype="double")
        k = np.log(x)
        l = np.sin(x)
        m = np.cos(x)
        self.a.send([self.name, 1.0])
        if self.number == 0: print("<cell>", self.name, self.B.recv())
        if self.number == 1: print("<cell>", self.name, self.T.recv())
        
    def run(self):  # simulation run loop
        step = 0
        while(True):
            delta_t = self.a.recv()
            if delta_t == 0:
                break
            print("<cell>", self.name, "step", step)
            self.solve(delta_t)
            step += 1
    