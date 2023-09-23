#!/usr/bin/env python
# coding=utf-8

import Register


class BitRegister(Register):
    def __init__(self, size):
        super.__init__(size)
        return

    def set_bit(self, bit):
        self.value |= 1 << bit
        return

    def clear_bit(self, bit):
        self.value = ~self.value | (1 << bit)
        return

    def get_bit(self, bit) -> bool:
        return bool(self.value & (1 << bit))
