#!/usr/bin/env python
# coding=utf-8

from collections import namedtuple
from enum import Enum, auto

import InstructionDecoder


class Mode6502(Enum):
    none = auto()
    A = auto()  # accumulator
    imm = auto()  # immediate
    zpg = auto()  # zero page
    abs = auto()  # absolute
    ind_X = auto()  # indirect by X
    ind_Y = auto()  # indirect by Y
    X = auto()  # indexed by X register
    Y = auto()  # indexed by Y register
    rel = auto()  # relative


class MOS6502Decoder(InstructionDecoder):
    MAP: {()}

    ins = namedtuple("ins", "ins mode")
    MAP = [None] * 0x100
    MAP[0x00] = ins("BRK", Mode6502.none)
    MAP[0x01] = ins("ORA", Mode6502.X)
    MAP[0x05] = ins("ORA", Mode6502.zpg)
    MAP[0x06] = ins("ASL", Mode6502.zpg)
    MAP[0x08] = ins("PHP", Mode6502.none)
    MAP[0x09] = ins("ORA", Mode6502.imm)
    MAP[0x0a] = ins("ASLA", Mode6502.A)
    MAP[0x0d] = ins("ORA", Mode6502.abs)
    MAP[0x0e] = ins("ASL", Mode6502.abs)

    MAP[0x10] = ins("BPL", Mode6502.rel)
    MAP[0x11] = ins("ORA", Mode6502.ind_Y)

    def __init__(self):
        fred = [None] * 10
        fred[1] = 1
        self.instructions = {}
        return

    def decode(self, byte: int):
        ins = self.MAP[byte]
        return ins
