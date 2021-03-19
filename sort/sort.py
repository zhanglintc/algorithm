#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :

def timer(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__}: {t2 - t1} secs")
    return wrapper

def swap_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

@timer
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

@timer
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            min_idx = min_idx if a[min_idx] < a[j] else j
        a[i], a[min_idx] = a[min_idx], a[i]

@timer
def insertion_sort(a):
    n = len(a)
    for i in range(n):
        pre_idx = i - 1
        current = a[i]
        while pre_idx >= 0 and a[pre_idx] > current:
            a[pre_idx+1] = a[pre_idx]
            pre_idx -= 1
        a[pre_idx+1] = current

@timer
def heap_sort(a):
    import heapq
    h = []
    for n in a:
        heapq.heappush(h, n)
    a.clear()
    for _ in range(len(h)):
        n = heapq.heappop(h)
        a.append(n)

@timer
def qsort(a):
    import sys
    sys.setrecursionlimit(5000)
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

