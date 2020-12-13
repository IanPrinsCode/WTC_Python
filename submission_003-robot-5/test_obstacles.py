import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
from maze import obstacles


class MyTestCase(unittest.TestCase):
    def test_generate_obstacles(self):
        obstacles.create_random_obstacles()
        test_list = obstacles.get_obstacles()

        self.assertTrue(0 <= len(test_list) <= 10)
        for item in test_list:
            self.assertTrue(-100 <= item[0] <= 100)
            self.assertTrue(-200 <= item[1] <= 200)


    def test_is_position_blocked(self):
        test_tuple = (50, -100)
        obstacles.obstacles.clear()
        obstacles.obstacles.append(test_tuple)

        self.assertEqual(True, obstacles.is_position_blocked(52, -97))
        self.assertEqual(False, obstacles.is_position_blocked(100, 50))


    def test_is_path_blocked(self):
        test_tuple = (50, 50)
        test_tuple_2 = (-80, 150)
        obstacles.obstacles.clear()
        obstacles.obstacles.append(test_tuple)
        obstacles.obstacles.append(test_tuple_2)

        self.assertEqual(True, obstacles.is_path_blocked(51, 20, 51, 70))
        self.assertEqual(False, obstacles.is_path_blocked(55, 20, 55, 70))
        self.assertEqual(False, obstacles.is_path_blocked(49, 20, 49, 70))
        self.assertEqual(True, obstacles.is_path_blocked(54, 60, 54, 10))
        self.assertEqual(False, obstacles.is_path_blocked(-90, 149, -50, 149))
        self.assertEqual(True, obstacles.is_path_blocked(-100, 152, 0, 152))
