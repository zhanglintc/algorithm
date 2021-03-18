#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :

def qsort(a):
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

qsort([5,8,6,3,4,7])
