#!/usr/bin/env python
# coding=utf-8

class Region(object):
    start: int = 0
    end: int = 0

    def __init__(self, start: int, end: int, read_only: bool = False):
        assert start <= end
        self.start = start
        self.end = end
        self.read_only = read_only
        region_size = end - start + 1
        self.map = [0x00] * region_size
        return

    def region_range(self):
        return range(self.start, self.end)

    def set(self, location: int, value: int):
        offset = location - self.start
        self.map[offset] = value
        return

    def get(self, location: int) -> int:
        offset = location - self.start
        return self.map[offset]
