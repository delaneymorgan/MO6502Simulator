#!/usr/bin/env python
# coding=utf-8

from typing import Callable


class Instruction(object):
    mnemonic: str
    cycles: int = 0
    action: Callable

    def __init__(self, mnemonic, bytes, cycles, action):
        self.mnemonic = mnemonic
        self.bytes = bytes
        self.cycles = cycles
        self.action = action
        return
