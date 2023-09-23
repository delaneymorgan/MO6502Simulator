#!/usr/bin/env python
# coding=utf-8

from Base.Instruction import Instruction
from MOS6502AddressingMode import MOS6502AddressingMode
from MOS6502RegisterSet import StatusBits, MOS6502RegisterSet


class MOS6502Instruction(Instruction):
    mode: MOS6502AddressingMode

    def __init__(self, mnemonic, mode, bytes, cycles, action):
        super().__init__(mnemonic, cycles, action)
        self.mode = mode
        return

    @staticmethod
    def _operand8(registers, memory):
        operand = memory.get(registers.PC)
        return operand

    @staticmethod
    def _operand16(registers, memory):
        operand = (memory.get(registers.PC) << 8) | memory.get(registers.PC + 1)
        return operand

    @staticmethod
    def _set_status(status, value):
        return

    @staticmethod
    def BRK(registers, memory, ram, rom):
        ram.set(0x0100 | registers.SP, registers.PC + 2)
        registers.SP -= 2
        status = registers.S.set_bit(StatusBits.I)
        ram.set(0x0100 | registers.SP, status)
        registers.SP -= 1
        return

    @staticmethod
    def ORA_imm(registers, memory, ram, rom):
        registers.A.value |= MOS6502Instruction._operand8(registers, memory)
        registers.set_status(registers.A.value)
        registers.PC += 2
        return

    @staticmethod
    def ORA_zpg(registers, ram, rom):
        return

    def execute(self, registers, ram, rom):
        if self.action is not None:
            self.action(registers, ram, rom)
        return
