#! /usr/bin/env python

__author__ = 'jonathan'
import unittest
from CellularAutomata import  CellularAutomata

class TestCellularAutomata(unittest.TestCase):

    def test_buildgridpasses(self):
        cA = CellularAutomata()
        cA.buildGrid('10', 100)
        grid = cA.buildGrid('1' * 8, 9) #Width of the grid is greater than the length of the start state
        self.assertEqual(len(grid[0]), 9)
        grid = cA.buildGrid('1' * 10, 9) #Width of the grid is less than the length of the start state
        self.assertEqual(len(grid[0]), 10)

    #It is quite difficult to assert correctness, so I have chosen to use a row high up, row 3, and
    #ensure that it contains a substring that it should. The string used
    #was copied from http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P1/
    def test_rowsarecorrect(self):
        cA = CellularAutomata()
        grid = cA.buildGrid('1', 100)
        cA.buildRules('30')
        grid = cA.mutate(grid, int(3))
        self.assertTrue('0110010' in '%s' % ''.join(map(str, grid[2])))

def main():
        unittest.main()

if __name__ == '__main__':
    unittest.main()

