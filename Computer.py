#!/usr/bin/env python
# coding=utf-8

from BootROM import BootROM
from CPU import CPU
from PersonalityROM import PersonalityROM
from RAM import RAM


class Computer(object):
    boot_rom: BootROM
    pers_rom: PersonalityROM
    ram: RAM
    cpu: CPU

    def __init__(self, boot_rom, pers_rom, ram, cpu):
        self.boot_rom = boot_rom
        self.pers_rom = pers_rom
        self.ram = ram
        self.cpu = cpu
        return
