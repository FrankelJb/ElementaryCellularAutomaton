<h1>Assignment 1 </h1>
Coded using python and pygame to generate the graphical display, using TDD and appropriate OO patterns.

<h2>Elementary Cellular Automata </h2>
The elementary cellular automata are very basic forms of cellular mutation. The simulation of these automata produce chaotic and non-repeating patterns that occur in nature.

This method of cellular mutation is performed by applying a set of rules that are defined based on a cell's value combined with the values of its two immediate neighbours represented, in this scenario, using binary numbers. Since there are 8 possible states (2^3) that a cell and its neighbours can exist in, the mutations can be outlined using a table where each column of the table defines what the possible cell permuations should produce. The table is constructed as a set of possible operations that occur during each discreet step in time using the constant *Neighbourhood* and a rule dependent *New Centre Cell*. The *New Centre Cell* is described using the 8-bit representation of first 256 natural numbers (including 0). If a cell and its neighbours are in the state described by the *Neighbourhood* row at time *t*, then the cell's value is given by the *New Centre Cell* row at time *t + 1*.  Here is the table structure for rule 30:

|Neighbourhood | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|New Centre Cell | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 |

To run the algorithm, from the root directory of the cloned repository, type ./CellularAutomaton -r &lt;rule-number&gt; -s &lt;number-of-steps&gt; -c &lt;starting-cell-structure&gt; -w &lt;width-of-grid&gt; (optional). The arguments for the algorithm are 
+ -r: Rule Number is the integer of the rule used to define the value of the *New Centre Cell*
+ -s: Number of Steps to simulate
+ -c: The starting state of the cells as a string of 1s and 0s
+ -w: An optional width that is used when creating a graphical display of the mutation

The output of this will be a grid of 'X's and ' 's printed to the standard output where the 'X's represent '1' and the ' 's represent '0'. There will also be a graphical display of the mutation.


<h3> Notes </h3>
This script needs the pygame module to execute completely. If the module is not installed then only the grid of 'X's and ' 's will be produced.
To install pygame
+ Linux
  - Type: `sudo apt-get install python-pygame`
+ Windows:
  - Visit http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi and download the installer
+ Mac OS
  - Visit http://pygame.org/ftp/ and download the tar.gz or zip of the version of python that you have and run it


To check that pygame installed type `import pygame` into the interactive shell. If nothing appears after you hit the Enter key, then you know Pygame has successfully been installed. If the error ImportError: No module named pygame appears, then try to install Pygame again (and make sure you typed import pygame correctly).

If you have any problems please visit 'http://pygame.seul.org/install.html'
