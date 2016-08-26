#!/usr/bin/env python

# https://www.hackerrank.com/contests/101hack40/challenges/lazy-mayor-and-lasers

n = input() # Number of buildings
buildings = map(int, raw_input().split()) # Heights
m = input() # Number of lasers
lasers = map(int, raw_input().split()) # Positions of lasers

lasers.sort() # More efficient than sorted()

prev_l = 0
for l in lasers:
    l = l - 1
    for i in range(prev_l,l):
        buildings[i] = min(l-i,buildings[i])
    prev_l = l

print sum(buildings)
