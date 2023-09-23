#!/usr/bin/env python
# coding=utf-8

from collections import namedtuple

from Base import InstructionDecoder
from MOS6502Instruction import MOS6502Instruction
from MOS6502AddressingMode import MOS6502AddressingMode


class MOS6502Decoder(InstructionDecoder):
    MAP: {()}

    ins = namedtuple("ins", "ins mode")
    MAP = [None] * 0x100
    MAP[0x00] = MOS6502Instruction("BRK", MOS6502AddressingMode.none, 7, MOS6502Instruction.BRK)
    MAP[0x01] = MOS6502Instruction("ORA", MOS6502AddressingMode.ind_x, 4, MOS6502Instruction.ORA_ind_x)
    MAP[0x05] = MOS6502Instruction("ORA", MOS6502AddressingMode.zpg, 1, MOS6502Instruction.ORA_zpg)
    MAP[0x06] = MOS6502Instruction("ASL", MOS6502AddressingMode.zpg, 5, MOS6502Instruction.ASL_zpg)
    MAP[0x08] = MOS6502Instruction("PHP", MOS6502AddressingMode.none, 3, MOS6502Instruction.PHP)
    MAP[0x09] = MOS6502Instruction("ORA", MOS6502AddressingMode.imm, 2, MOS6502Instruction.ORA_imm)
    MAP[0x0a] = MOS6502Instruction("ASLA", MOS6502AddressingMode.a, 2, MOS6502Instruction.ASL_a)
    MAP[0x0d] = MOS6502Instruction("ORA", MOS6502AddressingMode.abs, 4, MOS6502Instruction.ORA_abs)
    MAP[0x0e] = MOS6502Instruction("ASL", MOS6502AddressingMode.abs, 6, MOS6502Instruction.ASL_abs)

    MAP[0x10] = MOS6502Instruction("BPL", MOS6502AddressingMode.rel, 2, MOS6502Instruction.BPL_rel)
    MAP[0x11] = MOS6502Instruction("ORA", MOS6502AddressingMode.ind_y, 5, MOS6502Instruction.ORA_ind_y)
    MAP[0x15] = MOS6502Instruction("ORA", MOS6502AddressingMode.zpg_x, 5, MOS6502Instruction.ORA_zpg_x)
    MAP[0x16] = MOS6502Instruction("ASL", MOS6502AddressingMode.zpg_x, 5, MOS6502Instruction.ASL_zpg_x)
    MAP[0x18] = MOS6502Instruction("CLC", MOS6502AddressingMode.none, 5, MOS6502Instruction.CLC)
    MAP[0x19] = MOS6502Instruction("ORA", MOS6502AddressingMode.abs_y, 5, MOS6502Instruction.ORA_abs_y)
    MAP[0x1d] = MOS6502Instruction("ORA", MOS6502AddressingMode.abs_x, 5, MOS6502Instruction.ORA_abs_x)
    MAP[0x1e] = MOS6502Instruction("ASL", MOS6502AddressingMode.abs_x, 5, MOS6502Instruction.ASL_abs_x)

    def __init__(self):
        return

    def decode(self, byte: int):
        ins = self.MAP[byte]
        return ins

    def execute(self, code, registers, ram, rom):
        if self.MAP[code] is not None:
            self.MAP[code].execute(registers, ram, rom)
