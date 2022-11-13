from DAH import MCP23S17

mcp= MCP23S17(chip=0, address= 0x20)

while True:
    print(mcp.portRead())