#!/usr/bin/env python
# coding=utf-8

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main:
    boot = BootROM()
    ram = RAM()
    personality = PersonalityROM()
    cpu = MOS6502(ram, boot, personality)
    computer = Computer()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

