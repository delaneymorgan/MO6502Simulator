#!/usr/bin/env python
# coding=utf-8


class MOS6502(CPU):
    def __init__(self, ram, boot, personality):

        super.__init__(ram, boot, personality)