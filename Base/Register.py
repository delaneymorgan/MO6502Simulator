#!/usr/bin/env python
# coding=utf-8

class Register(object):
    size: int = 0
    value: int = 0

    def __init__(self, size: int):
        self.size = size
        self.value = 0
        return
