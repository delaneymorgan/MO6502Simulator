#!/usr/bin/env python
# coding=utf-8

from AppleIIeBootROM import AppleIIeBootROM
from AppleIIePersROM import AppleIIePersonalityROM
from Base.Computer import Computer
from Base.RAM import RAM
from Base.MemoryMap import MemoryMap
from MOS6502.MOS6502 import MOS6502


class AppleIIe(Computer):
    def __init__(self):
        boot_rom = AppleIIeBootROM()
        pers_rom = AppleIIePersonalityROM()
        ram = RAM(0x000, 0x0400 * 48)       # 48k RAM
        memory_map = MemoryMap()
        memory_map.add(ram)
        memory_map.add(boot_rom)
        memory_map.add(pers_rom)
        cpu = MOS6502(1.0)
        super().__init__(memory_map, cpu)
        return

    def run(self):
        return
