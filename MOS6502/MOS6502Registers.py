#!/usr/bin/env python
# coding=utf-8

from Register import Register
import RegisterSet

class MOS6502Registers(RegisterSet):
    def __init__(self):
        self.A = Register(8)
        self.X = Register(8)
        self.Y = Register(8)
        self.S = Register(8)
        self.SP = Register(8)
        self.PC = Register(16)
        return