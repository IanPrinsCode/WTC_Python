from turtle import position
import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.text.world as text
import world.turtle.world as turtle

class MyTestCase(unittest.TestCase):
    def test_text_start_world(self):

        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            text.start_world()

        output = out.getvalue().strip()

        self.assertEqual(text.position_x, 0)
        self.assertEqual(text.position_y, 0)
        self.assertEqual(text.current_direction_index, 0)
