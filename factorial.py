#!/usr/local/bin/python3

"""Print all factorials less than 1000."""

"""c = 1
f = 1
while (f < 1000):
    print(f)
    c += 1
    f = 1
    for n in range(c, 0, -1):
        f = f * n
"""

c = 1
f = 1
while (f < 1000):
    print(f)
    c += 1
    f *= c
