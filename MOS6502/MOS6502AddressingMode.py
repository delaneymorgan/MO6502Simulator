#!/usr/bin/env python
# coding=utf-8

from enum import Enum, auto


class MOS6502AddressingMode(Enum):
    none = auto()
    a = auto()  # accumulator
    abs = auto()  # absolute
    abs_x = auto()  # absolute,X
    abs_y = auto()  # absolute,y
    imm = auto()  # immediate
    ind_x = auto()  # indirect by X
    ind_y = auto()  # indirect by Y
    rel = auto()  # relative
    x = auto()  # indexed by X register
    y = auto()  # indexed by Y register
    zpg = auto()  # zero page
    zpg_x = auto()  # zero page,x
    zpg_y = auto()  # zero page,y
