#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :

def swap_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def qsort(a):
    import sys
    sys.setrecursionlimit(3000)
    def _qsort(a, bl, br):
        if bl >= br:
            return
        l = bl; r = br
        m = a[l]
        while l < r:
            while l < r and a[r] >= m:
                r -= 1
            if l < r:
                a[l] = a[r]
                l += 1
            while l < r and a[l] <= m:
                l += 1
            if l < r:
                a[r] = a[l]
                r -= 1
        a[l] = m
        _qsort(a, bl, l-1)
        _qsort(a, l+1, br)
    _qsort(a, bl=0, br=len(a)-1)

