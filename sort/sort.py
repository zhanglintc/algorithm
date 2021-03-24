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
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__}: {t2 - t1} secs")
        return res
    return wrapper

@timer
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
def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(n):
            pre_idx = i - gap
            current = a[i]
            while pre_idx >= 0 and a[pre_idx] > current:
                a[pre_idx+gap] = a[pre_idx]
                pre_idx -= gap
            a[pre_idx+gap] = current
        gap //= 2

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
def merge_sort(a):
    def _sort(a):
        n = len(a)
        if n <= 1:
            return a
        m = n // 2
        return _merge(_sort(a[:m]), _sort(a[m:]))
    def _merge(left, right):
        res = []
        while left and right:
            if left[0] < right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        if left:
            res += left
        if right:
            res += right
        return res
    res = _sort(a)[:]
    a.clear()
    for n in res:
        a.append(n)

@timer
def quick_sort(a):
    def _qsort(a, bl, br):
        q = [(bl, br)]
        while q:
            bl, br = q.pop(0)
            if bl >= br:
                continue
            l, r = bl, br
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
            q.append((bl, l-1))
            q.append((l+1, br))
    _qsort(a, bl=0, br=len(a)-1)

@timer
def counting_sort(a):
    # https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653195533&idx=1&sn=02918dc51b07837ce1119f00d7900dbc
    if not a:
        return
    low = min(a)  # offset
    high = max(a)
    counter = [0] * (high - low + 1)
    for n in a:
        counter[n-low] += 1
    a.clear()
    for i in range(len(counter)):
        a += [i+low] * counter[i]

@timer
def counting_sort_stable(a):
    # https://mp.weixin.qq.com/s?__biz=MzIxMjE5MTE1Nw==&mid=2653195533&idx=1&sn=02918dc51b07837ce1119f00d7900dbc
    if not a:
        return
    low = min(a)
    high = max(a)
    counter = [0] * (high - low + 1)
    for n in a:
        counter[n-low] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    res = [0] * len(a)
    for i in range(len(a)-1, -1, -1):
        counter_idx = a[i] - low
        res_idx = counter[counter_idx] - 1
        res[res_idx] = a[i]
        counter[counter_idx] -= 1
    a.clear()
    for n in res:
        a.append(n)

counting_sort_stable([1])