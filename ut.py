#!/usr/bin/python3
# -*- coding: utf-8 -*-
# -*- mode: python -*-
# vi: set ft=python :

import unittest

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('######################################################################')
        print("{0}:".format(cls.__name__))

class Base64Test(BaseTestCase):
    def test_base64(self):
        import base64 as base64
        import b64.b64 as b64
        # encode
        for c in 'AZaz09+-':
            self.assertEqual(base64.b64encode(c.encode()), b64.base64_encode(c.encode()))
        self.assertEqual(base64.b64encode(b'Man'), b64.base64_encode(b'Man'))
        self.assertEqual(base64.b64encode(b'any carnal pleasure.'), b64.base64_encode(b'any carnal pleasure.'))
        # decode
        self.assertEqual(base64.b64decode('QQ=='), b64.base64_decode('QQ=='))
        self.assertEqual(base64.b64decode('TWFu'), b64.base64_decode('TWFu'))

class AlgorithmSortTest(BaseTestCase):
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
            ([x for x in range(1000, -1, -1)], [x for x in range(1000, -1, -1)]),
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

    def test_merge_sort(self):
        self.sort_test_helper(self._sort.merge_sort)

    def test_quick_sort(self):
        self.sort_test_helper(self._sort.quick_sort)

    def test_counting_sort(self):
        self.sort_test_helper(self._sort.counting_sort)
        self.sort_test_helper(self._sort.counting_sort_stable)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    load_class = unittest.TestLoader().loadTestsFromTestCase
    suites = [
        load_class(Base64Test),
        load_class(AlgorithmSortTest),
    ]
    result = [runner.run(suite) for suite in suites]
    list(map(print, result))

