#!/usr/bin/env python
# coding=utf-8

from enum import Enum

from Base import RegisterSet
from Base.BitRegister import BitRegister
from Base.Register import Register


class StatusBits(Enum):
    C = 0
    Z = 1
    I = 2
    D = 3
    B = 4
    V = 6
    N = 7


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
        self.S = BitRegister(8)
        self.SP = Register(8)
        self.PC = Register(16)
        return

    def set_status(self, value):
        if value == 0:
            self.S.set_bit(StatusBits.Z)
        if value < 0:
            self.S.set_bit(StatusBits.N)
        else:
            self.S.clear_bit(StatusBits.N)
        return
