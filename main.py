import logging
from utils import hex2int as h2i
from memory import Memory

def init():
    logging.basicConfig(level=logging.DEBUG)

    mem = Memory()

    with open("bios.gb", mode="rb") as file:
        boot = file.read()
    mem.load(boot, h2i("0000"))
    mem.printmem(end="100")
init()