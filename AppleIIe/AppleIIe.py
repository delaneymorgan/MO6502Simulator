#!/usr/bin/env python
# coding=utf-8

from AppleIIeBootROM import AppleIIeBootROM
from AppleIIePersROM import AppleIIePersonalityROM
from Computer import Computer
from MOS6502 import MOS6502
from RAM import RAM


class AppleIIe(Computer):
    def __init__(self, boot_rom, pers_rom, ram):
        boot_rom = AppleIIeBootROM()
        pers_rom = AppleIIePersonalityROM()
        ram = RAM()
        cpu = MOS6502()
        super().__init__(boot_rom, pers_rom, ram, cpu)
        return
