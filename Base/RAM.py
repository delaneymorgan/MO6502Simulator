#!/usr/bin/env python
# coding=utf-8


import Region


class RAM(Region):
    def __init__(self, start: int, end: int):
        super().__init__(start, end, True)
        return
