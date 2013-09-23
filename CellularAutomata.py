#! /usr/bin/env python
__author__ = 'jonathan'
import argparse


class CellularAutomata():

    __rules = {}
    __neighbourhood = ["111", "110", "101", "100", "011", "010", "001", "000"]

    def mutate(self, grid, steps):
        row = 0
        while row < steps:
            current_row = grid[row]
            new = []
            for i in range(len(current_row)):
                currentCells = str(current_row[i])
                if i == 0:
                    currentCells = '0' + currentCells + str(current_row[i + 1])
                elif i == len(current_row) - 1:
                    currentCells = str(current_row[i - 1]) + currentCells + '0'
                else:
                    currentCells = str(current_row[i - 1]) + currentCells + str(current_row[i + 1])

                if self.__rules[currentCells]:
                    new.append(1)
                else:
                    new.append(0)
            grid.append(new)
            row += 1

        return grid

    #This makes a matrix of width x height <1>, we append the
    #new rows dynamically as we mutate
    def buildGrid(self, start_state, width):
        if len(start_state) > width:
            raise RuntimeError('Start state is too wide for this grid')

        startPosition = -1
        while startPosition + len(start_state) > width / 2:
            startPosition -= 1

        grid = [[0]*width]

        for i in range(len(start_state)):
            grid[0][width / 2 + startPosition + i] = int(start_state[i])

        return grid

    #Create a dictionary where the key is the current cell and its 2 neighbours
    #and the value is a boolean given by the rule in binary.
    def buildRules(self, rule):
        rule = str("{0:08b}".format(int(rule)))
        for i in range(len(rule)):
            self.__rules[self.__neighbourhood[i]] = True if int(rule[i]) == 1 else False

    def getRules(self):
        return self.__rules

    def display_grid(self, width, grid):
        try:
            import pygame
            print "Press Q or Down to quit"
            pygame.init()
            screen = pygame.display.set_mode((width * 2, int(width * 1.33)), 0, 32)
            pygame.display.set_caption("Elementary Cellular Automata")
            pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

            back = pygame.Surface(screen.get_size())
            back = back.convert()
            back.fill((255, 255, 255))

            while True:
                screen.blit(back, (0, 0))

                for row in range(len(grid)):
                    for event in pygame.event.get():
                        if event.type in (pygame.QUIT, pygame.KEYDOWN):
                            exit()
                    for i in range(len(grid[row])):
                        if grid[row][i] == 1:
                            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((i * 2, row * 2), (2, 2)))
                    pygame.display.update()
                    pygame.time.delay(50)

                pygame.time.delay(5000)
        except ImportError:
            print "\n\nPlease make sure that the pygame module is installed to see a graphical presentation of the mutation"




def main():
    parser = argparse.ArgumentParser(description='Simulate elementary cell automata')
    parser.add_argument('-c', '--start_state', help='The string that represents the starting state', required=True)
    parser.add_argument('-r', '--rule', help='The rule that is used to mutate each cell', required=True)
    parser.add_argument('-s', '--steps', help='The number of steps to simulate', required=True)
    parser.add_argument('-w', '--width', help='The width of the grid', required=False, default=480)
    args = parser.parse_args()

    cellularAutomata = CellularAutomata()
    grid = cellularAutomata.buildGrid(args.start_state, int(args.width))
    cellularAutomata.buildRules(args.rule)
    grid = cellularAutomata.mutate(grid, int(args.steps))

    for row in range(len(grid)):
        print ('%s' % ''.join(map(str, grid[row]))).replace('1', 'X').replace('0', ' ')

    cellularAutomata.display_grid(int(args.width), grid)

if __name__ == '__main__':
    main()

