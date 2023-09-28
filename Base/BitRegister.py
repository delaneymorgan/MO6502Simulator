#!/usr/bin/env python
# coding=utf-8

import Register
import RegisterBits


class BitRegister(Register):
    def __init__(self, size: int):
        super().__init__(size)
        return

    def set_bit(self, bit: RegisterBits):
        self.value |= 1 << bit
        return

    def clear_bit(self, bit: RegisterBits):
        self.value = ~self.value | (1 << bit)
        return

    def get_bit(self, bit: RegisterBits) -> bool:
        return bool(self.value & (1 << bit))
