#!/usr/bin/env python    # -*- coding: utf-8 -*

# import sys

# line = sys.stdin.readline().strip()
# lines = line.split()
# 将一句话按空格或者逗号分割成str类型存入list中
# print int(lines[1])+int(lines[2])

# print type(lines[1])

import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        lines = line.split()
        print int(lines[0]) + int(lines[1])
except:
    pass
