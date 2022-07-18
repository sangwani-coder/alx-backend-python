#!/usr/bin/env python3

import unittest

l = [["foo", "a", "a",], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequence(unittest.TestCase):
    def testsample(self):
        for name, x, y in l:
            print("test", name)
            self.assertEqual(name ,y)

if __name__ == '__main__':
    unittest.main()
