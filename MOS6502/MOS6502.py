#!/usr/bin/env python
# coding=utf-8

from Base.CPU import CPU
from MOS6502Decoder import MOS6502Decoder
from MOS6502RegisterSet import MOS6502RegisterSet


class MOS6502(CPU):
    def __init__(self, clock_frequency: float):
        registers = MOS6502RegisterSet()
        decoder = MOS6502Decoder()
        super().__init__(clock_frequency, registers, decoder)
        return
