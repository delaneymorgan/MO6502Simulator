#!/usr/bin/env python
# coding=utf-8

from enum import Enum, unique

from Base.Instruction import Instruction
from MOS6502AddressingMode import MOS6502AddressingMode
from MOS6502RegisterSet import StatusBits


@unique
class MOS6502Mnemonic(Enum):
    ADC = "Add Memory to Accumulator with Carry"
    AND = "AND Memory with Accumulator"
    ASL = "Shift Left One Bit (Memory or Accumulator)"
    BCC = "Branch on Carry Clear"
    BCS = "Branch on Carry Set"
    BEQ = "Branch on Result Zero"
    BIT = "Test Bits in Memory with Accumulator"
    BMI = "Branch on Result Minus"
    BNE = "Branch on Result not Zero"
    BPL = "Branch on Result Plus"
    BRK = "Force Break"
    BVC = "Branch on Overflow Clear"
    BVS = "Branch on Overflow Set"
    CLC = "Clear Carry Flag"
    CLD = "Clear Decimal Mode"
    CLI = "Clear Interrupt Disable Bit"
    CLV = "Clear Overflow Flag"
    CMP = "Compare Memory with Accumulator"
    CPX = "Compare Memory and Index X"
    CPY = "Compare Memory and Index Y"
    DEC = "Decrement Memory by One"
    DEX = "Decrement Index X by One"
    DEY = "Decrement Index Y by One"
    EOR = "Exclusive-OR Memory with Accumulator"
    INC = "Increment Memory by One"
    INX = "Increment Index X by One"
    INY = "Increment Index Y by One"
    JMP = "Jump to New Location"
    JSR = "Jump to New Location Saving Return Address"
    LDA = "Load Accumulator with Memory"
    LDX = "Load Index X with Memory"
    LDY = "Load Index Y with Memory"
    LSR = "Shift One Bit Right (Memory or Accumulator)"
    NOP = "No Operation"
    ORA = "OR Memory with Accumulator"
    PHA = "Push Accumulator on Stack"
    PHP = "Push Processor Status on Stack"
    PLA = "Pull Accumulator from Stack"
    PLP = "Pull Processor Status from Stack"
    ROL = "Rotate One Bit Left (Memory or Accumulator)"
    ROR = "Rotate One Bit Right (Memory or Accumulator)"
    RTI = "Return from Interrupt"
    RTS = "Return from Subroutine"
    SBC = "Subtract Memory from Accumulator with Borrow"
    SEC = "Set Carry Flag"
    SED = "Set Decimal Flag"
    SEI = "Set Interrupt Disable Status"
    STA = "Store Accumulator in Memory"
    STX = "Store Index X in Memory"
    STY = "Store Index Y in Memory"
    TAX = "Transfer Accumulator to Index X"
    TAY = "Transfer Accumulator to Index Y"
    TSX = "Transfer Stack Pointer to Index X"
    TXA = "Transfer Index X to Accumulator"
    TXS = "Transfer Index X to Stack Register"
    TYA = "Transfer Index Y to Accumulator"


class MOS6502Instruction(Instruction):
    mode: MOS6502AddressingMode

    def __init__(self, mnemonic, mode, num_bytes, cycles, action):
        super().__init__(mnemonic, num_bytes, cycles, action)
        self.mode = mode
        return

    @staticmethod
    def _operand8(registers, memory_map):
        operand = memory_map.get(registers.PC)
        return operand

    @staticmethod
    def _operand16(registers, memory_map):
        operand = (memory_map.get(registers.PC) << 8) | memory_map.get(registers.PC + 1)
        return operand

    @staticmethod
    def _set_status(status, value):
        return

    @staticmethod
    def brk(registers, memory_map):
        memory_map.set(0x0100 | registers.SP, registers.PC + 2)
        registers.SP -= 2
        status = registers.S.set_bit(StatusBits.I)
        memory_map.set(0x0100 | registers.SP, status)
        registers.SP -= 1
        return

    @staticmethod
    def ora_imm(registers, memory_map):
        registers.A.value |= MOS6502Instruction._operand8(registers, memory_map)
        registers.set_status(registers.A.value)
        registers.PC += 2
        return

    @staticmethod
    def ora_zpg(registers, memory_map):
        return

    def execute(self, registers, memory_map):
        if self.action is not None:
            self.action(registers, memory_map)
        return
