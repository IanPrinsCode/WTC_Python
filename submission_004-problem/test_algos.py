import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import super_algos


class MyTestCase(unittest.TestCase):
    """Testing if the find_min function is working properly by matching expected minimum value in return value. Invalid
    elements passed in the list or an empty list must return (-1)"""
    def test_find_min(self):
        self.assertEqual(2, super_algos.find_min([4, 2, 3, 7, 8]))
        self.assertEqual(1, super_algos.find_min([1, 2, 3, 4]))
        self.assertEqual(-1, super_algos.find_min([1, 2, "s", 4]))
        self.assertEqual(-1, super_algos.find_min([]))


    """Testing if the sum_all function is working properly by matching expected sum total in return value. Invalid elements
    passed in the list or an empty list must return (-1)"""
    def test_sum_all(self):
        self.assertEqual(24, super_algos.sum_all([4, 2, 3, 7, 8]))
        self.assertEqual(10, super_algos.sum_all([1, 2, 3, 4]))
        self.assertEqual(-1, super_algos.sum_all([1, 2, "s", 4]))
        self.assertEqual(-1, super_algos.sum_all([]))


    """Testing list output of find_possible_string function by checking if expected strings are present in the return list
    for different scenarios. Empty character-set parameter must return an empty list."""
    def test_find_possible_strings(self):
        self.assertTrue("aa" and "bb" and "ab" and "ba" in super_algos.find_possible_strings(["a", "b"], 2))
        self.assertTrue("aaa" and "aab" and "aba" and "abb" and "baa" and "bab" and "bba" and "bbb" in super_algos.find_possible_strings(["a", "b"], 3))
        self.assertEqual(super_algos.find_possible_strings([], 2), [])
        self.assertEqual(super_algos.find_possible_strings([], 1), [])