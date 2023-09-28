#!/usr/bin/env python
# coding=utf-8

import Region


class ROM(Region):
    def __init__(self, start: int, end: int):
        super().__init__(start, end)
        return

    def load(self, rom_filepath: str):
        return
