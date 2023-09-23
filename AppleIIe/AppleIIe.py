#!/usr/bin/env python
# coding=utf-8

from AppleIIeBootROM import AppleIIeBootROM
from AppleIIePersROM import AppleIIePersonalityROM
from Base.Computer import Computer
from Base.RAM import RAM
from MOS6502.MOS6502 import MOS6502


class AppleIIe(Computer):
    def __init__(self):
        boot_rom = AppleIIeBootROM()
        pers_rom = AppleIIePersonalityROM()
        ram = RAM()
        cpu = MOS6502(1.0)
        super().__init__(boot_rom, pers_rom, ram, cpu)
        return

    def run(self):
        return
