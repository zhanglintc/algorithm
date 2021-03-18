#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :

import unittest

class BaseMmrzTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("{0}:".format(cls.__name__))

class AlgorithmSortTest(BaseMmrzTestCase):
    def __new__(cls, *args, **kwargs):
        import sort.sort as _sort
        cls._sort = _sort
        import random
        cls._array = [random.randint(0, 100000) for _ in range(1000)]
        instance = super(cls.__class__, cls).__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    # @unittest.skip('bug')
    def test_swap_sort(self):
        by_swap = self._array[:]
        by_system = self._array[:]
        self._sort.swap_sort(by_swap)
        by_system.sort()
        self.assertEqual(by_swap, by_system)

    # @unittest.skip('bug')
    def test_bubble_sort(self):
        by_bubble = self._array[:]
        by_system = self._array[:]
        self._sort.bubble_sort(by_bubble)
        by_system.sort()
        self.assertEqual(by_bubble, by_system)

    def test_qsort(self):
        by_qsort = self._array[:]
        by_system = self._array[:]
        self._sort.qsort(by_qsort)
        by_system.sort()
        self.assertEqual(by_qsort, by_system)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    load_class = unittest.TestLoader().loadTestsFromTestCase
    suites = [
        load_class(AlgorithmSortTest),
    ]
    result = [runner.run(suite) for suite in suites]
    list(map(print, result))

