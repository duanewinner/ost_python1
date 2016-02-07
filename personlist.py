#!/usr/local/bin/python3
"""Produce a listing of people's names, ages and weights."""

data = [
    ("Steve", 59, 202),
    ("Dorothy", 49, 99),
    ("Simon", 39, 155),
    ("David", 61, 135) ]

#for row in data:
#    print("{0[0]:<12s} {0[1]:4d} {0[2]:4d}".format(row))

for name, age, weight in data:
    print("{0:.<12s}{1:.>4d}{2:.>10d}".format(name, age, weight))

