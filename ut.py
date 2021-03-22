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
        cls._array = [random.randint(0, 100000) for _ in range(3000)]
        instance = super(cls.__class__, cls).__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

    # @unittest.skip('pass')

    def sort_test_helper(self, func):
        print()
        pairs = [
            ([], []),
            ([1], [1]),
            (self._array[:], self._array[:]),
        ]
        for pair in pairs:
            by_testee, by_system = pair
            func(by_testee); by_system.sort()
            self.assertEqual(by_testee, by_system)

    def test_swap_sort(self):
        self.sort_test_helper(self._sort.swap_sort)

    def test_bubble_sort(self):
        self.sort_test_helper(self._sort.bubble_sort)

    def test_selection_sort(self):
        self.sort_test_helper(self._sort.selection_sort)

    def test_insertion_sort(self):
        self.sort_test_helper(self._sort.insertion_sort)

    def test_shell_sort(self):
        self.sort_test_helper(self._sort.shell_sort)

    def test_heap_sort(self):
        self.sort_test_helper(self._sort.heap_sort)

    def test_quick_sort(self):
        self.sort_test_helper(self._sort.quick_sort)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    load_class = unittest.TestLoader().loadTestsFromTestCase
    suites = [
        load_class(AlgorithmSortTest),
    ]
    result = [runner.run(suite) for suite in suites]
    list(map(print, result))

