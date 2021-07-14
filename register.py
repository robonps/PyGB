class Register:

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


    # Bsic function to print the regs
    def printreg(self):
        print("A:\t{0:X}".format(self._A))
        print("B:\t{0:X}".format(self._B))
        print("C:\t{0:X}".format(self._C))
        print("D:\t{0:X}".format(self._D))
        print("E:\t{0:X}".format(self._E))
        print("H:\t{0:X}".format(self._H))
        print("L:\t{0:X}".format(self._L))


    # Functions to set 8 bit reg
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


    # Functions to set 16 bit regs

    def _set_AF(self, val):
        self._A = val & 0b0000000011111111
        self._F = (val & 0b1111111100000000) >> 8
    
    def _set_BC(self, val):
        self._B = val & 0b0000000011111111
        self._C = (val & 0b1111111100000000) >> 8

    def _set_DE(self, val):
        self._D = val & 0b0000000011111111
        self._E = (val & 0b1111111100000000) >> 8

    def _set_HL(self, val):
        self._H = val & 0b0000000011111111
        self._L = (val & 0b1111111100000000) >> 8

    def _set_SP(self, val):
        self.SP = val
    
    def _set_PC(self, val):
        self.PC = val


    # Higher level functions to set reg
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

    def _set_16(self, reg, val):
        registers = {
            "AF": self._set_AF,
            "BC": self._set_BC,
            "DE": self._set_DE,
            "HL": self._set_HL,
            "SP": self._set_SP,
            "PC": self._set_PC
        }
        registers[reg](val)

    def __init__(self):
        pass