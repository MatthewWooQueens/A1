## STUDENT CODE
from cagey_csp import cagey_csp_model, binary_ne_grid, nary_ad_grid
from propagators import prop_FC, prop_GAC
from heuristics import ord_mrv, ord_dh
## END OF STUDENT CODE

## TESTING CODE STARTS AT LINE 140

from cspbase import *
from answer_set import *

from copy import deepcopy
import itertools
import sys
import unittest
import os
import json
import time

from unittest.runner import TextTestResult

## STUDENT SCORE
NARY_POINTS = 0
BINARY_POINTS = 0
CAGE_POINTS = 0
FC_POINTS = 0
GAC_POINTS = 0
MRV_POINTS = 0
DH_POINTS = 0

## FULL SCORE
NARY_FULL = 0.5
BINARY_FULL = 0.5
CAGE_FULL = 1.0
FC_FULL = 1.0
GAC_FULL = 1.5
MRV_FULL = 0.5
DH_FULL = 0.5

## ALLOWED TIME IN SECONDS
TIME_ALLOWED = 60

## OUTPUT MESSAGE
OUT_MSG = ""
OUT_MSG += ("----------------------------------------------------------------------")
OUT_MSG += ("\nTime spent:\n\n")

## UTILITIES

def check_diff(vars, board):
    N = board[0]
    for i in range(0,N):
        for j in range(0,N):
            for k in range(j+1,N):
                if vars[i][j].get_assigned_value() == vars[i][k].get_assigned_value():
                    return False
            for l in range(i+1,N):
                if vars[i][j].get_assigned_value() == vars[l][j].get_assigned_value():
                    return False
    return True

def add_valid(target, values):
    return target == sum(values)


def sub_valid(target, values):
    values.sort(reverse=True)
    total = values[0]
    for v in values[1:]:
        total -= v
    if total == target:
        return True
    return False


def div_valid(target, values):
    arrangements = itertools.permutations(values)
    for arr in arrangements:
        total = arr[0]
        for v in arr[1:]:
            total /= v
        if total == target:
            return True
    return False


def mul_valid(target, values):
    product = 1
    for v in values:
        product *= v
    return product == target

def check_cage(csp, grid, var):
    cage_dict = {}
    for cage in grid[1]:
        in_cage = []
        for v in cage[1]:
            in_cage.append(var[v[0]-1][v[1]-1])
        cage_dict[(f'Cage_op({cage[0]}:{cage[2]}:{in_cage})')] = (cage[0], in_cage.copy())

    to_be_checked = var[grid[0] ** 2:]

    for cage in to_be_checked:
        assigned_values = [v.assignedValue for v in cage_dict[cage.name][1]]
        if cage.assignedValue == '+':
            if not add_valid(cage_dict[cage.name][0], assigned_values):
                print('fail on add ' + cage.name)
                return False
        elif cage.assignedValue == '-':
            if not sub_valid(cage_dict[cage.name][0], assigned_values):
                print('fail on sub ' + cage.name)
                return False
        elif cage.assignedValue == '*':
            if not mul_valid(cage_dict[cage.name][0], assigned_values):
                print('fail on mul ' + cage.name)
                return False
        elif cage.assignedValue == '/':
            if not div_valid(cage_dict[cage.name][0], assigned_values):
                print('fail on div ' + cage.name)
                return False
        else:
            if len(cage_dict[cage.name][1]) == 1 and cage_dict[cage.name][1][0].assignedValue != cage_dict[cage.name][0]:
                print('fail on freecell' + cage.name)
                return False
            elif not add_valid(cage_dict[cage.name][0], assigned_values) and not sub_valid(cage_dict[cage.name][0], assigned_values) \
                and not mul_valid(cage_dict[cage.name][0], assigned_values) and not div_valid(cage_dict[cage.name][0], assigned_values):
                print('fail on unknown' + cage.name)
                return False
    return True

class NoTraceResult(TextTestResult):
    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super(NoTraceResult, self).__init__(stream, descriptions, verbosity)

    def addFailure(self, test, err):
        err_sans_tb = (err[0], err[1], None)
        super(NoTraceResult, self).addFailure(test, err_sans_tb)

######THIS IS THE START OF THE TESTING CODE

## nary_ad_grid

class TestNaryGrid(unittest.TestCase):
    def setUp(self):
        pass

    def test_nary_grid_1(self):
        start_time = time.time()
        
        global OUT_MSG

        global NARY_POINTS

        b = (3, [(2, [(1, 1), (1, 2)], '-'), (2, [(1, 3)], '?'), (2, [(2, 1), (3, 1)], '/'), (3, [(2, 2), (2, 3)], '/'),
                 (1, [(3, 2), (3, 3)], '-')])


        message = ""
        passed = True
        try:
            csp_nary = nary_ad_grid(b)[0]
            constraints_nary = csp_nary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False

        answer_nary = test_nary_grid_1_answer_nary()

        if len(constraints_nary) == b[0] * 2:
            passed = True
            sats = [c.sat_tuples for c in constraints_nary]
            for a in answer_nary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_nary_grid_1"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            NARY_POINTS += 1

    def test_nary_grid_2(self):
        start_time = time.time()
        
        global OUT_MSG

        global NARY_POINTS

        b = (4, [(2, [(1,1),(1,2)],'/'),(7,[(1,3),(2,3)],'+'),(4,[(1,4)],'?'),(1,[(2,1),(2,2)],'-'),(3,[(2,2),(3,2)],'-'),(2,[(2,4),(3,4)],'-'),(4,[(3,3),(4,3),(4,4)],'*'),(1,[(4,1),(4,2)],'-')])

        message = ""
        passed = True
        try:
            csp_nary = nary_ad_grid(b)[0]
            constraints_nary = csp_nary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False

        answer_nary = test_nary_grid_2_answer_nary()
        if len(constraints_nary) == b[0] * 2:
            passed = True
            sats = [c.sat_tuples for c in constraints_nary]
            for a in answer_nary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_nary_grid_2"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            NARY_POINTS += 1

    def test_nary_grid_3(self):
        start_time = time.time()
        
        global OUT_MSG

        global NARY_POINTS
        b = (5, [(2, [(1,1), (2,1)], '/'), (1, [(1,2), (2,2)], '-'), (2, [(1,3), (2,3)], '-'), (4, [(1,4), (1,5)], '-'), (6, [(2,4), (2,5)],'*'), (2, [(3,1),(3,2)],'-'), (3,[(3,3), (4,3)], '-'),(2, [(3,4), (4,4)],'/'), (3,[(3,5), (4,5)], '-'), (8,[(4,1), (4,2)],'+'), (7, [(5,1), (5,2),(5,3)],'+'), (2, [(5,4),(5,5)],'-')])
        message = ""
        passed = True
        try:
            csp_nary = nary_ad_grid(b)[0]
            constraints_nary = csp_nary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False

        answer_nary = test_nary_grid_3_answer_nary()    
        if len(constraints_nary) == b[0] * 2:
            passed = True
            sats = [c.sat_tuples for c in constraints_nary]
            for a in answer_nary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_nary_grid_3"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            NARY_POINTS += 1

    def test_nary_grid_4(self):
        start_time = time.time()
        
        global OUT_MSG

        global NARY_POINTS

        b = (6, [(2, [(1, 1), (1, 2)], '-'), (3, [(1, 3), (2, 3)], '-'), (5, [(1, 4), (1, 5)], '-'),
                 (1, [(1, 6), (2, 6)], '-'), (2, [(2, 1), (2, 2)], '-'), (10, [(2, 4), (2, 5)], '*'),
                 (2, [(3, 1), (4, 1)], '-'), (2, [(3, 2), (4, 2)], '/'), (30, [(3, 3), (3, 4)], '*'),
                 (3, [(3, 5), (3, 6)], '-'), (6, [(4, 3), (4, 4)], '*'), (6, [(4, 4), (4, 5)], '+'),
                 (6, [(5, 1), (5, 2)], '+'),
                 (2, [(5, 3), (6, 3)], '/'), (2, [(5, 4), (5, 5)], '-'), (1, [(5, 6), (6, 6)], '-'),
                 (3, [(6, 1), (6, 2)], '+'), (7, [(6, 4), (6, 5)], '+')])

        message = ""
        passed = True
        try:
            csp_nary = nary_ad_grid(b)[0]
            constraints_nary = csp_nary.get_all_cons()
        except Exception as e:
            message += "Failed to construct board %s. " %b
            message += "Got exception %s\n" % e
            constraints_nary = []

        answer_nary = test_nary_grid_4_answer_nary()
        if len(constraints_nary) == b[0] * 2:
            passed = True
            sats = [c.sat_tuples for c in constraints_nary]
            for a in answer_nary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_nary_grid_4"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            NARY_POINTS += 1

## binary_ne_grid

class TestBinaryGrid(unittest.TestCase):
    def setUp(self):
        pass

    def test_bne_grid_1(self):
        start_time = time.time()
        
        global OUT_MSG

        global BINARY_POINTS

        b = (3, [(2, [(1, 1), (1, 2)], '-'), (2, [(1, 3)], '?'), (2, [(2, 1), (3, 1)], '/'), (3, [(2, 2), (2, 3)], '/'),
                 (1, [(3, 2), (3, 3)], '-')])

        message = ""
        passed = True
        try:
            csp_binary = binary_ne_grid(b)[0]
            constraints_binary = csp_binary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False

        answer_binary = test_bne_grid_1_answer_binary()
        unidirectional_ans = b[0] ** 2 * (b[0]-1)
        bidirectional_ans = unidirectional_ans * 2
        if len(constraints_binary) == unidirectional_ans or len(constraints_binary) == bidirectional_ans:
            passed = True
            sats = [c.sat_tuples for c in constraints_binary]
            for a in answer_binary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_bne_grid_1"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            BINARY_POINTS += 1

    def test_bne_grid_2(self):
        start_time = time.time()
        
        global OUT_MSG

        global BINARY_POINTS

        b = (3, [(3, [(1, 1), (2, 1)], '+'), (1, [(1, 2)], '?'), (8, [(1, 3), (2, 3), (2, 2)], "+"), (3, [(3, 1)], '?'),
                 (3, [(3, 2), (3, 3)], "+")])

        message = ""
        passed = True
        try:
            csp_binary = binary_ne_grid(b)[0]
            constraints_binary = csp_binary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False
        answer_binary = test_bne_grid_2_answer_binary()

        unidirectional_ans = b[0] ** 2 * (b[0] - 1)
        bidirectional_ans = unidirectional_ans * 2
        if len(constraints_binary) == unidirectional_ans or len(constraints_binary) == bidirectional_ans:
            passed = True
            sats = [c.sat_tuples for c in constraints_binary]
            for a in answer_binary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_bne_grid_2"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            BINARY_POINTS += 1


    def test_bne_grid_3(self):
        start_time = time.time()
        
        global OUT_MSG

        global BINARY_POINTS

        b = (4, [(2, [(1, 1), (1, 2)], '/'), (3, [(1, 3), (1, 4), (2, 3)], '*'), (8, [(2, 1), (2, 2), (3, 2)], '+'),
                 (4, [(3, 4)], '?'), (3, [(3, 1), (4, 1)], '-'), (4, [(3, 3)], '?'), (6, [(3, 4), (4, 4)], '*'),
                 (2, [(4, 2), (4, 3)], "/")])

        message = ""
        passed = True
        try:
            csp_binary = binary_ne_grid(b)[0]
            constraints_binary = csp_binary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False
        answer_binary = test_bne_grid_3_answer_binary()

        unidirectional_ans = b[0] ** 2 * (b[0] - 1)
        bidirectional_ans = unidirectional_ans * 2
        if len(constraints_binary) == unidirectional_ans or len(constraints_binary) == bidirectional_ans:
            passed = True
            sats = [c.sat_tuples for c in constraints_binary]
            for a in answer_binary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_bne_grid_3"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            BINARY_POINTS += 1

    def test_bne_grid_4(self):
        start_time = time.time()
        
        global OUT_MSG

        global BINARY_POINTS

        b = (5, [(1, [(1, 1), (2, 1)], '-'), (10, [(1, 2), (1, 3), (2, 3), (4, 3)], '+'),
                 (9, [(1, 4), (1, 5), (2, 4), (2, 5)], '+'), (40, [(2, 2), (3, 1), (3, 2)], '*'),
                 (50, [(3, 4), (4, 3), (4, 4)], '*'), (10, [(3, 5), (4, 5), (5, 5)], '+'),
                 (9, [(4, 1), (4, 2), (5, 1), (5, 2)], '+'), (4, [(5, 3), (5, 4)], '/')])

        message = ""
        passed = True
        try:
            csp_binary = binary_ne_grid(b)[0]
            constraints_binary = csp_binary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False

        answer_binary = test_bne_grid_4_answer_binary()
        unidirectional_ans = b[0] ** 2 * (b[0] - 1)
        bidirectional_ans = unidirectional_ans * 2
        if len(constraints_binary) == unidirectional_ans or len(constraints_binary) == bidirectional_ans:
            passed = True
            sats = [c.sat_tuples for c in constraints_binary]
            for a in answer_binary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: %s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_bne_grid_4"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            BINARY_POINTS += 1

    def test_bne_grid_5(self):
        start_time = time.time()
        
        global OUT_MSG

        global BINARY_POINTS

        b = (6, [(11, [(1, 1), (2, 1)], '+'), (3, [(1, 2), (2, 2)], '*'), (20, [(1, 3), (2, 3), (3, 3)], '*'),
                 (2, [(1, 4), (1, 5)], '-'), (6, [(1, 6), (2, 6)], '/'), (6, [(2, 4), (2, 5)], '*'),
                 (5, [(3, 1), (4, 1)], '+'), (40, [(3, 2), (4, 2), (5, 2)], '*'), (10, [(3, 4), (4, 4)], '+'),
                 (10, [(3, 5), (3, 6)], '*'), (3, [(4, 3), (5, 3)], '-'), (8, [(4, 5), (4, 6), (5, 6)], '+'),
                 (1, [(5, 1), (6, 1), (6, 2)], '-'), (11, [(5, 4), (5, 5)], '+'), (1, [(6, 3), (6, 4)], '-'),
                 (2, [(6, 5), (6, 6)], '-')])

        message = ""
        passed = True
        try:
            csp_binary = binary_ne_grid(b)[0]
            constraints_binary = csp_binary.get_all_cons()
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        passed = False

        answer_binary = test_bne_grid_5_answer_binary()
        unidirectional_ans = b[0] ** 2 * (b[0] - 1)
        bidirectional_ans = unidirectional_ans * 2
        if len(constraints_binary) == unidirectional_ans or len(constraints_binary) == bidirectional_ans:
            passed = True
            sats = [c.sat_tuples for c in constraints_binary]
            for a in answer_binary:
                if a.sat_tuples not in sats:
                    passed = False
                    message += "Failed to encode: % s\n" % a.sat_tuples
        else:
            message += "Encoded incorrect number of constraints for board: %s\n" % str(b)

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_bne_grid_5"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            BINARY_POINTS += 1

## cagey_csp_model

class TestCageConstraints(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_cage_existence(self):
        global CAGE_POINTS
        
        board = (2,[(6, [(1, 1), (1, 2), (2, 1), (2, 2)], '+')])
        csp, var_array = cagey_csp_model(board)
        correct = "Cage_op(6:+:[Var-Cell(1,1), Var-Cell(1,2), Var-Cell(2,1), Var-Cell(2,2)])"
        
        message = "failed to find cage variable"
        passed = False
        for v in var_array:
            if v.name == correct:
                message = ""
                passed = True
                break
        if passed:
            CAGE_POINTS+=3
            
        self.assertTrue(passed, message)

    def test_cages_1(self):
        start_time = time.time()
        
        global OUT_MSG

        global CAGE_POINTS

        board = (2,[(4, [(1, 1), (1, 2), (2, 1), (2, 2)], '+')])
        correct = test_cages_1_correct()

        message = ""
        passed = True
        try:
            b = deepcopy(board)
            csp, var_array = cagey_csp_model(b)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)

        guess = [c for c in csp.get_all_cons() if len(c.scope) == 5]
        answered = []
        used_guess = []

        normalized_guess = []
        # Flip if the first element is not a string.
        if not isinstance(guess[0].scope[0].dom[0], str):
            # flip the csp
            normalized_guess = []
            for g in guess:
                normalized_guess.append(Constraint(g.name, [g.scope[-1]]+g.scope[:-1]))
                rev_sat = []
                for s in g.sat_tuples:
                    rev_sat.append(((s[-1],)+s[:-1]))
                normalized_guess[-1].add_satisfying_tuples(rev_sat)
        else:
            normalized_guess = guess

        guess = normalized_guess

        for g in range(len(guess)):
            gue = guess[g]
            for a in range(len(correct)):
                ans = correct[a]
                if gue.sat_tuples == ans.sat_tuples and a not in answered:
                    CAGE_POINTS += 1.5
                    answered.append(a)
                    used_guess.append(g)

        for i in range(len(correct)):
            if i not in answered:
                message += "\n\nFailed to encode:\n %s" % correct[i].sat_tuples
                message += "\nInput board: %s\n" % str(b)
                passed = False

        for g in range(len(guess)):
            if g not in used_guess:
                message += "\n\nEncoded incorrect constraint:\n %s" % guess[g].sat_tuples
                passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_cages_1"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)

    def test_cages_2(self):
        start_time = time.time()
        
        global OUT_MSG

        global CAGE_POINTS

        board = (2,[(4, [(1, 1), (1, 2), (2, 1), (2, 2)], '-')])
        correct = test_cages_2_correct()

        message = ""
        passed = True
        try:
            b = deepcopy(board)
            csp, var_array = cagey_csp_model(b)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)

        guess = [c for c in csp.get_all_cons() if len(c.scope) == 5]
        answered = []
        used_guess = []

        normalized_guess = []
        # Flip if the first element is not a string.
        if not isinstance(guess[0].scope[0].dom[0], str):
            # flip the csp
            normalized_guess = []
            for g in guess:
                normalized_guess.append(Constraint(g.name, [g.scope[-1]] + g.scope[:-1]))
                rev_sat = []
                for s in g.sat_tuples:
                    rev_sat.append(((s[-1],) + s[:-1]))
                normalized_guess[-1].add_satisfying_tuples(rev_sat)
        else:
            normalized_guess = guess

        guess = normalized_guess

        for g in range(len(guess)):
            gue = guess[g]
            for a in range(len(correct)):
                ans = correct[a]
                if gue.sat_tuples == ans.sat_tuples and a not in answered:
                    CAGE_POINTS += 1.5
                    answered.append(a)
                    used_guess.append(g)

        for i in range(len(correct)):
            if i not in answered:
                message += "\n\nFailed to encode:\n %s" % correct[i].sat_tuples
                passed = False

        for g in range(len(guess)):
            if g not in used_guess:
                message += "\n\nEncoded incorrect constraint:\n %s" % guess[g].sat_tuples
                message += "\nInput board: %s\n" % str(b)
                passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_cages_2"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)

    def test_cages_3(self):
        start_time = time.time()
        
        global OUT_MSG

        global CAGE_POINTS

        board = (2,[(4, [(1, 1), (1, 2), (2, 1), (2, 2)],'*')])
        correct = test_cages_3_correct()

        message = ""
        passed = True
        try:
            b = deepcopy(board)
            csp, var_array = cagey_csp_model(b)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)

        guess = [c for c in csp.get_all_cons() if len(c.scope) == 5]
        
        answered = []
        used_guess = []
         
        normalized_guess = []
        # Flip if the first element is not a string.
        if not isinstance(guess[0].scope[0].dom[0], str):
            # flip the csp
            normalized_guess = []
            for g in guess:
                normalized_guess.append(Constraint(g.name, [g.scope[-1]] + g.scope[:-1]))
                rev_sat = []
                for s in g.sat_tuples:
                    rev_sat.append(((s[-1],) + s[:-1]))
                normalized_guess[-1].add_satisfying_tuples(rev_sat)
        else:
            normalized_guess = guess

        guess = normalized_guess

        for g in range(len(guess)):
            gue = guess[g]
            for a in range(len(correct)):
                ans = correct[a]
                if gue.sat_tuples == ans.sat_tuples and a not in answered:
                    CAGE_POINTS += 1.5
                    answered.append(a)
                    used_guess.append(g)

        for i in range(len(correct)):
            if i not in answered:
                message += "\n\nFailed to encode:\n %s" % correct[i].sat_tuples
                message += "\nInput board: %s\n" % str(b)
                passed = False

        for g in range(len(guess)):
            if g not in used_guess:
                message += "\n\nEncoded incorrect constraint:\n %s" % guess[g].sat_tuples
                passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_cages_3"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)

    def test_cages_4(self):
        start_time = time.time()
        
        global OUT_MSG

        global CAGE_POINTS

        board = (3,[(10, [(1, 1), (1, 2), (1, 3), (2, 1),(2, 2),(2, 3)], '+')])
        correct = test_cages_4_correct()

        message = ""
        passed = True
        try:
            b = deepcopy(board)
            csp, var_array = cagey_csp_model(b)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)

        guess = [c for c in csp.get_all_cons() if len(c.scope) == 7]
        answered = []
        used_guess = []

        normalized_guess = []
        # Flip if the first element is not a string.
        if not isinstance(guess[0].scope[0].dom[0], str):
            # flip the csp
            normalized_guess = []
            for g in guess:
                normalized_guess.append(Constraint(g.name, [g.scope[-1]] + g.scope[:-1]))
                rev_sat = []
                for s in g.sat_tuples:
                    rev_sat.append(((s[-1],) + s[:-1]))
                normalized_guess[-1].add_satisfying_tuples(rev_sat)
        else:
            normalized_guess = guess

        guess = normalized_guess

        for g in range(len(guess)):
            gue = guess[g]
            for a in range(len(correct)):
                ans = correct[a]
                if gue.sat_tuples == ans.sat_tuples and a not in answered:
                    CAGE_POINTS += 1.5
                    answered.append(a)
                    used_guess.append(g)

        for i in range(len(correct)):
            if i not in answered:
                message += "\n\nFailed to encode:\n %s" % correct[i].sat_tuples
                message += "\nInput board: %s\n" % str(b)
                passed = False

        for g in range(len(guess)):
            if g not in used_guess:
                message += "\n\nEncoded incorrect constraint:\n %s" % guess[g].sat_tuples
                passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_cages_4"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)

    def test_cages_5(self):
        start_time = time.time()
        
        global OUT_MSG

        global CAGE_POINTS

        board = (3, [(7, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)], '-')])
        correct = test_cages_5_correct()

        message = ""
        passed = True
        try:
            b = deepcopy(board)
            csp, var_array = cagey_csp_model(b)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)

        guess = [c for c in csp.get_all_cons() if len(c.scope) == 7]
        answered = []
        used_guess = []

        normalized_guess = []
        # Flip if the first element is not a string.
        if not isinstance(guess[0].scope[0].dom[0], str):
            # flip the csp
            normalized_guess = []
            for g in guess:
                normalized_guess.append(Constraint(g.name, [g.scope[-1]] + g.scope[:-1]))
                rev_sat = []
                for s in g.sat_tuples:
                    rev_sat.append(((s[-1],) + s[:-1]))
                normalized_guess[-1].add_satisfying_tuples(rev_sat)
        else:
            normalized_guess = guess

        guess = normalized_guess

        for g in range(len(guess)):
            gue = guess[g]
            for a in range(len(correct)):
                ans = correct[a]
                if gue.sat_tuples == ans.sat_tuples and a not in answered:
                    CAGE_POINTS += 1.5
                    answered.append(a)
                    used_guess.append(g)

        for i in range(len(correct)):
            if i not in answered:
                message += "\n\nFailed to encode:\n %s" % correct[i].sat_tuples
                message += "\nInput board: %s\n" % str(b)
                passed = False

        for g in range(len(guess)):
            if g not in used_guess:
                message += "\n\nEncoded incorrect constraint:\n %s" % guess[g].sat_tuples
                passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_cages_5"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)

    def test_cages_6(self):
        start_time = time.time()
        
        global OUT_MSG

        global CAGE_POINTS

        board = (3,[(10, [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)], '*')])
        correct = test_cages_6_correct()

        message = ""
        passed = True
        try:
            b = deepcopy(board)
            csp, var_array = cagey_csp_model(b)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to construct board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)

        guess = [c for c in csp.get_all_cons() if len(c.scope) == 7]
        answered = []
        used_guess = []

        normalized_guess = []
        # Flip if the first element is not a string.
        if not isinstance(guess[0].scope[0].dom[0], str):
            # flip the csp
            normalized_guess = []
            for g in guess:
                normalized_guess.append(Constraint(g.name, [g.scope[-1]] + g.scope[:-1]))
                rev_sat = []
                for s in g.sat_tuples:
                    rev_sat.append(((s[-1],) + s[:-1]))
                normalized_guess[-1].add_satisfying_tuples(rev_sat)
        else:
            normalized_guess = guess

        guess = normalized_guess

        for g in range(len(guess)):
            gue = guess[g]
            for a in range(len(correct)):
                ans = correct[a]
                if gue.sat_tuples == ans.sat_tuples and a not in answered:
                    CAGE_POINTS += 1.5
                    answered.append(a)
                    used_guess.append(g)

        for i in range(len(correct)):
            if i not in answered:
                message += "\n\nFailed to encode:\n %s" % correct[i].sat_tuples
                message += "\nInput board: %s\n" % str(b)
                passed = False

        for g in range(len(guess)):
            if g not in used_guess:
                message += "\n\nEncoded incorrect constraint:\n %s" % guess[g].sat_tuples
                passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = "test_cages_6"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)

## Propagators

boards = [ (3, [(3, [(1, 1), (2, 1)], '+'),
                (2, [(1, 2), (2, 2)], '-'),
                (6, [(1, 3), (2, 3), (3, 3)],'*'),
                (5, [(3, 1), (3, 2)], '+')]),
           (4, [(6, [(1, 1), (2, 1)], '*'),
                (3, [(1, 2), (1, 3)], '+'),
                (3, [(1, 4), (2, 4)], '-'),
                (7, [(2, 2), (2, 3)], '+'),
                (2, [(3, 1), (3, 2)], '/'),
                (3, [(3, 3), (4, 3)], '-'),
                (6, [(3, 4), (4, 4)], '*'),
                (7, [(4, 1), (4, 2)], '+')]),
           (4, [(16, [(1, 1), (1, 2), (2, 2)], '*'),
                (7, [(1, 3), (1, 4), (2, 3)], '+'),
                (4, [(2, 4)], '?'),
                (2, [(2, 1), (3, 1)], '-'),
                (2, [(3, 3), (3, 4)], '/'),
                (2, [(4, 3), (4, 4)], '/'),
                (12, [(3, 2), (4, 1), (4, 2)], '*')]),
           (4, [(4, [(1, 1)], '?'),
                (2, [(1, 2), (1, 3)], '/'),
                (1, [(1, 4), (2, 4)], '-'),
                (6, [(2, 1), (2, 2), (3, 2)], '+'),
                (12, [(2, 3), (3, 3), (3, 4)], '*'),
                (1, [(3, 1), (4, 1)], '-'),
                (5, [(4, 2), (4, 3)], '+'),
                (2, [(4, 4)], '?')]),
           (4, [(2, [(1, 1), (1, 2)], '/'),
                (3, [(1, 3), (1, 4), (2, 3)], '*'),
                (8, [(2, 1), (2, 2), (3, 1)], '+'),
                (6, [(2, 4), (3, 4)], '*'),
                (2, [(3, 2), (3, 3)], '-'),
                (2, [(4, 1), (4, 2)], '-'),
                (2, [(4, 3), (4, 4)], '/')]),
           (5, [(4, [(1, 1), (2, 1)], '-'),
                (2, [(1, 2), (1, 3)], '/'),
                (1, [(1, 4), (2, 4)], '-'),
                (1, [(1, 5), (2, 5)], '-'),
                (9, [(2, 2), (2, 3)], '+'),
                (3, [(3, 1), (3, 2)], '-'),
                (6, [(3, 3), (3, 4), (4, 4)], '*'),
                (9, [(3, 5), (4, 5)], '+'),
                (7, [(4, 1), (5, 1)], '+'),
                (3, [(4, 2), (4, 3)], '-'),
                (6, [(5, 2), (5, 3)], '*'),
                (4, [(5, 4), (5, 5)], '-')]),
           (5, [(10, [(1, 1), (1, 2), (2, 1), (2, 2)], '+'),
                (18, [(1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], '+'),
                (2, [(1, 5), (2, 5), (3, 5)], '-'),
                (1, [(3, 1), (3, 2), (3, 3)], '-'),
                (600, [(4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)], '*'),
                (2, [(4, 4), (5, 4), (5, 5)], '/'),
                (3, [(4, 5)], '?')]),
           (5, [(2, [(1, 1), (2, 1)], '-'),
                (2, [(1, 2), (1, 3)], '/'),
                (1, [(1, 4), (1, 5)], '-'),
                (1, [(2, 2)], '?'),
                (2, [(2, 3), (2, 4)], '-'),
                (9, [(2, 5), (3, 5), (4, 5)], '+'),
                (6, [(3, 1), (3, 2)], '*'),
                (4, [(3, 3)], '?'),
                (3, [(3, 4), (4, 4)], '+'),
                (3, [(4, 1), (5, 1)], '-'),
                (15, [(4, 2), (4, 3)], '*'),
                (9, [(5, 2), (5, 3)], '+'),
                (1, [(5, 4), (5, 5)], '-')]),
           (6, [(11, [(1, 1), (2, 1)], '+'),
                (2, [(1, 2), (1, 3)], '/'),
                (20, [(1, 4), (2, 4)], '*'),
                (6, [(1, 5), (1, 6), (2, 6), (3, 6)], '*'),
                (3, [(2, 2), (2, 3)], '-'),
                (3, [(2, 5), (3, 5)], '/'),
                (240, [(3, 1), (3, 2), (4, 1), (4, 2)], '*'),
                (6, [(3, 3), (3, 4)], '*'),
                (6, [(4, 3), (5, 3)], '*'),
                (7, [(4, 4), (5, 4), (5, 5)], '+'),
                (30, [(4, 5), (4, 6)], '*'),
                (6, [(5, 1), (5, 2)], '*'),
                (9, [(5, 6), (6, 6)], '+'),
                (8, [(6, 1), (6, 2), (6, 3)], '+'),
                (2, [(6, 4), (6, 5)], '/')]),
           (6, [(2, [(1, 1), (1, 2), (1, 3)], '/'),
                (3, [(1, 4), (1, 5)], '-'),
                (11, [(1, 6), (2, 6), (3, 6)], '+'),
                (2, [(2, 1), (2, 2), (2, 3)],'/'),
                (40, [(2, 4), (2, 5), (3, 4), (3, 5)], '*'),
                (14, [(3, 1), (4, 1), (5, 1), (6, 1)], '+'),
                (3600, [(3, 2), (3, 3), (4, 2), (4, 3), (5, 2), (5, 3)], '*'),
                (120, [(4, 4), (5, 4), (6, 4)], '*'),
                (1, [(4, 5), (4, 6), (5, 5), (5, 6)],'-'),
                (5, [(6, 2), (6, 3)], '-'),
                (5, [(6, 5), (6, 6)], '+')]) ]

## prop_FC

class TestPropFC(unittest.TestCase):
    def setUp(self):
        pass
        
    def prop_fc_bin_helper(self, b_num):
        start_time = time.time()
        
        global OUT_MSG

        global FC_POINTS
        message = ""
        passed = True
        b = boards[b_num]
        try:
            csp, var_array = bin_board_fixed(b_num)

            # solve csp
            solver = BT(csp)
            solver.quiet()
            solver.bt_search(prop_FC)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to solve board!\n%s\n" % b
            passed = False
            
        self.assertTrue(passed, message)
        if check_diff(var_array[:b[0]], b) == False:
            message += "\n\nFailed an all-diff check!"
            message += "Failed to solve board!\n%s\n" % b
            passed = False
            
        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = f"test_bin_prop_fc_{b_num}"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            FC_POINTS += 1
    

    def prop_fc_helper(self, b_num):
        start_time = time.time()
        
        global OUT_MSG

        global FC_POINTS
        message = ""
        passed = True
        b = boards[b_num]
        try:
            csp, var_array = cagey_cages_fixed(b_num)
                
            #solve csp
            solver = BT(csp)
            solver.quiet()
            solver.bt_search(prop_FC)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to solve board!\n%s\n" % str(b)
            passed = False

        self.assertTrue(passed, message)
        if check_diff(var_array[:b[0]],b) == False:
            message += "\n\nFailed an all-diff check!"
            message += "Failed to solve board!\n%s\n" % str(b)
            passed = False
        if check_cage(csp, b, var_array) == False:
            message += "\n\nFailed a cage check!"
            message += "Failed to solve board!\n%s\n" % str(b)
            passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = f"test_prop_fc_{b_num}"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            FC_POINTS += 1

    def test_prop_fc_0(self):
        self.prop_fc_helper(0)

    def test_prop_fc_1(self):
        self.prop_fc_helper(1)

    def test_prop_fc_2(self):
        self.prop_fc_helper(2)

    def test_prop_fc_3(self):
        self.prop_fc_helper(3)

    def test_prop_fc_4(self):
        self.prop_fc_helper(4)
        
    def test_bin_prop_fc_0(self):
        self.prop_fc_bin_helper(0)
        
    def test_bin_prop_fc_1(self):
        self.prop_fc_bin_helper(1)
        
    def test_bin_prop_fc_2(self):
        self.prop_fc_bin_helper(2)
        
    def test_bin_prop_fc_3(self):
        self.prop_fc_bin_helper(3)
        
    def test_bin_prop_fc_4(self):
        self.prop_fc_bin_helper(4)

## prop_GAC

class TestPropGAC(unittest.TestCase):
    def setUp(self):
        pass

    def prop_GAC_helper(self, b_num):
        start_time = time.time()
        
        global OUT_MSG

        global GAC_POINTS
        message = ""
        passed = True
        b = boards[b_num]
        try:
            csp, var_array = cagey_cages_fixed(b_num)

            #solve csp
            solver = BT(csp)
            solver.quiet()
            solver.bt_search(prop_GAC)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            message += "Failed to solve board!\n%s\n" %b
            passed = False

        self.assertTrue(passed, message)
        if check_diff(var_array[:b[0]],b) == False:
            message += "\n\nFailed an all-diff check!"
            message += "Failed to solve board!\n%s\n" %b
            passed = False
        if check_cage(csp, b, var_array) == False:
            message += "\n\nFailed a cage check!"
            message += "Failed to solve board!\n%s\n" %b
            passed = False

        end_time = time.time()
        time_spent = end_time-start_time
        
        test_name = f"test_prop_GAC_{b_num}"
        OUT_MSG += "%s: %.4fs\n" % (test_name, time_spent)
        print("%s done" % (test_name))
        if (time_spent>TIME_ALLOWED):
            passed = False
            message += "Over time!\n"

        self.assertTrue(passed, message)
        if passed:
            GAC_POINTS += 1

    def test_prop_GAC_0(self):
        self.prop_GAC_helper(0)

    def test_prop_GAC_1(self):
        self.prop_GAC_helper(1)

    def test_prop_GAC_2(self):
        self.prop_GAC_helper(2)

    def test_prop_GAC_3(self):
        self.prop_GAC_helper(3)

    def test_prop_GAC_4(self):
        self.prop_GAC_helper(4)

    def test_prop_GAC_5(self):
        self.prop_GAC_helper(5)

    def test_prop_GAC_6(self):
        self.prop_GAC_helper(6)

    def test_prop_GAC_7(self):
        self.prop_GAC_helper(7)

    def test_prop_GAC_8(self):
        self.prop_GAC_helper(8)

    def test_prop_GAC_9(self):
        self.prop_GAC_helper(9)

## Heuristics

## ord_mrv

class TestMRV(unittest.TestCase):
    def setUp(self):
        pass

    def test_mrv_1(self):
        start_time = time.time()
        
        global OUT_MSG

        global MRV_POINTS
        message = ""
        passed = True

        a = Variable('A', [1])
        b = Variable('B', [1])
        c = Variable('C', [1])
        d = Variable('D', [1])
        e = Variable('E', [1])

        simpleCSP = CSP("Simple", [a,b,c,d,e])

        count = 0
        for i in range(0,len(simpleCSP.vars)):
            simpleCSP.vars[count].add_domain_values(range(0, count))
            count += 1
        try:
            var = []
            var = ord_mrv(simpleCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:

            if var:
                if((var.name) == 'A'):
                    MRV_POINTS += 1
                else:
                    message += "Failed First Ord MRV Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord MRV"
                passed = False

        self.assertTrue(passed, message)

    def test_mrv_2(self):
        start_time = time.time()
        
        global OUT_MSG

        global MRV_POINTS
        message = ""
        passed = True

        a = Variable('A', [1,2,3,4,5])
        b = Variable('B', [1,2,3,4])
        c = Variable('C', [1,2])
        d = Variable('D', [1,2,3])
        e = Variable('E', [1])

        simpleCSP = CSP("Simple", [a,b,c,d,e])
        try:
            var = []
            var = ord_mrv(simpleCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:

            if var:
                if((var.name) == 'E'):
                    MRV_POINTS += 1
                else:
                    message += "Failed second Ord MRV Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord MRV"
                passed = False

        self.assertTrue(passed, message)


    def test_mrv_3(self):
        start_time = time.time()
        
        global OUT_MSG

        global MRV_POINTS
        message = ""
        passed = True

        a = Variable('A', [1,2])
        b = Variable('B', [1,2,3])
        c = Variable('C', [1,2,3])
        d = Variable('D', [1,2,3])
        e = Variable('E', [1,2])

        simpleCSP = CSP("Simple", [a,b,c,d,e])
        try:
            var = []
            var = ord_mrv(simpleCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:
            if var:
                if((var.name) == 'A' or (var.name) == 'E'):
                    MRV_POINTS += 1
                else:
                    message += "Failed third Ord MRV Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord MRV"
                passed = False

        self.assertTrue(passed, message)

    def test_mrv_4(self):
        start_time = time.time()
        
        global OUT_MSG

        global MRV_POINTS
        message = ""
        passed = True

        a = Variable('A', [1,2,3])
        b = Variable('B', [1,2,3])
        c = Variable('C', [1,2])
        d = Variable('D', [1,2,3])
        e = Variable('E', [1,2,3])

        simpleCSP = CSP("Simple", [a,b,c,d,e])
        try:
            var = []
            var = ord_mrv(simpleCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:
            if var:
                if((var.name) == 'C'):
                    MRV_POINTS += 1
                else:
                    message += "Failed fourth Ord MRV Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord MRV"
                passed = False

        self.assertTrue(passed, message)

## ord_dh

class TestDH(unittest.TestCase):
    def setUp(self):
        bin_sat_tuples = []
        for i in range(1,4):
            for j in range(1,4):
                if i == j:
                    continue
                bin_sat_tuples.append((i,j))

        a = Variable('WA', [1,2,3])
        b = Variable('NT', [1,2,3])
        c = Variable('SA', [1,2,3])
        d = Variable('Q', [1,2,3])
        e = Variable('NSW', [1,2,3])
        f = Variable('V', [1,2,3])
        g = Variable('T', [1,2,3])

        self.mapCSP = CSP("Map", [a,b,c,d,e,f,g])

        const_list = []
        c1 = Constraint("WA_NT",[a,b])
        c1.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c1)

        c2 = Constraint("WA_SA",[a,c])
        c2.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c2)

        c3 = Constraint("NT_SA",[b,c])
        c3.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c3)

        c4 = Constraint("NT_Q",[b,d])
        c4.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c4)

        c5 = Constraint("SA_Q",[c,d])
        c5.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c5)

        c6 = Constraint("SA_NSW",[c,e])
        c6.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c6)

        c7 = Constraint("SA_V",[c,f])
        c7.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c7)

        c8 = Constraint("Q_NSW",[d,e])
        c8.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c8)

        c9 = Constraint("NSW_V",[e,f])
        c9.add_satisfying_tuples(bin_sat_tuples)
        const_list.append(c9)

        for c in const_list:
            self.mapCSP.add_constraint(c)

        pass

    def test_dh_1(self):
        start_time = time.time()
        
        global OUT_MSG

        global DH_POINTS
        message = ""
        passed = True

        try:
            var = []
            var = ord_dh(self.mapCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:
            if var:
                if(var.name == 'SA'):
                    DH_POINTS += 1
                else:
                    message += "Failed first DH Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord DH"
                passed = False

        self.assertTrue(passed, message)

    def test_dh_2(self):
        start_time = time.time()
        
        global OUT_MSG

        global DH_POINTS
        message = ""
        passed = True

        self.mapCSP.vars[2].assign(1) #assign SA

        try:
            var = []
            var = ord_dh(self.mapCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:
            if var:
                if(var.name == 'NT' or var.name == 'Q' or var.name == 'NSW'):
                    DH_POINTS += 1
                else:
                    message += "Failed second DH Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord DH"
                passed = False

        self.assertTrue(passed, message)

    def test_dh_3(self):
        start_time = time.time()
        
        global OUT_MSG

        global DH_POINTS
        message = ""
        passed = True

        self.mapCSP.vars[2].assign(1) # assign SA
        self.mapCSP.vars[4].assign(2) # assign NSW
        self.mapCSP.vars[5].assign(3) # assign V

        try:
            var = []
            var = ord_dh(self.mapCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:
            if var:
                if(var.name == 'NT'):
                    DH_POINTS += 1
                else:
                    message += "Failed third DH Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord DH"
                passed = False

        self.assertTrue(passed, message)

    def test_dh_4(self):
        start_time = time.time()
        
        global OUT_MSG

        global DH_POINTS
        message = ""
        passed = True

        self.mapCSP.vars[2].assign(1) #assign SA
        self.mapCSP.vars[4].assign(2) # assign NSW
        self.mapCSP.vars[5].assign(3) #assign V
        self.mapCSP.vars[3].assign(3) # assign Q
        self.mapCSP.vars[1].assign(2) # assign NT
        self.mapCSP.vars[0].assign(3) #assign WA

        try:
            var = []
            var = ord_dh(self.mapCSP)
        except Exception as e:
            message += "\n\nStudent code threw exception \"%s\". " % e
            passed = False
        else:
            if var:
                if(var.name == 'T'):
                    DH_POINTS += 1
                else:
                    message += "Failed fourth DH Test"
                    passed = False
            else:
                message += "No Variable Returned from Ord DH"
                passed = False

        self.assertTrue(passed, message)

def main(verbosity=2):
    global OUT_MSG
    file_name = "results.txt"
    with open(file_name, "a") as out:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(out, verbosity=verbosity, resultclass=NoTraceResult).run(suite)
        binary_score = (BINARY_POINTS/5.0)*BINARY_FULL
        nary_score = (NARY_POINTS/4.0)*NARY_FULL
        cage_score = (CAGE_POINTS/12.0)*CAGE_FULL
        fc_score = (FC_POINTS/10.0)*FC_FULL
        gac_score = (GAC_POINTS/10.0)*GAC_FULL
        mrv_score = (MRV_POINTS/4.0)*MRV_FULL
        dh_score = (DH_POINTS/4.0)*DH_FULL
        total_score = binary_score + nary_score + cage_score + fc_score + gac_score + mrv_score + dh_score
        total_full = BINARY_FULL + NARY_FULL + CAGE_FULL + FC_FULL + GAC_FULL + MRV_FULL + DH_FULL

        OUT_MSG += ("----------------------------------------------------------------------")
        OUT_MSG += ("\nGrades:\n\n")
        OUT_MSG += (f"FC: {fc_score}/{FC_FULL}\n")
        OUT_MSG += (f"GAC: {gac_score}/{GAC_FULL}\n")
        OUT_MSG += (f"MRV: {mrv_score}/{MRV_FULL}\n")
        OUT_MSG += (f"DH: {dh_score}/{DH_FULL}\n")
        OUT_MSG += (f"BINARY: {binary_score}/{BINARY_FULL}\n")
        OUT_MSG += (f"NARY: {nary_score}/{NARY_FULL}\n")
        OUT_MSG += (f"CAGEY: {cage_score}/{CAGE_FULL}\n\n")
        OUT_MSG += (f"TOTAL: {total_score}/{total_full}\n")
        OUT_MSG += (f"Code quality: ?/0.5\n")

        print(OUT_MSG)

        running_time = time.strftime("%Y_%m_%d-%H:%M:%S")
        OUT_MSG += (f"\nRunning time: {running_time}\n\n")
        OUT_MSG += ("===========================================\n")

        out.write(OUT_MSG)

if __name__ == '__main__':
    main()
    