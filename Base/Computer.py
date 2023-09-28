#!/usr/bin/env python
# coding=utf-8

from CPU import CPU
from MemoryMap import MemoryMap


class Computer(object):
    memory_map: MemoryMap
    cpu: CPU

    def __init__(self, memory_map: MemoryMap, cpu: CPU):
        self.memory_map = memory_map
        self.cpu = cpu
        return
