# =============================
# Student Names: Justin Woo, Attila Tavakolli, Matthew Woo
# Group ID: 69
# Date: January 22, 2023
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc: 
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all variables in the given csp. If you are returning an entire grid's worth of variables
they should be arranged in a linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 20/100 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
import itertools
from math import prod

def binary_ne_grid(cagey_grid):
    ##IMPLEMENT
    var_array = [] #List to hold all the variables of the grid
    n = cagey_grid[0] #Dimension of the grid
    dom = [i for i in range(1, n + 1)] #Domain of the variables
    sat_tuples = [[o, x] for (o, x) in itertools.permutations(range(1, n+1), 2)] #Satisfiable tuples of the binary constraints
    #Getting all possible variable cells
    arr = itertools.product(dom, dom)
    var_array = [Variable("Cell({},{})".format(x,y), dom) for (x,y) in arr]
    csp = CSP("binary_cagey", var_array)
    for i in range(n):
        #Create the binary constraints
        rowc = var_array[i * n : (i+1) * n]
        colc = [var_array[j] for j in range(i, n*n, n)]
        for (o, x) in itertools.combinations(rowc, 2):
            con = Constraint("C({},{})".format(o, x), [o, x])
            con.add_satisfying_tuples(sat_tuples)
            csp.add_constraint(con)
        for (o, x) in itertools.combinations(colc, 2):
            con = Constraint("C({},{})".format(o, x), [o, x])
            con.add_satisfying_tuples(sat_tuples)
            csp.add_constraint(con)

    return csp, var_array


def nary_ad_grid(cagey_grid):
    ## IMPLEMENT
    var_array = [] #List to hold all the variables of the grid
    n = cagey_grid[0] #Dimension of the grid
    dom = [i for i in range(1, n + 1)] #Domain of the variables
    sat_tuples = [x for x in itertools.permutations(range(1, n+1), n)]
    arr = itertools.product(dom, dom)
    var_array = [Variable("Cell({},{})".format(x,y), dom) for (x,y) in arr]
    csp = CSP("nary_cagey", var_array)
    for i in range(n):
        rowc = var_array[i * n : (i+1) * n]
        colc = [var_array[j] for j in range(i, n*n, n)]
        for x in itertools.combinations(rowc, n):
            con = Constraint("C({})".format(x), x)
            con.add_satisfying_tuples(sat_tuples)
            csp.add_constraint(con)
        for x in itertools.combinations(colc, n):
            con = Constraint("C({})".format(x), x)
            con.add_satisfying_tuples(sat_tuples)
            csp.add_constraint(con)

    return csp, var_array

def cagey_csp_model(cagey_grid):
    ## Implemented using binary_ne_grid
    csp, var_array = binary_ne_grid(cagey_grid)
    # Dimension of the board
    n = cagey_grid[0]
    for cage in cagey_grid[1]:
        # Amount of cells in cage
        cagesize = len(cage[1])
        sat_vals = []
        scope = [var_array[(n * (y-1)) + (x-1)] for (y, x) in cage[1]]
        opVar = Variable("Cage_op(" + str(cage[0]) + ":" + cage[2] + ":" + str(scope) + ")", ['+','-','*','/','?'])
        con = Constraint("Cage(" + str(cage[0]) + ":" + cage[2] + ":" + str(scope) + ")", [opVar] + scope)
        var_array.append(opVar)
        # Create satisfiable tuples for constraint
        if cagesize == 1:
            sat_vals = [[cage[2]] + list(x) for x in itertools.product(scope[0].domain(),repeat=cagesize)]
        else:
            if cage[2] == "+" or cage[2] == "?":
                sat_vals = [["+"] + list(x) for x in itertools.product(scope[0].domain(),repeat=cagesize) if sum(x) == cage[0]]
                con.add_satisfying_tuples(sat_vals)
            if cage[2] == "*" or cage[2] == "?":
                sat_vals = [["*"] + list(x) for x in itertools.product(scope[0].domain(),repeat=cagesize) if prod(x) == cage[0]]
                con.add_satisfying_tuples(sat_vals)
            if cage[2] == "-" or cage[2] == "?":
                sat_vals = [["-"] + list(x) for x in itertools.product(scope[0].domain(),repeat=cagesize) if x[0] - sum(x[1:]) == cage[0]]
                con.add_satisfying_tuples(sat_vals)
            if cage[2] == "/" or cage[2] == "?":
                sat_vals = [["/"] + list(x) for x in itertools.product(scope[0].domain(),repeat=cagesize) if x[0] / prod(x[1:]) == cage[0]]
                con.add_satisfying_tuples(sat_vals)
        
        csp.add_var(opVar)
        csp.add_constraint(con)
    return (csp, var_array)