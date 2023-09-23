#!/usr/bin/env python
# coding=utf-8

import RegisterSet
from BitRegister import BitRegister
from Register import Register


class MOS6502RegisterSet(RegisterSet):
    A: Register
    X: Register
    Y: Register
    S: BitRegister
    SP: Register
    PC: Register

    def __init__(self):
        self.A = Register(8)
        self.X = Register(8)
        self.Y = Register(8)
        bit_map = dict(N=7, V=6, B=4, D=3, I=2, Z=1, C=0)
        self.S = BitRegister(8, bit_map)
        self.SP = Register(8)
        self.PC = Register(16)
        return
