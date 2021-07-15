import logging
from utils import hex2int as h2i
from memory import Memory
from cpu import Cpu

mem = Memory()
def init():
    logging.basicConfig(level=logging.DEBUG)

    with open("bios.gb", mode="rb") as file:
        boot = file.read()
    mem.load(boot, h2i("0000"))
init()
cpu = Cpu(mem)
def mainloop():
    for i in range(2):
        cpu.printreg()
        logging.debug("------------")
        cpu.execute()
        cpu.printreg()
        logging.debug("Next Instruction")

mainloop()