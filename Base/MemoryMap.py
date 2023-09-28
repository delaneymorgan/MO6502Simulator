#!/usr/bin/env python
# coding=utf-8

import Region


class MemoryMap(object):
    def __init__(self):
        self.regions = {}
        return

    def add(self, region: Region):
        region_range = region.region_range()
        self.regions[region_range] = region
        return

    def set(self, location, value):
        for region_range, region in self.regions.items():
            if location in region_range:
                region.set(location, value)
        return

    def get(self, location) -> int:
        value = 0x00
        for region_range, region in self.regions.items():
            if location in region_range:
                value = region.set(location)
        return value
