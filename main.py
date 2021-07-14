import logging
from utils import hex2int as h2i
from memory import Memory
from cpu import Cpu

def init():
    logging.basicConfig(level=logging.DEBUG)

    mem = Memory()

    with open("bios.gb", mode="rb") as file:
        boot = file.read()
    mem.load(boot, h2i("0000"))
init()
cpu = Cpu()
def mainloop():
    for i in range(1):
        cpu.printreg()
        cpu.execute()
        cpu.printreg()

mainloop()