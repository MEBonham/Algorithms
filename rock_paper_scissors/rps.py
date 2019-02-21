#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    
    if n == 0:
        return [[]]
    
    base = rock_paper_scissors(n - 1)
    r = []
    p = []
    s = []
    for item in base:
        r.append(['rock'] + item)
        p.append(['paper'] + item)
        s.append(['scissors'] + item)
    return r + p + s


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')