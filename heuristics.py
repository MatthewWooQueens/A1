# =============================
# Student Names: Justin Woo, Attila Tavakolli, Matthew Woo
# Group ID: 69
# Date: January 22, 2023
# =============================
# CISC 352 - W23
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return variables according to the Degree Heuristic '''
    # IMPLEMENT
    vars = csp.get_all_unasgn_vars()
    big = (vars[0], 0)
    for var in vars:
        cons = csp.get_cons_with_var(var)
        num = 0
        for con in cons:
        #Greater than 1 as there must be another unassigned var in constraint beside current var
            if con.get_n_unasgn() > 1:
                num += 1
        if num > big[1]:
            big = (var, num)
    return big[0]

def ord_mrv(csp):
    ''' return variable according to the Minimum Remaining Values heuristic '''
    # IMPLEMENT
    ordList = csp.get_all_unasgn_vars()
    next = ordList[0]
    for var in ordList:
        if len(var.cur_domain()) < len(next.cur_domain()):
            next = var
    return next
