from DAH import MCP23S17

mcp= MCP23S17(chip= 0, address= 0x20)
B0, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10= 0,1,2,3,4,5,6,7,8,9,10

while True:
    if mcp.digitalRead(B0)== False:
        print(0)
    elif mcp.digitalRead(B1)== False:
        print(1)
    elif mcp.digitalRead(B2)== False:
        print(2)
    elif mcp.digitalRead(B3)== False:
        print(3)
    elif mcp.digitalRead(B4)== False:
        print(4)
    elif mcp.digitalRead(B5)== False:
        print(5)
    elif mcp.digitalRead(B6)== False:
        print(6)
    elif mcp.digitalRead(B7)== False:
        print(7)
    elif mcp.digitalRead(B8)== False:
        print(8)
    elif mcp.digitalRead(B9)== False:
        print(9)
    elif mcp.digitalRead(B10)== False:
        print(10)
    else:
        print('off')
