#!/usr/bin/env python
# coding=utf-8

from InstructionDecoder import InstructionDecoder
from RegisterSet import RegisterSet


class CPU(object):
    clock_frequency: float = 1
    system_clock: float = 0
    registers: RegisterSet
    decoder: InstructionDecoder

    def __init__(self, clock_frequency, registers, decoder):
        self.clock_frequency = clock_frequency
        self.system_clock = 0
        self.registers = registers
        self.decoder = decoder
        return
