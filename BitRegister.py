#!/usr/bin/env python
# coding=utf-8

import Register


class BitRegister(Register):
    bit_map: ()

    def __init__(self, size, bit_map):
        super.__init__(size)
        self.bit_map = bit_map
        return

    def set(self, bit, value):
        raise NotImplementedError

    def get(self, bit, value):
        raise NotImplementedError
