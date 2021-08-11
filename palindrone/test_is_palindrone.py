import unittest
from is_palindrone import *

class TestPalindrone(unittest.TestCase):
    def test_palindrone(self):
        testcases = [
            ["abc", False],
            ["abcba", True],
            ["", True],
            ["abcdedcba", True],
            ["fooooo", False]
        ]

        for testcase in testcases:
            with self.subTest(msg=f"Input: {testcase[0]}, Expected: {testcase[1]}"):
                self.assertEqual(is_palindrone(testcase[0]), testcase[1])

    def test_longest_palindrone(self):
        testcases = [
            ["avkesekjhkj", "kesek"],
            ["foobar", "oo"],
            ["ovo", "ovo"]
        ]
        for testcase in testcases:
            with self.subTest(msg=f"Input: {testcase[0]}, Expected: {testcase[1]}"):
                self.assertEqual(longest_palindrone(testcase[0]), testcase[1])


def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()