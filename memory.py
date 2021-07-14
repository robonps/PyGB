import logging
from utils import hex2int as h2i

class Memory:
    memory = bytearray(65536)

    def __init__(self):
        for i in range(len(self.memory)):
            self.memory[i] = 0

    def load(self, data, offset):
        logging.debug("Loading data to memory starting at {}".format(offset))
        for i in range(len(data)):
            self.memory[int(i+offset)] = data[i]

    def read_byte(self, addr):
        return self.memory[addr]

    def read_16byte(self, addr):
        return (self.memory[addr] | (self.memory[addr+1] << 8))
    
    def printmem(self, start="0000", end="FFFF", mode="hex"):
        if mode == "hex":
            for i in range(h2i(start), h2i(end)-1):
                print("{0:X}:\t{1:02X}\t{2:02X}".format(i, self.memory[i], self.memory[i+1]))