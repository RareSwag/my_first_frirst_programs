# This program demonstrates how to use the math module.
# Jaden Heinle

import math

#
# August 30th 2017


def gram_area(b, h):
    ga = b * h
    return ga

def trap_area(a, b, h):
    ga = ((a + b) / 2) * h
    return ga

def rect_volume(w, h, l):
    rv = w * h * l
    return rv

def circ_volume(r, h):
    cv = 3.141 * (r ** 2) * (h / 3)
    return cv

def sphere_volume(r):
    sv = (4/3) * 3.141 * r ** 3
    return sv

def rect_sa(l, w , h):
    sa = 2 * (w * l + h * l + h * w)
    return sa

def sphere_sa(r):
    ssa =  4 * 3.141 *r ** r
    return ssa

def tri_legs(a, b):
    tl = math.sqrt(a ** 2 + b ** 2)
    return tl

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    hf = math.sqrt( s * ( s - a) * (s - b) * ( s - c))
    return hf

# function calls
print(gram_area(2, 4))
print(trap_area(2, 4, 2))
print(rect_volume(2, 4, 2))
print(circ_volume(2, 4))
print(sphere_volume(2))
print(rect_sa(2, 2 , 2))
print(sphere_sa(2))
print(tri_legs(2, 2))
print(herons_formula(5, 10, 15))
