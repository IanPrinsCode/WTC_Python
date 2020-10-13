from sys import setdlopenflags
import unittest
import mastermind
from test_base import captured_io
from io import StringIO
from mastermind import check_correctness, create_code

class MastermindTest(unittest.TestCase):
    def test_create_code(self):
        for i in range(100):
            self.assertEqual (len(create_code()), 4)
            for j in range(0, 4):
                self.assertTrue (0 < create_code()[j] < 9)
            code = create_code()
            test_set = set()
            for j in range(0, 4):
                test_set.add(code[j])
            self.assertTrue(len(test_set) == 4)

    def test_show_instructions(self):
        with captured_io(StringIO()) as (out, err):
            mastermind.show_instructions()
        output = out.getvalue().strip()
        self.assertEqual("""4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.""", output)

    def test_show_results(self):
        with captured_io(StringIO("1234\n")) as (out, err):
            mastermind.show_results(4, 0)
        output = out.getvalue().strip()
        self.assertEqual("""Number of correct digits in correct place:     4
Number of correct digits not in correct place: 0""", output)

    def test_take_turn(self):
        with captured_io(StringIO("12345\n1234\n")) as (out, err):
            mastermind.take_turn([5, 6, 7, 8])
        output = out.getvalue().strip()
        self.assertEqual("""Input 4 digit code: Please enter exactly 4 digits.
Input 4 digit code: Number of correct digits in correct place:     0
Number of correct digits not in correct place: 0""", output)

    def test_show_code(self):
        code = create_code()
        with captured_io(StringIO()) as (out, err):
            mastermind.show_code(code)
        output = out.getvalue().strip()
        self.assertEqual(f"""The code was: {code}""", output)

    def test_check_correctness(self):
        code = create_code()
        with captured_io(StringIO()) as (out, err):
            mastermind.check_correctness(False, 7, 4)
        output = out.getvalue().strip()
        self.assertEqual("""Congratulations! You are a codebreaker!""", output)
        self.assertEqual(check_correctness(False, 7, 4), True)

        with captured_io(StringIO()) as (out, err):
            mastermind.check_correctness(False, 7, 3)
        output = out.getvalue().strip()
        self.assertEqual("""Turns left: 5""", output)

if __name__ == '__main__':
    unittest.main()