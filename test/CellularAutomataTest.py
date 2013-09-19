#! /usr/bin/env python

__author__ = 'jonathan'
import unittest
from src.CellularAutomata import CellularAutomata

class TestCellularAutomata(unittest.TestCase):

    def test_buildgridpasses(self):
        cA = CellularAutomata()
        cA.buildGrid('10')
        self.assertRaises(RuntimeError, lambda: cA.buildGrid('101010110111111111111111111111111111111111'))

    #It is quite difficult to assert correctness, so I have chosen to use a row high up, row 3, and
    #ensure that it contains a substring that it should. The string used
    #was copied from http://www-inst.eecs.berkeley.edu/~selfpace/cs9honline/P1/
    def test_rowsarecorrect(self):
        cA = CellularAutomata()
        grid = cA.buildGrid('1')
        cA.buildRules('30')
        grid = cA.mutate(grid, int(3))
        self.assertTrue('0110010' in '%s' % ''.join(map(str, grid[2])))

def main():
        unittest.main()

if __name__ == '__main__':
    main()

