#!/usr/bin/env python
# coding=utf-8


import RegisterSet

class CPU(object):
    def __init__(self, registers, decoder):
        self.registers = registers
        self.decoder = decoder
        return