#!/usr/bin/env python
# coding=utf-8


import ROM


class BootROM(ROM):
    def __init__(self, start: int, end: int):
        super().__init__(start, end)
        return
