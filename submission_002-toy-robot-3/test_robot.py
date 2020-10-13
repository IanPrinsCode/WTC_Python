import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot


class MyTestCase(unittest.TestCase):

    """Tests output when entering your robot name."""
    def test_name_robot(self):
        with captured_io(StringIO("jEff\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEFF: Hello kiddo!
JEFF: What must I do next? JEFF: Shutting down..""", output)


    """Tests the command that terminates the program loop."""
    def test_off_command(self):
        with captured_io(StringIO("jeif\noFf\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests the help command, which displays possible commands."""
    def test_help_off(self):
        with captured_io(StringIO("jeif\nhelP\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next? I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay previous movement commands
REPLAY SILENT - replay previous commands without output of single commands
REPLAY REVERSED - replay previous commands in reverse
REPLAY REVERSED SILENT - replay commands in reverse without output
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests the right turn function as well as the movement and coordinates update of the x-axis."""
    def test_right_back_forward_off(self):
        with captured_io(StringIO("JEIF\nright\nback 20\nforward 45\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next?  > JEIF turned right.
 > JEIF now at position (0,0).
JEIF: What must I do next?  > JEIF moved back by 20 steps.
 > JEIF now at position (-20,0).
JEIF: What must I do next?  > JEIF moved forward by 45 steps.
 > JEIF now at position (25,0).
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests the left turn function as well as the movement and coordinates update of the x-axis."""
    def test_left_back_forward_off(self):
        with captured_io(StringIO("JEIF\nleft\nback 80\nforward 100\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next?  > JEIF turned left.
 > JEIF now at position (0,0).
JEIF: What must I do next?  > JEIF moved back by 80 steps.
 > JEIF now at position (80,0).
JEIF: What must I do next?  > JEIF moved forward by 100 steps.
 > JEIF now at position (-20,0).
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests the movement and coordinates update of the y-axis."""
    def test_back_forward_off(self):
        with captured_io(StringIO("JEIF\nback 145\nforward 300\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next?  > JEIF moved back by 145 steps.
 > JEIF now at position (0,-145).
JEIF: What must I do next?  > JEIF moved forward by 300 steps.
 > JEIF now at position (0,155).
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests the out of range feedback for movement on the y-axis."""
    def test_OOR_front_and_back_off(self):
        with captured_io(StringIO("JEIF\nback 201\nforward 300\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next? JEIF: Sorry, I cannot go outside my safe zone.
 > JEIF now at position (0,0).
JEIF: What must I do next? JEIF: Sorry, I cannot go outside my safe zone.
 > JEIF now at position (0,0).
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests the out of range feedback for movement on the x-axis."""
    def test_OOR_left_and_right_off(self):
        with captured_io(StringIO("JEIF\nright\nforward 150\nback 120\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? JEIF: Hello kiddo!
JEIF: What must I do next?  > JEIF turned right.
 > JEIF now at position (0,0).
JEIF: What must I do next? JEIF: Sorry, I cannot go outside my safe zone.
 > JEIF now at position (0,0).
JEIF: What must I do next? JEIF: Sorry, I cannot go outside my safe zone.
 > JEIF now at position (0,0).
JEIF: What must I do next? JEIF: Shutting down..""", output)


    """Tests feedback for multiple invalid cammand-inputs and also that the sprint function works correctly."""
    def test_2wrongs_back_sprint_off(self):
        with captured_io(StringIO("Paulie\njump up\nFallDown\nback 5\nsprint 5\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? PAULIE: Hello kiddo!
PAULIE: What must I do next? PAULIE: Sorry, I did not understand 'jump up'.
PAULIE: What must I do next? PAULIE: Sorry, I did not understand 'FallDown'.
PAULIE: What must I do next?  > PAULIE moved back by 5 steps.
 > PAULIE now at position (0,-5).
PAULIE: What must I do next?  > PAULIE moved forward by 5 steps.
 > PAULIE moved forward by 4 steps.
 > PAULIE moved forward by 3 steps.
 > PAULIE moved forward by 2 steps.
 > PAULIE moved forward by 1 steps.
 > PAULIE now at position (0,10).
PAULIE: What must I do next? PAULIE: Shutting down..""", output)


    def test_replay(self):
        with captured_io(StringIO("bob\nleft\nright\nreplay\noff")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BOB: Hello kiddo!
BOB: What must I do next?  > BOB turned left.
 > BOB now at position (0,0).
BOB: What must I do next?  > BOB turned right.
 > BOB now at position (0,0).
BOB: What must I do next?  > BOB turned left.
 > BOB now at position (0,0).
 > BOB turned right.
 > BOB now at position (0,0).
 > BOB replayed 2 commands.
 > BOB now at position (0,0).
BOB: What must I do next? BOB: Shutting down..""", output)


    def test_replay_silent(self):
        with captured_io(StringIO("bob\nforward 20\nback 10\nreplay silent\noff")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BOB: Hello kiddo!
BOB: What must I do next?  > BOB moved forward by 20 steps.
 > BOB now at position (0,20).
BOB: What must I do next?  > BOB moved back by 10 steps.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB replayed 2 commands silently.
 > BOB now at position (0,20).
BOB: What must I do next? BOB: Shutting down..""", output)


    def test_replay_reversed(self):
        with captured_io(StringIO("bob\nleft\nright\nreplay reversed\noff")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BOB: Hello kiddo!
BOB: What must I do next?  > BOB turned left.
 > BOB now at position (0,0).
BOB: What must I do next?  > BOB turned right.
 > BOB now at position (0,0).
BOB: What must I do next?  > BOB turned right.
 > BOB now at position (0,0).
 > BOB turned left.
 > BOB now at position (0,0).
 > BOB replayed 2 commands in reverse.
 > BOB now at position (0,0).
BOB: What must I do next? BOB: Shutting down..""", output)


    def test_replay_reversed_silent(self):
        with captured_io(StringIO("bob\nforward 10\nleft\nreplay reversed silent\noff")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BOB: Hello kiddo!
BOB: What must I do next?  > BOB moved forward by 10 steps.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB turned left.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB replayed 2 commands in reverse silently.
 > BOB now at position (0,0).
BOB: What must I do next? BOB: Shutting down..""", output)


    def test_replay_reversed_silent_range(self):
        with captured_io(StringIO("bob\nforward 10\nleft\nforward 5\nreplay reversed silent 2\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BOB: Hello kiddo!
BOB: What must I do next?  > BOB moved forward by 10 steps.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB turned left.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB moved forward by 5 steps.
 > BOB now at position (-5,10).
BOB: What must I do next?  > BOB replayed 2 commands in reverse silently.
 > BOB now at position (-5,0).
BOB: What must I do next? BOB: Shutting down..""", output)


    def test_replay_reversed_silent_range(self):
        with captured_io(StringIO("bob\nforward 10\nleft\nforward 5\nreplay reversed silent 3-1\noff\n")) as (out, err):
            robot.robot_start()
        output = out.getvalue().strip()
        self.assertEqual("""What do you want to name your robot? BOB: Hello kiddo!
BOB: What must I do next?  > BOB moved forward by 10 steps.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB turned left.
 > BOB now at position (0,10).
BOB: What must I do next?  > BOB moved forward by 5 steps.
 > BOB now at position (-5,10).
BOB: What must I do next?  > BOB replayed 2 commands in reverse silently.
 > BOB now at position (-10,10).
BOB: What must I do next? BOB: Shutting down..""", output)
