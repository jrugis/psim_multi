#
# main simulation file
#

import time 
from multiprocessing import Process, Pipe

import cell  # defines the cell class
T = 0  # index for top of pipe (the acinus end)
B = 1  #          bottom       (the cell end)

# execution timer
start = time.time()

# initialise the cell processes and pipes
cell_names = ["a1c1", "a1c2", "a1c3", "a1c4"] 
cells = []
cell_pipes = []
for name in cell_names:
    cell_pipes.append(Pipe())
    cells.append(Process(target = cell.cell_class, args = (name, cell_pipes[-1][B])))

# simulation time stepping
for step in range(3):  
    for p in cell_pipes: p[T].send(1)  # send delta_t message to cell
    if step == 0:  # only once per cell
        for c in cells: c.start()
    for p in cell_pipes:
        print("a1", step, "result", p[T].recv())  # receive result message from cell 

# send "done" message to cell processes
for p in cell_pipes: p[T].send(0)     

# wait for cell processes to close
for c in cells: c.join()

# execution timer
end = time.time()
print(end - start)

