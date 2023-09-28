#!/usr/bin/env python
# coding=utf-8

from typing import Callable


class Instruction(object):
    mnemonic: str
    num_bytes: int = 0
    cycles: int = 0
    action: Callable

    def __init__(self, mnemonic, num_bytes, cycles, action):
        self.mnemonic = mnemonic
        self.num_bytes = num_bytes
        self.cycles = cycles
        self.action = action
        return
