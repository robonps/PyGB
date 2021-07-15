from opcodes import opcodes
from utils import hex2int as h2i
import logging
class Cpu:

    # Set the Registers
    _A=0
    _F=0
    _B=0
    _C=0
    _D=0
    _E=0
    _H=0
    _L=0

    # Stack pointer and program counter
    _SP=0
    _PC=0

    _mem=0

    # Bsic function to print the regs
    def printreg(self):
        print("A:\t{0:X}".format(self._A))
        print("F:\t{0:X}".format(self._F))
        print("B:\t{0:X}".format(self._B))
        print("C:\t{0:X}".format(self._C))
        print("D:\t{0:X}".format(self._D))
        print("E:\t{0:X}".format(self._E))
        print("H:\t{0:X}".format(self._H))
        print("L:\t{0:X}".format(self._L))
        print("SP:\t{0:X}".format(self._SP))
        print("PC:\t{0:X}".format(self._PC))


    # Functions to set and get 8 bit reg
    def _set_A(self, val):
        self._A = val
    def _set_B(self, val):
        self._B = val
    def _set_C(self, val):
        self._C = val
    def _set_D(self, val):
        self._D = val
    def _set_E(self, val):
        self._E = val
    def _set_H(self, val):
        self._H = val
    def _set_L(self, val):
        self._L = val

    def _get_A(self):
        return self._A
    def _get_B(self):
        return self._B
    def _get_C(self):
        return self._C
    def _get_D(self):
        return self._D
    def _get_E(self):
        return self._E
    def _get_H(self):
        return self._H
    def _get_L(self):
        return self._L


    # Functions to set and get 16 bit regs
    def _set_AF(self, val):
        self._A = (val >> 8) & 0b1111111100000000
        self._F = (val & 0b0000000011111111)
    def _set_BC(self, val):
        self._B = (val >> 8) & 0b1111111100000000
        self._C = (val & 0b0000000011111111)
    def _set_DE(self, val):
        self._D = (val >> 8) & 0b1111111100000000
        self._E = (val & 0b0000000011111111)
    def _set_HL(self, val):
        self._H = (val >> 8) & 0b1111111100000000
        self._L = (val & 0b0000000011111111)
    def _set_SP(self, val):
        self._SP = val
    def _set_PC(self, val):
        self._PC = val

    def _get_AF(self):
        return ((self._A << 8) | self._F)
    def _get_BC(self):
        return ((self._B << 8) | self._C)
    def _get_DE(self):
        return ((self._D << 8) | self._E)
    def _get_HL(self):
        return ((self._H << 8) | self._L)
    def _get_SP(self):
        return self._SP
    def _get_PC(self):
        return self._PC


    # Higher level functions to set and get reg
    def set_reg_8(self, reg, val):
        registers = {
            "A": self._set_A,
            "B": self._set_B,
            "C": self._set_C,
            "D": self._set_D,
            "E": self._set_E,
            "H": self._set_H,
            "L": self._set_L
        }
        registers[reg](val)

    def set_reg_16(self, reg, val):
        registers = {
            "AF": self._set_AF,
            "BC": self._set_BC,
            "DE": self._set_DE,
            "HL": self._set_HL,
            "SP": self._set_SP,
            "PC": self._set_PC
        }
        registers[reg](val)

    def get_reg_8(self, reg):
        registers = {
            "A": self._get_A,
            "B": self._get_B,
            "C": self._get_C,
            "D": self._get_D,
            "E": self._get_E,
            "H": self._get_H,
            "L": self._get_L
        }
        return registers[reg]()

    def get_reg_16(self, reg):
        registers = {
            "AF": self._get_AF,
            "BC": self._get_BC,
            "DE": self._get_DE,
            "HL": self._get_HL,
            "SP": self._get_SP,
            "PC": self._get_PC
        }
        return registers[reg]()
    
    # Flags
    def set_flag(self, flag):
        flags = {
            "Z": 0b10000000,
            "N": 0b01000000,
            "H": 0b00100000,
            "C": 0b00010000
        }

    # Instructions
    def _LD_n_nn(self, args):
        n = args[0]
        nn = args[1]
        self.set_reg_16(n, nn)
    
    def _XOR_n(self, args):
        n = args[0]
        self._set_A(self._get_A() ^ self.get_reg_8(n))


    def __init__(self, mem):
        self._mem = mem
        logging.debug("Setting")
        self.set_reg_16("AF", 0x01)
        self.set_reg_16("BC", 0x0013)
        self.set_reg_16("DE", 0x00D8)
        self.set_reg_16("HL", 0x014D)
        self.set_reg_16("SP", 0xFFFE)
        self.printreg()
        logging.debug("Default registers set")

    def execute(self):
        # Fetch inst
        instruction = self._mem.read_byte(self._get_PC())
        # Decode
        cmd = opcodes[instruction]
        # Evaluate instruction
        args = []
        if cmd.get("register", False):
            args.append(cmd["register"])

        if cmd.get("next_16", False):
            args.append(self._mem.read_16byte(self._get_PC()+1))
        elif cmd.get("next_8", False):
            args.append(self._mem.read_byte(self._get_PC()+1))
        # Execute
        eval(cmd["fn"])(args)
        # Increment PC
        self._set_PC(self._get_PC() + cmd["PC"])
        # Set Flags(if needed)
        pass