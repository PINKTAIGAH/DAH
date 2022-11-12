from DAH import MCP23S17
import numpy as np
import time

mcp= MCP23S17(chip= 0, address= 0x20)
buttons= np.array(['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'], dtype= "str")

def buttons_pressed(port_state):
    index= []
    for i, _ in enumerate(port_state):
        
        if port_state[i]== 0:
            index.append(i)
    return(index)
    
while True:
    port_state= bin(mcp.portRead())
    port_state= [int(x) for x in str(port_state[2:])]
    port_state= port_state[::-1]
    down_state= buttons_pressed(port_state[:-2])
    print(down_state)


    
    
