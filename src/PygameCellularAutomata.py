__author__ = 'jonathan'
import pygame
from pygame.locals import *
from sys import exit
from CellularAutomata import CellularAutomata
import argparse

parser = argparse.ArgumentParser(description='Simulate elementary cell automata. '
                                             'Please press \"q\" to exit')
parser.add_argument('-c', '--start_state', help='The string that represents the starting state', required=True)
parser.add_argument('-s', '--rule', help='The rule that is used to mutate each cell', required=True)
parser.add_argument('-r', '--steps', help='The number of steps to simulate', required=True)
parser.add_argument('-w', '--width', help='The width of the grid', required=False)
args = parser.parse_args()

width = 480
if args.width is not None:
    width = int(args.width)

pygame.init()
screen = pygame.display.set_mode((width * 2, int(width * 1.33)), pygame.RESIZABLE, 32)
pygame.display.set_caption("Elementary Cellular Automata")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

back = pygame.Surface(screen.get_size())
back = back.convert()
back.fill((255, 255, 255))
cellularAutomata = CellularAutomata()
grid = cellularAutomata.buildGrid(args.start_state, width)
cellularAutomata.buildRules(args.rule)
grid = cellularAutomata.mutate(grid, int(args.steps))

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
        pygame.time.delay(10)

    pygame.time.delay(5000)




