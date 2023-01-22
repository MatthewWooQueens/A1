from cspbase import *

def test_bne_grid_1_answer_binary():

    scope0 = [Variable("V11", [1, 2, 3]), Variable("V12", [1, 2, 3])]
    scope1 = [Variable("V11", [1, 2, 3]), Variable("V13", [1, 2, 3])]
    scope2 = [Variable("V11", [1, 2, 3]), Variable("V21", [1, 2, 3])]
    scope3 = [Variable("V11", [1, 2, 3]), Variable("V31", [1, 2, 3])]
    scope4 = [Variable("V12", [1, 2, 3]), Variable("V13", [1, 2, 3])]
    scope5 = [Variable("V12", [1, 2, 3]), Variable("V22", [1, 2, 3])]
    scope6 = [Variable("V12", [1, 2, 3]), Variable("V32", [1, 2, 3])]
    scope7 = [Variable("V13", [1, 2, 3]), Variable("V23", [1, 2, 3])]
    scope8 = [Variable("V13", [1, 2, 3]), Variable("V33", [1, 2, 3])]
    scope9 = [Variable("V21", [1, 2, 3]), Variable("V22", [1, 2, 3])]
    scope10 = [Variable("V21", [1, 2, 3]), Variable("V23", [1, 2, 3])]
    scope11 = [Variable("V21", [1, 2, 3]), Variable("V31", [1, 2, 3])]
    scope12 = [Variable("V22", [1, 2, 3]), Variable("V23", [1, 2, 3])]
    scope13 = [Variable("V22", [1, 2, 3]), Variable("V32", [1, 2, 3])]
    scope14 = [Variable("V23", [1, 2, 3]), Variable("V33", [1, 2, 3])]
    scope15 = [Variable("V31", [1, 2, 3]), Variable("V32", [1, 2, 3])]
    scope16 = [Variable("V31", [1, 2, 3]), Variable("V33", [1, 2, 3])]
    scope17 = [Variable("V32", [1, 2, 3]), Variable("V33", [1, 2, 3])]

    con0 = Constraint("NE(V11V12)", scope0)
    con1 = Constraint("NE(V11V13)", scope1)
    con2 = Constraint("NE(V11V21)", scope2)
    con3 = Constraint("NE(V11V31)", scope3)
    con4 = Constraint("NE(V12V13)", scope4)
    con5 = Constraint("NE(V12V22)", scope5)
    con6 = Constraint("NE(V12V32)", scope6)
    con7 = Constraint("NE(V13V23)", scope7)
    con8 = Constraint("NE(V13V33)", scope8)
    con9 = Constraint("NE(V21V22)", scope9)
    con10 = Constraint("NE(V21V23)", scope10)
    con11 = Constraint("NE(V21V31)", scope11)
    con12 = Constraint("NE(V22V23)", scope12)
    con13 = Constraint("NE(V22V32)", scope13)
    con14 = Constraint("NE(V23V33)", scope14)
    con15 = Constraint("NE(V31V32)", scope15)
    con16 = Constraint("NE(V31V33)", scope16)
    con17 = Constraint("NE(V32V33)", scope17)

    con0.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con1.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con2.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con3.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con4.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con5.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con6.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con7.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con8.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con9.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con10.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con11.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con12.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con13.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con14.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con15.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con16.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con17.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])

    answer = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17]

    return answer

def test_bne_grid_2_answer_binary():

    scope0 = [Variable("V11", [1, 2, 3]), Variable("V12", [1, 2, 3])]
    scope1 = [Variable("V11", [1, 2, 3]), Variable("V13", [1, 2, 3])]
    scope2 = [Variable("V11", [1, 2, 3]), Variable("V21", [1, 2, 3])]
    scope3 = [Variable("V11", [1, 2, 3]), Variable("V31", [1, 2, 3])]
    scope4 = [Variable("V12", [1, 2, 3]), Variable("V13", [1, 2, 3])]
    scope5 = [Variable("V12", [1, 2, 3]), Variable("V22", [1, 2, 3])]
    scope6 = [Variable("V12", [1, 2, 3]), Variable("V32", [1, 2, 3])]
    scope7 = [Variable("V13", [1, 2, 3]), Variable("V23", [1, 2, 3])]
    scope8 = [Variable("V13", [1, 2, 3]), Variable("V33", [1, 2, 3])]
    scope9 = [Variable("V21", [1, 2, 3]), Variable("V22", [1, 2, 3])]
    scope10 = [Variable("V21", [1, 2, 3]), Variable("V23", [1, 2, 3])]
    scope11 = [Variable("V21", [1, 2, 3]), Variable("V31", [1, 2, 3])]
    scope12 = [Variable("V22", [1, 2, 3]), Variable("V23", [1, 2, 3])]
    scope13 = [Variable("V22", [1, 2, 3]), Variable("V32", [1, 2, 3])]
    scope14 = [Variable("V23", [1, 2, 3]), Variable("V33", [1, 2, 3])]
    scope15 = [Variable("V31", [1, 2, 3]), Variable("V32", [1, 2, 3])]
    scope16 = [Variable("V31", [1, 2, 3]), Variable("V33", [1, 2, 3])]
    scope17 = [Variable("V32", [1, 2, 3]), Variable("V33", [1, 2, 3])]

    con0 = Constraint("NE(V11V12)", scope0)
    con1 = Constraint("NE(V11V13)", scope1)
    con2 = Constraint("NE(V11V21)", scope2)
    con3 = Constraint("NE(V11V31)", scope3)
    con4 = Constraint("NE(V12V13)", scope4)
    con5 = Constraint("NE(V12V22)", scope5)
    con6 = Constraint("NE(V12V32)", scope6)
    con7 = Constraint("NE(V13V23)", scope7)
    con8 = Constraint("NE(V13V33)", scope8)
    con9 = Constraint("NE(V21V22)", scope9)
    con10 = Constraint("NE(V21V23)", scope10)
    con11 = Constraint("NE(V21V31)", scope11)
    con12 = Constraint("NE(V22V23)", scope12)
    con13 = Constraint("NE(V22V32)", scope13)
    con14 = Constraint("NE(V23V33)", scope14)
    con15 = Constraint("NE(V31V32)", scope15)
    con16 = Constraint("NE(V31V33)", scope16)
    con17 = Constraint("NE(V32V33)", scope17)

    con0.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con1.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con2.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con3.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con4.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con5.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con6.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con7.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con8.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con9.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con10.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con11.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con12.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con13.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con14.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con15.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con16.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
    con17.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])

    answer = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17]

    return answer

def test_bne_grid_3_answer_binary():

    scope0 = [Variable("V11", [1, 2, 3, 4]), Variable("V12", [1, 2, 3, 4])]
    scope1 = [Variable("V11", [1, 2, 3, 4]), Variable("V13", [1, 2, 3, 4])]
    scope2 = [Variable("V11", [1, 2, 3, 4]), Variable("V14", [1, 2, 3, 4])]
    scope3 = [Variable("V11", [1, 2, 3, 4]), Variable("V21", [1, 2, 3, 4])]
    scope4 = [Variable("V11", [1, 2, 3, 4]), Variable("V31", [1, 2, 3, 4])]
    scope5 = [Variable("V11", [1, 2, 3, 4]), Variable("V41", [1, 2, 3, 4])]
    scope6 = [Variable("V12", [1, 2, 3, 4]), Variable("V13", [1, 2, 3, 4])]
    scope7 = [Variable("V12", [1, 2, 3, 4]), Variable("V14", [1, 2, 3, 4])]
    scope8 = [Variable("V12", [1, 2, 3, 4]), Variable("V22", [1, 2, 3, 4])]
    scope9 = [Variable("V12", [1, 2, 3, 4]), Variable("V32", [1, 2, 3, 4])]
    scope10 = [Variable("V12", [1, 2, 3, 4]), Variable("V42", [1, 2, 3, 4])]
    scope11 = [Variable("V13", [1, 2, 3, 4]), Variable("V14", [1, 2, 3, 4])]
    scope12 = [Variable("V13", [1, 2, 3, 4]), Variable("V23", [1, 2, 3, 4])]
    scope13 = [Variable("V13", [1, 2, 3, 4]), Variable("V33", [1, 2, 3, 4])]
    scope14 = [Variable("V13", [1, 2, 3, 4]), Variable("V43", [1, 2, 3, 4])]
    scope15 = [Variable("V14", [1, 2, 3, 4]), Variable("V24", [1, 2, 3, 4])]
    scope16 = [Variable("V14", [1, 2, 3, 4]), Variable("V34", [1, 2, 3, 4])]
    scope17 = [Variable("V14", [1, 2, 3, 4]), Variable("V44", [1, 2, 3, 4])]
    scope18 = [Variable("V21", [1, 2, 3, 4]), Variable("V22", [1, 2, 3, 4])]
    scope19 = [Variable("V21", [1, 2, 3, 4]), Variable("V23", [1, 2, 3, 4])]
    scope20 = [Variable("V21", [1, 2, 3, 4]), Variable("V24", [1, 2, 3, 4])]
    scope21 = [Variable("V21", [1, 2, 3, 4]), Variable("V31", [1, 2, 3, 4])]
    scope22 = [Variable("V21", [1, 2, 3, 4]), Variable("V41", [1, 2, 3, 4])]
    scope23 = [Variable("V22", [1, 2, 3, 4]), Variable("V23", [1, 2, 3, 4])]
    scope24 = [Variable("V22", [1, 2, 3, 4]), Variable("V24", [1, 2, 3, 4])]
    scope25 = [Variable("V22", [1, 2, 3, 4]), Variable("V32", [1, 2, 3, 4])]
    scope26 = [Variable("V22", [1, 2, 3, 4]), Variable("V42", [1, 2, 3, 4])]
    scope27 = [Variable("V23", [1, 2, 3, 4]), Variable("V24", [1, 2, 3, 4])]
    scope28 = [Variable("V23", [1, 2, 3, 4]), Variable("V33", [1, 2, 3, 4])]
    scope29 = [Variable("V23", [1, 2, 3, 4]), Variable("V43", [1, 2, 3, 4])]
    scope30 = [Variable("V24", [1, 2, 3, 4]), Variable("V34", [1, 2, 3, 4])]
    scope31 = [Variable("V24", [1, 2, 3, 4]), Variable("V44", [1, 2, 3, 4])]
    scope32 = [Variable("V31", [1, 2, 3, 4]), Variable("V32", [1, 2, 3, 4])]
    scope33 = [Variable("V31", [1, 2, 3, 4]), Variable("V33", [1, 2, 3, 4])]
    scope34 = [Variable("V31", [1, 2, 3, 4]), Variable("V34", [1, 2, 3, 4])]
    scope35 = [Variable("V31", [1, 2, 3, 4]), Variable("V41", [1, 2, 3, 4])]
    scope36 = [Variable("V32", [1, 2, 3, 4]), Variable("V33", [1, 2, 3, 4])]
    scope37 = [Variable("V32", [1, 2, 3, 4]), Variable("V34", [1, 2, 3, 4])]
    scope38 = [Variable("V32", [1, 2, 3, 4]), Variable("V42", [1, 2, 3, 4])]
    scope39 = [Variable("V33", [1, 2, 3, 4]), Variable("V34", [1, 2, 3, 4])]
    scope40 = [Variable("V33", [1, 2, 3, 4]), Variable("V43", [1, 2, 3, 4])]
    scope41 = [Variable("V34", [1, 2, 3, 4]), Variable("V44", [1, 2, 3, 4])]
    scope42 = [Variable("V41", [1, 2, 3, 4]), Variable("V42", [1, 2, 3, 4])]
    scope43 = [Variable("V41", [1, 2, 3, 4]), Variable("V43", [1, 2, 3, 4])]
    scope44 = [Variable("V41", [1, 2, 3, 4]), Variable("V44", [1, 2, 3, 4])]
    scope45 = [Variable("V42", [1, 2, 3, 4]), Variable("V43", [1, 2, 3, 4])]
    scope46 = [Variable("V42", [1, 2, 3, 4]), Variable("V44", [1, 2, 3, 4])]
    scope47 = [Variable("V43", [1, 2, 3, 4]), Variable("V44", [1, 2, 3, 4])]

    con0 = Constraint("NE(V11V12)", scope0)
    con1 = Constraint("NE(V11V13)", scope1)
    con2 = Constraint("NE(V11V14)", scope2)
    con3 = Constraint("NE(V11V21)", scope3)
    con4 = Constraint("NE(V11V31)", scope4)
    con5 = Constraint("NE(V11V41)", scope5)
    con6 = Constraint("NE(V12V13)", scope6)
    con7 = Constraint("NE(V12V14)", scope7)
    con8 = Constraint("NE(V12V22)", scope8)
    con9 = Constraint("NE(V12V32)", scope9)
    con10 = Constraint("NE(V12V42)", scope10)
    con11 = Constraint("NE(V13V14)", scope11)
    con12 = Constraint("NE(V13V23)", scope12)
    con13 = Constraint("NE(V13V33)", scope13)
    con14 = Constraint("NE(V13V43)", scope14)
    con15 = Constraint("NE(V14V24)", scope15)
    con16 = Constraint("NE(V14V34)", scope16)
    con17 = Constraint("NE(V14V44)", scope17)
    con18 = Constraint("NE(V21V22)", scope18)
    con19 = Constraint("NE(V21V23)", scope19)
    con20 = Constraint("NE(V21V24)", scope20)
    con21 = Constraint("NE(V21V31)", scope21)
    con22 = Constraint("NE(V21V41)", scope22)
    con23 = Constraint("NE(V22V23)", scope23)
    con24 = Constraint("NE(V22V24)", scope24)
    con25 = Constraint("NE(V22V32)", scope25)
    con26 = Constraint("NE(V22V42)", scope26)
    con27 = Constraint("NE(V23V24)", scope27)
    con28 = Constraint("NE(V23V33)", scope28)
    con29 = Constraint("NE(V23V43)", scope29)
    con30 = Constraint("NE(V24V34)", scope30)
    con31 = Constraint("NE(V24V44)", scope31)
    con32 = Constraint("NE(V31V32)", scope32)
    con33 = Constraint("NE(V31V33)", scope33)
    con34 = Constraint("NE(V31V34)", scope34)
    con35 = Constraint("NE(V31V41)", scope35)
    con36 = Constraint("NE(V32V33)", scope36)
    con37 = Constraint("NE(V32V34)", scope37)
    con38 = Constraint("NE(V32V42)", scope38)
    con39 = Constraint("NE(V33V34)", scope39)
    con40 = Constraint("NE(V33V43)", scope40)
    con41 = Constraint("NE(V34V44)", scope41)
    con42 = Constraint("NE(V41V42)", scope42)
    con43 = Constraint("NE(V41V43)", scope43)
    con44 = Constraint("NE(V41V44)", scope44)
    con45 = Constraint("NE(V42V43)", scope45)
    con46 = Constraint("NE(V42V44)", scope46)
    con47 = Constraint("NE(V43V44)", scope47)

    con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
    con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])

    answer = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47]

    return answer

def test_bne_grid_4_answer_binary():

    scope0 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V12", [1, 2, 3, 4, 5])]
    scope1 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V13", [1, 2, 3, 4, 5])]
    scope2 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V14", [1, 2, 3, 4, 5])]
    scope3 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V15", [1, 2, 3, 4, 5])]
    scope4 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V21", [1, 2, 3, 4, 5])]
    scope5 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V31", [1, 2, 3, 4, 5])]
    scope6 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V41", [1, 2, 3, 4, 5])]
    scope7 = [Variable("V11", [1, 2, 3, 4, 5]), Variable("V51", [1, 2, 3, 4, 5])]
    scope8 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V13", [1, 2, 3, 4, 5])]
    scope9 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V14", [1, 2, 3, 4, 5])]
    scope10 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V15", [1, 2, 3, 4, 5])]
    scope11 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V22", [1, 2, 3, 4, 5])]
    scope12 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V32", [1, 2, 3, 4, 5])]
    scope13 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V42", [1, 2, 3, 4, 5])]
    scope14 = [Variable("V12", [1, 2, 3, 4, 5]), Variable("V52", [1, 2, 3, 4, 5])]
    scope15 = [Variable("V13", [1, 2, 3, 4, 5]), Variable("V14", [1, 2, 3, 4, 5])]
    scope16 = [Variable("V13", [1, 2, 3, 4, 5]), Variable("V15", [1, 2, 3, 4, 5])]
    scope17 = [Variable("V13", [1, 2, 3, 4, 5]), Variable("V23", [1, 2, 3, 4, 5])]
    scope18 = [Variable("V13", [1, 2, 3, 4, 5]), Variable("V33", [1, 2, 3, 4, 5])]
    scope19 = [Variable("V13", [1, 2, 3, 4, 5]), Variable("V43", [1, 2, 3, 4, 5])]
    scope20 = [Variable("V13", [1, 2, 3, 4, 5]), Variable("V53", [1, 2, 3, 4, 5])]
    scope21 = [Variable("V14", [1, 2, 3, 4, 5]), Variable("V15", [1, 2, 3, 4, 5])]
    scope22 = [Variable("V14", [1, 2, 3, 4, 5]), Variable("V24", [1, 2, 3, 4, 5])]
    scope23 = [Variable("V14", [1, 2, 3, 4, 5]), Variable("V34", [1, 2, 3, 4, 5])]
    scope24 = [Variable("V14", [1, 2, 3, 4, 5]), Variable("V44", [1, 2, 3, 4, 5])]
    scope25 = [Variable("V14", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope26 = [Variable("V15", [1, 2, 3, 4, 5]), Variable("V25", [1, 2, 3, 4, 5])]
    scope27 = [Variable("V15", [1, 2, 3, 4, 5]), Variable("V35", [1, 2, 3, 4, 5])]
    scope28 = [Variable("V15", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope29 = [Variable("V15", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope30 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V22", [1, 2, 3, 4, 5])]
    scope31 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V23", [1, 2, 3, 4, 5])]
    scope32 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V24", [1, 2, 3, 4, 5])]
    scope33 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V25", [1, 2, 3, 4, 5])]
    scope34 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V31", [1, 2, 3, 4, 5])]
    scope35 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V41", [1, 2, 3, 4, 5])]
    scope36 = [Variable("V21", [1, 2, 3, 4, 5]), Variable("V51", [1, 2, 3, 4, 5])]
    scope37 = [Variable("V22", [1, 2, 3, 4, 5]), Variable("V23", [1, 2, 3, 4, 5])]
    scope38 = [Variable("V22", [1, 2, 3, 4, 5]), Variable("V24", [1, 2, 3, 4, 5])]
    scope39 = [Variable("V22", [1, 2, 3, 4, 5]), Variable("V25", [1, 2, 3, 4, 5])]
    scope40 = [Variable("V22", [1, 2, 3, 4, 5]), Variable("V32", [1, 2, 3, 4, 5])]
    scope41 = [Variable("V22", [1, 2, 3, 4, 5]), Variable("V42", [1, 2, 3, 4, 5])]
    scope42 = [Variable("V22", [1, 2, 3, 4, 5]), Variable("V52", [1, 2, 3, 4, 5])]
    scope43 = [Variable("V23", [1, 2, 3, 4, 5]), Variable("V24", [1, 2, 3, 4, 5])]
    scope44 = [Variable("V23", [1, 2, 3, 4, 5]), Variable("V25", [1, 2, 3, 4, 5])]
    scope45 = [Variable("V23", [1, 2, 3, 4, 5]), Variable("V33", [1, 2, 3, 4, 5])]
    scope46 = [Variable("V23", [1, 2, 3, 4, 5]), Variable("V43", [1, 2, 3, 4, 5])]
    scope47 = [Variable("V23", [1, 2, 3, 4, 5]), Variable("V53", [1, 2, 3, 4, 5])]
    scope48 = [Variable("V24", [1, 2, 3, 4, 5]), Variable("V25", [1, 2, 3, 4, 5])]
    scope49 = [Variable("V24", [1, 2, 3, 4, 5]), Variable("V34", [1, 2, 3, 4, 5])]
    scope50 = [Variable("V24", [1, 2, 3, 4, 5]), Variable("V44", [1, 2, 3, 4, 5])]
    scope51 = [Variable("V24", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope52 = [Variable("V25", [1, 2, 3, 4, 5]), Variable("V35", [1, 2, 3, 4, 5])]
    scope53 = [Variable("V25", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope54 = [Variable("V25", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope55 = [Variable("V31", [1, 2, 3, 4, 5]), Variable("V32", [1, 2, 3, 4, 5])]
    scope56 = [Variable("V31", [1, 2, 3, 4, 5]), Variable("V33", [1, 2, 3, 4, 5])]
    scope57 = [Variable("V31", [1, 2, 3, 4, 5]), Variable("V34", [1, 2, 3, 4, 5])]
    scope58 = [Variable("V31", [1, 2, 3, 4, 5]), Variable("V35", [1, 2, 3, 4, 5])]
    scope59 = [Variable("V31", [1, 2, 3, 4, 5]), Variable("V41", [1, 2, 3, 4, 5])]
    scope60 = [Variable("V31", [1, 2, 3, 4, 5]), Variable("V51", [1, 2, 3, 4, 5])]
    scope61 = [Variable("V32", [1, 2, 3, 4, 5]), Variable("V33", [1, 2, 3, 4, 5])]
    scope62 = [Variable("V32", [1, 2, 3, 4, 5]), Variable("V34", [1, 2, 3, 4, 5])]
    scope63 = [Variable("V32", [1, 2, 3, 4, 5]), Variable("V35", [1, 2, 3, 4, 5])]
    scope64 = [Variable("V32", [1, 2, 3, 4, 5]), Variable("V42", [1, 2, 3, 4, 5])]
    scope65 = [Variable("V32", [1, 2, 3, 4, 5]), Variable("V52", [1, 2, 3, 4, 5])]
    scope66 = [Variable("V33", [1, 2, 3, 4, 5]), Variable("V34", [1, 2, 3, 4, 5])]
    scope67 = [Variable("V33", [1, 2, 3, 4, 5]), Variable("V35", [1, 2, 3, 4, 5])]
    scope68 = [Variable("V33", [1, 2, 3, 4, 5]), Variable("V43", [1, 2, 3, 4, 5])]
    scope69 = [Variable("V33", [1, 2, 3, 4, 5]), Variable("V53", [1, 2, 3, 4, 5])]
    scope70 = [Variable("V34", [1, 2, 3, 4, 5]), Variable("V35", [1, 2, 3, 4, 5])]
    scope71 = [Variable("V34", [1, 2, 3, 4, 5]), Variable("V44", [1, 2, 3, 4, 5])]
    scope72 = [Variable("V34", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope73 = [Variable("V35", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope74 = [Variable("V35", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope75 = [Variable("V41", [1, 2, 3, 4, 5]), Variable("V42", [1, 2, 3, 4, 5])]
    scope76 = [Variable("V41", [1, 2, 3, 4, 5]), Variable("V43", [1, 2, 3, 4, 5])]
    scope77 = [Variable("V41", [1, 2, 3, 4, 5]), Variable("V44", [1, 2, 3, 4, 5])]
    scope78 = [Variable("V41", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope79 = [Variable("V41", [1, 2, 3, 4, 5]), Variable("V51", [1, 2, 3, 4, 5])]
    scope80 = [Variable("V42", [1, 2, 3, 4, 5]), Variable("V43", [1, 2, 3, 4, 5])]
    scope81 = [Variable("V42", [1, 2, 3, 4, 5]), Variable("V44", [1, 2, 3, 4, 5])]
    scope82 = [Variable("V42", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope83 = [Variable("V42", [1, 2, 3, 4, 5]), Variable("V52", [1, 2, 3, 4, 5])]
    scope84 = [Variable("V43", [1, 2, 3, 4, 5]), Variable("V44", [1, 2, 3, 4, 5])]
    scope85 = [Variable("V43", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope86 = [Variable("V43", [1, 2, 3, 4, 5]), Variable("V53", [1, 2, 3, 4, 5])]
    scope87 = [Variable("V44", [1, 2, 3, 4, 5]), Variable("V45", [1, 2, 3, 4, 5])]
    scope88 = [Variable("V44", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope89 = [Variable("V45", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope90 = [Variable("V51", [1, 2, 3, 4, 5]), Variable("V52", [1, 2, 3, 4, 5])]
    scope91 = [Variable("V51", [1, 2, 3, 4, 5]), Variable("V53", [1, 2, 3, 4, 5])]
    scope92 = [Variable("V51", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope93 = [Variable("V51", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope94 = [Variable("V52", [1, 2, 3, 4, 5]), Variable("V53", [1, 2, 3, 4, 5])]
    scope95 = [Variable("V52", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope96 = [Variable("V52", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope97 = [Variable("V53", [1, 2, 3, 4, 5]), Variable("V54", [1, 2, 3, 4, 5])]
    scope98 = [Variable("V53", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]
    scope99 = [Variable("V54", [1, 2, 3, 4, 5]), Variable("V55", [1, 2, 3, 4, 5])]

    con0 = Constraint("NE(V11V12)", scope0)
    con1 = Constraint("NE(V11V13)", scope1)
    con2 = Constraint("NE(V11V14)", scope2)
    con3 = Constraint("NE(V11V15)", scope3)
    con4 = Constraint("NE(V11V21)", scope4)
    con5 = Constraint("NE(V11V31)", scope5)
    con6 = Constraint("NE(V11V41)", scope6)
    con7 = Constraint("NE(V11V51)", scope7)
    con8 = Constraint("NE(V12V13)", scope8)
    con9 = Constraint("NE(V12V14)", scope9)
    con10 = Constraint("NE(V12V15)", scope10)
    con11 = Constraint("NE(V12V22)", scope11)
    con12 = Constraint("NE(V12V32)", scope12)
    con13 = Constraint("NE(V12V42)", scope13)
    con14 = Constraint("NE(V12V52)", scope14)
    con15 = Constraint("NE(V13V14)", scope15)
    con16 = Constraint("NE(V13V15)", scope16)
    con17 = Constraint("NE(V13V23)", scope17)
    con18 = Constraint("NE(V13V33)", scope18)
    con19 = Constraint("NE(V13V43)", scope19)
    con20 = Constraint("NE(V13V53)", scope20)
    con21 = Constraint("NE(V14V15)", scope21)
    con22 = Constraint("NE(V14V24)", scope22)
    con23 = Constraint("NE(V14V34)", scope23)
    con24 = Constraint("NE(V14V44)", scope24)
    con25 = Constraint("NE(V14V54)", scope25)
    con26 = Constraint("NE(V15V25)", scope26)
    con27 = Constraint("NE(V15V35)", scope27)
    con28 = Constraint("NE(V15V45)", scope28)
    con29 = Constraint("NE(V15V55)", scope29)
    con30 = Constraint("NE(V21V22)", scope30)
    con31 = Constraint("NE(V21V23)", scope31)
    con32 = Constraint("NE(V21V24)", scope32)
    con33 = Constraint("NE(V21V25)", scope33)
    con34 = Constraint("NE(V21V31)", scope34)
    con35 = Constraint("NE(V21V41)", scope35)
    con36 = Constraint("NE(V21V51)", scope36)
    con37 = Constraint("NE(V22V23)", scope37)
    con38 = Constraint("NE(V22V24)", scope38)
    con39 = Constraint("NE(V22V25)", scope39)
    con40 = Constraint("NE(V22V32)", scope40)
    con41 = Constraint("NE(V22V42)", scope41)
    con42 = Constraint("NE(V22V52)", scope42)
    con43 = Constraint("NE(V23V24)", scope43)
    con44 = Constraint("NE(V23V25)", scope44)
    con45 = Constraint("NE(V23V33)", scope45)
    con46 = Constraint("NE(V23V43)", scope46)
    con47 = Constraint("NE(V23V53)", scope47)
    con48 = Constraint("NE(V24V25)", scope48)
    con49 = Constraint("NE(V24V34)", scope49)
    con50 = Constraint("NE(V24V44)", scope50)
    con51 = Constraint("NE(V24V54)", scope51)
    con52 = Constraint("NE(V25V35)", scope52)
    con53 = Constraint("NE(V25V45)", scope53)
    con54 = Constraint("NE(V25V55)", scope54)
    con55 = Constraint("NE(V31V32)", scope55)
    con56 = Constraint("NE(V31V33)", scope56)
    con57 = Constraint("NE(V31V34)", scope57)
    con58 = Constraint("NE(V31V35)", scope58)
    con59 = Constraint("NE(V31V41)", scope59)
    con60 = Constraint("NE(V31V51)", scope60)
    con61 = Constraint("NE(V32V33)", scope61)
    con62 = Constraint("NE(V32V34)", scope62)
    con63 = Constraint("NE(V32V35)", scope63)
    con64 = Constraint("NE(V32V42)", scope64)
    con65 = Constraint("NE(V32V52)", scope65)
    con66 = Constraint("NE(V33V34)", scope66)
    con67 = Constraint("NE(V33V35)", scope67)
    con68 = Constraint("NE(V33V43)", scope68)
    con69 = Constraint("NE(V33V53)", scope69)
    con70 = Constraint("NE(V34V35)", scope70)
    con71 = Constraint("NE(V34V44)", scope71)
    con72 = Constraint("NE(V34V54)", scope72)
    con73 = Constraint("NE(V35V45)", scope73)
    con74 = Constraint("NE(V35V55)", scope74)
    con75 = Constraint("NE(V41V42)", scope75)
    con76 = Constraint("NE(V41V43)", scope76)
    con77 = Constraint("NE(V41V44)", scope77)
    con78 = Constraint("NE(V41V45)", scope78)
    con79 = Constraint("NE(V41V51)", scope79)
    con80 = Constraint("NE(V42V43)", scope80)
    con81 = Constraint("NE(V42V44)", scope81)
    con82 = Constraint("NE(V42V45)", scope82)
    con83 = Constraint("NE(V42V52)", scope83)
    con84 = Constraint("NE(V43V44)", scope84)
    con85 = Constraint("NE(V43V45)", scope85)
    con86 = Constraint("NE(V43V53)", scope86)
    con87 = Constraint("NE(V44V45)", scope87)
    con88 = Constraint("NE(V44V54)", scope88)
    con89 = Constraint("NE(V45V55)", scope89)
    con90 = Constraint("NE(V51V52)", scope90)
    con91 = Constraint("NE(V51V53)", scope91)
    con92 = Constraint("NE(V51V54)", scope92)
    con93 = Constraint("NE(V51V55)", scope93)
    con94 = Constraint("NE(V52V53)", scope94)
    con95 = Constraint("NE(V52V54)", scope95)
    con96 = Constraint("NE(V52V55)", scope96)
    con97 = Constraint("NE(V53V54)", scope97)
    con98 = Constraint("NE(V53V55)", scope98)
    con99 = Constraint("NE(V54V55)", scope99)

    con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con48.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con49.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con50.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con51.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con52.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con53.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con54.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con55.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con56.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con57.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con58.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con59.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con60.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con61.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con62.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con63.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con64.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con65.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con66.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con67.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con68.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con69.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con70.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con71.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con72.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con73.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con74.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con75.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con76.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con77.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con78.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con79.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con80.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con81.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con82.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con83.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con84.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con85.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con86.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con87.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con88.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con89.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con90.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con91.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con92.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con93.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con94.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con95.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con96.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con97.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con98.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])
    con99.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)])

    answer = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47, con48, con49, con50, con51, con52, con53, con54, con55, con56, con57, con58, con59, con60, con61, con62, con63, con64, con65, con66, con67, con68, con69, con70, con71, con72, con73, con74, con75, con76, con77, con78, con79, con80, con81, con82, con83, con84, con85, con86, con87, con88, con89, con90, con91, con92, con93, con94, con95, con96, con97, con98, con99]

    return answer

def test_bne_grid_5_answer_binary():

    scope0 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V12", [1, 2, 3, 4, 5, 6])]
    scope1 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V13", [1, 2, 3, 4, 5, 6])]
    scope2 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V14", [1, 2, 3, 4, 5, 6])]
    scope3 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V15", [1, 2, 3, 4, 5, 6])]
    scope4 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V16", [1, 2, 3, 4, 5, 6])]
    scope5 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V21", [1, 2, 3, 4, 5, 6])]
    scope6 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V31", [1, 2, 3, 4, 5, 6])]
    scope7 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V41", [1, 2, 3, 4, 5, 6])]
    scope8 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V51", [1, 2, 3, 4, 5, 6])]
    scope9 = [Variable("V11", [1, 2, 3, 4, 5, 6]), Variable("V61", [1, 2, 3, 4, 5, 6])]
    scope10 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V13", [1, 2, 3, 4, 5, 6])]
    scope11 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V14", [1, 2, 3, 4, 5, 6])]
    scope12 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V15", [1, 2, 3, 4, 5, 6])]
    scope13 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V16", [1, 2, 3, 4, 5, 6])]
    scope14 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V22", [1, 2, 3, 4, 5, 6])]
    scope15 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V32", [1, 2, 3, 4, 5, 6])]
    scope16 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V42", [1, 2, 3, 4, 5, 6])]
    scope17 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V52", [1, 2, 3, 4, 5, 6])]
    scope18 = [Variable("V12", [1, 2, 3, 4, 5, 6]), Variable("V62", [1, 2, 3, 4, 5, 6])]
    scope19 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V14", [1, 2, 3, 4, 5, 6])]
    scope20 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V15", [1, 2, 3, 4, 5, 6])]
    scope21 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V16", [1, 2, 3, 4, 5, 6])]
    scope22 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V23", [1, 2, 3, 4, 5, 6])]
    scope23 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V33", [1, 2, 3, 4, 5, 6])]
    scope24 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V43", [1, 2, 3, 4, 5, 6])]
    scope25 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V53", [1, 2, 3, 4, 5, 6])]
    scope26 = [Variable("V13", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope27 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V15", [1, 2, 3, 4, 5, 6])]
    scope28 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V16", [1, 2, 3, 4, 5, 6])]
    scope29 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V24", [1, 2, 3, 4, 5, 6])]
    scope30 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V34", [1, 2, 3, 4, 5, 6])]
    scope31 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V44", [1, 2, 3, 4, 5, 6])]
    scope32 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope33 = [Variable("V14", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope34 = [Variable("V15", [1, 2, 3, 4, 5, 6]), Variable("V16", [1, 2, 3, 4, 5, 6])]
    scope35 = [Variable("V15", [1, 2, 3, 4, 5, 6]), Variable("V25", [1, 2, 3, 4, 5, 6])]
    scope36 = [Variable("V15", [1, 2, 3, 4, 5, 6]), Variable("V35", [1, 2, 3, 4, 5, 6])]
    scope37 = [Variable("V15", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope38 = [Variable("V15", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope39 = [Variable("V15", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope40 = [Variable("V16", [1, 2, 3, 4, 5, 6]), Variable("V26", [1, 2, 3, 4, 5, 6])]
    scope41 = [Variable("V16", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope42 = [Variable("V16", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope43 = [Variable("V16", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope44 = [Variable("V16", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope45 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V22", [1, 2, 3, 4, 5, 6])]
    scope46 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V23", [1, 2, 3, 4, 5, 6])]
    scope47 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V24", [1, 2, 3, 4, 5, 6])]
    scope48 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V25", [1, 2, 3, 4, 5, 6])]
    scope49 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V26", [1, 2, 3, 4, 5, 6])]
    scope50 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V31", [1, 2, 3, 4, 5, 6])]
    scope51 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V41", [1, 2, 3, 4, 5, 6])]
    scope52 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V51", [1, 2, 3, 4, 5, 6])]
    scope53 = [Variable("V21", [1, 2, 3, 4, 5, 6]), Variable("V61", [1, 2, 3, 4, 5, 6])]
    scope54 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V23", [1, 2, 3, 4, 5, 6])]
    scope55 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V24", [1, 2, 3, 4, 5, 6])]
    scope56 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V25", [1, 2, 3, 4, 5, 6])]
    scope57 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V26", [1, 2, 3, 4, 5, 6])]
    scope58 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V32", [1, 2, 3, 4, 5, 6])]
    scope59 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V42", [1, 2, 3, 4, 5, 6])]
    scope60 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V52", [1, 2, 3, 4, 5, 6])]
    scope61 = [Variable("V22", [1, 2, 3, 4, 5, 6]), Variable("V62", [1, 2, 3, 4, 5, 6])]
    scope62 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V24", [1, 2, 3, 4, 5, 6])]
    scope63 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V25", [1, 2, 3, 4, 5, 6])]
    scope64 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V26", [1, 2, 3, 4, 5, 6])]
    scope65 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V33", [1, 2, 3, 4, 5, 6])]
    scope66 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V43", [1, 2, 3, 4, 5, 6])]
    scope67 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V53", [1, 2, 3, 4, 5, 6])]
    scope68 = [Variable("V23", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope69 = [Variable("V24", [1, 2, 3, 4, 5, 6]), Variable("V25", [1, 2, 3, 4, 5, 6])]
    scope70 = [Variable("V24", [1, 2, 3, 4, 5, 6]), Variable("V26", [1, 2, 3, 4, 5, 6])]
    scope71 = [Variable("V24", [1, 2, 3, 4, 5, 6]), Variable("V34", [1, 2, 3, 4, 5, 6])]
    scope72 = [Variable("V24", [1, 2, 3, 4, 5, 6]), Variable("V44", [1, 2, 3, 4, 5, 6])]
    scope73 = [Variable("V24", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope74 = [Variable("V24", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope75 = [Variable("V25", [1, 2, 3, 4, 5, 6]), Variable("V26", [1, 2, 3, 4, 5, 6])]
    scope76 = [Variable("V25", [1, 2, 3, 4, 5, 6]), Variable("V35", [1, 2, 3, 4, 5, 6])]
    scope77 = [Variable("V25", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope78 = [Variable("V25", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope79 = [Variable("V25", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope80 = [Variable("V26", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope81 = [Variable("V26", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope82 = [Variable("V26", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope83 = [Variable("V26", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope84 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V32", [1, 2, 3, 4, 5, 6])]
    scope85 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V33", [1, 2, 3, 4, 5, 6])]
    scope86 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V34", [1, 2, 3, 4, 5, 6])]
    scope87 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V35", [1, 2, 3, 4, 5, 6])]
    scope88 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope89 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V41", [1, 2, 3, 4, 5, 6])]
    scope90 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V51", [1, 2, 3, 4, 5, 6])]
    scope91 = [Variable("V31", [1, 2, 3, 4, 5, 6]), Variable("V61", [1, 2, 3, 4, 5, 6])]
    scope92 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V33", [1, 2, 3, 4, 5, 6])]
    scope93 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V34", [1, 2, 3, 4, 5, 6])]
    scope94 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V35", [1, 2, 3, 4, 5, 6])]
    scope95 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope96 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V42", [1, 2, 3, 4, 5, 6])]
    scope97 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V52", [1, 2, 3, 4, 5, 6])]
    scope98 = [Variable("V32", [1, 2, 3, 4, 5, 6]), Variable("V62", [1, 2, 3, 4, 5, 6])]
    scope99 = [Variable("V33", [1, 2, 3, 4, 5, 6]), Variable("V34", [1, 2, 3, 4, 5, 6])]
    scope100 = [Variable("V33", [1, 2, 3, 4, 5, 6]), Variable("V35", [1, 2, 3, 4, 5, 6])]
    scope101 = [Variable("V33", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope102 = [Variable("V33", [1, 2, 3, 4, 5, 6]), Variable("V43", [1, 2, 3, 4, 5, 6])]
    scope103 = [Variable("V33", [1, 2, 3, 4, 5, 6]), Variable("V53", [1, 2, 3, 4, 5, 6])]
    scope104 = [Variable("V33", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope105 = [Variable("V34", [1, 2, 3, 4, 5, 6]), Variable("V35", [1, 2, 3, 4, 5, 6])]
    scope106 = [Variable("V34", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope107 = [Variable("V34", [1, 2, 3, 4, 5, 6]), Variable("V44", [1, 2, 3, 4, 5, 6])]
    scope108 = [Variable("V34", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope109 = [Variable("V34", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope110 = [Variable("V35", [1, 2, 3, 4, 5, 6]), Variable("V36", [1, 2, 3, 4, 5, 6])]
    scope111 = [Variable("V35", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope112 = [Variable("V35", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope113 = [Variable("V35", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope114 = [Variable("V36", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope115 = [Variable("V36", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope116 = [Variable("V36", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope117 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V42", [1, 2, 3, 4, 5, 6])]
    scope118 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V43", [1, 2, 3, 4, 5, 6])]
    scope119 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V44", [1, 2, 3, 4, 5, 6])]
    scope120 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope121 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope122 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V51", [1, 2, 3, 4, 5, 6])]
    scope123 = [Variable("V41", [1, 2, 3, 4, 5, 6]), Variable("V61", [1, 2, 3, 4, 5, 6])]
    scope124 = [Variable("V42", [1, 2, 3, 4, 5, 6]), Variable("V43", [1, 2, 3, 4, 5, 6])]
    scope125 = [Variable("V42", [1, 2, 3, 4, 5, 6]), Variable("V44", [1, 2, 3, 4, 5, 6])]
    scope126 = [Variable("V42", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope127 = [Variable("V42", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope128 = [Variable("V42", [1, 2, 3, 4, 5, 6]), Variable("V52", [1, 2, 3, 4, 5, 6])]
    scope129 = [Variable("V42", [1, 2, 3, 4, 5, 6]), Variable("V62", [1, 2, 3, 4, 5, 6])]
    scope130 = [Variable("V43", [1, 2, 3, 4, 5, 6]), Variable("V44", [1, 2, 3, 4, 5, 6])]
    scope131 = [Variable("V43", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope132 = [Variable("V43", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope133 = [Variable("V43", [1, 2, 3, 4, 5, 6]), Variable("V53", [1, 2, 3, 4, 5, 6])]
    scope134 = [Variable("V43", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope135 = [Variable("V44", [1, 2, 3, 4, 5, 6]), Variable("V45", [1, 2, 3, 4, 5, 6])]
    scope136 = [Variable("V44", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope137 = [Variable("V44", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope138 = [Variable("V44", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope139 = [Variable("V45", [1, 2, 3, 4, 5, 6]), Variable("V46", [1, 2, 3, 4, 5, 6])]
    scope140 = [Variable("V45", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope141 = [Variable("V45", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope142 = [Variable("V46", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope143 = [Variable("V46", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope144 = [Variable("V51", [1, 2, 3, 4, 5, 6]), Variable("V52", [1, 2, 3, 4, 5, 6])]
    scope145 = [Variable("V51", [1, 2, 3, 4, 5, 6]), Variable("V53", [1, 2, 3, 4, 5, 6])]
    scope146 = [Variable("V51", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope147 = [Variable("V51", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope148 = [Variable("V51", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope149 = [Variable("V51", [1, 2, 3, 4, 5, 6]), Variable("V61", [1, 2, 3, 4, 5, 6])]
    scope150 = [Variable("V52", [1, 2, 3, 4, 5, 6]), Variable("V53", [1, 2, 3, 4, 5, 6])]
    scope151 = [Variable("V52", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope152 = [Variable("V52", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope153 = [Variable("V52", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope154 = [Variable("V52", [1, 2, 3, 4, 5, 6]), Variable("V62", [1, 2, 3, 4, 5, 6])]
    scope155 = [Variable("V53", [1, 2, 3, 4, 5, 6]), Variable("V54", [1, 2, 3, 4, 5, 6])]
    scope156 = [Variable("V53", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope157 = [Variable("V53", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope158 = [Variable("V53", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope159 = [Variable("V54", [1, 2, 3, 4, 5, 6]), Variable("V55", [1, 2, 3, 4, 5, 6])]
    scope160 = [Variable("V54", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope161 = [Variable("V54", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope162 = [Variable("V55", [1, 2, 3, 4, 5, 6]), Variable("V56", [1, 2, 3, 4, 5, 6])]
    scope163 = [Variable("V55", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope164 = [Variable("V56", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope165 = [Variable("V61", [1, 2, 3, 4, 5, 6]), Variable("V62", [1, 2, 3, 4, 5, 6])]
    scope166 = [Variable("V61", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope167 = [Variable("V61", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope168 = [Variable("V61", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope169 = [Variable("V61", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope170 = [Variable("V62", [1, 2, 3, 4, 5, 6]), Variable("V63", [1, 2, 3, 4, 5, 6])]
    scope171 = [Variable("V62", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope172 = [Variable("V62", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope173 = [Variable("V62", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope174 = [Variable("V63", [1, 2, 3, 4, 5, 6]), Variable("V64", [1, 2, 3, 4, 5, 6])]
    scope175 = [Variable("V63", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope176 = [Variable("V63", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope177 = [Variable("V64", [1, 2, 3, 4, 5, 6]), Variable("V65", [1, 2, 3, 4, 5, 6])]
    scope178 = [Variable("V64", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]
    scope179 = [Variable("V65", [1, 2, 3, 4, 5, 6]), Variable("V66", [1, 2, 3, 4, 5, 6])]

    con0 = Constraint("NE(V11V12)", scope0)
    con1 = Constraint("NE(V11V13)", scope1)
    con2 = Constraint("NE(V11V14)", scope2)
    con3 = Constraint("NE(V11V15)", scope3)
    con4 = Constraint("NE(V11V16)", scope4)
    con5 = Constraint("NE(V11V21)", scope5)
    con6 = Constraint("NE(V11V31)", scope6)
    con7 = Constraint("NE(V11V41)", scope7)
    con8 = Constraint("NE(V11V51)", scope8)
    con9 = Constraint("NE(V11V61)", scope9)
    con10 = Constraint("NE(V12V13)", scope10)
    con11 = Constraint("NE(V12V14)", scope11)
    con12 = Constraint("NE(V12V15)", scope12)
    con13 = Constraint("NE(V12V16)", scope13)
    con14 = Constraint("NE(V12V22)", scope14)
    con15 = Constraint("NE(V12V32)", scope15)
    con16 = Constraint("NE(V12V42)", scope16)
    con17 = Constraint("NE(V12V52)", scope17)
    con18 = Constraint("NE(V12V62)", scope18)
    con19 = Constraint("NE(V13V14)", scope19)
    con20 = Constraint("NE(V13V15)", scope20)
    con21 = Constraint("NE(V13V16)", scope21)
    con22 = Constraint("NE(V13V23)", scope22)
    con23 = Constraint("NE(V13V33)", scope23)
    con24 = Constraint("NE(V13V43)", scope24)
    con25 = Constraint("NE(V13V53)", scope25)
    con26 = Constraint("NE(V13V63)", scope26)
    con27 = Constraint("NE(V14V15)", scope27)
    con28 = Constraint("NE(V14V16)", scope28)
    con29 = Constraint("NE(V14V24)", scope29)
    con30 = Constraint("NE(V14V34)", scope30)
    con31 = Constraint("NE(V14V44)", scope31)
    con32 = Constraint("NE(V14V54)", scope32)
    con33 = Constraint("NE(V14V64)", scope33)
    con34 = Constraint("NE(V15V16)", scope34)
    con35 = Constraint("NE(V15V25)", scope35)
    con36 = Constraint("NE(V15V35)", scope36)
    con37 = Constraint("NE(V15V45)", scope37)
    con38 = Constraint("NE(V15V55)", scope38)
    con39 = Constraint("NE(V15V65)", scope39)
    con40 = Constraint("NE(V16V26)", scope40)
    con41 = Constraint("NE(V16V36)", scope41)
    con42 = Constraint("NE(V16V46)", scope42)
    con43 = Constraint("NE(V16V56)", scope43)
    con44 = Constraint("NE(V16V66)", scope44)
    con45 = Constraint("NE(V21V22)", scope45)
    con46 = Constraint("NE(V21V23)", scope46)
    con47 = Constraint("NE(V21V24)", scope47)
    con48 = Constraint("NE(V21V25)", scope48)
    con49 = Constraint("NE(V21V26)", scope49)
    con50 = Constraint("NE(V21V31)", scope50)
    con51 = Constraint("NE(V21V41)", scope51)
    con52 = Constraint("NE(V21V51)", scope52)
    con53 = Constraint("NE(V21V61)", scope53)
    con54 = Constraint("NE(V22V23)", scope54)
    con55 = Constraint("NE(V22V24)", scope55)
    con56 = Constraint("NE(V22V25)", scope56)
    con57 = Constraint("NE(V22V26)", scope57)
    con58 = Constraint("NE(V22V32)", scope58)
    con59 = Constraint("NE(V22V42)", scope59)
    con60 = Constraint("NE(V22V52)", scope60)
    con61 = Constraint("NE(V22V62)", scope61)
    con62 = Constraint("NE(V23V24)", scope62)
    con63 = Constraint("NE(V23V25)", scope63)
    con64 = Constraint("NE(V23V26)", scope64)
    con65 = Constraint("NE(V23V33)", scope65)
    con66 = Constraint("NE(V23V43)", scope66)
    con67 = Constraint("NE(V23V53)", scope67)
    con68 = Constraint("NE(V23V63)", scope68)
    con69 = Constraint("NE(V24V25)", scope69)
    con70 = Constraint("NE(V24V26)", scope70)
    con71 = Constraint("NE(V24V34)", scope71)
    con72 = Constraint("NE(V24V44)", scope72)
    con73 = Constraint("NE(V24V54)", scope73)
    con74 = Constraint("NE(V24V64)", scope74)
    con75 = Constraint("NE(V25V26)", scope75)
    con76 = Constraint("NE(V25V35)", scope76)
    con77 = Constraint("NE(V25V45)", scope77)
    con78 = Constraint("NE(V25V55)", scope78)
    con79 = Constraint("NE(V25V65)", scope79)
    con80 = Constraint("NE(V26V36)", scope80)
    con81 = Constraint("NE(V26V46)", scope81)
    con82 = Constraint("NE(V26V56)", scope82)
    con83 = Constraint("NE(V26V66)", scope83)
    con84 = Constraint("NE(V31V32)", scope84)
    con85 = Constraint("NE(V31V33)", scope85)
    con86 = Constraint("NE(V31V34)", scope86)
    con87 = Constraint("NE(V31V35)", scope87)
    con88 = Constraint("NE(V31V36)", scope88)
    con89 = Constraint("NE(V31V41)", scope89)
    con90 = Constraint("NE(V31V51)", scope90)
    con91 = Constraint("NE(V31V61)", scope91)
    con92 = Constraint("NE(V32V33)", scope92)
    con93 = Constraint("NE(V32V34)", scope93)
    con94 = Constraint("NE(V32V35)", scope94)
    con95 = Constraint("NE(V32V36)", scope95)
    con96 = Constraint("NE(V32V42)", scope96)
    con97 = Constraint("NE(V32V52)", scope97)
    con98 = Constraint("NE(V32V62)", scope98)
    con99 = Constraint("NE(V33V34)", scope99)
    con100 = Constraint("NE(V33V35)", scope100)
    con101 = Constraint("NE(V33V36)", scope101)
    con102 = Constraint("NE(V33V43)", scope102)
    con103 = Constraint("NE(V33V53)", scope103)
    con104 = Constraint("NE(V33V63)", scope104)
    con105 = Constraint("NE(V34V35)", scope105)
    con106 = Constraint("NE(V34V36)", scope106)
    con107 = Constraint("NE(V34V44)", scope107)
    con108 = Constraint("NE(V34V54)", scope108)
    con109 = Constraint("NE(V34V64)", scope109)
    con110 = Constraint("NE(V35V36)", scope110)
    con111 = Constraint("NE(V35V45)", scope111)
    con112 = Constraint("NE(V35V55)", scope112)
    con113 = Constraint("NE(V35V65)", scope113)
    con114 = Constraint("NE(V36V46)", scope114)
    con115 = Constraint("NE(V36V56)", scope115)
    con116 = Constraint("NE(V36V66)", scope116)
    con117 = Constraint("NE(V41V42)", scope117)
    con118 = Constraint("NE(V41V43)", scope118)
    con119 = Constraint("NE(V41V44)", scope119)
    con120 = Constraint("NE(V41V45)", scope120)
    con121 = Constraint("NE(V41V46)", scope121)
    con122 = Constraint("NE(V41V51)", scope122)
    con123 = Constraint("NE(V41V61)", scope123)
    con124 = Constraint("NE(V42V43)", scope124)
    con125 = Constraint("NE(V42V44)", scope125)
    con126 = Constraint("NE(V42V45)", scope126)
    con127 = Constraint("NE(V42V46)", scope127)
    con128 = Constraint("NE(V42V52)", scope128)
    con129 = Constraint("NE(V42V62)", scope129)
    con130 = Constraint("NE(V43V44)", scope130)
    con131 = Constraint("NE(V43V45)", scope131)
    con132 = Constraint("NE(V43V46)", scope132)
    con133 = Constraint("NE(V43V53)", scope133)
    con134 = Constraint("NE(V43V63)", scope134)
    con135 = Constraint("NE(V44V45)", scope135)
    con136 = Constraint("NE(V44V46)", scope136)
    con137 = Constraint("NE(V44V54)", scope137)
    con138 = Constraint("NE(V44V64)", scope138)
    con139 = Constraint("NE(V45V46)", scope139)
    con140 = Constraint("NE(V45V55)", scope140)
    con141 = Constraint("NE(V45V65)", scope141)
    con142 = Constraint("NE(V46V56)", scope142)
    con143 = Constraint("NE(V46V66)", scope143)
    con144 = Constraint("NE(V51V52)", scope144)
    con145 = Constraint("NE(V51V53)", scope145)
    con146 = Constraint("NE(V51V54)", scope146)
    con147 = Constraint("NE(V51V55)", scope147)
    con148 = Constraint("NE(V51V56)", scope148)
    con149 = Constraint("NE(V51V61)", scope149)
    con150 = Constraint("NE(V52V53)", scope150)
    con151 = Constraint("NE(V52V54)", scope151)
    con152 = Constraint("NE(V52V55)", scope152)
    con153 = Constraint("NE(V52V56)", scope153)
    con154 = Constraint("NE(V52V62)", scope154)
    con155 = Constraint("NE(V53V54)", scope155)
    con156 = Constraint("NE(V53V55)", scope156)
    con157 = Constraint("NE(V53V56)", scope157)
    con158 = Constraint("NE(V53V63)", scope158)
    con159 = Constraint("NE(V54V55)", scope159)
    con160 = Constraint("NE(V54V56)", scope160)
    con161 = Constraint("NE(V54V64)", scope161)
    con162 = Constraint("NE(V55V56)", scope162)
    con163 = Constraint("NE(V55V65)", scope163)
    con164 = Constraint("NE(V56V66)", scope164)
    con165 = Constraint("NE(V61V62)", scope165)
    con166 = Constraint("NE(V61V63)", scope166)
    con167 = Constraint("NE(V61V64)", scope167)
    con168 = Constraint("NE(V61V65)", scope168)
    con169 = Constraint("NE(V61V66)", scope169)
    con170 = Constraint("NE(V62V63)", scope170)
    con171 = Constraint("NE(V62V64)", scope171)
    con172 = Constraint("NE(V62V65)", scope172)
    con173 = Constraint("NE(V62V66)", scope173)
    con174 = Constraint("NE(V63V64)", scope174)
    con175 = Constraint("NE(V63V65)", scope175)
    con176 = Constraint("NE(V63V66)", scope176)
    con177 = Constraint("NE(V64V65)", scope177)
    con178 = Constraint("NE(V64V66)", scope178)
    con179 = Constraint("NE(V65V66)", scope179)

    con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con48.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con49.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con50.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con51.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con52.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con53.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con54.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con55.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con56.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con57.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con58.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con59.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con60.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con61.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con62.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con63.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con64.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con65.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con66.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con67.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con68.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con69.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con70.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con71.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con72.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con73.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con74.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con75.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con76.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con77.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con78.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con79.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con80.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con81.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con82.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con83.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con84.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con85.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con86.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con87.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con88.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con89.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con90.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con91.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con92.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con93.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con94.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con95.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con96.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con97.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con98.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con99.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con100.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con101.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con102.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con103.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con104.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con105.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con106.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con107.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con108.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con109.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con110.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con111.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con112.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con113.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con114.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con115.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con116.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con117.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con118.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con119.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con120.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con121.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con122.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con123.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con124.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con125.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con126.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con127.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con128.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con129.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con130.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con131.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con132.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con133.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con134.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con135.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con136.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con137.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con138.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con139.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con140.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con141.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con142.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con143.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con144.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con145.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con146.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con147.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con148.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con149.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con150.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con151.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con152.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con153.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con154.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con155.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con156.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con157.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con158.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con159.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con160.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con161.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con162.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con163.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con164.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con165.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con166.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con167.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con168.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con169.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con170.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con171.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con172.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con173.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con174.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con175.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con176.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con177.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con178.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])
    con179.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)])

    answer = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47, con48, con49, con50, con51, con52, con53, con54, con55, con56, con57, con58, con59, con60, con61, con62, con63, con64, con65, con66, con67, con68, con69, con70, con71, con72, con73, con74, con75, con76, con77, con78, con79, con80, con81, con82, con83, con84, con85, con86, con87, con88, con89, con90, con91, con92, con93, con94, con95, con96, con97, con98, con99, con100, con101, con102, con103, con104, con105, con106, con107, con108, con109, con110, con111, con112, con113, con114, con115, con116, con117, con118, con119, con120, con121, con122, con123, con124, con125, con126, con127, con128, con129, con130, con131, con132, con133, con134, con135, con136, con137, con138, con139, con140, con141, con142, con143, con144, con145, con146, con147, con148, con149, con150, con151, con152, con153, con154, con155, con156, con157, con158, con159, con160, con161, con162, con163, con164, con165, con166, con167, con168, con169, con170, con171, con172, con173, con174, con175, con176, con177, con178, con179]

    return answer

def test_cages_1_correct():

    scope0 = [Variable("Cage_op(4:+:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])", ['+', '-', '/', '*', 'f']), Variable("Cell11", [1, 2]), Variable("Cell12", [1, 2]), Variable("Cell21", [1, 2]), Variable("Cell22", [1, 2])]

    con0 = Constraint('Cage(4:+:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])', scope0)

    con0.add_satisfying_tuples([('+', 1, 1, 1, 1)])

    answer = [con0]

    return answer

def test_cages_2_correct():

    scope0 = [Variable("Cage_op(4:-:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])", ['+', '-', '/', '*', 'f']), Variable("Cell11", [1, 2]), Variable("Cell12", [1, 2]), Variable("Cell21", [1, 2]), Variable("Cell22", [1, 2])]

    con0 = Constraint('Cage(4:-:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])', scope0)

    con0.add_satisfying_tuples([])

    answer = [con0]

    return answer

def test_cages_3_correct():

    scope0 = [Variable("Cage_op(4:*:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])", ['+', '-', '/', '*', 'f']), Variable("Cell11", [1, 2]), Variable("Cell12", [1, 2]), Variable("Cell21", [1, 2]), Variable("Cell22", [1, 2])]

    con0 = Constraint('Cage(4:*:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])', scope0)

    con0.add_satisfying_tuples([('*', 1, 1, 2, 2), ('*', 1, 2, 1, 2), ('*', 1, 2, 2, 1), ('*', 2, 1, 1, 2), ('*', 2, 1, 2, 1), ('*', 2, 2, 1, 1)])

    answer = [con0]

    return answer

def test_cages_4_correct():

    scope0 = [Variable("Cage_op(10:+:[Var-Cell11, Var-Cell12, Var-Cell13, Var-Cell21, Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f']), Variable("Cell11", [1, 2, 3]), Variable("Cell12", [1, 2, 3]), Variable("Cell13", [1, 2, 3]), Variable("Cell21", [1, 2, 3]), Variable("Cell22", [1, 2, 3]), Variable("Cell23", [1, 2, 3])]

    con0 = Constraint('Cage(10:+:[Var-Cell11, Var-Cell12, Var-Cell13, Var-Cell21, Var-Cell22, Var-Cell23])', scope0)

    con0.add_satisfying_tuples([('+', 1, 1, 1, 1, 3, 3), ('+', 1, 1, 1, 2, 2, 3), ('+', 1, 1, 1, 2, 3, 2), ('+', 1, 1, 1, 3, 1, 3), ('+', 1, 1, 1, 3, 2, 2), ('+', 1, 1, 1, 3, 3, 1), ('+', 1, 1, 2, 1, 2, 3), ('+', 1, 1, 2, 1, 3, 2), ('+', 1, 1, 2, 2, 1, 3), ('+', 1, 1, 2, 2, 2, 2), ('+', 1, 1, 2, 2, 3, 1), ('+', 1, 1, 2, 3, 1, 2), ('+', 1, 1, 2, 3, 2, 1), ('+', 1, 1, 3, 1, 1, 3), ('+', 1, 1, 3, 1, 2, 2), ('+', 1, 1, 3, 1, 3, 1), ('+', 1, 1, 3, 2, 1, 2), ('+', 1, 1, 3, 2, 2, 1), ('+', 1, 1, 3, 3, 1, 1), ('+', 1, 2, 1, 1, 2, 3), ('+', 1, 2, 1, 1, 3, 2), ('+', 1, 2, 1, 2, 1, 3), ('+', 1, 2, 1, 2, 2, 2), ('+', 1, 2, 1, 2, 3, 1), ('+', 1, 2, 1, 3, 1, 2), ('+', 1, 2, 1, 3, 2, 1), ('+', 1, 2, 2, 1, 1, 3), ('+', 1, 2, 2, 1, 2, 2), ('+', 1, 2, 2, 1, 3, 1), ('+', 1, 2, 2, 2, 1, 2), ('+', 1, 2, 2, 2, 2, 1), ('+', 1, 2, 2, 3, 1, 1), ('+', 1, 2, 3, 1, 1, 2), ('+', 1, 2, 3, 1, 2, 1), ('+', 1, 2, 3, 2, 1, 1), ('+', 1, 3, 1, 1, 1, 3), ('+', 1, 3, 1, 1, 2, 2), ('+', 1, 3, 1, 1, 3, 1), ('+', 1, 3, 1, 2, 1, 2), ('+', 1, 3, 1, 2, 2, 1), ('+', 1, 3, 1, 3, 1, 1), ('+', 1, 3, 2, 1, 1, 2), ('+', 1, 3, 2, 1, 2, 1), ('+', 1, 3, 2, 2, 1, 1), ('+', 1, 3, 3, 1, 1, 1), ('+', 2, 1, 1, 1, 2, 3), ('+', 2, 1, 1, 1, 3, 2), ('+', 2, 1, 1, 2, 1, 3), ('+', 2, 1, 1, 2, 2, 2), ('+', 2, 1, 1, 2, 3, 1), ('+', 2, 1, 1, 3, 1, 2), ('+', 2, 1, 1, 3, 2, 1), ('+', 2, 1, 2, 1, 1, 3), ('+', 2, 1, 2, 1, 2, 2), ('+', 2, 1, 2, 1, 3, 1), ('+', 2, 1, 2, 2, 1, 2), ('+', 2, 1, 2, 2, 2, 1), ('+', 2, 1, 2, 3, 1, 1), ('+', 2, 1, 3, 1, 1, 2), ('+', 2, 1, 3, 1, 2, 1), ('+', 2, 1, 3, 2, 1, 1), ('+', 2, 2, 1, 1, 1, 3), ('+', 2, 2, 1, 1, 2, 2), ('+', 2, 2, 1, 1, 3, 1), ('+', 2, 2, 1, 2, 1, 2), ('+', 2, 2, 1, 2, 2, 1), ('+', 2, 2, 1, 3, 1, 1), ('+', 2, 2, 2, 1, 1, 2), ('+', 2, 2, 2, 1, 2, 1), ('+', 2, 2, 2, 2, 1, 1), ('+', 2, 2, 3, 1, 1, 1), ('+', 2, 3, 1, 1, 1, 2), ('+', 2, 3, 1, 1, 2, 1), ('+', 2, 3, 1, 2, 1, 1), ('+', 2, 3, 2, 1, 1, 1), ('+', 3, 1, 1, 1, 1, 3), ('+', 3, 1, 1, 1, 2, 2), ('+', 3, 1, 1, 1, 3, 1), ('+', 3, 1, 1, 2, 1, 2), ('+', 3, 1, 1, 2, 2, 1), ('+', 3, 1, 1, 3, 1, 1), ('+', 3, 1, 2, 1, 1, 2), ('+', 3, 1, 2, 1, 2, 1), ('+', 3, 1, 2, 2, 1, 1), ('+', 3, 1, 3, 1, 1, 1), ('+', 3, 2, 1, 1, 1, 2), ('+', 3, 2, 1, 1, 2, 1), ('+', 3, 2, 1, 2, 1, 1), ('+', 3, 2, 2, 1, 1, 1), ('+', 3, 3, 1, 1, 1, 1)])

    answer = [con0]

    return answer

def test_cages_5_correct():

    scope0 = [Variable("Cage_op(7:-:[Var-Cell11, Var-Cell12, Var-Cell13, Var-Cell21, Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f']), Variable("Cell11", [1, 2, 3]), Variable("Cell12", [1, 2, 3]), Variable("Cell13", [1, 2, 3]), Variable("Cell21", [1, 2, 3]), Variable("Cell22", [1, 2, 3]), Variable("Cell23", [1, 2, 3])]

    con0 = Constraint('Cage(7:-:[Var-Cell11, Var-Cell12, Var-Cell13, Var-Cell21, Var-Cell22, Var-Cell23])', scope0)

    con0.add_satisfying_tuples([])

    answer = [con0]

    return answer

def test_cages_6_correct():

    scope0 = [Variable("Cage_op(10:*:[Var-Cell11, Var-Cell12, Var-Cell13, Var-Cell21, Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f']), Variable("Cell11", [1, 2, 3]), Variable("Cell12", [1, 2, 3]), Variable("Cell13", [1, 2, 3]), Variable("Cell21", [1, 2, 3]), Variable("Cell22", [1, 2, 3]), Variable("Cell23", [1, 2, 3])]

    con0 = Constraint('Cage(10:*:[Var-Cell11, Var-Cell12, Var-Cell13, Var-Cell21, Var-Cell22, Var-Cell23])', scope0)

    con0.add_satisfying_tuples([])

    answer = [con0]

    return answer

def bin_board_fixed(b_num):

    if b_num == 0:
        
        var0 = Variable("Cell(1,1)", [1, 2, 3])
        var1 = Variable("Cell(1,2)", [1, 2, 3])
        var2 = Variable("Cell(1,3)", [1, 2, 3])
        var3 = Variable("Cell(2,1)", [1, 2, 3])
        var4 = Variable("Cell(2,2)", [1, 2, 3])
        var5 = Variable("Cell(2,3)", [1, 2, 3])
        var6 = Variable("Cell(3,1)", [1, 2, 3])
        var7 = Variable("Cell(3,2)", [1, 2, 3])
        var8 = Variable("Cell(3,3)", [1, 2, 3])

        scope0 = [var0, var1]
        scope1 = [var0, var2]
        scope2 = [var0, var3]
        scope3 = [var0, var6]
        scope4 = [var1, var0]
        scope5 = [var1, var2]
        scope6 = [var1, var4]
        scope7 = [var1, var7]
        scope8 = [var2, var0]
        scope9 = [var2, var1]
        scope10 = [var2, var5]
        scope11 = [var2, var8]
        scope12 = [var3, var4]
        scope13 = [var3, var5]
        scope14 = [var3, var0]
        scope15 = [var3, var6]
        scope16 = [var4, var3]
        scope17 = [var4, var5]
        scope18 = [var4, var1]
        scope19 = [var4, var7]
        scope20 = [var5, var3]
        scope21 = [var5, var4]
        scope22 = [var5, var2]
        scope23 = [var5, var8]
        scope24 = [var6, var7]
        scope25 = [var6, var8]
        scope26 = [var6, var0]
        scope27 = [var6, var3]
        scope28 = [var7, var6]
        scope29 = [var7, var8]
        scope30 = [var7, var1]
        scope31 = [var7, var4]
        scope32 = [var8, var6]
        scope33 = [var8, var7]
        scope34 = [var8, var2]
        scope35 = [var8, var5]

        con0 = Constraint('Relation(Cell(1,1),Cell(1,2))', scope0)
        con1 = Constraint('Relation(Cell(1,1),Cell(1,3))', scope1)
        con2 = Constraint('Relation(Cell(1,1),Cell(2,1))', scope2)
        con3 = Constraint('Relation(Cell(1,1),Cell(3,1))', scope3)
        con4 = Constraint('Relation(Cell(1,2),Cell(1,1))', scope4)
        con5 = Constraint('Relation(Cell(1,2),Cell(1,3))', scope5)
        con6 = Constraint('Relation(Cell(1,2),Cell(2,2))', scope6)
        con7 = Constraint('Relation(Cell(1,2),Cell(3,2))', scope7)
        con8 = Constraint('Relation(Cell(1,3),Cell(1,1))', scope8)
        con9 = Constraint('Relation(Cell(1,3),Cell(1,2))', scope9)
        con10 = Constraint('Relation(Cell(1,3),Cell(2,3))', scope10)
        con11 = Constraint('Relation(Cell(1,3),Cell(3,3))', scope11)
        con12 = Constraint('Relation(Cell(2,1),Cell(2,2))', scope12)
        con13 = Constraint('Relation(Cell(2,1),Cell(2,3))', scope13)
        con14 = Constraint('Relation(Cell(2,1),Cell(1,1))', scope14)
        con15 = Constraint('Relation(Cell(2,1),Cell(3,1))', scope15)
        con16 = Constraint('Relation(Cell(2,2),Cell(2,1))', scope16)
        con17 = Constraint('Relation(Cell(2,2),Cell(2,3))', scope17)
        con18 = Constraint('Relation(Cell(2,2),Cell(1,2))', scope18)
        con19 = Constraint('Relation(Cell(2,2),Cell(3,2))', scope19)
        con20 = Constraint('Relation(Cell(2,3),Cell(2,1))', scope20)
        con21 = Constraint('Relation(Cell(2,3),Cell(2,2))', scope21)
        con22 = Constraint('Relation(Cell(2,3),Cell(1,3))', scope22)
        con23 = Constraint('Relation(Cell(2,3),Cell(3,3))', scope23)
        con24 = Constraint('Relation(Cell(3,1),Cell(3,2))', scope24)
        con25 = Constraint('Relation(Cell(3,1),Cell(3,3))', scope25)
        con26 = Constraint('Relation(Cell(3,1),Cell(1,1))', scope26)
        con27 = Constraint('Relation(Cell(3,1),Cell(2,1))', scope27)
        con28 = Constraint('Relation(Cell(3,2),Cell(3,1))', scope28)
        con29 = Constraint('Relation(Cell(3,2),Cell(3,3))', scope29)
        con30 = Constraint('Relation(Cell(3,2),Cell(1,2))', scope30)
        con31 = Constraint('Relation(Cell(3,2),Cell(2,2))', scope31)
        con32 = Constraint('Relation(Cell(3,3),Cell(3,1))', scope32)
        con33 = Constraint('Relation(Cell(3,3),Cell(3,2))', scope33)
        con34 = Constraint('Relation(Cell(3,3),Cell(1,3))', scope34)
        con35 = Constraint('Relation(Cell(3,3),Cell(2,3))', scope35)

        con0.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con1.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con2.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con3.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con4.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con5.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con6.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con7.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con8.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con9.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con10.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con11.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con12.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con13.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con14.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con15.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con16.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con17.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con18.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con19.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con20.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con21.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con22.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con23.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con24.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con25.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con26.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con27.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con28.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con29.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con30.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con31.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con32.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con33.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con34.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])
        con35.add_satisfying_tuples([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35]

        var_array = [
            [var0, var1, var2],
            [var3, var4, var5],
            [var6, var7, var8]
        ]

        vars = [
            var0, var1, var2,
            var3, var4, var5,
            var6, var7, var8
        ]

        csp = CSP("Bin_Cagey(3x3)", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 1:

        var0 = Variable("Cell(1,1)", [1, 2, 3, 4])
        var1 = Variable("Cell(1,2)", [1, 2, 3, 4])
        var2 = Variable("Cell(1,3)", [1, 2, 3, 4])
        var3 = Variable("Cell(1,4)", [1, 2, 3, 4])
        var4 = Variable("Cell(2,1)", [1, 2, 3, 4])
        var5 = Variable("Cell(2,2)", [1, 2, 3, 4])
        var6 = Variable("Cell(2,3)", [1, 2, 3, 4])
        var7 = Variable("Cell(2,4)", [1, 2, 3, 4])
        var8 = Variable("Cell(3,1)", [1, 2, 3, 4])
        var9 = Variable("Cell(3,2)", [1, 2, 3, 4])
        var10 = Variable("Cell(3,3)", [1, 2, 3, 4])
        var11 = Variable("Cell(3,4)", [1, 2, 3, 4])
        var12 = Variable("Cell(4,1)", [1, 2, 3, 4])
        var13 = Variable("Cell(4,2)", [1, 2, 3, 4])
        var14 = Variable("Cell(4,3)", [1, 2, 3, 4])
        var15 = Variable("Cell(4,4)", [1, 2, 3, 4])

        scope0 = [var0, var1]
        scope1 = [var0, var2]
        scope2 = [var0, var3]
        scope3 = [var0, var4]
        scope4 = [var0, var8]
        scope5 = [var0, var12]
        scope6 = [var1, var0]
        scope7 = [var1, var2]
        scope8 = [var1, var3]
        scope9 = [var1, var5]
        scope10 = [var1, var9]
        scope11 = [var1, var13]
        scope12 = [var2, var0]
        scope13 = [var2, var1]
        scope14 = [var2, var3]
        scope15 = [var2, var6]
        scope16 = [var2, var10]
        scope17 = [var2, var14]
        scope18 = [var3, var0]
        scope19 = [var3, var1]
        scope20 = [var3, var2]
        scope21 = [var3, var7]
        scope22 = [var3, var11]
        scope23 = [var3, var15]
        scope24 = [var4, var5]
        scope25 = [var4, var6]
        scope26 = [var4, var7]
        scope27 = [var4, var0]
        scope28 = [var4, var8]
        scope29 = [var4, var12]
        scope30 = [var5, var4]
        scope31 = [var5, var6]
        scope32 = [var5, var7]
        scope33 = [var5, var1]
        scope34 = [var5, var9]
        scope35 = [var5, var13]
        scope36 = [var6, var4]
        scope37 = [var6, var5]
        scope38 = [var6, var7]
        scope39 = [var6, var2]
        scope40 = [var6, var10]
        scope41 = [var6, var14]
        scope42 = [var7, var4]
        scope43 = [var7, var5]
        scope44 = [var7, var6]
        scope45 = [var7, var3]
        scope46 = [var7, var11]
        scope47 = [var7, var15]
        scope48 = [var8, var9]
        scope49 = [var8, var10]
        scope50 = [var8, var11]
        scope51 = [var8, var0]
        scope52 = [var8, var4]
        scope53 = [var8, var12]
        scope54 = [var9, var8]
        scope55 = [var9, var10]
        scope56 = [var9, var11]
        scope57 = [var9, var1]
        scope58 = [var9, var5]
        scope59 = [var9, var13]
        scope60 = [var10, var8]
        scope61 = [var10, var9]
        scope62 = [var10, var11]
        scope63 = [var10, var2]
        scope64 = [var10, var6]
        scope65 = [var10, var14]
        scope66 = [var11, var8]
        scope67 = [var11, var9]
        scope68 = [var11, var10]
        scope69 = [var11, var3]
        scope70 = [var11, var7]
        scope71 = [var11, var15]
        scope72 = [var12, var13]
        scope73 = [var12, var14]
        scope74 = [var12, var15]
        scope75 = [var12, var0]
        scope76 = [var12, var4]
        scope77 = [var12, var8]
        scope78 = [var13, var12]
        scope79 = [var13, var14]
        scope80 = [var13, var15]
        scope81 = [var13, var1]
        scope82 = [var13, var5]
        scope83 = [var13, var9]
        scope84 = [var14, var12]
        scope85 = [var14, var13]
        scope86 = [var14, var15]
        scope87 = [var14, var2]
        scope88 = [var14, var6]
        scope89 = [var14, var10]
        scope90 = [var15, var12]
        scope91 = [var15, var13]
        scope92 = [var15, var14]
        scope93 = [var15, var3]
        scope94 = [var15, var7]
        scope95 = [var15, var11]

        con0 = Constraint('Relation(Cell(1,1),Cell(1,2))', scope0)
        con1 = Constraint('Relation(Cell(1,1),Cell(1,3))', scope1)
        con2 = Constraint('Relation(Cell(1,1),Cell(1,4))', scope2)
        con3 = Constraint('Relation(Cell(1,1),Cell(2,1))', scope3)
        con4 = Constraint('Relation(Cell(1,1),Cell(3,1))', scope4)
        con5 = Constraint('Relation(Cell(1,1),Cell(4,1))', scope5)
        con6 = Constraint('Relation(Cell(1,2),Cell(1,1))', scope6)
        con7 = Constraint('Relation(Cell(1,2),Cell(1,3))', scope7)
        con8 = Constraint('Relation(Cell(1,2),Cell(1,4))', scope8)
        con9 = Constraint('Relation(Cell(1,2),Cell(2,2))', scope9)
        con10 = Constraint('Relation(Cell(1,2),Cell(3,2))', scope10)
        con11 = Constraint('Relation(Cell(1,2),Cell(4,2))', scope11)
        con12 = Constraint('Relation(Cell(1,3),Cell(1,1))', scope12)
        con13 = Constraint('Relation(Cell(1,3),Cell(1,2))', scope13)
        con14 = Constraint('Relation(Cell(1,3),Cell(1,4))', scope14)
        con15 = Constraint('Relation(Cell(1,3),Cell(2,3))', scope15)
        con16 = Constraint('Relation(Cell(1,3),Cell(3,3))', scope16)
        con17 = Constraint('Relation(Cell(1,3),Cell(4,3))', scope17)
        con18 = Constraint('Relation(Cell(1,4),Cell(1,1))', scope18)
        con19 = Constraint('Relation(Cell(1,4),Cell(1,2))', scope19)
        con20 = Constraint('Relation(Cell(1,4),Cell(1,3))', scope20)
        con21 = Constraint('Relation(Cell(1,4),Cell(2,4))', scope21)
        con22 = Constraint('Relation(Cell(1,4),Cell(3,4))', scope22)
        con23 = Constraint('Relation(Cell(1,4),Cell(4,4))', scope23)
        con24 = Constraint('Relation(Cell(2,1),Cell(2,2))', scope24)
        con25 = Constraint('Relation(Cell(2,1),Cell(2,3))', scope25)
        con26 = Constraint('Relation(Cell(2,1),Cell(2,4))', scope26)
        con27 = Constraint('Relation(Cell(2,1),Cell(1,1))', scope27)
        con28 = Constraint('Relation(Cell(2,1),Cell(3,1))', scope28)
        con29 = Constraint('Relation(Cell(2,1),Cell(4,1))', scope29)
        con30 = Constraint('Relation(Cell(2,2),Cell(2,1))', scope30)
        con31 = Constraint('Relation(Cell(2,2),Cell(2,3))', scope31)
        con32 = Constraint('Relation(Cell(2,2),Cell(2,4))', scope32)
        con33 = Constraint('Relation(Cell(2,2),Cell(1,2))', scope33)
        con34 = Constraint('Relation(Cell(2,2),Cell(3,2))', scope34)
        con35 = Constraint('Relation(Cell(2,2),Cell(4,2))', scope35)
        con36 = Constraint('Relation(Cell(2,3),Cell(2,1))', scope36)
        con37 = Constraint('Relation(Cell(2,3),Cell(2,2))', scope37)
        con38 = Constraint('Relation(Cell(2,3),Cell(2,4))', scope38)
        con39 = Constraint('Relation(Cell(2,3),Cell(1,3))', scope39)
        con40 = Constraint('Relation(Cell(2,3),Cell(3,3))', scope40)
        con41 = Constraint('Relation(Cell(2,3),Cell(4,3))', scope41)
        con42 = Constraint('Relation(Cell(2,4),Cell(2,1))', scope42)
        con43 = Constraint('Relation(Cell(2,4),Cell(2,2))', scope43)
        con44 = Constraint('Relation(Cell(2,4),Cell(2,3))', scope44)
        con45 = Constraint('Relation(Cell(2,4),Cell(1,4))', scope45)
        con46 = Constraint('Relation(Cell(2,4),Cell(3,4))', scope46)
        con47 = Constraint('Relation(Cell(2,4),Cell(4,4))', scope47)
        con48 = Constraint('Relation(Cell(3,1),Cell(3,2))', scope48)
        con49 = Constraint('Relation(Cell(3,1),Cell(3,3))', scope49)
        con50 = Constraint('Relation(Cell(3,1),Cell(3,4))', scope50)
        con51 = Constraint('Relation(Cell(3,1),Cell(1,1))', scope51)
        con52 = Constraint('Relation(Cell(3,1),Cell(2,1))', scope52)
        con53 = Constraint('Relation(Cell(3,1),Cell(4,1))', scope53)
        con54 = Constraint('Relation(Cell(3,2),Cell(3,1))', scope54)
        con55 = Constraint('Relation(Cell(3,2),Cell(3,3))', scope55)
        con56 = Constraint('Relation(Cell(3,2),Cell(3,4))', scope56)
        con57 = Constraint('Relation(Cell(3,2),Cell(1,2))', scope57)
        con58 = Constraint('Relation(Cell(3,2),Cell(2,2))', scope58)
        con59 = Constraint('Relation(Cell(3,2),Cell(4,2))', scope59)
        con60 = Constraint('Relation(Cell(3,3),Cell(3,1))', scope60)
        con61 = Constraint('Relation(Cell(3,3),Cell(3,2))', scope61)
        con62 = Constraint('Relation(Cell(3,3),Cell(3,4))', scope62)
        con63 = Constraint('Relation(Cell(3,3),Cell(1,3))', scope63)
        con64 = Constraint('Relation(Cell(3,3),Cell(2,3))', scope64)
        con65 = Constraint('Relation(Cell(3,3),Cell(4,3))', scope65)
        con66 = Constraint('Relation(Cell(3,4),Cell(3,1))', scope66)
        con67 = Constraint('Relation(Cell(3,4),Cell(3,2))', scope67)
        con68 = Constraint('Relation(Cell(3,4),Cell(3,3))', scope68)
        con69 = Constraint('Relation(Cell(3,4),Cell(1,4))', scope69)
        con70 = Constraint('Relation(Cell(3,4),Cell(2,4))', scope70)
        con71 = Constraint('Relation(Cell(3,4),Cell(4,4))', scope71)
        con72 = Constraint('Relation(Cell(4,1),Cell(4,2))', scope72)
        con73 = Constraint('Relation(Cell(4,1),Cell(4,3))', scope73)
        con74 = Constraint('Relation(Cell(4,1),Cell(4,4))', scope74)
        con75 = Constraint('Relation(Cell(4,1),Cell(1,1))', scope75)
        con76 = Constraint('Relation(Cell(4,1),Cell(2,1))', scope76)
        con77 = Constraint('Relation(Cell(4,1),Cell(3,1))', scope77)
        con78 = Constraint('Relation(Cell(4,2),Cell(4,1))', scope78)
        con79 = Constraint('Relation(Cell(4,2),Cell(4,3))', scope79)
        con80 = Constraint('Relation(Cell(4,2),Cell(4,4))', scope80)
        con81 = Constraint('Relation(Cell(4,2),Cell(1,2))', scope81)
        con82 = Constraint('Relation(Cell(4,2),Cell(2,2))', scope82)
        con83 = Constraint('Relation(Cell(4,2),Cell(3,2))', scope83)
        con84 = Constraint('Relation(Cell(4,3),Cell(4,1))', scope84)
        con85 = Constraint('Relation(Cell(4,3),Cell(4,2))', scope85)
        con86 = Constraint('Relation(Cell(4,3),Cell(4,4))', scope86)
        con87 = Constraint('Relation(Cell(4,3),Cell(1,3))', scope87)
        con88 = Constraint('Relation(Cell(4,3),Cell(2,3))', scope88)
        con89 = Constraint('Relation(Cell(4,3),Cell(3,3))', scope89)
        con90 = Constraint('Relation(Cell(4,4),Cell(4,1))', scope90)
        con91 = Constraint('Relation(Cell(4,4),Cell(4,2))', scope91)
        con92 = Constraint('Relation(Cell(4,4),Cell(4,3))', scope92)
        con93 = Constraint('Relation(Cell(4,4),Cell(1,4))', scope93)
        con94 = Constraint('Relation(Cell(4,4),Cell(2,4))', scope94)
        con95 = Constraint('Relation(Cell(4,4),Cell(3,4))', scope95)

        con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con48.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con49.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con50.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con51.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con52.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con53.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con54.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con55.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con56.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con57.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con58.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con59.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con60.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con61.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con62.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con63.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con64.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con65.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con66.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con67.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con68.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con69.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con70.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con71.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con72.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con73.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con74.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con75.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con76.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con77.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con78.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con79.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con80.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con81.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con82.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con83.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con84.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con85.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con86.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con87.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con88.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con89.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con90.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con91.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con92.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con93.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con94.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con95.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47, con48, con49, con50, con51, con52, con53, con54, con55, con56, con57, con58, con59, con60, con61, con62, con63, con64, con65, con66, con67, con68, con69, con70, con71, con72, con73, con74, con75, con76, con77, con78, con79, con80, con81, con82, con83, con84, con85, con86, con87, con88, con89, con90, con91, con92, con93, con94, con95]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15]
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15
        ]

        csp = CSP("Bin_Cagey(4x4)", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 2:

        var0 = Variable("Cell(1,1)", [1, 2, 3, 4])
        var1 = Variable("Cell(1,2)", [1, 2, 3, 4])
        var2 = Variable("Cell(1,3)", [1, 2, 3, 4])
        var3 = Variable("Cell(1,4)", [1, 2, 3, 4])
        var4 = Variable("Cell(2,1)", [1, 2, 3, 4])
        var5 = Variable("Cell(2,2)", [1, 2, 3, 4])
        var6 = Variable("Cell(2,3)", [1, 2, 3, 4])
        var7 = Variable("Cell(2,4)", [1, 2, 3, 4])
        var8 = Variable("Cell(3,1)", [1, 2, 3, 4])
        var9 = Variable("Cell(3,2)", [1, 2, 3, 4])
        var10 = Variable("Cell(3,3)", [1, 2, 3, 4])
        var11 = Variable("Cell(3,4)", [1, 2, 3, 4])
        var12 = Variable("Cell(4,1)", [1, 2, 3, 4])
        var13 = Variable("Cell(4,2)", [1, 2, 3, 4])
        var14 = Variable("Cell(4,3)", [1, 2, 3, 4])
        var15 = Variable("Cell(4,4)", [1, 2, 3, 4])

        scope0 = [var0, var1]
        scope1 = [var0, var2]
        scope2 = [var0, var3]
        scope3 = [var0, var4]
        scope4 = [var0, var8]
        scope5 = [var0, var12]
        scope6 = [var1, var0]
        scope7 = [var1, var2]
        scope8 = [var1, var3]
        scope9 = [var1, var5]
        scope10 = [var1, var9]
        scope11 = [var1, var13]
        scope12 = [var2, var0]
        scope13 = [var2, var1]
        scope14 = [var2, var3]
        scope15 = [var2, var6]
        scope16 = [var2, var10]
        scope17 = [var2, var14]
        scope18 = [var3, var0]
        scope19 = [var3, var1]
        scope20 = [var3, var2]
        scope21 = [var3, var7]
        scope22 = [var3, var11]
        scope23 = [var3, var15]
        scope24 = [var4, var5]
        scope25 = [var4, var6]
        scope26 = [var4, var7]
        scope27 = [var4, var0]
        scope28 = [var4, var8]
        scope29 = [var4, var12]
        scope30 = [var5, var4]
        scope31 = [var5, var6]
        scope32 = [var5, var7]
        scope33 = [var5, var1]
        scope34 = [var5, var9]
        scope35 = [var5, var13]
        scope36 = [var6, var4]
        scope37 = [var6, var5]
        scope38 = [var6, var7]
        scope39 = [var6, var2]
        scope40 = [var6, var10]
        scope41 = [var6, var14]
        scope42 = [var7, var4]
        scope43 = [var7, var5]
        scope44 = [var7, var6]
        scope45 = [var7, var3]
        scope46 = [var7, var11]
        scope47 = [var7, var15]
        scope48 = [var8, var9]
        scope49 = [var8, var10]
        scope50 = [var8, var11]
        scope51 = [var8, var0]
        scope52 = [var8, var4]
        scope53 = [var8, var12]
        scope54 = [var9, var8]
        scope55 = [var9, var10]
        scope56 = [var9, var11]
        scope57 = [var9, var1]
        scope58 = [var9, var5]
        scope59 = [var9, var13]
        scope60 = [var10, var8]
        scope61 = [var10, var9]
        scope62 = [var10, var11]
        scope63 = [var10, var2]
        scope64 = [var10, var6]
        scope65 = [var10, var14]
        scope66 = [var11, var8]
        scope67 = [var11, var9]
        scope68 = [var11, var10]
        scope69 = [var11, var3]
        scope70 = [var11, var7]
        scope71 = [var11, var15]
        scope72 = [var12, var13]
        scope73 = [var12, var14]
        scope74 = [var12, var15]
        scope75 = [var12, var0]
        scope76 = [var12, var4]
        scope77 = [var12, var8]
        scope78 = [var13, var12]
        scope79 = [var13, var14]
        scope80 = [var13, var15]
        scope81 = [var13, var1]
        scope82 = [var13, var5]
        scope83 = [var13, var9]
        scope84 = [var14, var12]
        scope85 = [var14, var13]
        scope86 = [var14, var15]
        scope87 = [var14, var2]
        scope88 = [var14, var6]
        scope89 = [var14, var10]
        scope90 = [var15, var12]
        scope91 = [var15, var13]
        scope92 = [var15, var14]
        scope93 = [var15, var3]
        scope94 = [var15, var7]
        scope95 = [var15, var11]

        con0 = Constraint('Relation(Cell(1,1),Cell(1,2))', scope0)
        con1 = Constraint('Relation(Cell(1,1),Cell(1,3))', scope1)
        con2 = Constraint('Relation(Cell(1,1),Cell(1,4))', scope2)
        con3 = Constraint('Relation(Cell(1,1),Cell(2,1))', scope3)
        con4 = Constraint('Relation(Cell(1,1),Cell(3,1))', scope4)
        con5 = Constraint('Relation(Cell(1,1),Cell(4,1))', scope5)
        con6 = Constraint('Relation(Cell(1,2),Cell(1,1))', scope6)
        con7 = Constraint('Relation(Cell(1,2),Cell(1,3))', scope7)
        con8 = Constraint('Relation(Cell(1,2),Cell(1,4))', scope8)
        con9 = Constraint('Relation(Cell(1,2),Cell(2,2))', scope9)
        con10 = Constraint('Relation(Cell(1,2),Cell(3,2))', scope10)
        con11 = Constraint('Relation(Cell(1,2),Cell(4,2))', scope11)
        con12 = Constraint('Relation(Cell(1,3),Cell(1,1))', scope12)
        con13 = Constraint('Relation(Cell(1,3),Cell(1,2))', scope13)
        con14 = Constraint('Relation(Cell(1,3),Cell(1,4))', scope14)
        con15 = Constraint('Relation(Cell(1,3),Cell(2,3))', scope15)
        con16 = Constraint('Relation(Cell(1,3),Cell(3,3))', scope16)
        con17 = Constraint('Relation(Cell(1,3),Cell(4,3))', scope17)
        con18 = Constraint('Relation(Cell(1,4),Cell(1,1))', scope18)
        con19 = Constraint('Relation(Cell(1,4),Cell(1,2))', scope19)
        con20 = Constraint('Relation(Cell(1,4),Cell(1,3))', scope20)
        con21 = Constraint('Relation(Cell(1,4),Cell(2,4))', scope21)
        con22 = Constraint('Relation(Cell(1,4),Cell(3,4))', scope22)
        con23 = Constraint('Relation(Cell(1,4),Cell(4,4))', scope23)
        con24 = Constraint('Relation(Cell(2,1),Cell(2,2))', scope24)
        con25 = Constraint('Relation(Cell(2,1),Cell(2,3))', scope25)
        con26 = Constraint('Relation(Cell(2,1),Cell(2,4))', scope26)
        con27 = Constraint('Relation(Cell(2,1),Cell(1,1))', scope27)
        con28 = Constraint('Relation(Cell(2,1),Cell(3,1))', scope28)
        con29 = Constraint('Relation(Cell(2,1),Cell(4,1))', scope29)
        con30 = Constraint('Relation(Cell(2,2),Cell(2,1))', scope30)
        con31 = Constraint('Relation(Cell(2,2),Cell(2,3))', scope31)
        con32 = Constraint('Relation(Cell(2,2),Cell(2,4))', scope32)
        con33 = Constraint('Relation(Cell(2,2),Cell(1,2))', scope33)
        con34 = Constraint('Relation(Cell(2,2),Cell(3,2))', scope34)
        con35 = Constraint('Relation(Cell(2,2),Cell(4,2))', scope35)
        con36 = Constraint('Relation(Cell(2,3),Cell(2,1))', scope36)
        con37 = Constraint('Relation(Cell(2,3),Cell(2,2))', scope37)
        con38 = Constraint('Relation(Cell(2,3),Cell(2,4))', scope38)
        con39 = Constraint('Relation(Cell(2,3),Cell(1,3))', scope39)
        con40 = Constraint('Relation(Cell(2,3),Cell(3,3))', scope40)
        con41 = Constraint('Relation(Cell(2,3),Cell(4,3))', scope41)
        con42 = Constraint('Relation(Cell(2,4),Cell(2,1))', scope42)
        con43 = Constraint('Relation(Cell(2,4),Cell(2,2))', scope43)
        con44 = Constraint('Relation(Cell(2,4),Cell(2,3))', scope44)
        con45 = Constraint('Relation(Cell(2,4),Cell(1,4))', scope45)
        con46 = Constraint('Relation(Cell(2,4),Cell(3,4))', scope46)
        con47 = Constraint('Relation(Cell(2,4),Cell(4,4))', scope47)
        con48 = Constraint('Relation(Cell(3,1),Cell(3,2))', scope48)
        con49 = Constraint('Relation(Cell(3,1),Cell(3,3))', scope49)
        con50 = Constraint('Relation(Cell(3,1),Cell(3,4))', scope50)
        con51 = Constraint('Relation(Cell(3,1),Cell(1,1))', scope51)
        con52 = Constraint('Relation(Cell(3,1),Cell(2,1))', scope52)
        con53 = Constraint('Relation(Cell(3,1),Cell(4,1))', scope53)
        con54 = Constraint('Relation(Cell(3,2),Cell(3,1))', scope54)
        con55 = Constraint('Relation(Cell(3,2),Cell(3,3))', scope55)
        con56 = Constraint('Relation(Cell(3,2),Cell(3,4))', scope56)
        con57 = Constraint('Relation(Cell(3,2),Cell(1,2))', scope57)
        con58 = Constraint('Relation(Cell(3,2),Cell(2,2))', scope58)
        con59 = Constraint('Relation(Cell(3,2),Cell(4,2))', scope59)
        con60 = Constraint('Relation(Cell(3,3),Cell(3,1))', scope60)
        con61 = Constraint('Relation(Cell(3,3),Cell(3,2))', scope61)
        con62 = Constraint('Relation(Cell(3,3),Cell(3,4))', scope62)
        con63 = Constraint('Relation(Cell(3,3),Cell(1,3))', scope63)
        con64 = Constraint('Relation(Cell(3,3),Cell(2,3))', scope64)
        con65 = Constraint('Relation(Cell(3,3),Cell(4,3))', scope65)
        con66 = Constraint('Relation(Cell(3,4),Cell(3,1))', scope66)
        con67 = Constraint('Relation(Cell(3,4),Cell(3,2))', scope67)
        con68 = Constraint('Relation(Cell(3,4),Cell(3,3))', scope68)
        con69 = Constraint('Relation(Cell(3,4),Cell(1,4))', scope69)
        con70 = Constraint('Relation(Cell(3,4),Cell(2,4))', scope70)
        con71 = Constraint('Relation(Cell(3,4),Cell(4,4))', scope71)
        con72 = Constraint('Relation(Cell(4,1),Cell(4,2))', scope72)
        con73 = Constraint('Relation(Cell(4,1),Cell(4,3))', scope73)
        con74 = Constraint('Relation(Cell(4,1),Cell(4,4))', scope74)
        con75 = Constraint('Relation(Cell(4,1),Cell(1,1))', scope75)
        con76 = Constraint('Relation(Cell(4,1),Cell(2,1))', scope76)
        con77 = Constraint('Relation(Cell(4,1),Cell(3,1))', scope77)
        con78 = Constraint('Relation(Cell(4,2),Cell(4,1))', scope78)
        con79 = Constraint('Relation(Cell(4,2),Cell(4,3))', scope79)
        con80 = Constraint('Relation(Cell(4,2),Cell(4,4))', scope80)
        con81 = Constraint('Relation(Cell(4,2),Cell(1,2))', scope81)
        con82 = Constraint('Relation(Cell(4,2),Cell(2,2))', scope82)
        con83 = Constraint('Relation(Cell(4,2),Cell(3,2))', scope83)
        con84 = Constraint('Relation(Cell(4,3),Cell(4,1))', scope84)
        con85 = Constraint('Relation(Cell(4,3),Cell(4,2))', scope85)
        con86 = Constraint('Relation(Cell(4,3),Cell(4,4))', scope86)
        con87 = Constraint('Relation(Cell(4,3),Cell(1,3))', scope87)
        con88 = Constraint('Relation(Cell(4,3),Cell(2,3))', scope88)
        con89 = Constraint('Relation(Cell(4,3),Cell(3,3))', scope89)
        con90 = Constraint('Relation(Cell(4,4),Cell(4,1))', scope90)
        con91 = Constraint('Relation(Cell(4,4),Cell(4,2))', scope91)
        con92 = Constraint('Relation(Cell(4,4),Cell(4,3))', scope92)
        con93 = Constraint('Relation(Cell(4,4),Cell(1,4))', scope93)
        con94 = Constraint('Relation(Cell(4,4),Cell(2,4))', scope94)
        con95 = Constraint('Relation(Cell(4,4),Cell(3,4))', scope95)

        con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con48.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con49.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con50.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con51.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con52.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con53.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con54.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con55.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con56.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con57.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con58.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con59.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con60.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con61.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con62.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con63.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con64.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con65.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con66.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con67.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con68.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con69.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con70.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con71.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con72.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con73.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con74.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con75.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con76.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con77.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con78.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con79.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con80.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con81.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con82.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con83.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con84.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con85.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con86.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con87.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con88.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con89.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con90.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con91.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con92.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con93.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con94.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con95.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47, con48, con49, con50, con51, con52, con53, con54, con55, con56, con57, con58, con59, con60, con61, con62, con63, con64, con65, con66, con67, con68, con69, con70, con71, con72, con73, con74, con75, con76, con77, con78, con79, con80, con81, con82, con83, con84, con85, con86, con87, con88, con89, con90, con91, con92, con93, con94, con95]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15]
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15
        ]

        csp = CSP("Bin_Cagey(4x4)", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array
    
    if b_num == 3:

        var0 = Variable("Cell(1,1)", [1, 2, 3, 4])
        var1 = Variable("Cell(1,2)", [1, 2, 3, 4])
        var2 = Variable("Cell(1,3)", [1, 2, 3, 4])
        var3 = Variable("Cell(1,4)", [1, 2, 3, 4])
        var4 = Variable("Cell(2,1)", [1, 2, 3, 4])
        var5 = Variable("Cell(2,2)", [1, 2, 3, 4])
        var6 = Variable("Cell(2,3)", [1, 2, 3, 4])
        var7 = Variable("Cell(2,4)", [1, 2, 3, 4])
        var8 = Variable("Cell(3,1)", [1, 2, 3, 4])
        var9 = Variable("Cell(3,2)", [1, 2, 3, 4])
        var10 = Variable("Cell(3,3)", [1, 2, 3, 4])
        var11 = Variable("Cell(3,4)", [1, 2, 3, 4])
        var12 = Variable("Cell(4,1)", [1, 2, 3, 4])
        var13 = Variable("Cell(4,2)", [1, 2, 3, 4])
        var14 = Variable("Cell(4,3)", [1, 2, 3, 4])
        var15 = Variable("Cell(4,4)", [1, 2, 3, 4])

        scope0 = [var0, var1]
        scope1 = [var0, var2]
        scope2 = [var0, var3]
        scope3 = [var0, var4]
        scope4 = [var0, var8]
        scope5 = [var0, var12]
        scope6 = [var1, var0]
        scope7 = [var1, var2]
        scope8 = [var1, var3]
        scope9 = [var1, var5]
        scope10 = [var1, var9]
        scope11 = [var1, var13]
        scope12 = [var2, var0]
        scope13 = [var2, var1]
        scope14 = [var2, var3]
        scope15 = [var2, var6]
        scope16 = [var2, var10]
        scope17 = [var2, var14]
        scope18 = [var3, var0]
        scope19 = [var3, var1]
        scope20 = [var3, var2]
        scope21 = [var3, var7]
        scope22 = [var3, var11]
        scope23 = [var3, var15]
        scope24 = [var4, var5]
        scope25 = [var4, var6]
        scope26 = [var4, var7]
        scope27 = [var4, var0]
        scope28 = [var4, var8]
        scope29 = [var4, var12]
        scope30 = [var5, var4]
        scope31 = [var5, var6]
        scope32 = [var5, var7]
        scope33 = [var5, var1]
        scope34 = [var5, var9]
        scope35 = [var5, var13]
        scope36 = [var6, var4]
        scope37 = [var6, var5]
        scope38 = [var6, var7]
        scope39 = [var6, var2]
        scope40 = [var6, var10]
        scope41 = [var6, var14]
        scope42 = [var7, var4]
        scope43 = [var7, var5]
        scope44 = [var7, var6]
        scope45 = [var7, var3]
        scope46 = [var7, var11]
        scope47 = [var7, var15]
        scope48 = [var8, var9]
        scope49 = [var8, var10]
        scope50 = [var8, var11]
        scope51 = [var8, var0]
        scope52 = [var8, var4]
        scope53 = [var8, var12]
        scope54 = [var9, var8]
        scope55 = [var9, var10]
        scope56 = [var9, var11]
        scope57 = [var9, var1]
        scope58 = [var9, var5]
        scope59 = [var9, var13]
        scope60 = [var10, var8]
        scope61 = [var10, var9]
        scope62 = [var10, var11]
        scope63 = [var10, var2]
        scope64 = [var10, var6]
        scope65 = [var10, var14]
        scope66 = [var11, var8]
        scope67 = [var11, var9]
        scope68 = [var11, var10]
        scope69 = [var11, var3]
        scope70 = [var11, var7]
        scope71 = [var11, var15]
        scope72 = [var12, var13]
        scope73 = [var12, var14]
        scope74 = [var12, var15]
        scope75 = [var12, var0]
        scope76 = [var12, var4]
        scope77 = [var12, var8]
        scope78 = [var13, var12]
        scope79 = [var13, var14]
        scope80 = [var13, var15]
        scope81 = [var13, var1]
        scope82 = [var13, var5]
        scope83 = [var13, var9]
        scope84 = [var14, var12]
        scope85 = [var14, var13]
        scope86 = [var14, var15]
        scope87 = [var14, var2]
        scope88 = [var14, var6]
        scope89 = [var14, var10]
        scope90 = [var15, var12]
        scope91 = [var15, var13]
        scope92 = [var15, var14]
        scope93 = [var15, var3]
        scope94 = [var15, var7]
        scope95 = [var15, var11]

        con0 = Constraint('Relation(Cell(1,1),Cell(1,2))', scope0)
        con1 = Constraint('Relation(Cell(1,1),Cell(1,3))', scope1)
        con2 = Constraint('Relation(Cell(1,1),Cell(1,4))', scope2)
        con3 = Constraint('Relation(Cell(1,1),Cell(2,1))', scope3)
        con4 = Constraint('Relation(Cell(1,1),Cell(3,1))', scope4)
        con5 = Constraint('Relation(Cell(1,1),Cell(4,1))', scope5)
        con6 = Constraint('Relation(Cell(1,2),Cell(1,1))', scope6)
        con7 = Constraint('Relation(Cell(1,2),Cell(1,3))', scope7)
        con8 = Constraint('Relation(Cell(1,2),Cell(1,4))', scope8)
        con9 = Constraint('Relation(Cell(1,2),Cell(2,2))', scope9)
        con10 = Constraint('Relation(Cell(1,2),Cell(3,2))', scope10)
        con11 = Constraint('Relation(Cell(1,2),Cell(4,2))', scope11)
        con12 = Constraint('Relation(Cell(1,3),Cell(1,1))', scope12)
        con13 = Constraint('Relation(Cell(1,3),Cell(1,2))', scope13)
        con14 = Constraint('Relation(Cell(1,3),Cell(1,4))', scope14)
        con15 = Constraint('Relation(Cell(1,3),Cell(2,3))', scope15)
        con16 = Constraint('Relation(Cell(1,3),Cell(3,3))', scope16)
        con17 = Constraint('Relation(Cell(1,3),Cell(4,3))', scope17)
        con18 = Constraint('Relation(Cell(1,4),Cell(1,1))', scope18)
        con19 = Constraint('Relation(Cell(1,4),Cell(1,2))', scope19)
        con20 = Constraint('Relation(Cell(1,4),Cell(1,3))', scope20)
        con21 = Constraint('Relation(Cell(1,4),Cell(2,4))', scope21)
        con22 = Constraint('Relation(Cell(1,4),Cell(3,4))', scope22)
        con23 = Constraint('Relation(Cell(1,4),Cell(4,4))', scope23)
        con24 = Constraint('Relation(Cell(2,1),Cell(2,2))', scope24)
        con25 = Constraint('Relation(Cell(2,1),Cell(2,3))', scope25)
        con26 = Constraint('Relation(Cell(2,1),Cell(2,4))', scope26)
        con27 = Constraint('Relation(Cell(2,1),Cell(1,1))', scope27)
        con28 = Constraint('Relation(Cell(2,1),Cell(3,1))', scope28)
        con29 = Constraint('Relation(Cell(2,1),Cell(4,1))', scope29)
        con30 = Constraint('Relation(Cell(2,2),Cell(2,1))', scope30)
        con31 = Constraint('Relation(Cell(2,2),Cell(2,3))', scope31)
        con32 = Constraint('Relation(Cell(2,2),Cell(2,4))', scope32)
        con33 = Constraint('Relation(Cell(2,2),Cell(1,2))', scope33)
        con34 = Constraint('Relation(Cell(2,2),Cell(3,2))', scope34)
        con35 = Constraint('Relation(Cell(2,2),Cell(4,2))', scope35)
        con36 = Constraint('Relation(Cell(2,3),Cell(2,1))', scope36)
        con37 = Constraint('Relation(Cell(2,3),Cell(2,2))', scope37)
        con38 = Constraint('Relation(Cell(2,3),Cell(2,4))', scope38)
        con39 = Constraint('Relation(Cell(2,3),Cell(1,3))', scope39)
        con40 = Constraint('Relation(Cell(2,3),Cell(3,3))', scope40)
        con41 = Constraint('Relation(Cell(2,3),Cell(4,3))', scope41)
        con42 = Constraint('Relation(Cell(2,4),Cell(2,1))', scope42)
        con43 = Constraint('Relation(Cell(2,4),Cell(2,2))', scope43)
        con44 = Constraint('Relation(Cell(2,4),Cell(2,3))', scope44)
        con45 = Constraint('Relation(Cell(2,4),Cell(1,4))', scope45)
        con46 = Constraint('Relation(Cell(2,4),Cell(3,4))', scope46)
        con47 = Constraint('Relation(Cell(2,4),Cell(4,4))', scope47)
        con48 = Constraint('Relation(Cell(3,1),Cell(3,2))', scope48)
        con49 = Constraint('Relation(Cell(3,1),Cell(3,3))', scope49)
        con50 = Constraint('Relation(Cell(3,1),Cell(3,4))', scope50)
        con51 = Constraint('Relation(Cell(3,1),Cell(1,1))', scope51)
        con52 = Constraint('Relation(Cell(3,1),Cell(2,1))', scope52)
        con53 = Constraint('Relation(Cell(3,1),Cell(4,1))', scope53)
        con54 = Constraint('Relation(Cell(3,2),Cell(3,1))', scope54)
        con55 = Constraint('Relation(Cell(3,2),Cell(3,3))', scope55)
        con56 = Constraint('Relation(Cell(3,2),Cell(3,4))', scope56)
        con57 = Constraint('Relation(Cell(3,2),Cell(1,2))', scope57)
        con58 = Constraint('Relation(Cell(3,2),Cell(2,2))', scope58)
        con59 = Constraint('Relation(Cell(3,2),Cell(4,2))', scope59)
        con60 = Constraint('Relation(Cell(3,3),Cell(3,1))', scope60)
        con61 = Constraint('Relation(Cell(3,3),Cell(3,2))', scope61)
        con62 = Constraint('Relation(Cell(3,3),Cell(3,4))', scope62)
        con63 = Constraint('Relation(Cell(3,3),Cell(1,3))', scope63)
        con64 = Constraint('Relation(Cell(3,3),Cell(2,3))', scope64)
        con65 = Constraint('Relation(Cell(3,3),Cell(4,3))', scope65)
        con66 = Constraint('Relation(Cell(3,4),Cell(3,1))', scope66)
        con67 = Constraint('Relation(Cell(3,4),Cell(3,2))', scope67)
        con68 = Constraint('Relation(Cell(3,4),Cell(3,3))', scope68)
        con69 = Constraint('Relation(Cell(3,4),Cell(1,4))', scope69)
        con70 = Constraint('Relation(Cell(3,4),Cell(2,4))', scope70)
        con71 = Constraint('Relation(Cell(3,4),Cell(4,4))', scope71)
        con72 = Constraint('Relation(Cell(4,1),Cell(4,2))', scope72)
        con73 = Constraint('Relation(Cell(4,1),Cell(4,3))', scope73)
        con74 = Constraint('Relation(Cell(4,1),Cell(4,4))', scope74)
        con75 = Constraint('Relation(Cell(4,1),Cell(1,1))', scope75)
        con76 = Constraint('Relation(Cell(4,1),Cell(2,1))', scope76)
        con77 = Constraint('Relation(Cell(4,1),Cell(3,1))', scope77)
        con78 = Constraint('Relation(Cell(4,2),Cell(4,1))', scope78)
        con79 = Constraint('Relation(Cell(4,2),Cell(4,3))', scope79)
        con80 = Constraint('Relation(Cell(4,2),Cell(4,4))', scope80)
        con81 = Constraint('Relation(Cell(4,2),Cell(1,2))', scope81)
        con82 = Constraint('Relation(Cell(4,2),Cell(2,2))', scope82)
        con83 = Constraint('Relation(Cell(4,2),Cell(3,2))', scope83)
        con84 = Constraint('Relation(Cell(4,3),Cell(4,1))', scope84)
        con85 = Constraint('Relation(Cell(4,3),Cell(4,2))', scope85)
        con86 = Constraint('Relation(Cell(4,3),Cell(4,4))', scope86)
        con87 = Constraint('Relation(Cell(4,3),Cell(1,3))', scope87)
        con88 = Constraint('Relation(Cell(4,3),Cell(2,3))', scope88)
        con89 = Constraint('Relation(Cell(4,3),Cell(3,3))', scope89)
        con90 = Constraint('Relation(Cell(4,4),Cell(4,1))', scope90)
        con91 = Constraint('Relation(Cell(4,4),Cell(4,2))', scope91)
        con92 = Constraint('Relation(Cell(4,4),Cell(4,3))', scope92)
        con93 = Constraint('Relation(Cell(4,4),Cell(1,4))', scope93)
        con94 = Constraint('Relation(Cell(4,4),Cell(2,4))', scope94)
        con95 = Constraint('Relation(Cell(4,4),Cell(3,4))', scope95)

        con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con48.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con49.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con50.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con51.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con52.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con53.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con54.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con55.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con56.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con57.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con58.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con59.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con60.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con61.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con62.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con63.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con64.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con65.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con66.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con67.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con68.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con69.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con70.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con71.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con72.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con73.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con74.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con75.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con76.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con77.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con78.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con79.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con80.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con81.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con82.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con83.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con84.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con85.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con86.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con87.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con88.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con89.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con90.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con91.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con92.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con93.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con94.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con95.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47, con48, con49, con50, con51, con52, con53, con54, con55, con56, con57, con58, con59, con60, con61, con62, con63, con64, con65, con66, con67, con68, con69, con70, con71, con72, con73, con74, con75, con76, con77, con78, con79, con80, con81, con82, con83, con84, con85, con86, con87, con88, con89, con90, con91, con92, con93, con94, con95]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15]
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15
        ]

        csp = CSP("Bin_Cagey(4x4)", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 4:

        var0 = Variable("Cell(1,1)", [1, 2, 3, 4])
        var1 = Variable("Cell(1,2)", [1, 2, 3, 4])
        var2 = Variable("Cell(1,3)", [1, 2, 3, 4])
        var3 = Variable("Cell(1,4)", [1, 2, 3, 4])
        var4 = Variable("Cell(2,1)", [1, 2, 3, 4])
        var5 = Variable("Cell(2,2)", [1, 2, 3, 4])
        var6 = Variable("Cell(2,3)", [1, 2, 3, 4])
        var7 = Variable("Cell(2,4)", [1, 2, 3, 4])
        var8 = Variable("Cell(3,1)", [1, 2, 3, 4])
        var9 = Variable("Cell(3,2)", [1, 2, 3, 4])
        var10 = Variable("Cell(3,3)", [1, 2, 3, 4])
        var11 = Variable("Cell(3,4)", [1, 2, 3, 4])
        var12 = Variable("Cell(4,1)", [1, 2, 3, 4])
        var13 = Variable("Cell(4,2)", [1, 2, 3, 4])
        var14 = Variable("Cell(4,3)", [1, 2, 3, 4])
        var15 = Variable("Cell(4,4)", [1, 2, 3, 4])

        scope0 = [var0, var1]
        scope1 = [var0, var2]
        scope2 = [var0, var3]
        scope3 = [var0, var4]
        scope4 = [var0, var8]
        scope5 = [var0, var12]
        scope6 = [var1, var0]
        scope7 = [var1, var2]
        scope8 = [var1, var3]
        scope9 = [var1, var5]
        scope10 = [var1, var9]
        scope11 = [var1, var13]
        scope12 = [var2, var0]
        scope13 = [var2, var1]
        scope14 = [var2, var3]
        scope15 = [var2, var6]
        scope16 = [var2, var10]
        scope17 = [var2, var14]
        scope18 = [var3, var0]
        scope19 = [var3, var1]
        scope20 = [var3, var2]
        scope21 = [var3, var7]
        scope22 = [var3, var11]
        scope23 = [var3, var15]
        scope24 = [var4, var5]
        scope25 = [var4, var6]
        scope26 = [var4, var7]
        scope27 = [var4, var0]
        scope28 = [var4, var8]
        scope29 = [var4, var12]
        scope30 = [var5, var4]
        scope31 = [var5, var6]
        scope32 = [var5, var7]
        scope33 = [var5, var1]
        scope34 = [var5, var9]
        scope35 = [var5, var13]
        scope36 = [var6, var4]
        scope37 = [var6, var5]
        scope38 = [var6, var7]
        scope39 = [var6, var2]
        scope40 = [var6, var10]
        scope41 = [var6, var14]
        scope42 = [var7, var4]
        scope43 = [var7, var5]
        scope44 = [var7, var6]
        scope45 = [var7, var3]
        scope46 = [var7, var11]
        scope47 = [var7, var15]
        scope48 = [var8, var9]
        scope49 = [var8, var10]
        scope50 = [var8, var11]
        scope51 = [var8, var0]
        scope52 = [var8, var4]
        scope53 = [var8, var12]
        scope54 = [var9, var8]
        scope55 = [var9, var10]
        scope56 = [var9, var11]
        scope57 = [var9, var1]
        scope58 = [var9, var5]
        scope59 = [var9, var13]
        scope60 = [var10, var8]
        scope61 = [var10, var9]
        scope62 = [var10, var11]
        scope63 = [var10, var2]
        scope64 = [var10, var6]
        scope65 = [var10, var14]
        scope66 = [var11, var8]
        scope67 = [var11, var9]
        scope68 = [var11, var10]
        scope69 = [var11, var3]
        scope70 = [var11, var7]
        scope71 = [var11, var15]
        scope72 = [var12, var13]
        scope73 = [var12, var14]
        scope74 = [var12, var15]
        scope75 = [var12, var0]
        scope76 = [var12, var4]
        scope77 = [var12, var8]
        scope78 = [var13, var12]
        scope79 = [var13, var14]
        scope80 = [var13, var15]
        scope81 = [var13, var1]
        scope82 = [var13, var5]
        scope83 = [var13, var9]
        scope84 = [var14, var12]
        scope85 = [var14, var13]
        scope86 = [var14, var15]
        scope87 = [var14, var2]
        scope88 = [var14, var6]
        scope89 = [var14, var10]
        scope90 = [var15, var12]
        scope91 = [var15, var13]
        scope92 = [var15, var14]
        scope93 = [var15, var3]
        scope94 = [var15, var7]
        scope95 = [var15, var11]

        con0 = Constraint('Relation(Cell(1,1),Cell(1,2))', scope0)
        con1 = Constraint('Relation(Cell(1,1),Cell(1,3))', scope1)
        con2 = Constraint('Relation(Cell(1,1),Cell(1,4))', scope2)
        con3 = Constraint('Relation(Cell(1,1),Cell(2,1))', scope3)
        con4 = Constraint('Relation(Cell(1,1),Cell(3,1))', scope4)
        con5 = Constraint('Relation(Cell(1,1),Cell(4,1))', scope5)
        con6 = Constraint('Relation(Cell(1,2),Cell(1,1))', scope6)
        con7 = Constraint('Relation(Cell(1,2),Cell(1,3))', scope7)
        con8 = Constraint('Relation(Cell(1,2),Cell(1,4))', scope8)
        con9 = Constraint('Relation(Cell(1,2),Cell(2,2))', scope9)
        con10 = Constraint('Relation(Cell(1,2),Cell(3,2))', scope10)
        con11 = Constraint('Relation(Cell(1,2),Cell(4,2))', scope11)
        con12 = Constraint('Relation(Cell(1,3),Cell(1,1))', scope12)
        con13 = Constraint('Relation(Cell(1,3),Cell(1,2))', scope13)
        con14 = Constraint('Relation(Cell(1,3),Cell(1,4))', scope14)
        con15 = Constraint('Relation(Cell(1,3),Cell(2,3))', scope15)
        con16 = Constraint('Relation(Cell(1,3),Cell(3,3))', scope16)
        con17 = Constraint('Relation(Cell(1,3),Cell(4,3))', scope17)
        con18 = Constraint('Relation(Cell(1,4),Cell(1,1))', scope18)
        con19 = Constraint('Relation(Cell(1,4),Cell(1,2))', scope19)
        con20 = Constraint('Relation(Cell(1,4),Cell(1,3))', scope20)
        con21 = Constraint('Relation(Cell(1,4),Cell(2,4))', scope21)
        con22 = Constraint('Relation(Cell(1,4),Cell(3,4))', scope22)
        con23 = Constraint('Relation(Cell(1,4),Cell(4,4))', scope23)
        con24 = Constraint('Relation(Cell(2,1),Cell(2,2))', scope24)
        con25 = Constraint('Relation(Cell(2,1),Cell(2,3))', scope25)
        con26 = Constraint('Relation(Cell(2,1),Cell(2,4))', scope26)
        con27 = Constraint('Relation(Cell(2,1),Cell(1,1))', scope27)
        con28 = Constraint('Relation(Cell(2,1),Cell(3,1))', scope28)
        con29 = Constraint('Relation(Cell(2,1),Cell(4,1))', scope29)
        con30 = Constraint('Relation(Cell(2,2),Cell(2,1))', scope30)
        con31 = Constraint('Relation(Cell(2,2),Cell(2,3))', scope31)
        con32 = Constraint('Relation(Cell(2,2),Cell(2,4))', scope32)
        con33 = Constraint('Relation(Cell(2,2),Cell(1,2))', scope33)
        con34 = Constraint('Relation(Cell(2,2),Cell(3,2))', scope34)
        con35 = Constraint('Relation(Cell(2,2),Cell(4,2))', scope35)
        con36 = Constraint('Relation(Cell(2,3),Cell(2,1))', scope36)
        con37 = Constraint('Relation(Cell(2,3),Cell(2,2))', scope37)
        con38 = Constraint('Relation(Cell(2,3),Cell(2,4))', scope38)
        con39 = Constraint('Relation(Cell(2,3),Cell(1,3))', scope39)
        con40 = Constraint('Relation(Cell(2,3),Cell(3,3))', scope40)
        con41 = Constraint('Relation(Cell(2,3),Cell(4,3))', scope41)
        con42 = Constraint('Relation(Cell(2,4),Cell(2,1))', scope42)
        con43 = Constraint('Relation(Cell(2,4),Cell(2,2))', scope43)
        con44 = Constraint('Relation(Cell(2,4),Cell(2,3))', scope44)
        con45 = Constraint('Relation(Cell(2,4),Cell(1,4))', scope45)
        con46 = Constraint('Relation(Cell(2,4),Cell(3,4))', scope46)
        con47 = Constraint('Relation(Cell(2,4),Cell(4,4))', scope47)
        con48 = Constraint('Relation(Cell(3,1),Cell(3,2))', scope48)
        con49 = Constraint('Relation(Cell(3,1),Cell(3,3))', scope49)
        con50 = Constraint('Relation(Cell(3,1),Cell(3,4))', scope50)
        con51 = Constraint('Relation(Cell(3,1),Cell(1,1))', scope51)
        con52 = Constraint('Relation(Cell(3,1),Cell(2,1))', scope52)
        con53 = Constraint('Relation(Cell(3,1),Cell(4,1))', scope53)
        con54 = Constraint('Relation(Cell(3,2),Cell(3,1))', scope54)
        con55 = Constraint('Relation(Cell(3,2),Cell(3,3))', scope55)
        con56 = Constraint('Relation(Cell(3,2),Cell(3,4))', scope56)
        con57 = Constraint('Relation(Cell(3,2),Cell(1,2))', scope57)
        con58 = Constraint('Relation(Cell(3,2),Cell(2,2))', scope58)
        con59 = Constraint('Relation(Cell(3,2),Cell(4,2))', scope59)
        con60 = Constraint('Relation(Cell(3,3),Cell(3,1))', scope60)
        con61 = Constraint('Relation(Cell(3,3),Cell(3,2))', scope61)
        con62 = Constraint('Relation(Cell(3,3),Cell(3,4))', scope62)
        con63 = Constraint('Relation(Cell(3,3),Cell(1,3))', scope63)
        con64 = Constraint('Relation(Cell(3,3),Cell(2,3))', scope64)
        con65 = Constraint('Relation(Cell(3,3),Cell(4,3))', scope65)
        con66 = Constraint('Relation(Cell(3,4),Cell(3,1))', scope66)
        con67 = Constraint('Relation(Cell(3,4),Cell(3,2))', scope67)
        con68 = Constraint('Relation(Cell(3,4),Cell(3,3))', scope68)
        con69 = Constraint('Relation(Cell(3,4),Cell(1,4))', scope69)
        con70 = Constraint('Relation(Cell(3,4),Cell(2,4))', scope70)
        con71 = Constraint('Relation(Cell(3,4),Cell(4,4))', scope71)
        con72 = Constraint('Relation(Cell(4,1),Cell(4,2))', scope72)
        con73 = Constraint('Relation(Cell(4,1),Cell(4,3))', scope73)
        con74 = Constraint('Relation(Cell(4,1),Cell(4,4))', scope74)
        con75 = Constraint('Relation(Cell(4,1),Cell(1,1))', scope75)
        con76 = Constraint('Relation(Cell(4,1),Cell(2,1))', scope76)
        con77 = Constraint('Relation(Cell(4,1),Cell(3,1))', scope77)
        con78 = Constraint('Relation(Cell(4,2),Cell(4,1))', scope78)
        con79 = Constraint('Relation(Cell(4,2),Cell(4,3))', scope79)
        con80 = Constraint('Relation(Cell(4,2),Cell(4,4))', scope80)
        con81 = Constraint('Relation(Cell(4,2),Cell(1,2))', scope81)
        con82 = Constraint('Relation(Cell(4,2),Cell(2,2))', scope82)
        con83 = Constraint('Relation(Cell(4,2),Cell(3,2))', scope83)
        con84 = Constraint('Relation(Cell(4,3),Cell(4,1))', scope84)
        con85 = Constraint('Relation(Cell(4,3),Cell(4,2))', scope85)
        con86 = Constraint('Relation(Cell(4,3),Cell(4,4))', scope86)
        con87 = Constraint('Relation(Cell(4,3),Cell(1,3))', scope87)
        con88 = Constraint('Relation(Cell(4,3),Cell(2,3))', scope88)
        con89 = Constraint('Relation(Cell(4,3),Cell(3,3))', scope89)
        con90 = Constraint('Relation(Cell(4,4),Cell(4,1))', scope90)
        con91 = Constraint('Relation(Cell(4,4),Cell(4,2))', scope91)
        con92 = Constraint('Relation(Cell(4,4),Cell(4,3))', scope92)
        con93 = Constraint('Relation(Cell(4,4),Cell(1,4))', scope93)
        con94 = Constraint('Relation(Cell(4,4),Cell(2,4))', scope94)
        con95 = Constraint('Relation(Cell(4,4),Cell(3,4))', scope95)

        con0.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con1.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con2.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con3.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con4.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con5.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con6.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con7.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con8.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con9.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con10.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con11.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con12.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con13.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con14.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con15.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con16.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con17.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con18.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con19.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con20.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con21.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con22.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con23.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con24.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con25.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con26.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con27.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con28.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con29.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con30.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con31.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con32.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con33.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con34.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con35.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con36.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con37.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con38.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con39.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con40.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con41.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con42.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con43.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con44.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con45.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con46.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con47.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con48.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con49.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con50.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con51.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con52.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con53.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con54.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con55.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con56.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con57.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con58.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con59.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con60.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con61.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con62.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con63.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con64.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con65.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con66.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con67.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con68.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con69.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con70.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con71.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con72.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con73.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con74.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con75.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con76.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con77.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con78.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con79.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con80.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con81.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con82.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con83.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con84.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con85.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con86.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con87.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con88.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con89.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con90.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con91.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con92.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con93.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con94.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])
        con95.add_satisfying_tuples([(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26, con27, con28, con29, con30, con31, con32, con33, con34, con35, con36, con37, con38, con39, con40, con41, con42, con43, con44, con45, con46, con47, con48, con49, con50, con51, con52, con53, con54, con55, con56, con57, con58, con59, con60, con61, con62, con63, con64, con65, con66, con67, con68, con69, con70, con71, con72, con73, con74, con75, con76, con77, con78, con79, con80, con81, con82, con83, con84, con85, con86, con87, con88, con89, con90, con91, con92, con93, con94, con95]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15]
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15
        ]

        csp = CSP("Bin_Cagey(4x4)", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

def cagey_cages_fixed(b_num):

    if b_num == 0:

        var0 = Variable("Cell11", [1, 2, 3])
        var1 = Variable("Cell12", [1, 2, 3])
        var2 = Variable("Cell13", [1, 2, 3])
        var3 = Variable("Cell21", [1, 2, 3])
        var4 = Variable("Cell22", [1, 2, 3])
        var5 = Variable("Cell23", [1, 2, 3])
        var6 = Variable("Cell31", [1, 2, 3])
        var7 = Variable("Cell32", [1, 2, 3])
        var8 = Variable("Cell33", [1, 2, 3])
        var9 = Variable("Cage_op(3:+:[Var-Cell11, Var-Cell21])", ['+', '-', '/', '*', 'f'])
        var10 = Variable("Cage_op(2:-:[Var-Cell12, Var-Cell22])", ['+', '-', '/', '*', 'f'])
        var11 = Variable("Cage_op(6:*:[Var-Cell13, Var-Cell23, Var-Cell33])", ['+', '-', '/', '*', 'f'])
        var12 = Variable("Cage_op(5:+:[Var-Cell31, Var-Cell32])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2]
        scope1 = [var3, var4, var5]
        scope2 = [var6, var7, var8]
        scope3 = [var0, var3, var6]
        scope4 = [var1, var4, var7]
        scope5 = [var2, var5, var8]
        scope6 = [var9, var0, var3]
        scope7 = [var10, var1, var4]
        scope8 = [var11, var2, var5, var8]
        scope9 = [var12, var6, var7]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Col(0)', scope3)
        con4 = Constraint('Col(1)', scope4)
        con5 = Constraint('Col(2)', scope5)
        con6 = Constraint('Cage(3:+:[Var-Cell11, Var-Cell21])', scope6)
        con7 = Constraint('Cage(2:-:[Var-Cell12, Var-Cell22])', scope7)
        con8 = Constraint('Cage(6:*:[Var-Cell13, Var-Cell23, Var-Cell33])', scope8)
        con9 = Constraint('Cage(5:+:[Var-Cell31, Var-Cell32])', scope9)

        con0.add_satisfying_tuples([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        con6.add_satisfying_tuples([('+', 1, 2), ('+', 2, 1)])
        con7.add_satisfying_tuples([('-', 1, 3), ('-', 3, 1)])
        con8.add_satisfying_tuples([('*', 1, 2, 3), ('*', 1, 3, 2), ('*', 2, 1, 3), ('*', 2, 3, 1), ('*', 3, 1, 2), ('*', 3, 2, 1)])
        con9.add_satisfying_tuples([('+', 2, 3), ('+', 3, 2)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9]

        var_array = [
            [var0, var1, var2],
            [var3, var4, var5],
            [var6, var7, var8],
            var9,
            var10,
            var11,
            var12
        ]

        vars = [
            var0, var1, var2,
            var3, var4, var5,
            var6, var7, var8,
            var9,
            var10,
            var11,
            var12
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 1:

        var0 = Variable("Cell11", [1, 2, 3, 4])
        var1 = Variable("Cell12", [1, 2, 3, 4])
        var2 = Variable("Cell13", [1, 2, 3, 4])
        var3 = Variable("Cell14", [1, 2, 3, 4])
        var4 = Variable("Cell21", [1, 2, 3, 4])
        var5 = Variable("Cell22", [1, 2, 3, 4])
        var6 = Variable("Cell23", [1, 2, 3, 4])
        var7 = Variable("Cell24", [1, 2, 3, 4])
        var8 = Variable("Cell31", [1, 2, 3, 4])
        var9 = Variable("Cell32", [1, 2, 3, 4])
        var10 = Variable("Cell33", [1, 2, 3, 4])
        var11 = Variable("Cell34", [1, 2, 3, 4])
        var12 = Variable("Cell41", [1, 2, 3, 4])
        var13 = Variable("Cell42", [1, 2, 3, 4])
        var14 = Variable("Cell43", [1, 2, 3, 4])
        var15 = Variable("Cell44", [1, 2, 3, 4])
        var16 = Variable("Cage_op(6:*:[Var-Cell11, Var-Cell21])", ['+', '-', '/', '*', 'f'])
        var17 = Variable("Cage_op(3:+:[Var-Cell12, Var-Cell13])", ['+', '-', '/', '*', 'f'])
        var18 = Variable("Cage_op(3:-:[Var-Cell14, Var-Cell24])", ['+', '-', '/', '*', 'f'])
        var19 = Variable("Cage_op(7:+:[Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f'])
        var20 = Variable("Cage_op(2:/:[Var-Cell31, Var-Cell32])", ['+', '-', '/', '*', 'f'])
        var21 = Variable("Cage_op(3:-:[Var-Cell33, Var-Cell43])", ['+', '-', '/', '*', 'f'])
        var22 = Variable("Cage_op(6:*:[Var-Cell34, Var-Cell44])", ['+', '-', '/', '*', 'f'])
        var23 = Variable("Cage_op(7:+:[Var-Cell41, Var-Cell42])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3]
        scope1 = [var4, var5, var6, var7]
        scope2 = [var8, var9, var10, var11]
        scope3 = [var12, var13, var14, var15]
        scope4 = [var0, var4, var8, var12]
        scope5 = [var1, var5, var9, var13]
        scope6 = [var2, var6, var10, var14]
        scope7 = [var3, var7, var11, var15]
        scope8 = [var16, var0, var4]
        scope9 = [var17, var1, var2]
        scope10 = [var18, var3, var7]
        scope11 = [var19, var5, var6]
        scope12 = [var20, var8, var9]
        scope13 = [var21, var10, var14]
        scope14 = [var22, var11, var15]
        scope15 = [var23, var12, var13]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Col(0)', scope4)
        con5 = Constraint('Col(1)', scope5)
        con6 = Constraint('Col(2)', scope6)
        con7 = Constraint('Col(3)', scope7)
        con8 = Constraint('Cage(6:*:[Var-Cell11, Var-Cell21])', scope8)
        con9 = Constraint('Cage(3:+:[Var-Cell12, Var-Cell13])', scope9)
        con10 = Constraint('Cage(3:-:[Var-Cell14, Var-Cell24])', scope10)
        con11 = Constraint('Cage(7:+:[Var-Cell22, Var-Cell23])', scope11)
        con12 = Constraint('Cage(2:/:[Var-Cell31, Var-Cell32])', scope12)
        con13 = Constraint('Cage(3:-:[Var-Cell33, Var-Cell43])', scope13)
        con14 = Constraint('Cage(6:*:[Var-Cell34, Var-Cell44])', scope14)
        con15 = Constraint('Cage(7:+:[Var-Cell41, Var-Cell42])', scope15)

        con0.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con8.add_satisfying_tuples([('*', 2, 3), ('*', 3, 2)])
        con9.add_satisfying_tuples([('+', 1, 2), ('+', 2, 1)])
        con10.add_satisfying_tuples([('-', 1, 4), ('-', 4, 1)])
        con11.add_satisfying_tuples([('+', 3, 4), ('+', 4, 3)])
        con12.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 4, 2)])
        con13.add_satisfying_tuples([('-', 1, 4), ('-', 4, 1)])
        con14.add_satisfying_tuples([('*', 2, 3), ('*', 3, 2)])
        con15.add_satisfying_tuples([('+', 3, 4), ('+', 4, 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15],
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22,
            var23
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15,
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22,
            var23
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 2:
        var0 = Variable("Cell11", [1, 2, 3, 4])
        var1 = Variable("Cell12", [1, 2, 3, 4])
        var2 = Variable("Cell13", [1, 2, 3, 4])
        var3 = Variable("Cell14", [1, 2, 3, 4])
        var4 = Variable("Cell21", [1, 2, 3, 4])
        var5 = Variable("Cell22", [1, 2, 3, 4])
        var6 = Variable("Cell23", [1, 2, 3, 4])
        var7 = Variable("Cell24", [1, 2, 3, 4])
        var8 = Variable("Cell31", [1, 2, 3, 4])
        var9 = Variable("Cell32", [1, 2, 3, 4])
        var10 = Variable("Cell33", [1, 2, 3, 4])
        var11 = Variable("Cell34", [1, 2, 3, 4])
        var12 = Variable("Cell41", [1, 2, 3, 4])
        var13 = Variable("Cell42", [1, 2, 3, 4])
        var14 = Variable("Cell43", [1, 2, 3, 4])
        var15 = Variable("Cell44", [1, 2, 3, 4])
        var16 = Variable("Cage_op(16:*:[Var-Cell11, Var-Cell12, Var-Cell22])", ['+', '-', '/', '*', 'f'])
        var17 = Variable("Cage_op(7:+:[Var-Cell13, Var-Cell14, Var-Cell23])", ['+', '-', '/', '*', 'f'])
        var18 = Variable("Cage_op(4:?:[Var-Cell24])", ['+', '-', '/', '*', 'f'])
        var19 = Variable("Cage_op(2:-:[Var-Cell21, Var-Cell31])", ['+', '-', '/', '*', 'f'])
        var20 = Variable("Cage_op(2:/:[Var-Cell33, Var-Cell34])", ['+', '-', '/', '*', 'f'])
        var21 = Variable("Cage_op(2:/:[Var-Cell43, Var-Cell44])", ['+', '-', '/', '*', 'f'])
        var22 = Variable("Cage_op(12:*:[Var-Cell32, Var-Cell41, Var-Cell42])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3]
        scope1 = [var4, var5, var6, var7]
        scope2 = [var8, var9, var10, var11]
        scope3 = [var12, var13, var14, var15]
        scope4 = [var0, var4, var8, var12]
        scope5 = [var1, var5, var9, var13]
        scope6 = [var2, var6, var10, var14]
        scope7 = [var3, var7, var11, var15]
        scope8 = [var16, var0, var1, var5]
        scope9 = [var17, var2, var3, var6]
        scope10 = [var18, var7]
        scope11 = [var19, var4, var8]
        scope12 = [var20, var10, var11]
        scope13 = [var21, var14, var15]
        scope14 = [var22, var9, var12, var13]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Col(0)', scope4)
        con5 = Constraint('Col(1)', scope5)
        con6 = Constraint('Col(2)', scope6)
        con7 = Constraint('Col(3)', scope7)
        con8 = Constraint('Cage(16:*:[Var-Cell11, Var-Cell12, Var-Cell22])', scope8)
        con9 = Constraint('Cage(7:+:[Var-Cell13, Var-Cell14, Var-Cell23])', scope9)
        con10 = Constraint('Cage(4:?:[Var-Cell24])', scope10)
        con11 = Constraint('Cage(2:-:[Var-Cell21, Var-Cell31])', scope11)
        con12 = Constraint('Cage(2:/:[Var-Cell33, Var-Cell34])', scope12)
        con13 = Constraint('Cage(2:/:[Var-Cell43, Var-Cell44])', scope13)
        con14 = Constraint('Cage(12:*:[Var-Cell32, Var-Cell41, Var-Cell42])', scope14)

        con0.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con8.add_satisfying_tuples([('*', 1, 4, 4), ('*', 2, 2, 4), ('*', 2, 4, 2), ('*', 4, 1, 4), ('*', 4, 2, 2), ('*', 4, 4, 1)])
        con9.add_satisfying_tuples([('+', 1, 2, 4), ('+', 1, 3, 3), ('+', 1, 4, 2), ('+', 2, 1, 4), ('+', 2, 2, 3), ('+', 2, 3, 2), ('+', 2, 4, 1), ('+', 3, 1, 3), ('+', 3, 2, 2), ('+', 3, 3, 1), ('+', 4, 1, 2), ('+', 4, 2, 1)])
        con10.add_satisfying_tuples([('f', 4)])
        con11.add_satisfying_tuples([('-', 1, 3), ('-', 2, 4), ('-', 3, 1), ('-', 4, 2)])
        con12.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 4, 2)])
        con13.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 4, 2)])
        con14.add_satisfying_tuples([('*', 1, 3, 4), ('*', 1, 4, 3), ('*', 2, 2, 3), ('*', 2, 3, 2), ('*', 3, 1, 4), ('*', 3, 2, 2), ('*', 3, 4, 1), ('*', 4, 1, 3), ('*', 4, 3, 1)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15],
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15,
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 3:

        var0 = Variable("Cell11", [1, 2, 3, 4])
        var1 = Variable("Cell12", [1, 2, 3, 4])
        var2 = Variable("Cell13", [1, 2, 3, 4])
        var3 = Variable("Cell14", [1, 2, 3, 4])
        var4 = Variable("Cell21", [1, 2, 3, 4])
        var5 = Variable("Cell22", [1, 2, 3, 4])
        var6 = Variable("Cell23", [1, 2, 3, 4])
        var7 = Variable("Cell24", [1, 2, 3, 4])
        var8 = Variable("Cell31", [1, 2, 3, 4])
        var9 = Variable("Cell32", [1, 2, 3, 4])
        var10 = Variable("Cell33", [1, 2, 3, 4])
        var11 = Variable("Cell34", [1, 2, 3, 4])
        var12 = Variable("Cell41", [1, 2, 3, 4])
        var13 = Variable("Cell42", [1, 2, 3, 4])
        var14 = Variable("Cell43", [1, 2, 3, 4])
        var15 = Variable("Cell44", [1, 2, 3, 4])
        var16 = Variable("Cage_op(4:?:[Var-Cell11])", ['+', '-', '/', '*', 'f'])
        var17 = Variable("Cage_op(2:/:[Var-Cell12, Var-Cell13])", ['+', '-', '/', '*', 'f'])
        var18 = Variable("Cage_op(1:-:[Var-Cell14, Var-Cell24])", ['+', '-', '/', '*', 'f'])
        var19 = Variable("Cage_op(6:+:[Var-Cell21, Var-Cell22, Var-Cell32])", ['+', '-', '/', '*', 'f'])
        var20 = Variable("Cage_op(12:*:[Var-Cell23, Var-Cell33, Var-Cell34])", ['+', '-', '/', '*', 'f'])
        var21 = Variable("Cage_op(1:-:[Var-Cell31, Var-Cell41])", ['+', '-', '/', '*', 'f'])
        var22 = Variable("Cage_op(5:+:[Var-Cell42, Var-Cell43])", ['+', '-', '/', '*', 'f'])
        var23 = Variable("Cage_op(2:?:[Var-Cell44])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3]
        scope1 = [var4, var5, var6, var7]
        scope2 = [var8, var9, var10, var11]
        scope3 = [var12, var13, var14, var15]
        scope4 = [var0, var4, var8, var12]
        scope5 = [var1, var5, var9, var13]
        scope6 = [var2, var6, var10, var14]
        scope7 = [var3, var7, var11, var15]
        scope8 = [var16, var0]
        scope9 = [var17, var1, var2]
        scope10 = [var18, var3, var7]
        scope11 = [var19, var4, var5, var9]
        scope12 = [var20, var6, var10, var11]
        scope13 = [var21, var8, var12]
        scope14 = [var22, var13, var14]
        scope15 = [var23, var15]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Col(0)', scope4)
        con5 = Constraint('Col(1)', scope5)
        con6 = Constraint('Col(2)', scope6)
        con7 = Constraint('Col(3)', scope7)
        con8 = Constraint('Cage(4:?:[Var-Cell11])', scope8)
        con9 = Constraint('Cage(2:/:[Var-Cell12, Var-Cell13])', scope9)
        con10 = Constraint('Cage(1:-:[Var-Cell14, Var-Cell24])', scope10)
        con11 = Constraint('Cage(6:+:[Var-Cell21, Var-Cell22, Var-Cell32])', scope11)
        con12 = Constraint('Cage(12:*:[Var-Cell23, Var-Cell33, Var-Cell34])', scope12)
        con13 = Constraint('Cage(1:-:[Var-Cell31, Var-Cell41])', scope13)
        con14 = Constraint('Cage(5:+:[Var-Cell42, Var-Cell43])', scope14)
        con15 = Constraint('Cage(2:?:[Var-Cell44])', scope15)

        con0.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con8.add_satisfying_tuples([('f', 4)])
        con9.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 4, 2)])
        con10.add_satisfying_tuples([('-', 1, 2), ('-', 2, 1), ('-', 2, 3), ('-', 3, 2), ('-', 3, 4), ('-', 4, 3)])
        con11.add_satisfying_tuples([('+', 1, 1, 4), ('+', 1, 2, 3), ('+', 1, 3, 2), ('+', 1, 4, 1), ('+', 2, 1, 3), ('+', 2, 2, 2), ('+', 2, 3, 1), ('+', 3, 1, 2), ('+', 3, 2, 1), ('+', 4, 1, 1)])
        con12.add_satisfying_tuples([('*', 1, 3, 4), ('*', 1, 4, 3), ('*', 2, 2, 3), ('*', 2, 3, 2), ('*', 3, 1, 4), ('*', 3, 2, 2), ('*', 3, 4, 1), ('*', 4, 1, 3), ('*', 4, 3, 1)])
        con13.add_satisfying_tuples([('-', 1, 2), ('-', 2, 1), ('-', 2, 3), ('-', 3, 2), ('-', 3, 4), ('-', 4, 3)])
        con14.add_satisfying_tuples([('+', 1, 4), ('+', 2, 3), ('+', 3, 2), ('+', 4, 1)])
        con15.add_satisfying_tuples([('f', 2)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15],
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22,
            var23
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15,
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22,
            var23
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 4:
        var0 = Variable("Cell11", [1, 2, 3, 4])
        var1 = Variable("Cell12", [1, 2, 3, 4])
        var2 = Variable("Cell13", [1, 2, 3, 4])
        var3 = Variable("Cell14", [1, 2, 3, 4])
        var4 = Variable("Cell21", [1, 2, 3, 4])
        var5 = Variable("Cell22", [1, 2, 3, 4])
        var6 = Variable("Cell23", [1, 2, 3, 4])
        var7 = Variable("Cell24", [1, 2, 3, 4])
        var8 = Variable("Cell31", [1, 2, 3, 4])
        var9 = Variable("Cell32", [1, 2, 3, 4])
        var10 = Variable("Cell33", [1, 2, 3, 4])
        var11 = Variable("Cell34", [1, 2, 3, 4])
        var12 = Variable("Cell41", [1, 2, 3, 4])
        var13 = Variable("Cell42", [1, 2, 3, 4])
        var14 = Variable("Cell43", [1, 2, 3, 4])
        var15 = Variable("Cell44", [1, 2, 3, 4])
        var16 = Variable("Cage_op(2:/:[Var-Cell11, Var-Cell12])", ['+', '-', '/', '*', 'f'])
        var17 = Variable("Cage_op(3:*:[Var-Cell13, Var-Cell14, Var-Cell23])", ['+', '-', '/', '*', 'f'])
        var18 = Variable("Cage_op(8:+:[Var-Cell21, Var-Cell22, Var-Cell31])", ['+', '-', '/', '*', 'f'])
        var19 = Variable("Cage_op(6:*:[Var-Cell24, Var-Cell34])", ['+', '-', '/', '*', 'f'])
        var20 = Variable("Cage_op(2:-:[Var-Cell32, Var-Cell33])", ['+', '-', '/', '*', 'f'])
        var21 = Variable("Cage_op(2:-:[Var-Cell41, Var-Cell42])", ['+', '-', '/', '*', 'f'])
        var22 = Variable("Cage_op(2:/:[Var-Cell43, Var-Cell44])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3]
        scope1 = [var4, var5, var6, var7]
        scope2 = [var8, var9, var10, var11]
        scope3 = [var12, var13, var14, var15]
        scope4 = [var0, var4, var8, var12]
        scope5 = [var1, var5, var9, var13]
        scope6 = [var2, var6, var10, var14]
        scope7 = [var3, var7, var11, var15]
        scope8 = [var16, var0, var1]
        scope9 = [var17, var2, var3, var6]
        scope10 = [var18, var4, var5, var8]
        scope11 = [var19, var7, var11]
        scope12 = [var20, var9, var10]
        scope13 = [var21, var12, var13]
        scope14 = [var22, var14, var15]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Col(0)', scope4)
        con5 = Constraint('Col(1)', scope5)
        con6 = Constraint('Col(2)', scope6)
        con7 = Constraint('Col(3)', scope7)
        con8 = Constraint('Cage(2:/:[Var-Cell11, Var-Cell12])', scope8)
        con9 = Constraint('Cage(3:*:[Var-Cell13, Var-Cell14, Var-Cell23])', scope9)
        con10 = Constraint('Cage(8:+:[Var-Cell21, Var-Cell22, Var-Cell31])', scope10)
        con11 = Constraint('Cage(6:*:[Var-Cell24, Var-Cell34])', scope11)
        con12 = Constraint('Cage(2:-:[Var-Cell32, Var-Cell33])', scope12)
        con13 = Constraint('Cage(2:-:[Var-Cell41, Var-Cell42])', scope13)
        con14 = Constraint('Cage(2:/:[Var-Cell43, Var-Cell44])', scope14)

        con0.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)])
        con8.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 4, 2)])
        con9.add_satisfying_tuples([('*', 1, 1, 3), ('*', 1, 3, 1), ('*', 3, 1, 1)])
        con10.add_satisfying_tuples([('+', 1, 3, 4), ('+', 1, 4, 3), ('+', 2, 2, 4), ('+', 2, 3, 3), ('+', 2, 4, 2), ('+', 3, 1, 4), ('+', 3, 2, 3), ('+', 3, 3, 2), ('+', 3, 4, 1), ('+', 4, 1, 3), ('+', 4, 2, 2), ('+', 4, 3, 1)])
        con11.add_satisfying_tuples([('*', 2, 3), ('*', 3, 2)])
        con12.add_satisfying_tuples([('-', 1, 3), ('-', 2, 4), ('-', 3, 1), ('-', 4, 2)])
        con13.add_satisfying_tuples([('-', 1, 3), ('-', 2, 4), ('-', 3, 1), ('-', 4, 2)])
        con14.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 4, 2)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14]

        var_array = [
            [var0, var1, var2, var3],
            [var4, var5, var6, var7],
            [var8, var9, var10, var11],
            [var12, var13, var14, var15],
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22
        ]

        vars = [
            var0, var1, var2, var3,
            var4, var5, var6, var7,
            var8, var9, var10, var11,
            var12, var13, var14, var15,
            var16,
            var17,
            var18,
            var19,
            var20,
            var21,
            var22
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 5:

        var0 = Variable("Cell11", [1, 2, 3, 4, 5])
        var1 = Variable("Cell12", [1, 2, 3, 4, 5])
        var2 = Variable("Cell13", [1, 2, 3, 4, 5])
        var3 = Variable("Cell14", [1, 2, 3, 4, 5])
        var4 = Variable("Cell15", [1, 2, 3, 4, 5])
        var5 = Variable("Cell21", [1, 2, 3, 4, 5])
        var6 = Variable("Cell22", [1, 2, 3, 4, 5])
        var7 = Variable("Cell23", [1, 2, 3, 4, 5])
        var8 = Variable("Cell24", [1, 2, 3, 4, 5])
        var9 = Variable("Cell25", [1, 2, 3, 4, 5])
        var10 = Variable("Cell31", [1, 2, 3, 4, 5])
        var11 = Variable("Cell32", [1, 2, 3, 4, 5])
        var12 = Variable("Cell33", [1, 2, 3, 4, 5])
        var13 = Variable("Cell34", [1, 2, 3, 4, 5])
        var14 = Variable("Cell35", [1, 2, 3, 4, 5])
        var15 = Variable("Cell41", [1, 2, 3, 4, 5])
        var16 = Variable("Cell42", [1, 2, 3, 4, 5])
        var17 = Variable("Cell43", [1, 2, 3, 4, 5])
        var18 = Variable("Cell44", [1, 2, 3, 4, 5])
        var19 = Variable("Cell45", [1, 2, 3, 4, 5])
        var20 = Variable("Cell51", [1, 2, 3, 4, 5])
        var21 = Variable("Cell52", [1, 2, 3, 4, 5])
        var22 = Variable("Cell53", [1, 2, 3, 4, 5])
        var23 = Variable("Cell54", [1, 2, 3, 4, 5])
        var24 = Variable("Cell55", [1, 2, 3, 4, 5])
        var25 = Variable("Cage_op(4:-:[Var-Cell11, Var-Cell21])", ['+', '-', '/', '*', 'f'])
        var26 = Variable("Cage_op(2:/:[Var-Cell12, Var-Cell13])", ['+', '-', '/', '*', 'f'])
        var27 = Variable("Cage_op(1:-:[Var-Cell14, Var-Cell24])", ['+', '-', '/', '*', 'f'])
        var28 = Variable("Cage_op(1:-:[Var-Cell15, Var-Cell25])", ['+', '-', '/', '*', 'f'])
        var29 = Variable("Cage_op(9:+:[Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f'])
        var30 = Variable("Cage_op(3:-:[Var-Cell31, Var-Cell32])", ['+', '-', '/', '*', 'f'])
        var31 = Variable("Cage_op(6:*:[Var-Cell33, Var-Cell34, Var-Cell44])", ['+', '-', '/', '*', 'f'])
        var32 = Variable("Cage_op(9:+:[Var-Cell35, Var-Cell45])", ['+', '-', '/', '*', 'f'])
        var33 = Variable("Cage_op(7:+:[Var-Cell41, Var-Cell51])", ['+', '-', '/', '*', 'f'])
        var34 = Variable("Cage_op(3:-:[Var-Cell42, Var-Cell43])", ['+', '-', '/', '*', 'f'])
        var35 = Variable("Cage_op(6:*:[Var-Cell52, Var-Cell53])", ['+', '-', '/', '*', 'f'])
        var36 = Variable("Cage_op(4:-:[Var-Cell54, Var-Cell55])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3, var4]
        scope1 = [var5, var6, var7, var8, var9]
        scope2 = [var10, var11, var12, var13, var14]
        scope3 = [var15, var16, var17, var18, var19]
        scope4 = [var20, var21, var22, var23, var24]
        scope5 = [var0, var5, var10, var15, var20]
        scope6 = [var1, var6, var11, var16, var21]
        scope7 = [var2, var7, var12, var17, var22]
        scope8 = [var3, var8, var13, var18, var23]
        scope9 = [var4, var9, var14, var19, var24]
        scope10 = [var25, var0, var5]
        scope11 = [var26, var1, var2]
        scope12 = [var27, var3, var8]
        scope13 = [var28, var4, var9]
        scope14 = [var29, var6, var7]
        scope15 = [var30, var10, var11]
        scope16 = [var31, var12, var13, var18]
        scope17 = [var32, var14, var19]
        scope18 = [var33, var15, var20]
        scope19 = [var34, var16, var17]
        scope20 = [var35, var21, var22]
        scope21 = [var36, var23, var24]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Row(4)', scope4)
        con5 = Constraint('Col(0)', scope5)
        con6 = Constraint('Col(1)', scope6)
        con7 = Constraint('Col(2)', scope7)
        con8 = Constraint('Col(3)', scope8)
        con9 = Constraint('Col(4)', scope9)
        con10 = Constraint('Cage(4:-:[Var-Cell11, Var-Cell21])', scope10)
        con11 = Constraint('Cage(2:/:[Var-Cell12, Var-Cell13])', scope11)
        con12 = Constraint('Cage(1:-:[Var-Cell14, Var-Cell24])', scope12)
        con13 = Constraint('Cage(1:-:[Var-Cell15, Var-Cell25])', scope13)
        con14 = Constraint('Cage(9:+:[Var-Cell22, Var-Cell23])', scope14)
        con15 = Constraint('Cage(3:-:[Var-Cell31, Var-Cell32])', scope15)
        con16 = Constraint('Cage(6:*:[Var-Cell33, Var-Cell34, Var-Cell44])', scope16)
        con17 = Constraint('Cage(9:+:[Var-Cell35, Var-Cell45])', scope17)
        con18 = Constraint('Cage(7:+:[Var-Cell41, Var-Cell51])', scope18)
        con19 = Constraint('Cage(3:-:[Var-Cell42, Var-Cell43])', scope19)
        con20 = Constraint('Cage(6:*:[Var-Cell52, Var-Cell53])', scope20)
        con21 = Constraint('Cage(4:-:[Var-Cell54, Var-Cell55])', scope21)

        con0.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con8.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con9.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con10.add_satisfying_tuples([('-', 1, 5), ('-', 5, 1)])
        con11.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 2, 5), ('/', 4, 2), ('/', 5, 2)])
        con12.add_satisfying_tuples([('-', 1, 2), ('-', 2, 1), ('-', 2, 3), ('-', 3, 2), ('-', 3, 4), ('-', 4, 3), ('-', 4, 5), ('-', 5, 4)])
        con13.add_satisfying_tuples([('-', 1, 2), ('-', 2, 1), ('-', 2, 3), ('-', 3, 2), ('-', 3, 4), ('-', 4, 3), ('-', 4, 5), ('-', 5, 4)])
        con14.add_satisfying_tuples([('+', 4, 5), ('+', 5, 4)])
        con15.add_satisfying_tuples([('-', 1, 4), ('-', 2, 5), ('-', 4, 1), ('-', 5, 2)])
        con16.add_satisfying_tuples([('*', 1, 2, 3), ('*', 1, 3, 2), ('*', 2, 1, 3), ('*', 2, 3, 1), ('*', 3, 1, 2), ('*', 3, 2, 1)])
        con17.add_satisfying_tuples([('+', 4, 5), ('+', 5, 4)])
        con18.add_satisfying_tuples([('+', 2, 5), ('+', 3, 4), ('+', 4, 3), ('+', 5, 2)])
        con19.add_satisfying_tuples([('-', 1, 4), ('-', 2, 5), ('-', 4, 1), ('-', 5, 2)])
        con20.add_satisfying_tuples([('*', 2, 3), ('*', 3, 2)])
        con21.add_satisfying_tuples([('-', 1, 5), ('-', 5, 1)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21]      

        var_array = [
            [var0, var1, var2, var3, var4],
            [var5, var6, var7, var8, var9],
            [var10, var11, var12, var13, var14],
            [var15, var16, var17, var18, var19],
            [var20, var21, var22, var23, var24],
            var25,
            var26,
            var27,
            var28,
            var29,
            var30,
            var31,
            var32,
            var33,
            var34,
            var35,
            var36
        ]

        vars = [
            var0, var1, var2, var3, var4,
            var5, var6, var7, var8, var9,
            var10, var11, var12, var13, var14,
            var15, var16, var17, var18, var19,
            var20, var21, var22, var23, var24,
            var25,
            var26,
            var27,
            var28,
            var29,
            var30,
            var31,
            var32,
            var33,
            var34,
            var35,
            var36
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 6:
        var0 = Variable("Cell11", [1, 2, 3, 4, 5])
        var1 = Variable("Cell12", [1, 2, 3, 4, 5])
        var2 = Variable("Cell13", [1, 2, 3, 4, 5])
        var3 = Variable("Cell14", [1, 2, 3, 4, 5])
        var4 = Variable("Cell15", [1, 2, 3, 4, 5])
        var5 = Variable("Cell21", [1, 2, 3, 4, 5])
        var6 = Variable("Cell22", [1, 2, 3, 4, 5])
        var7 = Variable("Cell23", [1, 2, 3, 4, 5])
        var8 = Variable("Cell24", [1, 2, 3, 4, 5])
        var9 = Variable("Cell25", [1, 2, 3, 4, 5])
        var10 = Variable("Cell31", [1, 2, 3, 4, 5])
        var11 = Variable("Cell32", [1, 2, 3, 4, 5])
        var12 = Variable("Cell33", [1, 2, 3, 4, 5])
        var13 = Variable("Cell34", [1, 2, 3, 4, 5])
        var14 = Variable("Cell35", [1, 2, 3, 4, 5])
        var15 = Variable("Cell41", [1, 2, 3, 4, 5])
        var16 = Variable("Cell42", [1, 2, 3, 4, 5])
        var17 = Variable("Cell43", [1, 2, 3, 4, 5])
        var18 = Variable("Cell44", [1, 2, 3, 4, 5])
        var19 = Variable("Cell45", [1, 2, 3, 4, 5])
        var20 = Variable("Cell51", [1, 2, 3, 4, 5])
        var21 = Variable("Cell52", [1, 2, 3, 4, 5])
        var22 = Variable("Cell53", [1, 2, 3, 4, 5])
        var23 = Variable("Cell54", [1, 2, 3, 4, 5])
        var24 = Variable("Cell55", [1, 2, 3, 4, 5])
        var25 = Variable("Cage_op(10:+:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])", ['+', '-', '/', '*', 'f'])
        var26 = Variable("Cage_op(18:+:[Var-Cell13, Var-Cell14, Var-Cell23, Var-Cell24, Var-Cell34])", ['+', '-', '/', '*', 'f'])
        var27 = Variable("Cage_op(2:-:[Var-Cell15, Var-Cell25, Var-Cell35])", ['+', '-', '/', '*', 'f'])
        var28 = Variable("Cage_op(1:-:[Var-Cell31, Var-Cell32, Var-Cell33])", ['+', '-', '/', '*', 'f'])
        var29 = Variable("Cage_op(600:*:[Var-Cell41, Var-Cell42, Var-Cell43, Var-Cell51, Var-Cell52, Var-Cell53])", ['+', '-', '/', '*', 'f'])
        var30 = Variable("Cage_op(2:/:[Var-Cell44, Var-Cell54, Var-Cell55])", ['+', '-', '/', '*', 'f'])
        var31 = Variable("Cage_op(3:?:[Var-Cell45])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3, var4]
        scope1 = [var5, var6, var7, var8, var9]
        scope2 = [var10, var11, var12, var13, var14]
        scope3 = [var15, var16, var17, var18, var19]
        scope4 = [var20, var21, var22, var23, var24]
        scope5 = [var0, var5, var10, var15, var20]
        scope6 = [var1, var6, var11, var16, var21]
        scope7 = [var2, var7, var12, var17, var22]
        scope8 = [var3, var8, var13, var18, var23]
        scope9 = [var4, var9, var14, var19, var24]
        scope10 = [var25, var0, var1, var5, var6]
        scope11 = [var26, var2, var3, var7, var8, var13]
        scope12 = [var27, var4, var9, var14]
        scope13 = [var28, var10, var11, var12]
        scope14 = [var29, var15, var16, var17, var20, var21, var22]
        scope15 = [var30, var18, var23, var24]
        scope16 = [var31, var19]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Row(4)', scope4)
        con5 = Constraint('Col(0)', scope5)
        con6 = Constraint('Col(1)', scope6)
        con7 = Constraint('Col(2)', scope7)
        con8 = Constraint('Col(3)', scope8)
        con9 = Constraint('Col(4)', scope9)
        con10 = Constraint('Cage(10:+:[Var-Cell11, Var-Cell12, Var-Cell21, Var-Cell22])', scope10)
        con11 = Constraint('Cage(18:+:[Var-Cell13, Var-Cell14, Var-Cell23, Var-Cell24, Var-Cell34])', scope11)
        con12 = Constraint('Cage(2:-:[Var-Cell15, Var-Cell25, Var-Cell35])', scope12)
        con13 = Constraint('Cage(1:-:[Var-Cell31, Var-Cell32, Var-Cell33])', scope13)
        con14 = Constraint('Cage(600:*:[Var-Cell41, Var-Cell42, Var-Cell43, Var-Cell51, Var-Cell52, Var-Cell53])', scope14)
        con15 = Constraint('Cage(2:/:[Var-Cell44, Var-Cell54, Var-Cell55])', scope15)
        con16 = Constraint('Cage(3:?:[Var-Cell45])', scope16)

        con0.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con8.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con9.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con10.add_satisfying_tuples([('+', 1, 1, 3, 5), ('+', 1, 1, 4, 4), ('+', 1, 1, 5, 3), ('+', 1, 2, 2, 5), ('+', 1, 2, 3, 4), ('+', 1, 2, 4, 3), ('+', 1, 2, 5, 2), ('+', 1, 3, 1, 5), ('+', 1, 3, 2, 4), ('+', 1, 3, 3, 3), ('+', 1, 3, 4, 2), ('+', 1, 3, 5, 1), ('+', 1, 4, 1, 4), ('+', 1, 4, 2, 3), ('+', 1, 4, 3, 2), ('+', 1, 4, 4, 1), ('+', 1, 5, 1, 3), ('+', 1, 5, 2, 2), ('+', 1, 5, 3, 1), ('+', 2, 1, 2, 5), ('+', 2, 1, 3, 4), ('+', 2, 1, 4, 3), ('+', 2, 1, 5, 2), ('+', 2, 2, 1, 5), ('+', 2, 2, 2, 4), ('+', 2, 2, 3, 3), ('+', 2, 2, 4, 2), ('+', 2, 2, 5, 1), ('+', 2, 3, 1, 4), ('+', 2, 3, 2, 3), ('+', 2, 3, 3, 2), ('+', 2, 3, 4, 1), ('+', 2, 4, 1, 3), ('+', 2, 4, 2, 2), ('+', 2, 4, 3, 1), ('+', 2, 5, 1, 2), ('+', 2, 5, 2, 1), ('+', 3, 1, 1, 5), ('+', 3, 1, 2, 4), ('+', 3, 1, 3, 3), ('+', 3, 1, 4, 2), ('+', 3, 1, 5, 1), ('+', 3, 2, 1, 4), ('+', 3, 2, 2, 3), ('+', 3, 2, 3, 2), ('+', 3, 2, 4, 1), ('+', 3, 3, 1, 3), ('+', 3, 3, 2, 2), ('+', 3, 3, 3, 1), ('+', 3, 4, 1, 2), ('+', 3, 4, 2, 1), ('+', 3, 5, 1, 1), ('+', 4, 1, 1, 4), ('+', 4, 1, 2, 3), ('+', 4, 1, 3, 2), ('+', 4, 1, 4, 1), ('+', 4, 2, 1, 3), ('+', 4, 2, 2, 2), ('+', 4, 2, 3, 1), ('+', 4, 3, 1, 2), ('+', 4, 3, 2, 1), ('+', 4, 4, 1, 1), ('+', 5, 1, 1, 3), ('+', 5, 1, 2, 2), ('+', 5, 1, 3, 1), ('+', 5, 2, 1, 2), ('+', 5, 2, 2, 1), ('+', 5, 3, 1, 1)])
        con11.add_satisfying_tuples([('+', 1, 2, 5, 5, 5), ('+', 1, 3, 4, 5, 5), ('+', 1, 3, 5, 4, 5), ('+', 1, 3, 5, 5, 4), ('+', 1, 4, 3, 5, 5), ('+', 1, 4, 4, 4, 5), ('+', 1, 4, 4, 5, 4), ('+', 1, 4, 5, 3, 5), ('+', 1, 4, 5, 4, 4), ('+', 1, 4, 5, 5, 3), ('+', 1, 5, 2, 5, 5), ('+', 1, 5, 3, 4, 5), ('+', 1, 5, 3, 5, 4), ('+', 1, 5, 4, 3, 5), ('+', 1, 5, 4, 4, 4), ('+', 1, 5, 4, 5, 3), ('+', 1, 5, 5, 2, 5), ('+', 1, 5, 5, 3, 4), ('+', 1, 5, 5, 4, 3), ('+', 1, 5, 5, 5, 2), ('+', 2, 1, 5, 5, 5), ('+', 2, 2, 4, 5, 5), ('+', 2, 2, 5, 4, 5), ('+', 2, 2, 5, 5, 4), ('+', 2, 3, 3, 5, 5), ('+', 2, 3, 4, 4, 5), ('+', 2, 3, 4, 5, 4), ('+', 2, 3, 5, 3, 5), ('+', 2, 3, 5, 4, 4), ('+', 2, 3, 5, 5, 3), ('+', 2, 4, 2, 5, 5), ('+', 2, 4, 3, 4, 5), ('+', 2, 4, 3, 5, 4), ('+', 2, 4, 4, 3, 5), ('+', 2, 4, 4, 4, 4), ('+', 2, 4, 4, 5, 3), ('+', 2, 4, 5, 2, 5), ('+', 2, 4, 5, 3, 4), ('+', 2, 4, 5, 4, 3), ('+', 2, 4, 5, 5, 2), ('+', 2, 5, 1, 5, 5), ('+', 2, 5, 2, 4, 5), ('+', 2, 5, 2, 5, 4), ('+', 2, 5, 3, 3, 5), ('+', 2, 5, 3, 4, 4), ('+', 2, 5, 3, 5, 3), ('+', 2, 5, 4, 2, 5), ('+', 2, 5, 4, 3, 4), ('+', 2, 5, 4, 4, 3), ('+', 2, 5, 4, 5, 2), ('+', 2, 5, 5, 1, 5), ('+', 2, 5, 5, 2, 4), ('+', 2, 5, 5, 3, 3), ('+', 2, 5, 5, 4, 2), ('+', 2, 5, 5, 5, 1), ('+', 3, 1, 4, 5, 5), ('+', 3, 1, 5, 4, 5), ('+', 3, 1, 5, 5, 4), ('+', 3, 2, 3, 5, 5), ('+', 3, 2, 4, 4, 5), ('+', 3, 2, 4, 5, 4), ('+', 3, 2, 5, 3, 5), ('+', 3, 2, 5, 4, 4), ('+', 3, 2, 5, 5, 3), ('+', 3, 3, 2, 5, 5), ('+', 3, 3, 3, 4, 5), ('+', 3, 3, 3, 5, 4), ('+', 3, 3, 4, 3, 5), ('+', 3, 3, 4, 4, 4), ('+', 3, 3, 4, 5, 3), ('+', 3, 3, 5, 2, 5), ('+', 3, 3, 5, 3, 4), ('+', 3, 3, 5, 4, 3), ('+', 3, 3, 5, 5, 2), ('+', 3, 4, 1, 5, 5), ('+', 3, 4, 2, 4, 5), ('+', 3, 4, 2, 5, 4), ('+', 3, 4, 3, 3, 5), ('+', 3, 4, 3, 4, 4), ('+', 3, 4, 3, 5, 3), ('+', 3, 4, 4, 2, 5), ('+', 3, 4, 4, 3, 4), ('+', 3, 4, 4, 4, 3), ('+', 3, 4, 4, 5, 2), ('+', 3, 4, 5, 1, 5), ('+', 3, 4, 5, 2, 4), ('+', 3, 4, 5, 3, 3), ('+', 3, 4, 5, 4, 2), ('+', 3, 4, 5, 5, 1), ('+', 3, 5, 1, 4, 5), ('+', 3, 5, 1, 5, 4), ('+', 3, 5, 2, 3, 5), ('+', 3, 5, 2, 4, 4), ('+', 3, 5, 2, 5, 3), ('+', 3, 5, 3, 2, 5), ('+', 3, 5, 3, 3, 4), ('+', 3, 5, 3, 4, 3), ('+', 3, 5, 3, 5, 2), ('+', 3, 5, 4, 1, 5), ('+', 3, 5, 4, 2, 4), ('+', 3, 5, 4, 3, 3), ('+', 3, 5, 4, 4, 2), ('+', 3, 5, 4, 5, 1), ('+', 3, 5, 5, 1, 4), ('+', 3, 5, 5, 2, 3), ('+', 3, 5, 5, 3, 2), ('+', 3, 5, 5, 4, 1), ('+', 4, 1, 3, 5, 5), ('+', 4, 1, 4, 4, 5), ('+', 4, 1, 4, 5, 4), ('+', 4, 1, 5, 3, 5), ('+', 4, 1, 5, 4, 4), ('+', 4, 1, 5, 5, 3), ('+', 4, 2, 2, 5, 5), ('+', 4, 2, 3, 4, 5), ('+', 4, 2, 3, 5, 4), ('+', 4, 2, 4, 3, 5), ('+', 4, 2, 4, 4, 4), ('+', 4, 2, 4, 5, 3), ('+', 4, 2, 5, 2, 5), ('+', 4, 2, 5, 3, 4), ('+', 4, 2, 5, 4, 3), ('+', 4, 2, 5, 5, 2), ('+', 4, 3, 1, 5, 5), ('+', 4, 3, 2, 4, 5), ('+', 4, 3, 2, 5, 4), ('+', 4, 3, 3, 3, 5), ('+', 4, 3, 3, 4, 4), ('+', 4, 3, 3, 5, 3), ('+', 4, 3, 4, 2, 5), ('+', 4, 3, 4, 3, 4), ('+', 4, 3, 4, 4, 3), ('+', 4, 3, 4, 5, 2), ('+', 4, 3, 5, 1, 5), ('+', 4, 3, 5, 2, 4), ('+', 4, 3, 5, 3, 3), ('+', 4, 3, 5, 4, 2), ('+', 4, 3, 5, 5, 1), ('+', 4, 4, 1, 4, 5), ('+', 4, 4, 1, 5, 4), ('+', 4, 4, 2, 3, 5), ('+', 4, 4, 2, 4, 4), ('+', 4, 4, 2, 5, 3), ('+', 4, 4, 3, 2, 5), ('+', 4, 4, 3, 3, 4), ('+', 4, 4, 3, 4, 3), ('+', 4, 4, 3, 5, 2), ('+', 4, 4, 4, 1, 5), ('+', 4, 4, 4, 2, 4), ('+', 4, 4, 4, 3, 3), ('+', 4, 4, 4, 4, 2), ('+', 4, 4, 4, 5, 1), ('+', 4, 4, 5, 1, 4), ('+', 4, 4, 5, 2, 3), ('+', 4, 4, 5, 3, 2), ('+', 4, 4, 5, 4, 1), ('+', 4, 5, 1, 3, 5), ('+', 4, 5, 1, 4, 4), ('+', 4, 5, 1, 5, 3), ('+', 4, 5, 2, 2, 5), ('+', 4, 5, 2, 3, 4), ('+', 4, 5, 2, 4, 3), ('+', 4, 5, 2, 5, 2), ('+', 4, 5, 3, 1, 5), ('+', 4, 5, 3, 2, 4), ('+', 4, 5, 3, 3, 3), ('+', 4, 5, 3, 4, 2), ('+', 4, 5, 3, 5, 1), ('+', 4, 5, 4, 1, 4), ('+', 4, 5, 4, 2, 3), ('+', 4, 5, 4, 3, 2), ('+', 4, 5, 4, 4, 1), ('+', 4, 5, 5, 1, 3), ('+', 4, 5, 5, 2, 2), ('+', 4, 5, 5, 3, 1), ('+', 5, 1, 2, 5, 5), ('+', 5, 1, 3, 4, 5), ('+', 5, 1, 3, 5, 4), ('+', 5, 1, 4, 3, 5), ('+', 5, 1, 4, 4, 4), ('+', 5, 1, 4, 5, 3), ('+', 5, 1, 5, 2, 5), ('+', 5, 1, 5, 3, 4), ('+', 5, 1, 5, 4, 3), ('+', 5, 1, 5, 5, 2), ('+', 5, 2, 1, 5, 5), ('+', 5, 2, 2, 4, 5), ('+', 5, 2, 2, 5, 4), ('+', 5, 2, 3, 3, 5), ('+', 5, 2, 3, 4, 4), ('+', 5, 2, 3, 5, 3), ('+', 5, 2, 4, 2, 5), ('+', 5, 2, 4, 3, 4), ('+', 5, 2, 4, 4, 3), ('+', 5, 2, 4, 5, 2), ('+', 5, 2, 5, 1, 5), ('+', 5, 2, 5, 2, 4), ('+', 5, 2, 5, 3, 3), ('+', 5, 2, 5, 4, 2), ('+', 5, 2, 5, 5, 1), ('+', 5, 3, 1, 4, 5), ('+', 5, 3, 1, 5, 4), ('+', 5, 3, 2, 3, 5), ('+', 5, 3, 2, 4, 4), ('+', 5, 3, 2, 5, 3), ('+', 5, 3, 3, 2, 5), ('+', 5, 3, 3, 3, 4), ('+', 5, 3, 3, 4, 3), ('+', 5, 3, 3, 5, 2), ('+', 5, 3, 4, 1, 5), ('+', 5, 3, 4, 2, 4), ('+', 5, 3, 4, 3, 3), ('+', 5, 3, 4, 4, 2), ('+', 5, 3, 4, 5, 1), ('+', 5, 3, 5, 1, 4), ('+', 5, 3, 5, 2, 3), ('+', 5, 3, 5, 3, 2), ('+', 5, 3, 5, 4, 1), ('+', 5, 4, 1, 3, 5), ('+', 5, 4, 1, 4, 4), ('+', 5, 4, 1, 5, 3), ('+', 5, 4, 2, 2, 5), ('+', 5, 4, 2, 3, 4), ('+', 5, 4, 2, 4, 3), ('+', 5, 4, 2, 5, 2), ('+', 5, 4, 3, 1, 5), ('+', 5, 4, 3, 2, 4), ('+', 5, 4, 3, 3, 3), ('+', 5, 4, 3, 4, 2), ('+', 5, 4, 3, 5, 1), ('+', 5, 4, 4, 1, 4), ('+', 5, 4, 4, 2, 3), ('+', 5, 4, 4, 3, 2), ('+', 5, 4, 4, 4, 1), ('+', 5, 4, 5, 1, 3), ('+', 5, 4, 5, 2, 2), ('+', 5, 4, 5, 3, 1), ('+', 5, 5, 1, 2, 5), ('+', 5, 5, 1, 3, 4), ('+', 5, 5, 1, 4, 3), ('+', 5, 5, 1, 5, 2), ('+', 5, 5, 2, 1, 5), ('+', 5, 5, 2, 2, 4), ('+', 5, 5, 2, 3, 3), ('+', 5, 5, 2, 4, 2), ('+', 5, 5, 2, 5, 1), ('+', 5, 5, 3, 1, 4), ('+', 5, 5, 3, 2, 3), ('+', 5, 5, 3, 3, 2), ('+', 5, 5, 3, 4, 1), ('+', 5, 5, 4, 1, 3), ('+', 5, 5, 4, 2, 2), ('+', 5, 5, 4, 3, 1), ('+', 5, 5, 5, 1, 2), ('+', 5, 5, 5, 2, 1)])
        con12.add_satisfying_tuples([('-', 1, 1, 4), ('-', 1, 2, 5), ('-', 1, 4, 1), ('-', 1, 5, 2), ('-', 2, 1, 5), ('-', 2, 5, 1), ('-', 4, 1, 1), ('-', 5, 1, 2), ('-', 5, 2, 1)])
        con13.add_satisfying_tuples([('-', 1, 1, 3), ('-', 1, 2, 4), ('-', 1, 3, 1), ('-', 1, 3, 5), ('-', 1, 4, 2), ('-', 1, 5, 3), ('-', 2, 1, 4), ('-', 2, 2, 5), ('-', 2, 4, 1), ('-', 2, 5, 2), ('-', 3, 1, 1), ('-', 3, 1, 5), ('-', 3, 5, 1), ('-', 4, 1, 2), ('-', 4, 2, 1), ('-', 5, 1, 3), ('-', 5, 2, 2), ('-', 5, 3, 1)])     
        con14.add_satisfying_tuples([('*', 1, 2, 3, 4, 5, 5), ('*', 1, 2, 3, 5, 4, 5), ('*', 1, 2, 3, 5, 5, 4), ('*', 1, 2, 4, 3, 5, 5), ('*', 1, 2, 4, 5, 3, 5), ('*', 1, 2, 4, 5, 5, 3), ('*', 1, 2, 5, 3, 4, 5), ('*', 1, 2, 5, 3, 5, 4), ('*', 1, 2, 5, 4, 3, 5), ('*', 1, 2, 5, 4, 5, 3), ('*', 1, 2, 5, 5, 3, 4), ('*', 1, 2, 5, 5, 4, 3), ('*', 1, 3, 2, 4, 5, 5), ('*', 1, 3, 2, 5, 4, 5), ('*', 1, 3, 2, 5, 5, 4), ('*', 1, 3, 4, 2, 5, 5), ('*', 1, 3, 4, 5, 2, 5), ('*', 1, 3, 4, 5, 5, 2), ('*', 1, 3, 5, 2, 4, 5), ('*', 1, 3, 5, 2, 5, 4), ('*', 1, 3, 5, 4, 2, 5), ('*', 1, 3, 5, 4, 5, 2), ('*', 1, 3, 5, 5, 2, 4), ('*', 1, 3, 5, 5, 4, 2), ('*', 1, 4, 2, 3, 5, 5), ('*', 1, 4, 2, 5, 3, 5), ('*', 1, 4, 2, 5, 5, 3), ('*', 1, 4, 3, 2, 5, 5), ('*', 1, 4, 3, 5, 2, 5), ('*', 1, 4, 3, 5, 5, 2), ('*', 1, 4, 5, 2, 3, 5), ('*', 1, 4, 5, 2, 5, 3), ('*', 1, 4, 5, 3, 2, 5), ('*', 1, 4, 5, 3, 5, 2), ('*', 1, 4, 5, 5, 2, 3), ('*', 1, 4, 5, 5, 3, 2), ('*', 1, 5, 2, 3, 4, 5), ('*', 1, 5, 2, 3, 5, 4), ('*', 1, 5, 2, 4, 3, 5), ('*', 1, 5, 2, 4, 5, 3), ('*', 1, 5, 2, 5, 3, 4), ('*', 1, 5, 2, 5, 4, 3), ('*', 1, 5, 3, 2, 4, 5), ('*', 1, 5, 3, 2, 5, 4), ('*', 1, 5, 3, 4, 2, 5), ('*', 1, 5, 3, 4, 5, 2), ('*', 1, 5, 3, 5, 2, 4), ('*', 1, 5, 3, 5, 4, 2), ('*', 1, 5, 4, 2, 3, 5), ('*', 1, 5, 4, 2, 5, 3), ('*', 1, 5, 4, 3, 2, 5), ('*', 1, 5, 4, 3, 5, 2), ('*', 1, 5, 4, 5, 2, 3), ('*', 1, 5, 4, 5, 3, 2), ('*', 1, 5, 5, 2, 3, 4), ('*', 1, 5, 5, 2, 4, 3), ('*', 1, 5, 5, 3, 2, 4), ('*', 1, 5, 5, 3, 4, 2), ('*', 1, 5, 5, 4, 2, 3), ('*', 1, 5, 5, 4, 3, 2), ('*', 2, 1, 3, 4, 5, 5), ('*', 2, 1, 3, 5, 4, 5), ('*', 2, 1, 3, 5, 5, 4), ('*', 2, 1, 4, 3, 5, 5), ('*', 2, 1, 4, 5, 3, 5), ('*', 2, 1, 4, 5, 5, 3), ('*', 2, 1, 5, 3, 4, 5), ('*', 2, 1, 5, 3, 5, 4), ('*', 2, 1, 5, 4, 3, 5), ('*', 2, 1, 5, 4, 5, 3), ('*', 2, 1, 5, 5, 3, 4), ('*', 2, 1, 5, 5, 4, 3), ('*', 2, 2, 2, 3, 5, 5), ('*', 2, 2, 2, 5, 3, 5), ('*', 2, 2, 2, 5, 5, 3), ('*', 2, 2, 3, 2, 5, 5), ('*', 2, 2, 3, 5, 2, 5), ('*', 2, 2, 3, 5, 5, 2), ('*', 2, 2, 5, 2, 3, 5), ('*', 2, 2, 5, 2, 5, 3), ('*', 2, 2, 5, 3, 2, 5), ('*', 2, 2, 5, 3, 5, 2), ('*', 2, 2, 5, 5, 2, 3), ('*', 2, 2, 5, 5, 3, 2), ('*', 2, 3, 1, 4, 5, 5), ('*', 2, 3, 1, 5, 4, 5), ('*', 2, 3, 1, 5, 5, 4), ('*', 2, 3, 2, 2, 5, 5), ('*', 2, 3, 2, 5, 2, 5), ('*', 2, 3, 2, 5, 5, 2), ('*', 2, 3, 4, 1, 5, 5), ('*', 2, 3, 4, 5, 1, 5), ('*', 2, 3, 4, 5, 5, 1), ('*', 2, 3, 5, 1, 4, 5), ('*', 2, 3, 5, 1, 5, 4), ('*', 2, 3, 5, 2, 2, 5), ('*', 2, 3, 5, 2, 5, 2), ('*', 2, 3, 5, 4, 1, 5), ('*', 2, 3, 5, 4, 5, 1), ('*', 2, 3, 5, 5, 1, 4), ('*', 2, 3, 5, 5, 2, 2), ('*', 2, 3, 5, 5, 4, 1), ('*', 2, 4, 1, 3, 5, 5), ('*', 2, 4, 1, 5, 3, 5), ('*', 2, 4, 1, 5, 5, 3), ('*', 2, 4, 3, 1, 5, 5), ('*', 2, 4, 3, 5, 1, 5), ('*', 2, 4, 3, 5, 5, 1), ('*', 2, 4, 5, 1, 3, 5), ('*', 2, 4, 5, 1, 5, 3), ('*', 2, 4, 5, 3, 1, 5), ('*', 2, 4, 5, 3, 5, 1), ('*', 2, 4, 5, 5, 1, 3), ('*', 2, 4, 5, 5, 3, 1), ('*', 2, 5, 1, 3, 4, 5), ('*', 2, 5, 1, 3, 5, 4), ('*', 2, 5, 1, 4, 3, 5), ('*', 2, 5, 1, 4, 5, 3), ('*', 2, 5, 1, 5, 3, 4), ('*', 2, 5, 1, 5, 4, 3), ('*', 2, 5, 2, 2, 3, 5), ('*', 2, 5, 2, 2, 5, 3), ('*', 2, 5, 2, 3, 2, 5), ('*', 2, 5, 2, 3, 5, 2), ('*', 2, 5, 2, 5, 2, 3), ('*', 2, 5, 2, 5, 3, 2), ('*', 2, 5, 3, 1, 4, 5), ('*', 2, 5, 3, 1, 5, 4), ('*', 2, 5, 3, 2, 2, 5), ('*', 2, 5, 3, 2, 5, 2), ('*', 2, 5, 3, 4, 1, 5), ('*', 2, 5, 3, 4, 5, 1), ('*', 2, 5, 3, 5, 1, 4), ('*', 2, 5, 3, 5, 2, 2), ('*', 2, 5, 3, 5, 4, 1), ('*', 2, 5, 4, 1, 3, 5), ('*', 2, 5, 4, 1, 5, 3), ('*', 2, 5, 4, 3, 1, 5), ('*', 2, 5, 4, 3, 5, 1), ('*', 2, 5, 4, 5, 1, 3), ('*', 2, 5, 4, 5, 3, 1), ('*', 2, 5, 5, 1, 3, 4), ('*', 2, 5, 5, 1, 4, 3), ('*', 2, 5, 5, 2, 2, 3), ('*', 2, 5, 5, 2, 3, 2), ('*', 2, 5, 5, 3, 1, 4), ('*', 2, 5, 5, 3, 2, 2), ('*', 2, 5, 5, 3, 4, 1), ('*', 2, 5, 5, 4, 1, 3), ('*', 2, 5, 5, 4, 3, 1), ('*', 3, 1, 2, 4, 5, 5), ('*', 3, 1, 2, 5, 4, 5), ('*', 3, 1, 2, 5, 5, 4), ('*', 3, 1, 4, 2, 5, 5), ('*', 3, 1, 4, 5, 2, 5), ('*', 3, 1, 4, 5, 5, 2), ('*', 3, 1, 5, 2, 4, 5), ('*', 3, 1, 5, 2, 5, 4), ('*', 3, 1, 5, 4, 2, 5), ('*', 3, 1, 5, 4, 5, 2), ('*', 3, 1, 5, 5, 2, 4), ('*', 3, 1, 5, 5, 4, 2), ('*', 3, 2, 1, 4, 5, 5), ('*', 3, 2, 1, 5, 4, 5), ('*', 3, 2, 1, 5, 5, 4), ('*', 3, 2, 2, 2, 5, 5), ('*', 3, 2, 2, 5, 2, 5), ('*', 3, 2, 2, 5, 5, 2), ('*', 3, 2, 4, 1, 5, 5), ('*', 3, 2, 4, 5, 1, 5), ('*', 3, 2, 4, 5, 5, 1), ('*', 3, 2, 5, 1, 4, 5), ('*', 3, 2, 5, 1, 5, 4), ('*', 3, 2, 5, 2, 2, 5), ('*', 3, 2, 5, 2, 5, 2), ('*', 3, 2, 5, 4, 1, 5), ('*', 3, 2, 5, 4, 5, 1), ('*', 3, 2, 5, 5, 1, 4), ('*', 3, 2, 5, 5, 2, 2), ('*', 3, 2, 5, 5, 4, 1), ('*', 3, 4, 1, 2, 5, 5), ('*', 3, 4, 1, 5, 2, 5), ('*', 3, 4, 1, 5, 5, 2), ('*', 3, 4, 2, 1, 5, 5), ('*', 3, 4, 2, 5, 1, 5), ('*', 3, 4, 2, 5, 5, 1), ('*', 3, 4, 5, 1, 2, 5), ('*', 3, 4, 5, 1, 5, 2), ('*', 3, 4, 5, 2, 1, 5), ('*', 3, 4, 5, 2, 5, 1), ('*', 3, 4, 5, 5, 1, 2), ('*', 3, 4, 5, 5, 2, 1), ('*', 3, 5, 1, 2, 4, 5), ('*', 3, 5, 1, 2, 5, 4), ('*', 3, 5, 1, 4, 2, 5), ('*', 3, 5, 1, 4, 5, 2), ('*', 3, 5, 1, 5, 2, 4), ('*', 3, 5, 1, 5, 4, 2), ('*', 3, 5, 2, 1, 4, 5), ('*', 3, 5, 2, 1, 5, 4), ('*', 3, 5, 2, 2, 2, 5), ('*', 3, 5, 2, 2, 5, 2), ('*', 3, 5, 2, 4, 1, 5), ('*', 3, 5, 2, 4, 5, 1), ('*', 3, 5, 2, 5, 1, 4), ('*', 3, 5, 2, 5, 2, 2), ('*', 3, 5, 2, 5, 4, 1), ('*', 3, 5, 4, 1, 2, 5), ('*', 3, 5, 4, 1, 5, 2), ('*', 3, 5, 4, 2, 1, 5), ('*', 3, 5, 4, 2, 5, 1), ('*', 3, 5, 4, 5, 1, 2), ('*', 3, 5, 4, 5, 2, 1), ('*', 3, 5, 5, 1, 2, 4), ('*', 3, 5, 5, 1, 4, 2), ('*', 3, 5, 5, 2, 1, 4), ('*', 3, 5, 5, 2, 2, 2), ('*', 3, 5, 5, 2, 4, 1), ('*', 3, 5, 5, 4, 1, 2), ('*', 3, 5, 5, 4, 2, 1), ('*', 4, 1, 2, 3, 5, 5), ('*', 4, 1, 2, 5, 3, 5), ('*', 4, 1, 2, 5, 5, 3), ('*', 4, 1, 3, 2, 5, 5), ('*', 4, 1, 3, 5, 2, 5), ('*', 4, 1, 3, 5, 5, 2), ('*', 4, 1, 5, 2, 3, 5), ('*', 4, 1, 5, 2, 5, 3), ('*', 4, 1, 5, 3, 2, 5), ('*', 4, 1, 5, 3, 5, 2), ('*', 4, 1, 5, 5, 2, 3), ('*', 4, 1, 5, 5, 3, 2), ('*', 4, 2, 1, 3, 5, 5), ('*', 4, 2, 1, 5, 3, 5), ('*', 4, 2, 1, 5, 5, 3), ('*', 4, 2, 3, 1, 5, 5), ('*', 4, 2, 3, 5, 1, 5), ('*', 4, 2, 3, 5, 5, 1), ('*', 4, 2, 5, 1, 3, 5), ('*', 4, 2, 5, 1, 5, 3), ('*', 4, 2, 5, 3, 1, 5), ('*', 4, 2, 5, 3, 5, 1), ('*', 4, 2, 5, 5, 1, 3), ('*', 4, 2, 5, 5, 3, 1), ('*', 4, 3, 1, 2, 5, 5), ('*', 4, 3, 1, 5, 2, 5), ('*', 4, 3, 1, 5, 5, 2), ('*', 4, 3, 2, 1, 5, 5), ('*', 4, 3, 2, 5, 1, 5), ('*', 4, 3, 2, 5, 5, 1), ('*', 4, 3, 5, 1, 2, 5), ('*', 4, 3, 5, 1, 5, 2), ('*', 4, 3, 5, 2, 1, 5), ('*', 4, 3, 5, 2, 5, 1), ('*', 4, 3, 5, 5, 1, 2), ('*', 4, 3, 5, 5, 2, 1), ('*', 4, 5, 1, 2, 3, 5), ('*', 4, 5, 1, 2, 5, 3), ('*', 4, 5, 1, 3, 2, 5), ('*', 4, 5, 1, 3, 5, 2), ('*', 4, 5, 1, 5, 2, 3), ('*', 4, 5, 1, 5, 3, 2), ('*', 4, 5, 2, 1, 3, 5), ('*', 4, 5, 2, 1, 5, 3), ('*', 4, 5, 2, 3, 1, 5), ('*', 4, 5, 2, 3, 5, 1), ('*', 4, 5, 2, 5, 1, 3), ('*', 4, 5, 2, 5, 3, 1), ('*', 4, 5, 3, 1, 2, 5), ('*', 4, 5, 3, 1, 5, 2), ('*', 4, 5, 3, 2, 1, 5), ('*', 4, 5, 3, 2, 5, 1), ('*', 4, 5, 3, 5, 1, 2), ('*', 4, 5, 3, 5, 2, 1), ('*', 4, 5, 5, 1, 2, 3), ('*', 4, 5, 5, 1, 3, 2), ('*', 4, 5, 5, 2, 1, 3), ('*', 4, 5, 5, 2, 3, 1), ('*', 4, 5, 5, 3, 1, 2), ('*', 4, 5, 5, 3, 2, 1), ('*', 5, 1, 2, 3, 4, 5), ('*', 5, 1, 2, 3, 5, 4), ('*', 5, 1, 2, 4, 3, 5), ('*', 5, 1, 2, 4, 5, 3), ('*', 5, 1, 2, 5, 3, 4), ('*', 5, 1, 2, 5, 4, 3), ('*', 5, 1, 3, 2, 4, 5), ('*', 5, 1, 3, 2, 5, 4), ('*', 5, 1, 3, 4, 2, 5), ('*', 5, 1, 3, 4, 5, 2), ('*', 5, 1, 3, 5, 2, 4), ('*', 5, 1, 3, 5, 4, 2), ('*', 5, 1, 4, 2, 3, 5), ('*', 5, 1, 4, 2, 5, 3), ('*', 5, 1, 4, 3, 2, 5), ('*', 5, 1, 4, 3, 5, 2), ('*', 5, 1, 4, 5, 2, 3), ('*', 5, 1, 4, 5, 3, 2), ('*', 5, 1, 5, 2, 3, 4), ('*', 5, 1, 5, 2, 4, 3), ('*', 5, 1, 5, 3, 2, 4), ('*', 5, 1, 5, 3, 4, 2), ('*', 5, 1, 5, 4, 2, 3), ('*', 5, 1, 5, 4, 3, 2), ('*', 5, 2, 1, 3, 4, 5), ('*', 5, 2, 1, 3, 5, 4), ('*', 5, 2, 1, 4, 3, 5), ('*', 5, 2, 1, 4, 5, 3), ('*', 5, 2, 1, 5, 3, 4), ('*', 5, 2, 1, 5, 4, 3), ('*', 5, 2, 2, 2, 3, 5), ('*', 5, 2, 2, 2, 5, 3), ('*', 5, 2, 2, 3, 2, 5), ('*', 5, 2, 2, 3, 5, 2), ('*', 5, 2, 2, 5, 2, 3), ('*', 5, 2, 2, 5, 3, 2), ('*', 5, 2, 3, 1, 4, 5), ('*', 5, 2, 3, 1, 5, 4), ('*', 5, 2, 3, 2, 2, 5), ('*', 5, 2, 3, 2, 5, 2), ('*', 5, 2, 3, 4, 1, 5), ('*', 5, 2, 3, 4, 5, 1), ('*', 5, 2, 3, 5, 1, 4), ('*', 5, 2, 3, 5, 2, 2), ('*', 5, 2, 3, 5, 4, 1), ('*', 5, 2, 4, 1, 3, 5), ('*', 5, 2, 4, 1, 5, 3), ('*', 5, 2, 4, 3, 1, 5), ('*', 5, 2, 4, 3, 5, 1), ('*', 5, 2, 4, 5, 1, 3), ('*', 5, 2, 4, 5, 3, 1), ('*', 5, 2, 5, 1, 3, 4), ('*', 5, 2, 5, 1, 4, 3), ('*', 5, 2, 5, 2, 2, 3), ('*', 5, 2, 5, 2, 3, 2), ('*', 5, 2, 5, 3, 1, 4), ('*', 5, 2, 5, 3, 2, 2), ('*', 5, 2, 5, 3, 4, 1), ('*', 5, 2, 5, 4, 1, 3), ('*', 5, 2, 5, 4, 3, 1), ('*', 5, 3, 1, 2, 4, 5), ('*', 5, 3, 1, 2, 5, 4), ('*', 5, 3, 1, 4, 2, 5), ('*', 5, 3, 1, 4, 5, 2), ('*', 5, 3, 1, 5, 2, 4), ('*', 5, 3, 1, 5, 4, 2), ('*', 5, 3, 2, 1, 4, 5), ('*', 5, 3, 2, 1, 5, 4), ('*', 5, 3, 2, 2, 2, 5), ('*', 5, 3, 2, 2, 5, 2), ('*', 5, 3, 2, 4, 1, 5), ('*', 5, 3, 2, 4, 5, 1), ('*', 5, 3, 2, 5, 1, 4), ('*', 5, 3, 2, 5, 2, 2), ('*', 5, 3, 2, 5, 4, 1), ('*', 5, 3, 4, 1, 2, 5), ('*', 5, 3, 4, 1, 5, 2), ('*', 5, 3, 4, 2, 1, 5), ('*', 5, 3, 4, 2, 5, 1), ('*', 5, 3, 4, 5, 1, 2), ('*', 5, 3, 4, 5, 2, 1), ('*', 5, 3, 5, 1, 2, 4), ('*', 5, 3, 5, 1, 4, 2), ('*', 5, 3, 5, 2, 1, 4), ('*', 5, 3, 5, 2, 2, 2), ('*', 5, 3, 5, 2, 4, 1), ('*', 5, 3, 5, 4, 1, 2), ('*', 5, 3, 5, 4, 2, 1), ('*', 5, 4, 1, 2, 3, 5), ('*', 5, 4, 1, 2, 5, 3), ('*', 5, 4, 1, 3, 2, 5), ('*', 5, 4, 1, 3, 5, 2), ('*', 5, 4, 1, 5, 2, 3), ('*', 5, 4, 1, 5, 3, 2), ('*', 5, 4, 2, 1, 3, 5), ('*', 5, 4, 2, 1, 5, 3), ('*', 5, 4, 2, 3, 1, 5), ('*', 5, 4, 2, 3, 5, 1), ('*', 5, 4, 2, 5, 1, 3), ('*', 5, 4, 2, 5, 3, 1), ('*', 5, 4, 3, 1, 2, 5), ('*', 5, 4, 3, 1, 5, 2), ('*', 5, 4, 3, 2, 1, 5), ('*', 5, 4, 3, 2, 5, 1), ('*', 5, 4, 3, 5, 1, 2), ('*', 5, 4, 3, 5, 2, 1), ('*', 5, 4, 5, 1, 2, 3), ('*', 5, 4, 5, 1, 3, 2), ('*', 5, 4, 5, 2, 1, 3), ('*', 5, 4, 5, 2, 3, 1), ('*', 5, 4, 5, 3, 1, 2), ('*', 5, 4, 5, 3, 2, 1), ('*', 5, 5, 1, 2, 3, 4), ('*', 5, 5, 1, 2, 4, 3), ('*', 5, 5, 1, 3, 2, 4), ('*', 5, 5, 1, 3, 4, 2), ('*', 5, 5, 1, 4, 2, 3), ('*', 5, 5, 1, 4, 3, 2), ('*', 5, 5, 2, 1, 3, 4), ('*', 5, 5, 2, 1, 4, 3), ('*', 5, 5, 2, 2, 2, 3), ('*', 5, 5, 2, 2, 3, 2), ('*', 5, 5, 2, 3, 1, 4), ('*', 5, 5, 2, 3, 2, 2), ('*', 5, 5, 2, 3, 4, 1), ('*', 5, 5, 2, 4, 1, 3), ('*', 5, 5, 2, 4, 3, 1), ('*', 5, 5, 3, 1, 2, 4), ('*', 5, 5, 3, 1, 4, 2), ('*', 5, 5, 3, 2, 1, 4), ('*', 5, 5, 3, 2, 2, 2), ('*', 5, 5, 3, 2, 4, 1), ('*', 5, 5, 3, 4, 1, 2), ('*', 5, 5, 3, 4, 2, 1), ('*', 5, 5, 4, 1, 2, 3), ('*', 5, 5, 4, 1, 3, 2), ('*', 5, 5, 4, 2, 1, 3), ('*', 5, 5, 4, 2, 3, 1), ('*', 5, 5, 4, 3, 1, 2), ('*', 5, 5, 4, 3, 2, 1)])
        con15.add_satisfying_tuples([('/', 1, 1, 2), ('/', 1, 2, 1), ('/', 1, 2, 4), ('/', 1, 2, 5), ('/', 1, 4, 2), ('/', 1, 5, 2), ('/', 2, 1, 1), ('/', 2, 1, 4), ('/', 2, 1, 5), ('/', 2, 4, 1), ('/', 2, 5, 1), ('/', 4, 1, 2), ('/', 4, 2, 1), ('/', 5, 1, 2), ('/', 5, 2, 1)])
        con16.add_satisfying_tuples([('f', 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16]

        var_array = [
            [var0, var1, var2, var3, var4],
            [var5, var6, var7, var8, var9],
            [var10, var11, var12, var13, var14],
            [var15, var16, var17, var18, var19],
            [var20, var21, var22, var23, var24],
            var25,
            var26,
            var27,
            var28,
            var29,
            var30,
            var31
        ]

        vars = [
            var0, var1, var2, var3, var4,
            var5, var6, var7, var8, var9,
            var10, var11, var12, var13, var14,
            var15, var16, var17, var18, var19,
            var20, var21, var22, var23, var24,
            var25,
            var26,
            var27,
            var28,
            var29,
            var30,
            var31
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 7:
        var0 = Variable("Cell11", [1, 2, 3, 4, 5])
        var1 = Variable("Cell12", [1, 2, 3, 4, 5])
        var2 = Variable("Cell13", [1, 2, 3, 4, 5])
        var3 = Variable("Cell14", [1, 2, 3, 4, 5])
        var4 = Variable("Cell15", [1, 2, 3, 4, 5])
        var5 = Variable("Cell21", [1, 2, 3, 4, 5])
        var6 = Variable("Cell22", [1, 2, 3, 4, 5])
        var7 = Variable("Cell23", [1, 2, 3, 4, 5])
        var8 = Variable("Cell24", [1, 2, 3, 4, 5])
        var9 = Variable("Cell25", [1, 2, 3, 4, 5])
        var10 = Variable("Easter", [1, 2, 3, 4, 5])
        var10 = Variable("Cell31", [1, 2, 3, 4, 5])
        var11 = Variable("Cell32", [1, 2, 3, 4, 5])
        var12 = Variable("Cell33", [1, 2, 3, 4, 5])
        var13 = Variable("Cell34", [1, 2, 3, 4, 5])
        var14 = Variable("Cell35", [1, 2, 3, 4, 5])
        var15 = Variable("Cell41", [1, 2, 3, 4, 5])
        var16 = Variable("Cell42", [1, 2, 3, 4, 5])
        var17 = Variable("Cell43", [1, 2, 3, 4, 5])
        var18 = Variable("Cell44", [1, 2, 3, 4, 5])
        var19 = Variable("Cell45", [1, 2, 3, 4, 5])
        var20 = Variable("Cell51", [1, 2, 3, 4, 5])
        var21 = Variable("Cell52", [1, 2, 3, 4, 5])
        var22 = Variable("Cell53", [1, 2, 3, 4, 5])
        var23 = Variable("Cell54", [1, 2, 3, 4, 5])
        var24 = Variable("Cell55", [1, 2, 3, 4, 5])
        var25 = Variable("Cage_op(2:-:[Var-Cell11, Var-Cell21])", ['+', '-', '/', '*', 'f'])
        var26 = Variable("Cage_op(2:/:[Var-Cell12, Var-Cell13])", ['+', '-', '/', '*', 'f'])
        var27 = Variable("Cage_op(1:-:[Var-Cell14, Var-Cell15])", ['+', '-', '/', '*', 'f'])
        var28 = Variable("Cage_op(1:?:[Var-Cell22])", ['+', '-', '/', '*', 'f'])
        var29 = Variable("Cage_op(2:-:[Var-Cell23, Var-Cell24])", ['+', '-', '/', '*', 'f'])
        var30 = Variable("Cage_op(9:+:[Var-Cell25, Var-Cell35, Var-Cell45])", ['+', '-', '/', '*', 'f'])
        var31 = Variable("Cage_op(6:*:[Var-Cell31, Var-Cell32])", ['+', '-', '/', '*', 'f'])
        var32 = Variable("Cage_op(4:?:[Var-Cell33])", ['+', '-', '/', '*', 'f'])
        var33 = Variable("Cage_op(3:+:[Var-Cell34, Var-Cell44])", ['+', '-', '/', '*', 'f'])
        var34 = Variable("Cage_op(3:-:[Var-Cell41, Var-Cell51])", ['+', '-', '/', '*', 'f'])
        var35 = Variable("Cage_op(15:*:[Var-Cell42, Var-Cell43])", ['+', '-', '/', '*', 'f'])
        var36 = Variable("Cage_op(9:+:[Var-Cell52, Var-Cell53])", ['+', '-', '/', '*', 'f'])
        var37 = Variable("Cage_op(1:-:[Var-Cell54, Var-Cell55])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3, var4]
        scope1 = [var5, var6, var7, var8, var9]
        scope2 = [var10, var11, var12, var13, var14]
        scope3 = [var15, var16, var17, var18, var19]
        scope4 = [var20, var21, var22, var23, var24]
        scope5 = [var0, var5, var10, var15, var20]
        scope6 = [var1, var6, var11, var16, var21]
        scope7 = [var2, var7, var12, var17, var22]
        scope8 = [var3, var8, var13, var18, var23]
        scope9 = [var4, var9, var14, var19, var24]
        scope10 = [var25, var0, var5]
        scope11 = [var26, var1, var2]
        scope12 = [var27, var3, var4]
        scope13 = [var28, var6]
        scope14 = [var29, var7, var8]
        scope15 = [var30, var9, var14, var19]
        scope16 = [var31, var10, var11]
        scope17 = [var32, var12]
        scope18 = [var33, var13, var18]
        scope19 = [var34, var15, var20]
        scope20 = [var35, var16, var17]
        scope21 = [var36, var21, var22]
        scope22 = [var37, var23, var24]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Row(4)', scope4)
        con5 = Constraint('Col(0)', scope5)
        con6 = Constraint('Col(1)', scope6)
        con7 = Constraint('Col(2)', scope7)
        con8 = Constraint('Col(3)', scope8)
        con9 = Constraint('Col(4)', scope9)
        con10 = Constraint('Cage(2:-:[Var-Cell11, Var-Cell21])', scope10)
        con11 = Constraint('Cage(2:/:[Var-Cell12, Var-Cell13])', scope11)
        con12 = Constraint('Cage(1:-:[Var-Cell14, Var-Cell15])', scope12)
        con13 = Constraint('Cage(1:?:[Var-Cell22])', scope13)
        con14 = Constraint('Cage(2:-:[Var-Cell23, Var-Cell24])', scope14)
        con15 = Constraint('Cage(9:+:[Var-Cell25, Var-Cell35, Var-Cell45])', scope15)
        con16 = Constraint('Cage(6:*:[Var-Cell31, Var-Cell32])', scope16)
        con17 = Constraint('Cage(4:?:[Var-Cell33])', scope17)
        con18 = Constraint('Cage(3:+:[Var-Cell34, Var-Cell44])', scope18)
        con19 = Constraint('Cage(3:-:[Var-Cell41, Var-Cell51])', scope19)
        con20 = Constraint('Cage(15:*:[Var-Cell42, Var-Cell43])', scope20)
        con21 = Constraint('Cage(9:+:[Var-Cell52, Var-Cell53])', scope21)
        con22 = Constraint('Cage(1:-:[Var-Cell54, Var-Cell55])', scope22)

        con0.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con8.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con9.add_satisfying_tuples([(1, 2, 3, 4, 5), (1, 2, 3, 5, 4), (1, 2, 4, 3, 5), (1, 2, 4, 5, 3), (1, 2, 5, 3, 4), (1, 2, 5, 4, 3), (1, 3, 2, 4, 5), (1, 3, 2, 5, 4), (1, 3, 4, 2, 5), (1, 3, 4, 5, 2), (1, 3, 5, 2, 4), (1, 3, 5, 4, 2), (1, 4, 2, 3, 5), (1, 4, 2, 5, 3), (1, 4, 3, 2, 5), (1, 4, 3, 5, 2), (1, 4, 5, 2, 3), (1, 4, 5, 3, 2), (1, 5, 2, 3, 4), (1, 5, 2, 4, 3), (1, 5, 3, 2, 4), (1, 5, 3, 4, 2), (1, 5, 4, 2, 3), (1, 5, 4, 3, 2), (2, 1, 3, 4, 5), (2, 1, 3, 5, 4), (2, 1, 4, 3, 5), (2, 1, 4, 5, 3), (2, 1, 5, 3, 4), (2, 1, 5, 4, 3), (2, 3, 1, 4, 5), (2, 3, 1, 5, 4), (2, 3, 4, 1, 5), (2, 3, 4, 5, 1), (2, 3, 5, 1, 4), (2, 3, 5, 4, 1), (2, 4, 1, 3, 5), (2, 4, 1, 5, 3), (2, 4, 3, 1, 5), (2, 4, 3, 5, 1), (2, 4, 5, 1, 3), (2, 4, 5, 3, 1), (2, 5, 1, 3, 4), (2, 5, 1, 4, 3), (2, 5, 3, 1, 4), (2, 5, 3, 4, 1), (2, 5, 4, 1, 3), (2, 5, 4, 3, 1), (3, 1, 2, 4, 5), (3, 1, 2, 5, 4), (3, 1, 4, 2, 5), (3, 1, 4, 5, 2), (3, 1, 5, 2, 4), (3, 1, 5, 4, 2), (3, 2, 1, 4, 5), (3, 2, 1, 5, 4), (3, 2, 4, 1, 5), (3, 2, 4, 5, 1), (3, 2, 5, 1, 4), (3, 2, 5, 4, 1), (3, 4, 1, 2, 5), (3, 4, 1, 5, 2), (3, 4, 2, 1, 5), (3, 4, 2, 5, 1), (3, 4, 5, 1, 2), (3, 4, 5, 2, 1), (3, 5, 1, 2, 4), (3, 5, 1, 4, 2), (3, 5, 2, 1, 4), (3, 5, 2, 4, 1), (3, 5, 4, 1, 2), (3, 5, 4, 2, 1), (4, 1, 2, 3, 5), (4, 1, 2, 5, 3), (4, 1, 3, 2, 5), (4, 1, 3, 5, 2), (4, 1, 5, 2, 3), (4, 1, 5, 3, 2), (4, 2, 1, 3, 5), (4, 2, 1, 5, 3), (4, 2, 3, 1, 5), (4, 2, 3, 5, 1), (4, 2, 5, 1, 3), (4, 2, 5, 3, 1), (4, 3, 1, 2, 5), (4, 3, 1, 5, 2), (4, 3, 2, 1, 5), (4, 3, 2, 5, 1), (4, 3, 5, 1, 2), (4, 3, 5, 2, 1), (4, 5, 1, 2, 3), (4, 5, 1, 3, 2), (4, 5, 2, 1, 3), (4, 5, 2, 3, 1), (4, 5, 3, 1, 2), (4, 5, 3, 2, 1), (5, 1, 2, 3, 4), (5, 1, 2, 4, 3), (5, 1, 3, 2, 4), (5, 1, 3, 4, 2), (5, 1, 4, 2, 3), (5, 1, 4, 3, 2), (5, 2, 1, 3, 4), (5, 2, 1, 4, 3), (5, 2, 3, 1, 4), (5, 2, 3, 4, 1), (5, 2, 4, 1, 3), (5, 2, 4, 3, 1), (5, 3, 1, 2, 4), (5, 3, 1, 4, 2), (5, 3, 2, 1, 4), (5, 3, 2, 4, 1), (5, 3, 4, 1, 2), (5, 3, 4, 2, 1), (5, 4, 1, 2, 3), (5, 4, 1, 3, 2), (5, 4, 2, 1, 3), (5, 4, 2, 3, 1), (5, 4, 3, 1, 2), (5, 4, 3, 2, 1)])
        con10.add_satisfying_tuples([('-', 1, 3), ('-', 2, 4), ('-', 3, 1), ('-', 3, 5), ('-', 4, 2), ('-', 5, 3)])
        con11.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 2, 5), ('/', 4, 2), ('/', 5, 2)])
        con12.add_satisfying_tuples([('-', 1, 2), ('-', 2, 1), ('-', 2, 3), ('-', 3, 2), ('-', 3, 4), ('-', 4, 3), ('-', 4, 5), ('-', 5, 4)])
        con13.add_satisfying_tuples([('f', 1)])
        con14.add_satisfying_tuples([('-', 1, 3), ('-', 2, 4), ('-', 3, 1), ('-', 3, 5), ('-', 4, 2), ('-', 5, 3)])
        con15.add_satisfying_tuples([('+', 1, 3, 5), ('+', 1, 4, 4), ('+', 1, 5, 3), ('+', 2, 2, 5), ('+', 2, 3, 4), ('+', 2, 4, 3), ('+', 2, 5, 2), ('+', 3, 1, 5), ('+', 3, 2, 4), ('+', 3, 3, 3), ('+', 3, 4, 2), ('+', 3, 5, 1), ('+', 4, 1, 4), ('+', 4, 2, 3), ('+', 4, 3, 2), ('+', 4, 4, 1), ('+', 5, 1, 3), ('+', 5, 2, 2), ('+', 5, 3, 1)])
        con16.add_satisfying_tuples([('*', 2, 3), ('*', 3, 2)])
        con17.add_satisfying_tuples([('f', 4)])
        con18.add_satisfying_tuples([('+', 1, 2), ('+', 2, 1)])
        con19.add_satisfying_tuples([('-', 1, 4), ('-', 2, 5), ('-', 4, 1), ('-', 5, 2)])
        con20.add_satisfying_tuples([('*', 3, 5), ('*', 5, 3)])
        con21.add_satisfying_tuples([('+', 4, 5), ('+', 5, 4)])
        con22.add_satisfying_tuples([('-', 1, 2), ('-', 2, 1), ('-', 2, 3), ('-', 3, 2), ('-', 3, 4), ('-', 4, 3), ('-', 4, 5), ('-', 5, 4)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22]

        var_array = [
            [var0, var1, var2, var3, var4],
            [var5, var6, var7, var8, var9],
            [var10, var11, var12, var13, var14],
            [var15, var16, var17, var18, var19],
            [var20, var21, var22, var23, var24],
            var25,
            var26,
            var27,
            var28,
            var29,
            var30,
            var31,
            var32,
            var33,
            var34,
            var35,
            var36,
            var37
        ]

        vars = [
            var0, var1, var2, var3, var4,
            var5, var6, var7, var8, var9,
            var10, var11, var12, var13, var14,
            var15, var16, var17, var18, var19,
            var20, var21, var22, var23, var24,
            var25,
            var26,
            var27,
            var28,
            var29,
            var30,
            var31,
            var32,
            var33,
            var34,
            var35,
            var36,
            var37
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 8:
        var0 = Variable("Cell11", [1, 2, 3, 4, 5, 6])
        var1 = Variable("Cell12", [1, 2, 3, 4, 5, 6])
        var2 = Variable("Cell13", [1, 2, 3, 4, 5, 6])
        var3 = Variable("Cell14", [1, 2, 3, 4, 5, 6])
        var4 = Variable("Cell15", [1, 2, 3, 4, 5, 6])
        var5 = Variable("Cell16", [1, 2, 3, 4, 5, 6])
        var6 = Variable("Cell21", [1, 2, 3, 4, 5, 6])
        var7 = Variable("Cell22", [1, 2, 3, 4, 5, 6])
        var8 = Variable("Cell23", [1, 2, 3, 4, 5, 6])
        var9 = Variable("Cell24", [1, 2, 3, 4, 5, 6])
        var10 = Variable("Cell25", [1, 2, 3, 4, 5, 6])
        var11 = Variable("Cell26", [1, 2, 3, 4, 5, 6])
        var12 = Variable("Cell31", [1, 2, 3, 4, 5, 6])
        var13 = Variable("Cell32", [1, 2, 3, 4, 5, 6])
        var14 = Variable("Cell33", [1, 2, 3, 4, 5, 6])
        var15 = Variable("Cell34", [1, 2, 3, 4, 5, 6])
        var16 = Variable("Cell35", [1, 2, 3, 4, 5, 6])
        var17 = Variable("Cell36", [1, 2, 3, 4, 5, 6])
        var18 = Variable("Cell41", [1, 2, 3, 4, 5, 6])
        var19 = Variable("Cell42", [1, 2, 3, 4, 5, 6])
        var20 = Variable("Cell43", [1, 2, 3, 4, 5, 6])
        var21 = Variable("Cell44", [1, 2, 3, 4, 5, 6])
        var22 = Variable("Cell45", [1, 2, 3, 4, 5, 6])
        var23 = Variable("Cell46", [1, 2, 3, 4, 5, 6])
        var24 = Variable("Cell51", [1, 2, 3, 4, 5, 6])
        var25 = Variable("Cell52", [1, 2, 3, 4, 5, 6])
        var26 = Variable("Cell53", [1, 2, 3, 4, 5, 6])
        var27 = Variable("Cell54", [1, 2, 3, 4, 5, 6])
        var28 = Variable("Cell55", [1, 2, 3, 4, 5, 6])
        var29 = Variable("Cell56", [1, 2, 3, 4, 5, 6])
        var30 = Variable("Cell61", [1, 2, 3, 4, 5, 6])
        var31 = Variable("Cell62", [1, 2, 3, 4, 5, 6])
        var32 = Variable("Cell63", [1, 2, 3, 4, 5, 6])
        var33 = Variable("Cell64", [1, 2, 3, 4, 5, 6])
        var34 = Variable("Cell65", [1, 2, 3, 4, 5, 6])
        var35 = Variable("Cell66", [1, 2, 3, 4, 5, 6])
        var36 = Variable("Cage_op(11:+:[Var-Cell11, Var-Cell21])", ['+', '-', '/', '*', 'f'])
        var37 = Variable("Cage_op(2:/:[Var-Cell12, Var-Cell13])", ['+', '-', '/', '*', 'f'])
        var38 = Variable("Cage_op(20:*:[Var-Cell14, Var-Cell24])", ['+', '-', '/', '*', 'f'])
        var39 = Variable("Cage_op(6:*:[Var-Cell15, Var-Cell16, Var-Cell26, Var-Cell36])", ['+', '-', '/', '*', 'f'])
        var40 = Variable("Cage_op(3:-:[Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f'])
        var41 = Variable("Cage_op(3:/:[Var-Cell25, Var-Cell35])", ['+', '-', '/', '*', 'f'])
        var42 = Variable("Cage_op(240:*:[Var-Cell31, Var-Cell32, Var-Cell41, Var-Cell42])", ['+', '-', '/', '*', 'f'])
        var43 = Variable("Cage_op(6:*:[Var-Cell33, Var-Cell34])", ['+', '-', '/', '*', 'f'])
        var44 = Variable("Cage_op(6:*:[Var-Cell43, Var-Cell53])", ['+', '-', '/', '*', 'f'])
        var45 = Variable("Cage_op(7:+:[Var-Cell44, Var-Cell54, Var-Cell55])", ['+', '-', '/', '*', 'f'])
        var46 = Variable("Cage_op(30:*:[Var-Cell45, Var-Cell46])", ['+', '-', '/', '*', 'f'])
        var47 = Variable("Cage_op(6:*:[Var-Cell51, Var-Cell52])", ['+', '-', '/', '*', 'f'])
        var48 = Variable("Cage_op(9:+:[Var-Cell56, Var-Cell66])", ['+', '-', '/', '*', 'f'])
        var49 = Variable("Cage_op(8:+:[Var-Cell61, Var-Cell62, Var-Cell63])", ['+', '-', '/', '*', 'f'])
        var50 = Variable("Cage_op(2:/:[Var-Cell64, Var-Cell65])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3, var4, var5]
        scope1 = [var6, var7, var8, var9, var10, var11]
        scope2 = [var12, var13, var14, var15, var16, var17]
        scope3 = [var18, var19, var20, var21, var22, var23]
        scope4 = [var24, var25, var26, var27, var28, var29]
        scope5 = [var30, var31, var32, var33, var34, var35]
        scope6 = [var0, var6, var12, var18, var24, var30]
        scope7 = [var1, var7, var13, var19, var25, var31]
        scope8 = [var2, var8, var14, var20, var26, var32]
        scope9 = [var3, var9, var15, var21, var27, var33]
        scope10 = [var4, var10, var16, var22, var28, var34]
        scope11 = [var5, var11, var17, var23, var29, var35]
        scope12 = [var36, var0, var6]
        scope13 = [var37, var1, var2]
        scope14 = [var38, var3, var9]
        scope15 = [var39, var4, var5, var11, var17]
        scope16 = [var40, var7, var8]
        scope17 = [var41, var10, var16]
        scope18 = [var42, var12, var13, var18, var19]
        scope19 = [var43, var14, var15]
        scope20 = [var44, var20, var26]
        scope21 = [var45, var21, var27, var28]
        scope22 = [var46, var22, var23]
        scope23 = [var47, var24, var25]
        scope24 = [var48, var29, var35]
        scope25 = [var49, var30, var31, var32]
        scope26 = [var50, var33, var34]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Row(4)', scope4)
        con5 = Constraint('Row(5)', scope5)
        con6 = Constraint('Col(0)', scope6)
        con7 = Constraint('Col(1)', scope7)
        con8 = Constraint('Col(2)', scope8)
        con9 = Constraint('Col(3)', scope9)
        con10 = Constraint('Col(4)', scope10)
        con11 = Constraint('Col(5)', scope11)
        con12 = Constraint('Cage(11:+:[Var-Cell11, Var-Cell21])', scope12)
        con13 = Constraint('Cage(2:/:[Var-Cell12, Var-Cell13])', scope13)
        con14 = Constraint('Cage(20:*:[Var-Cell14, Var-Cell24])', scope14)
        con15 = Constraint('Cage(6:*:[Var-Cell15, Var-Cell16, Var-Cell26, Var-Cell36])', scope15)
        con16 = Constraint('Cage(3:-:[Var-Cell22, Var-Cell23])', scope16)
        con17 = Constraint('Cage(3:/:[Var-Cell25, Var-Cell35])', scope17)
        con18 = Constraint('Cage(240:*:[Var-Cell31, Var-Cell32, Var-Cell41, Var-Cell42])', scope18)
        con19 = Constraint('Cage(6:*:[Var-Cell33, Var-Cell34])', scope19)
        con20 = Constraint('Cage(6:*:[Var-Cell43, Var-Cell53])', scope20)
        con21 = Constraint('Cage(7:+:[Var-Cell44, Var-Cell54, Var-Cell55])', scope21)
        con22 = Constraint('Cage(30:*:[Var-Cell45, Var-Cell46])', scope22)
        con23 = Constraint('Cage(6:*:[Var-Cell51, Var-Cell52])', scope23)
        con24 = Constraint('Cage(9:+:[Var-Cell56, Var-Cell66])', scope24)
        con25 = Constraint('Cage(8:+:[Var-Cell61, Var-Cell62, Var-Cell63])', scope25)
        con26 = Constraint('Cage(2:/:[Var-Cell64, Var-Cell65])', scope26)

        con0.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5),
 (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4),
 (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con8.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con9.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con10.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con11.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con12.add_satisfying_tuples([('+', 5, 6), ('+', 6, 5)])
        con13.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 2, 5), ('/', 3, 6), ('/', 4, 2), ('/', 5, 2), ('/', 6, 3)])
        con14.add_satisfying_tuples([('*', 4, 5), ('*', 5, 4)])
        con15.add_satisfying_tuples([('*', 1, 1, 1, 6), ('*', 1, 1, 2, 3), ('*', 1, 1, 3, 2), ('*', 1, 1, 6, 1), ('*', 1, 2, 1, 3), ('*', 1, 2, 3, 1), ('*', 1, 3, 1, 2), ('*', 1, 3, 2, 1), ('*', 1, 6, 1, 1), ('*', 2, 1, 1, 3), ('*', 2, 1, 3, 1), ('*', 2, 3, 1, 1), ('*', 3, 1, 1, 2), ('*', 3, 1, 2, 1), ('*', 3, 2, 1, 1), ('*', 6, 1, 1, 1)])
        con16.add_satisfying_tuples([('-', 1, 4), ('-', 2, 5), ('-', 3, 6), ('-', 4, 1), ('-', 5, 2), ('-', 6, 3)])
        con17.add_satisfying_tuples([('/', 1, 3), ('/', 2, 6), ('/', 3, 1), ('/', 6, 2)])
        con18.add_satisfying_tuples([('*', 2, 4, 5, 6), ('*', 2, 4, 6, 5), ('*', 2, 5, 4, 6), ('*', 2, 5, 6, 4), ('*', 2, 6, 4, 5), ('*', 2, 6, 5, 4), ('*', 3, 4, 4, 5), ('*', 3, 4, 5, 4), ('*', 3, 5, 4, 4), ('*', 4, 2, 5, 6), ('*', 4, 2, 6, 5), ('*', 4, 3, 4, 5), ('*', 4, 3, 5, 4), ('*', 4, 4, 3, 5), ('*', 4, 4, 5, 3), ('*', 4, 5, 2, 6), ('*', 4, 5, 3, 4), ('*', 4, 5, 4, 3), ('*', 4, 5, 6, 2), ('*', 4, 6, 2, 5), ('*', 4, 6, 5, 2), ('*', 5, 2, 4, 6), ('*', 5, 2, 6, 4), ('*', 5, 3, 4, 4), ('*', 5, 4, 2, 6), ('*', 5, 4, 3, 4), ('*', 5, 4, 4, 3), ('*', 5, 4, 6, 2), ('*', 5, 6, 2, 4), ('*', 5, 6, 4, 2), ('*', 6, 2, 4, 5), ('*', 6, 2, 5, 4), ('*', 6, 4, 2, 5), ('*', 6, 4, 5, 2), ('*', 6, 5, 2, 4), ('*', 6, 5, 4, 2)])
        con19.add_satisfying_tuples([('*', 1, 6), ('*', 2, 3), ('*', 3, 2), ('*', 6, 1)])
        con20.add_satisfying_tuples([('*', 1, 6), ('*', 2, 3), ('*', 3, 2), ('*', 6, 1)])
        con21.add_satisfying_tuples([('+', 1, 1, 5), ('+', 1, 2, 4), ('+', 1, 3, 3), ('+', 1, 4, 2), ('+', 1, 5, 1), ('+', 2, 1, 4), ('+', 2, 2, 3), ('+', 2, 3, 2), ('+', 2, 4, 1), ('+', 3, 1, 3), ('+', 3, 2, 2), ('+', 3, 3, 1), ('+', 4, 1, 2), ('+', 4, 2, 1), ('+', 5, 1, 1)])
        con22.add_satisfying_tuples([('*', 5, 6), ('*', 6, 5)])
        con23.add_satisfying_tuples([('*', 1, 6), ('*', 2, 3), ('*', 3, 2), ('*', 6, 1)])
        con24.add_satisfying_tuples([('+', 3, 6), ('+', 4, 5), ('+', 5, 4), ('+', 6, 3)])
        con25.add_satisfying_tuples([('+', 1, 1, 6), ('+', 1, 2, 5), ('+', 1, 3, 4), ('+', 1, 4, 3), ('+', 1, 5, 2), ('+', 1, 6, 1), ('+', 2, 1, 5), ('+', 2, 2, 4), ('+', 2, 3, 3), ('+', 2, 4, 2), ('+', 2, 5, 1), ('+', 3, 1, 4), ('+', 3, 2, 3), ('+', 3, 3, 2), ('+', 3, 4, 1), ('+', 4, 1, 3), ('+', 4, 2, 2), ('+', 4, 3, 1), ('+', 5, 1, 2), ('+', 5, 2, 1), ('+', 6, 1, 1)])
        con26.add_satisfying_tuples([('/', 1, 2), ('/', 2, 1), ('/', 2, 4), ('/', 2, 5), ('/', 3, 6), ('/', 4, 2), ('/', 5, 2), ('/', 6, 3)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22, con23, con24, con25, con26]

        var_array = [
            [var0, var1, var2, var3, var4, var5],
            [var6, var7, var8, var9, var10, var11],
            [var12, var13, var14, var15, var16, var17],
            [var18, var19, var20, var21, var22, var23],
            [var24, var25, var26, var27, var28, var29],
            [var30, var31, var32, var33, var34, var35],
            var36,
            var37,
            var38,
            var39,
            var40,
            var41,
            var42,
            var43,
            var44,
            var45,
            var46,
            var47,
            var48,
            var49,
            var50
        ]

        vars = [
            var0, var1, var2, var3, var4, var5,
            var6, var7, var8, var9, var10, var11,
            var12, var13, var14, var15, var16, var17,
            var18, var19, var20, var21, var22, var23,
            var24, var25, var26, var27, var28, var29,
            var30, var31, var32, var33, var34, var35,
            var36,
            var37,
            var38,
            var39,
            var40,
            var41,
            var42,
            var43,
            var44,
            var45,
            var46,
            var47,
            var48,
            var49,
            var50
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array

    if b_num == 9:

        var0 = Variable("Cell11", [1, 2, 3, 4, 5, 6])
        var1 = Variable("Cell12", [1, 2, 3, 4, 5, 6])
        var2 = Variable("Cell13", [1, 2, 3, 4, 5, 6])
        var3 = Variable("Cell14", [1, 2, 3, 4, 5, 6])
        var4 = Variable("Cell15", [1, 2, 3, 4, 5, 6])
        var5 = Variable("Cell16", [1, 2, 3, 4, 5, 6])
        var6 = Variable("Cell21", [1, 2, 3, 4, 5, 6])
        var7 = Variable("Cell22", [1, 2, 3, 4, 5, 6])
        var8 = Variable("Cell23", [1, 2, 3, 4, 5, 6])
        var9 = Variable("Cell24", [1, 2, 3, 4, 5, 6])
        var10 = Variable("Cell25", [1, 2, 3, 4, 5, 6])
        var11 = Variable("Cell26", [1, 2, 3, 4, 5, 6])
        var12 = Variable("Cell31", [1, 2, 3, 4, 5, 6])
        var13 = Variable("Cell32", [1, 2, 3, 4, 5, 6])
        var14 = Variable("Cell33", [1, 2, 3, 4, 5, 6])
        var15 = Variable("Cell34", [1, 2, 3, 4, 5, 6])
        var16 = Variable("Cell35", [1, 2, 3, 4, 5, 6])
        var17 = Variable("Cell36", [1, 2, 3, 4, 5, 6])
        var18 = Variable("Cell41", [1, 2, 3, 4, 5, 6])
        var19 = Variable("Cell42", [1, 2, 3, 4, 5, 6])
        var20 = Variable("Cell43", [1, 2, 3, 4, 5, 6])
        var21 = Variable("Cell44", [1, 2, 3, 4, 5, 6])
        var22 = Variable("Cell45", [1, 2, 3, 4, 5, 6])
        var23 = Variable("Cell46", [1, 2, 3, 4, 5, 6])
        var24 = Variable("Cell51", [1, 2, 3, 4, 5, 6])
        var25 = Variable("Cell52", [1, 2, 3, 4, 5, 6])
        var26 = Variable("Cell53", [1, 2, 3, 4, 5, 6])
        var27 = Variable("Cell54", [1, 2, 3, 4, 5, 6])
        var28 = Variable("Cell55", [1, 2, 3, 4, 5, 6])
        var29 = Variable("Cell56", [1, 2, 3, 4, 5, 6])
        var30 = Variable("Cell61", [1, 2, 3, 4, 5, 6])
        var31 = Variable("Cell62", [1, 2, 3, 4, 5, 6])
        var32 = Variable("Cell63", [1, 2, 3, 4, 5, 6])
        var33 = Variable("Cell64", [1, 2, 3, 4, 5, 6])
        var34 = Variable("Cell65", [1, 2, 3, 4, 5, 6])
        var35 = Variable("Cell66", [1, 2, 3, 4, 5, 6])
        var36 = Variable("Cage_op(2:/:[Var-Cell11, Var-Cell12, Var-Cell13])", ['+', '-', '/', '*', 'f'])
        var37 = Variable("Cage_op(3:-:[Var-Cell14, Var-Cell15])", ['+', '-', '/', '*', 'f'])
        var38 = Variable("Cage_op(11:+:[Var-Cell16, Var-Cell26, Var-Cell36])", ['+', '-', '/', '*', 'f'])
        var39 = Variable("Cage_op(2:/:[Var-Cell21, Var-Cell22, Var-Cell23])", ['+', '-', '/', '*', 'f'])
        var40 = Variable("Cage_op(40:*:[Var-Cell24, Var-Cell25, Var-Cell34, Var-Cell35])", ['+', '-', '/', '*', 'f'])
        var41 = Variable("Cage_op(14:+:[Var-Cell31, Var-Cell41, Var-Cell51, Var-Cell61])", ['+', '-', '/', '*', 'f'])
        var42 = Variable("Cage_op(3600:*:[Var-Cell32, Var-Cell33, Var-Cell42, Var-Cell43, Var-Cell52, Var-Cell53])", ['+', '-', '/', '*', 'f'])
        var43 = Variable("Cage_op(120:*:[Var-Cell44, Var-Cell54, Var-Cell64])", ['+', '-', '/', '*', 'f'])
        var44 = Variable("Cage_op(1:-:[Var-Cell45, Var-Cell46, Var-Cell55, Var-Cell56])", ['+', '-', '/', '*', 'f'])
        var45 = Variable("Cage_op(5:-:[Var-Cell62, Var-Cell63])", ['+', '-', '/', '*', 'f'])
        var46 = Variable("Cage_op(5:+:[Var-Cell65, Var-Cell66])", ['+', '-', '/', '*', 'f'])

        scope0 = [var0, var1, var2, var3, var4, var5]
        scope1 = [var6, var7, var8, var9, var10, var11]
        scope2 = [var12, var13, var14, var15, var16, var17]
        scope3 = [var18, var19, var20, var21, var22, var23]
        scope4 = [var24, var25, var26, var27, var28, var29]
        scope5 = [var30, var31, var32, var33, var34, var35]
        scope6 = [var0, var6, var12, var18, var24, var30]
        scope7 = [var1, var7, var13, var19, var25, var31]
        scope8 = [var2, var8, var14, var20, var26, var32]
        scope9 = [var3, var9, var15, var21, var27, var33]
        scope10 = [var4, var10, var16, var22, var28, var34]
        scope11 = [var5, var11, var17, var23, var29, var35]
        scope12 = [var36, var0, var1, var2]
        scope13 = [var37, var3, var4]
        scope14 = [var38, var5, var11, var17]
        scope15 = [var39, var6, var7, var8]
        scope16 = [var40, var9, var10, var15, var16]
        scope17 = [var41, var12, var18, var24, var30]
        scope18 = [var42, var13, var14, var19, var20, var25, var26]
        scope19 = [var43, var21, var27, var33]
        scope20 = [var44, var22, var23, var28, var29]
        scope21 = [var45, var31, var32]
        scope22 = [var46, var34, var35]

        con0 = Constraint('Row(0)', scope0)
        con1 = Constraint('Row(1)', scope1)
        con2 = Constraint('Row(2)', scope2)
        con3 = Constraint('Row(3)', scope3)
        con4 = Constraint('Row(4)', scope4)
        con5 = Constraint('Row(5)', scope5)
        con6 = Constraint('Col(0)', scope6)
        con7 = Constraint('Col(1)', scope7)
        con8 = Constraint('Col(2)', scope8)
        con9 = Constraint('Col(3)', scope9)
        con10 = Constraint('Col(4)', scope10)
        con11 = Constraint('Col(5)', scope11)
        con12 = Constraint('Cage(2:/:[Var-Cell11, Var-Cell12, Var-Cell13])', scope12)
        con13 = Constraint('Cage(3:-:[Var-Cell14, Var-Cell15])', scope13)
        con14 = Constraint('Cage(11:+:[Var-Cell16, Var-Cell26, Var-Cell36])', scope14)
        con15 = Constraint('Cage(2:/:[Var-Cell21, Var-Cell22, Var-Cell23])', scope15)
        con16 = Constraint('Cage(40:*:[Var-Cell24, Var-Cell25, Var-Cell34, Var-Cell35])', scope16)
        con17 = Constraint('Cage(14:+:[Var-Cell31, Var-Cell41, Var-Cell51, Var-Cell61])', scope17)
        con18 = Constraint('Cage(3600:*:[Var-Cell32, Var-Cell33, Var-Cell42, Var-Cell43, Var-Cell52, Var-Cell53])', scope18)
        con19 = Constraint('Cage(120:*:[Var-Cell44, Var-Cell54, Var-Cell64])', scope19)
        con20 = Constraint('Cage(1:-:[Var-Cell45, Var-Cell46, Var-Cell55, Var-Cell56])', scope20)
        con21 = Constraint('Cage(5:-:[Var-Cell62, Var-Cell63])', scope21)
        con22 = Constraint('Cage(5:+:[Var-Cell65, Var-Cell66])', scope22)

        con0.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con1.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con2.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con3.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con4.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4),
 (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con5.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con6.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con7.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con8.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3),
 (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con9.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4),
 (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con10.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con11.add_satisfying_tuples([(1, 2, 3, 4, 5, 6), (1, 2, 3, 4, 6, 5), (1, 2, 3, 5, 4, 6), (1, 2, 3, 5, 6, 4), (1, 2, 3, 6, 4, 5), (1, 2, 3, 6, 5, 4), (1, 2, 4, 3, 5, 6), (1, 2, 4, 3, 6, 5), (1, 2, 4, 5, 3, 6), (1, 2, 4, 5, 6, 3), (1, 2, 4, 6, 3, 5), (1, 2, 4, 6, 5, 3), (1, 2, 5, 3, 4, 6), (1, 2, 5, 3, 6, 4), (1, 2, 5, 4, 3, 6), (1, 2, 5, 4, 6, 3), (1, 2, 5, 6, 3, 4), (1, 2, 5, 6, 4, 3), (1, 2, 6, 3, 4, 5), (1, 2, 6, 3, 5, 4), (1, 2, 6, 4, 3, 5), (1, 2, 6, 4, 5, 3), (1, 2, 6, 5, 3, 4), (1, 2, 6, 5, 4, 3), (1, 3, 2, 4, 5, 6), (1, 3, 2, 4, 6, 5), (1, 3, 2, 5, 4, 6), (1, 3, 2, 5, 6, 4), (1, 3, 2, 6, 4, 5), (1, 3, 2, 6, 5, 4), (1, 3, 4, 2, 5, 6), (1, 3, 4, 2, 6, 5), (1, 3, 4, 5, 2, 6), (1, 3, 4, 5, 6, 2), (1, 3, 4, 6, 2, 5), (1, 3, 4, 6, 5, 2), (1, 3, 5, 2, 4, 6), (1, 3, 5, 2, 6, 4), (1, 3, 5, 4, 2, 6), (1, 3, 5, 4, 6, 2), (1, 3, 5, 6, 2, 4), (1, 3, 5, 6, 4, 2), (1, 3, 6, 2, 4, 5), (1, 3, 6, 2, 5, 4), (1, 3, 6, 4, 2, 5), (1, 3, 6, 4, 5, 2), (1, 3, 6, 5, 2, 4), (1, 3, 6, 5, 4, 2), (1, 4, 2, 3, 5, 6), (1, 4, 2, 3, 6, 5), (1, 4, 2, 5, 3, 6), (1, 4, 2, 5, 6, 3), (1, 4, 2, 6, 3, 5), (1, 4, 2, 6, 5, 3), (1, 4, 3, 2, 5, 6), (1, 4, 3, 2, 6, 5), (1, 4, 3, 5, 2, 6), (1, 4, 3, 5, 6, 2), (1, 4, 3, 6, 2, 5), (1, 4, 3, 6, 5, 2), (1, 4, 5, 2, 3, 6), (1, 4, 5, 2, 6, 3), (1, 4, 5, 3, 2, 6), (1, 4, 5, 3, 6, 2), (1, 4, 5, 6, 2, 3), (1, 4, 5, 6, 3, 2), (1, 4, 6, 2, 3, 5), (1, 4, 6, 2, 5, 3), (1, 4, 6, 3, 2, 5), (1, 4, 6, 3, 5, 2), (1, 4, 6, 5, 2, 3), (1, 4, 6, 5, 3, 2), (1, 5, 2, 3, 4, 6), (1, 5, 2, 3, 6, 4), (1, 5, 2, 4, 3, 6), (1, 5, 2, 4, 6, 3), (1, 5, 2, 6, 3, 4), (1, 5, 2, 6, 4, 3), (1, 5, 3, 2, 4, 6), (1, 5, 3, 2, 6, 4), (1, 5, 3, 4, 2, 6), (1, 5, 3, 4, 6, 2), (1, 5, 3, 6, 2, 4), (1, 5, 3, 6, 4, 2), (1, 5, 4, 2, 3, 6), (1, 5, 4, 2, 6, 3), (1, 5, 4, 3, 2, 6), (1, 5, 4, 3, 6, 2), (1, 5, 4, 6, 2, 3), (1, 5, 4, 6, 3, 2), (1, 5, 6, 2, 3, 4), (1, 5, 6, 2, 4, 3), (1, 5, 6, 3, 2, 4), (1, 5, 6, 3, 4, 2), (1, 5, 6, 4, 2, 3), (1, 5, 6, 4, 3, 2), (1, 6, 2, 3, 4, 5), (1, 6, 2, 3, 5, 4), (1, 6, 2, 4, 3, 5), (1, 6, 2, 4, 5, 3), (1, 6, 2, 5, 3, 4), (1, 6, 2, 5, 4, 3), (1, 6, 3, 2, 4, 5), (1, 6, 3, 2, 5, 4), (1, 6, 3, 4, 2, 5), (1, 6, 3, 4, 5, 2), (1, 6, 3, 5, 2, 4), (1, 6, 3, 5, 4, 2), (1, 6, 4, 2, 3, 5), (1, 6, 4, 2, 5, 3), (1, 6, 4, 3, 2, 5), (1, 6, 4, 3, 5, 2), (1, 6, 4, 5, 2, 3), (1, 6, 4, 5, 3, 2), (1, 6, 5, 2, 3, 4), (1, 6, 5, 2, 4, 3), (1, 6, 5, 3, 2, 4), (1, 6, 5, 3, 4, 2), (1, 6, 5, 4, 2, 3), (1, 6, 5, 4, 3, 2), (2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 6, 5), (2, 1, 3, 5, 4, 6), (2, 1, 3, 5, 6, 4), (2, 1, 3, 6, 4, 5), (2, 1, 3, 6, 5, 4), (2, 1, 4, 3, 5, 6), (2, 1, 4, 3, 6, 5), (2, 1, 4, 5, 3, 6), (2, 1, 4, 5, 6, 3), (2, 1, 4, 6, 3, 5), (2, 1, 4, 6, 5, 3), (2, 1, 5, 3, 4, 6), (2, 1, 5, 3, 6, 4), (2, 1, 5, 4, 3, 6), (2, 1, 5, 4, 6, 3), (2, 1, 5, 6, 3, 4), (2, 1, 5, 6, 4, 3), (2, 1, 6, 3, 4, 5), (2, 1, 6, 3, 5, 4), (2, 1, 6, 4, 3, 5), (2, 1, 6, 4, 5, 3), (2, 1, 6, 5, 3, 4), (2, 1, 6, 5, 4, 3), (2, 3, 1, 4, 5, 6), (2, 3, 1, 4, 6, 5), (2, 3, 1, 5, 4, 6), (2, 3, 1, 5, 6, 4), (2, 3, 1, 6, 4, 5), (2, 3, 1, 6, 5, 4), (2, 3, 4, 1, 5, 6), (2, 3, 4, 1, 6, 5), (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 6, 1), (2, 3, 4, 6, 1, 5), (2, 3, 4, 6, 5, 1), (2, 3, 5, 1, 4, 6), (2, 3, 5, 1, 6, 4), (2, 3, 5, 4, 1, 6), (2, 3, 5, 4, 6, 1), (2, 3, 5, 6, 1, 4), (2, 3, 5, 6, 4, 1), (2, 3, 6, 1, 4, 5), (2, 3, 6, 1, 5, 4), (2, 3, 6, 4, 1, 5), (2, 3, 6, 4, 5, 1), (2, 3, 6, 5, 1, 4), (2, 3, 6, 5, 4, 1), (2, 4, 1, 3, 5, 6), (2, 4, 1, 3, 6, 5), (2, 4, 1, 5, 3, 6), (2, 4, 1, 5, 6, 3), (2, 4, 1, 6, 3, 5), (2, 4, 1, 6, 5, 3), (2, 4, 3, 1, 5, 6), (2, 4, 3, 1, 6, 5), (2, 4, 3, 5, 1, 6), (2, 4, 3, 5, 6, 1), (2, 4, 3, 6, 1, 5), (2, 4, 3, 6, 5, 1), (2, 4, 5, 1, 3, 6), (2, 4, 5, 1, 6, 3), (2, 4, 5, 3, 1, 6), (2, 4, 5, 3, 6, 1), (2, 4, 5, 6, 1, 3), (2, 4, 5, 6, 3, 1), (2, 4, 6, 1, 3, 5), (2, 4, 6, 1, 5, 3), (2, 4, 6, 3, 1, 5), (2, 4, 6, 3, 5, 1), (2, 4, 6, 5, 1, 3), (2, 4, 6, 5, 3, 1), (2, 5, 1, 3, 4, 6), (2, 5, 1, 3, 6, 4), (2, 5, 1, 4, 3, 6), (2, 5, 1, 4, 6, 3), (2, 5, 1, 6, 3, 4), (2, 5, 1, 6, 4, 3), (2, 5, 3, 1, 4, 6), (2, 5, 3, 1, 6, 4), (2, 5, 3, 4, 1, 6), (2, 5, 3, 4, 6, 1), (2, 5, 3, 6, 1, 4), (2, 5, 3, 6, 4, 1), (2, 5, 4, 1, 3, 6), (2, 5, 4, 1, 6, 3), (2, 5, 4, 3, 1, 6), (2, 5, 4, 3, 6, 1), (2, 5, 4, 6, 1, 3), (2, 5, 4, 6, 3, 1), (2, 5, 6, 1, 3, 4), (2, 5, 6, 1, 4, 3), (2, 5, 6, 3, 1, 4), (2, 5, 6, 3, 4, 1), (2, 5, 6, 4, 1, 3), (2, 5, 6, 4, 3, 1), (2, 6, 1, 3, 4, 5), (2, 6, 1, 3, 5, 4), (2, 6, 1, 4, 3, 5), (2, 6, 1, 4, 5, 3), (2, 6, 1, 5, 3, 4), (2, 6, 1, 5, 4, 3), (2, 6, 3, 1, 4, 5), (2, 6, 3, 1, 5, 4), (2, 6, 3, 4, 1, 5), (2, 6, 3, 4, 5, 1), (2, 6, 3, 5, 1, 4), (2, 6, 3, 5, 4, 1), (2, 6, 4, 1, 3, 5), (2, 6, 4, 1, 5, 3), (2, 6, 4, 3, 1, 5), (2, 6, 4, 3, 5, 1), (2, 6, 4, 5, 1, 3), (2, 6, 4, 5, 3, 1), (2, 6, 5, 1, 3, 4), (2, 6, 5, 1, 4, 3), (2, 6, 5, 3, 1, 4), (2, 6, 5, 3, 4, 1), (2, 6, 5, 4, 1, 3), (2, 6, 5, 4, 3, 1), (3, 1, 2, 4, 5, 6), (3, 1, 2, 4, 6, 5), (3, 1, 2, 5, 4, 6), (3, 1, 2, 5, 6, 4), (3, 1, 2, 6, 4, 5), (3, 1, 2, 6, 5, 4), (3, 1, 4, 2, 5, 6), (3, 1, 4, 2, 6, 5), (3, 1, 4, 5, 2, 6), (3, 1, 4, 5, 6, 2), (3, 1, 4, 6, 2, 5), (3, 1, 4, 6, 5, 2), (3, 1, 5, 2, 4, 6), (3, 1, 5, 2, 6, 4), (3, 1, 5, 4, 2, 6), (3, 1, 5, 4, 6, 2), (3, 1, 5, 6, 2, 4), (3, 1, 5, 6, 4, 2), (3, 1, 6, 2, 4, 5), (3, 1, 6, 2, 5, 4), (3, 1, 6, 4, 2, 5), (3, 1, 6, 4, 5, 2), (3, 1, 6, 5, 2, 4), (3, 1, 6, 5, 4, 2), (3, 2, 1, 4, 5, 6), (3, 2, 1, 4, 6, 5), (3, 2, 1, 5, 4, 6), (3, 2, 1, 5, 6, 4), (3, 2, 1, 6, 4, 5), (3, 2, 1, 6, 5, 4), (3, 2, 4, 1, 5, 6), (3, 2, 4, 1, 6, 5), (3, 2, 4, 5, 1, 6), (3, 2, 4, 5, 6, 1), (3, 2, 4, 6, 1, 5), (3, 2, 4, 6, 5, 1), (3, 2, 5, 1, 4, 6), (3, 2, 5, 1, 6, 4), (3, 2, 5, 4, 1, 6), (3, 2, 5, 4, 6, 1), (3, 2, 5, 6, 1, 4), (3, 2, 5, 6, 4, 1), (3, 2, 6, 1, 4, 5), (3, 2, 6, 1, 5, 4), (3, 2, 6, 4, 1, 5), (3, 2, 6, 4, 5, 1), (3, 2, 6, 5, 1, 4), (3, 2, 6, 5, 4, 1), (3, 4, 1, 2, 5, 6), (3, 4, 1, 2, 6, 5), (3, 4, 1, 5, 2, 6), (3, 4, 1, 5, 6, 2), (3, 4, 1, 6, 2, 5), (3, 4, 1, 6, 5, 2), (3, 4, 2, 1, 5, 6), (3, 4, 2, 1, 6, 5), (3, 4, 2, 5, 1, 6), (3, 4, 2, 5, 6, 1), (3, 4, 2, 6, 1, 5), (3, 4, 2, 6, 5, 1), (3, 4, 5, 1, 2, 6), (3, 4, 5, 1, 6, 2), (3, 4, 5, 2, 1, 6), (3, 4, 5, 2, 6, 1), (3, 4, 5, 6, 1, 2), (3, 4, 5, 6, 2, 1), (3, 4, 6, 1, 2, 5), (3, 4, 6, 1, 5, 2), (3, 4, 6, 2, 1, 5), (3, 4, 6, 2, 5, 1), (3, 4, 6, 5, 1, 2), (3, 4, 6, 5, 2, 1), (3, 5, 1, 2, 4, 6), (3, 5, 1, 2, 6, 4), (3, 5, 1, 4, 2, 6), (3, 5, 1, 4, 6, 2), (3, 5, 1, 6, 2, 4), (3, 5, 1, 6, 4, 2), (3, 5, 2, 1, 4, 6), (3, 5, 2, 1, 6, 4), (3, 5, 2, 4, 1, 6), (3, 5, 2, 4, 6, 1), (3, 5, 2, 6, 1, 4), (3, 5, 2, 6, 4, 1), (3, 5, 4, 1, 2, 6), (3, 5, 4, 1, 6, 2), (3, 5, 4, 2, 1, 6), (3, 5, 4, 2, 6, 1), (3, 5, 4, 6, 1, 2), (3, 5, 4, 6, 2, 1), (3, 5, 6, 1, 2, 4), (3, 5, 6, 1, 4, 2), (3, 5, 6, 2, 1, 4), (3, 5, 6, 2, 4, 1), (3, 5, 6, 4, 1, 2), (3, 5, 6, 4, 2, 1), (3, 6, 1, 2, 4, 5), (3, 6, 1, 2, 5, 4), (3, 6, 1, 4, 2, 5), (3, 6, 1, 4, 5, 2), (3, 6, 1, 5, 2, 4), (3, 6, 1, 5, 4, 2), (3, 6, 2, 1, 4, 5), (3, 6, 2, 1, 5, 4), (3, 6, 2, 4, 1, 5), (3, 6, 2, 4, 5, 1), (3, 6, 2, 5, 1, 4), (3, 6, 2, 5, 4, 1), (3, 6, 4, 1, 2, 5), (3, 6, 4, 1, 5, 2), (3, 6, 4, 2, 1, 5), (3, 6, 4, 2, 5, 1), (3, 6, 4, 5, 1, 2), (3, 6, 4, 5, 2, 1), (3, 6, 5, 1, 2, 4), (3, 6, 5, 1, 4, 2), (3, 6, 5, 2, 1, 4), (3, 6, 5, 2, 4, 1), (3, 6, 5, 4, 1, 2), (3, 6, 5, 4, 2, 1), (4, 1, 2, 3, 5, 6), (4, 1, 2, 3, 6, 5), (4, 1, 2, 5, 3, 6), (4, 1, 2, 5, 6, 3), (4, 1, 2, 6, 3, 5), (4, 1, 2, 6, 5, 3), (4, 1, 3, 2, 5, 6), (4, 1, 3, 2, 6, 5), (4, 1, 3, 5, 2, 6), (4, 1, 3, 5, 6, 2), (4, 1, 3, 6, 2, 5), (4, 1, 3, 6, 5, 2), (4, 1, 5, 2, 3, 6), (4, 1, 5, 2, 6, 3), (4, 1, 5, 3, 2, 6), (4, 1, 5, 3, 6, 2), (4, 1, 5, 6, 2, 3), (4, 1, 5, 6, 3, 2), (4, 1, 6, 2, 3, 5), (4, 1, 6, 2, 5, 3), (4, 1, 6, 3, 2, 5), (4, 1, 6, 3, 5, 2), (4, 1, 6, 5, 2, 3), (4, 1, 6, 5, 3, 2), (4, 2, 1, 3, 5, 6), (4, 2, 1, 3, 6, 5), (4, 2, 1, 5, 3, 6), (4, 2, 1, 5, 6, 3), (4, 2, 1, 6, 3, 5), (4, 2, 1, 6, 5, 3), (4, 2, 3, 1, 5, 6), (4, 2, 3, 1, 6, 5), (4, 2, 3, 5, 1, 6), (4, 2, 3, 5, 6, 1), (4, 2, 3, 6, 1, 5), (4, 2, 3, 6, 5, 1), (4, 2, 5, 1, 3, 6), (4, 2, 5, 1, 6, 3), (4, 2, 5, 3, 1, 6), (4, 2, 5, 3, 6, 1), (4, 2, 5, 6, 1, 3), (4, 2, 5, 6, 3, 1), (4, 2, 6, 1, 3, 5), (4, 2, 6, 1, 5, 3), (4, 2, 6, 3, 1, 5), (4, 2, 6, 3, 5, 1), (4, 2, 6, 5, 1, 3), (4, 2, 6, 5, 3, 1), (4, 3, 1, 2, 5, 6), (4, 3, 1, 2, 6, 5), (4, 3, 1, 5, 2, 6), (4, 3, 1, 5, 6, 2), (4, 3, 1, 6, 2, 5), (4, 3, 1, 6, 5, 2), (4, 3, 2, 1, 5, 6), (4, 3, 2, 1, 6, 5), (4, 3, 2, 5, 1, 6), (4, 3, 2, 5, 6, 1), (4, 3, 2, 6, 1, 5), (4, 3, 2, 6, 5, 1), (4, 3, 5, 1, 2, 6), (4, 3, 5, 1, 6, 2), (4, 3, 5, 2, 1, 6), (4, 3, 5, 2, 6, 1), (4, 3, 5, 6, 1, 2), (4, 3, 5, 6, 2, 1), (4, 3, 6, 1, 2, 5), (4, 3, 6, 1, 5, 2), (4, 3, 6, 2, 1, 5), (4, 3, 6, 2, 5, 1), (4, 3, 6, 5, 1, 2), (4, 3, 6, 5, 2, 1), (4, 5, 1, 2, 3, 6), (4, 5, 1, 2, 6, 3), (4, 5, 1, 3, 2, 6), (4, 5, 1, 3, 6, 2), (4, 5, 1, 6, 2, 3), (4, 5, 1, 6, 3, 2), (4, 5, 2, 1, 3, 6), (4, 5, 2, 1, 6, 3), (4, 5, 2, 3, 1, 6), (4, 5, 2, 3, 6, 1), (4, 5, 2, 6, 1, 3), (4, 5, 2, 6, 3, 1), (4, 5, 3, 1, 2, 6), (4, 5, 3, 1, 6, 2), (4, 5, 3, 2, 1, 6), (4, 5, 3, 2, 6, 1), (4, 5, 3, 6, 1, 2), (4, 5, 3, 6, 2, 1), (4, 5, 6, 1, 2, 3), (4, 5, 6, 1, 3, 2), (4, 5, 6, 2, 1, 3), (4, 5, 6, 2, 3, 1), (4, 5, 6, 3, 1, 2), (4, 5, 6, 3, 2, 1), (4, 6, 1, 2, 3, 5), (4, 6, 1, 2, 5, 3), (4, 6, 1, 3, 2, 5), (4, 6, 1, 3, 5, 2), (4, 6, 1, 5, 2, 3), (4, 6, 1, 5, 3, 2), (4, 6, 2, 1, 3, 5), (4, 6, 2, 1, 5, 3), (4, 6, 2, 3, 1, 5), (4, 6, 2, 3, 5, 1), (4, 6, 2, 5, 1, 3), (4, 6, 2, 5, 3, 1), (4, 6, 3, 1, 2, 5), (4, 6, 3, 1, 5, 2), (4, 6, 3, 2, 1, 5), (4, 6, 3, 2, 5, 1), (4, 6, 3, 5, 1, 2), (4, 6, 3, 5, 2, 1), (4, 6, 5, 1, 2, 3), (4, 6, 5, 1, 3, 2), (4, 6, 5, 2, 1, 3), (4, 6, 5, 2, 3, 1), (4, 6, 5, 3, 1, 2), (4, 6, 5, 3, 2, 1), (5, 1, 2, 3, 4, 6), (5, 1, 2, 3, 6, 4), (5, 1, 2, 4, 3, 6), (5, 1, 2, 4, 6, 3), (5, 1, 2, 6, 3, 4), (5, 1, 2, 6, 4, 3), (5, 1, 3, 2, 4, 6), (5, 1, 3, 2, 6, 4), (5, 1, 3, 4, 2, 6), (5, 1, 3, 4, 6, 2), (5, 1, 3, 6, 2, 4), (5, 1, 3, 6, 4, 2), (5, 1, 4, 2, 3, 6), (5, 1, 4, 2, 6, 3), (5, 1, 4, 3, 2, 6), (5, 1, 4, 3, 6, 2), (5, 1, 4, 6, 2, 3), (5, 1, 4, 6, 3, 2), (5, 1, 6, 2, 3, 4), (5, 1, 6, 2, 4, 3), (5, 1, 6, 3, 2, 4), (5, 1, 6, 3, 4, 2), (5, 1, 6, 4, 2, 3), (5, 1, 6, 4, 3, 2), (5, 2, 1, 3, 4, 6), (5, 2, 1, 3, 6, 4), (5, 2, 1, 4, 3, 6), (5, 2, 1, 4, 6, 3), (5, 2, 1, 6, 3, 4), (5, 2, 1, 6, 4, 3), (5, 2, 3, 1, 4, 6), (5, 2, 3, 1, 6, 4), (5, 2, 3, 4, 1, 6), (5, 2, 3, 4, 6, 1), (5, 2, 3, 6, 1, 4), (5, 2, 3, 6, 4, 1), (5, 2, 4, 1, 3, 6), (5, 2, 4, 1, 6, 3), (5, 2, 4, 3, 1, 6), (5, 2, 4, 3, 6, 1), (5, 2, 4, 6, 1, 3), (5, 2, 4, 6, 3, 1), (5, 2, 6, 1, 3, 4), (5, 2, 6, 1, 4, 3), (5, 2, 6, 3, 1, 4), (5, 2, 6, 3, 4, 1), (5, 2, 6, 4, 1, 3), (5, 2, 6, 4, 3, 1), (5, 3, 1, 2, 4, 6), (5, 3, 1, 2, 6, 4), (5, 3, 1, 4, 2, 6), (5, 3, 1, 4, 6, 2), (5, 3, 1, 6, 2, 4), (5, 3, 1, 6, 4, 2), (5, 3, 2, 1, 4, 6), (5, 3, 2, 1, 6, 4), (5, 3, 2, 4, 1, 6), (5, 3, 2, 4, 6, 1), (5, 3, 2, 6, 1, 4), (5, 3, 2, 6, 4, 1), (5, 3, 4, 1, 2, 6), (5, 3, 4, 1, 6, 2), (5, 3, 4, 2, 1, 6), (5, 3, 4, 2, 6, 1), (5, 3, 4, 6, 1, 2), (5, 3, 4, 6, 2, 1), (5, 3, 6, 1, 2, 4), (5, 3, 6, 1, 4, 2), (5, 3, 6, 2, 1, 4), (5, 3, 6, 2, 4, 1), (5, 3, 6, 4, 1, 2), (5, 3, 6, 4, 2, 1), (5, 4, 1, 2, 3, 6), (5, 4, 1, 2, 6, 3), (5, 4, 1, 3, 2, 6), (5, 4, 1, 3, 6, 2), (5, 4, 1, 6, 2, 3), (5, 4, 1, 6, 3, 2), (5, 4, 2, 1, 3, 6), (5, 4, 2, 1, 6, 3), (5, 4, 2, 3, 1, 6), (5, 4, 2, 3, 6, 1), (5, 4, 2, 6, 1, 3), (5, 4, 2, 6, 3, 1), (5, 4, 3, 1, 2, 6), (5, 4, 3, 1, 6, 2), (5, 4, 3, 2, 1, 6), (5, 4, 3, 2, 6, 1), (5, 4, 3, 6, 1, 2), (5, 4, 3, 6, 2, 1), (5, 4, 6, 1, 2, 3), (5, 4, 6, 1, 3, 2), (5, 4, 6, 2, 1, 3), (5, 4, 6, 2, 3, 1), (5, 4, 6, 3, 1, 2), (5, 4, 6, 3, 2, 1), (5, 6, 1, 2, 3, 4), (5, 6, 1, 2, 4, 3), (5, 6, 1, 3, 2, 4), (5, 6, 1, 3, 4, 2), (5, 6, 1, 4, 2, 3), (5, 6, 1, 4, 3, 2), (5, 6, 2, 1, 3, 4), (5, 6, 2, 1, 4, 3), (5, 6, 2, 3, 1, 4), (5, 6, 2, 3, 4, 1), (5, 6, 2, 4, 1, 3), (5, 6, 2, 4, 3, 1), (5, 6, 3, 1, 2, 4), (5, 6, 3, 1, 4, 2), (5, 6, 3, 2, 1, 4), (5, 6, 3, 2, 4, 1), (5, 6, 3, 4, 1, 2), (5, 6, 3, 4, 2, 1), (5, 6, 4, 1, 2, 3), (5, 6, 4, 1, 3, 2), (5, 6, 4, 2, 1, 3), (5, 6, 4, 2, 3, 1), (5, 6, 4, 3, 1, 2), (5, 6, 4, 3, 2, 1), (6, 1, 2, 3, 4, 5), (6, 1, 2, 3, 5, 4), (6, 1, 2, 4, 3, 5), (6, 1, 2, 4, 5, 3), (6, 1, 2, 5, 3, 4), (6, 1, 2, 5, 4, 3), (6, 1, 3, 2, 4, 5), (6, 1, 3, 2, 5, 4), (6, 1, 3, 4, 2, 5), (6, 1, 3, 4, 5, 2), (6, 1, 3, 5, 2, 4), (6, 1, 3, 5, 4, 2), (6, 1, 4, 2, 3, 5), (6, 1, 4, 2, 5, 3), (6, 1, 4, 3, 2, 5), (6, 1, 4, 3, 5, 2), (6, 1, 4, 5, 2, 3), (6, 1, 4, 5, 3, 2), (6, 1, 5, 2, 3, 4), (6, 1, 5, 2, 4, 3), (6, 1, 5, 3, 2, 4), (6, 1, 5, 3, 4, 2), (6, 1, 5, 4, 2, 3), (6, 1, 5, 4, 3, 2), (6, 2, 1, 3, 4, 5), (6, 2, 1, 3, 5, 4), (6, 2, 1, 4, 3, 5), (6, 2, 1, 4, 5, 3), (6, 2, 1, 5, 3, 4), (6, 2, 1, 5, 4, 3), (6, 2, 3, 1, 4, 5), (6, 2, 3, 1, 5, 4), (6, 2, 3, 4, 1, 5), (6, 2, 3, 4, 5, 1), (6, 2, 3, 5, 1, 4), (6, 2, 3, 5, 4, 1), (6, 2, 4, 1, 3, 5), (6, 2, 4, 1, 5, 3), (6, 2, 4, 3, 1, 5), (6, 2, 4, 3, 5, 1), (6, 2, 4, 5, 1, 3), (6, 2, 4, 5, 3, 1), (6, 2, 5, 1, 3, 4), (6, 2, 5, 1, 4, 3), (6, 2, 5, 3, 1, 4), (6, 2, 5, 3, 4, 1), (6, 2, 5, 4, 1, 3), (6, 2, 5, 4, 3, 1), (6, 3, 1, 2, 4, 5), (6, 3, 1, 2, 5, 4), (6, 3, 1, 4, 2, 5), (6, 3, 1, 4, 5, 2), (6, 3, 1, 5, 2, 4), (6, 3, 1, 5, 4, 2), (6, 3, 2, 1, 4, 5), (6, 3, 2, 1, 5, 4), (6, 3, 2, 4, 1, 5), (6, 3, 2, 4, 5, 1), (6, 3, 2, 5, 1, 4), (6, 3, 2, 5, 4, 1), (6, 3, 4, 1, 2, 5), (6, 3, 4, 1, 5, 2), (6, 3, 4, 2, 1, 5), (6, 3, 4, 2, 5, 1), (6, 3, 4, 5, 1, 2), (6, 3, 4, 5, 2, 1), (6, 3, 5, 1, 2, 4), (6, 3, 5, 1, 4, 2), (6, 3, 5, 2, 1, 4), (6, 3, 5, 2, 4, 1), (6, 3, 5, 4, 1, 2), (6, 3, 5, 4, 2, 1), (6, 4, 1, 2, 3, 5), (6, 4, 1, 2, 5, 3), (6, 4, 1, 3, 2, 5), (6, 4, 1, 3, 5, 2), (6, 4, 1, 5, 2, 3), (6, 4, 1, 5, 3, 2), (6, 4, 2, 1, 3, 5), (6, 4, 2, 1, 5, 3), (6, 4, 2, 3, 1, 5), (6, 4, 2, 3, 5, 1), (6, 4, 2, 5, 1, 3), (6, 4, 2, 5, 3, 1), (6, 4, 3, 1, 2, 5), (6, 4, 3, 1, 5, 2), (6, 4, 3, 2, 1, 5), (6, 4, 3, 2, 5, 1), (6, 4, 3, 5, 1, 2), (6, 4, 3, 5, 2, 1), (6, 4, 5, 1, 2, 3), (6, 4, 5, 1, 3, 2), (6, 4, 5, 2, 1, 3), (6, 4, 5, 2, 3, 1), (6, 4, 5, 3, 1, 2), (6, 4, 5, 3, 2, 1), (6, 5, 1, 2, 3, 4), (6, 5, 1, 2, 4, 3), (6, 5, 1, 3, 2, 4), (6, 5, 1, 3, 4, 2), (6, 5, 1, 4, 2, 3), (6, 5, 1, 4, 3, 2), (6, 5, 2, 1, 3, 4), (6, 5, 2, 1, 4, 3), (6, 5, 2, 3, 1, 4), (6, 5, 2, 3, 4, 1), (6, 5, 2, 4, 1, 3), (6, 5, 2, 4, 3, 1), (6, 5, 3, 1, 2, 4), (6, 5, 3, 1, 4, 2), (6, 5, 3, 2, 1, 4), (6, 5, 3, 2, 4, 1), (6, 5, 3, 4, 1, 2), (6, 5, 3, 4, 2, 1), (6, 5, 4, 1, 2, 3), (6, 5, 4, 1, 3, 2), (6, 5, 4, 2, 1, 3), (6, 5, 4, 2, 3, 1), (6, 5, 4, 3, 1, 2), (6, 5, 4, 3, 2, 1)])
        con12.add_satisfying_tuples([('/', 1, 1, 2), ('/', 1, 2, 1), ('/', 1, 2, 4), ('/', 1, 2, 5), ('/', 1, 3, 6), ('/', 1, 4, 2), ('/', 1, 5, 2), ('/', 1, 6, 3), ('/', 2, 1, 1), ('/', 2, 1, 4), ('/', 2, 1, 5), ('/', 2, 4, 1), ('/', 2, 5, 1), ('/', 3, 1, 6), ('/', 3, 6, 1), ('/', 4, 1, 2), ('/', 4, 2, 1), ('/', 5, 1, 2), ('/', 5, 2, 1), ('/', 6, 1, 3), ('/', 6, 3, 1)])
        con13.add_satisfying_tuples([('-', 1, 4), ('-', 2, 5), ('-', 3, 6), ('-', 4, 1), ('-', 5, 2), ('-', 6, 3)])
        con14.add_satisfying_tuples([('+', 1, 4, 6), ('+', 1, 5, 5), ('+', 1, 6, 4), ('+', 2, 3, 6), ('+', 2, 4, 5), ('+', 2, 5, 4), ('+', 2, 6, 3), ('+', 3, 2, 6), ('+', 3, 3, 5), ('+', 3, 4, 4), ('+', 3, 5, 3), ('+', 3, 6, 2), ('+', 4, 1, 6), ('+', 4, 2, 5), ('+', 4, 3, 4), ('+', 4, 4, 3), ('+', 4, 5, 2), ('+', 4, 6, 1), ('+', 5, 1, 5), ('+', 5, 2, 4), ('+', 5, 3, 3), ('+', 5, 4, 2), ('+', 5, 5, 1), ('+', 6, 1, 4), ('+', 6, 2, 3), ('+', 6, 3, 2), ('+', 6, 4, 1)])
        con15.add_satisfying_tuples([('/', 1, 1, 2), ('/', 1, 2, 1), ('/', 1, 2, 4), ('/', 1, 2, 5), ('/', 1, 3, 6), ('/', 1, 4, 2), ('/', 1, 5, 2), ('/', 1, 6, 3), ('/', 2, 1, 1), ('/', 2, 1, 4), ('/', 2, 1, 5), ('/', 2, 4, 1), ('/', 2, 5, 1), ('/', 3, 1, 6), ('/', 3, 6, 1), ('/', 4, 1, 2), ('/', 4, 2, 1), ('/', 5, 1, 2), ('/', 5, 2, 1), ('/', 6, 1, 3), ('/', 6, 3, 1)])
        con16.add_satisfying_tuples([('*', 1, 2, 4, 5), ('*', 1, 2, 5, 4), ('*', 1, 4, 2, 5), ('*', 1, 4, 5, 2), ('*', 1, 5, 2, 4), ('*', 1, 5, 4, 2), ('*', 2, 1, 4, 5), ('*', 2, 1, 5, 4), ('*', 2, 2, 2, 5), ('*', 2, 2, 5, 2), ('*', 2, 4, 1, 5), ('*', 2, 4, 5, 1), ('*', 2, 5, 1, 4), ('*', 2, 5, 2, 2), ('*', 2, 5, 4, 1), ('*', 4, 1, 2, 5), ('*', 4, 1, 5, 2), ('*', 4, 2, 1, 5), ('*', 4, 2, 5, 1), ('*', 4, 5, 1, 2), ('*', 4, 5, 2, 1), ('*', 5, 1, 2, 4), ('*', 5, 1, 4, 2), ('*', 5, 2, 1, 4), ('*', 5, 2, 2, 2), ('*', 5, 2, 4, 1), ('*', 5, 4, 1, 2), ('*', 5, 4, 2, 1)])
        con17.add_satisfying_tuples([('+', 1, 1, 6, 6), ('+', 1, 2, 5, 6), ('+', 1, 2, 6, 5), ('+', 1, 3, 4, 6), ('+', 1, 3, 5, 5), ('+', 1, 3, 6, 4), ('+', 1, 4, 3, 6), ('+', 1, 4, 4, 5), ('+', 1, 4, 5, 4), ('+', 1, 4, 6, 3), ('+', 1, 5, 2, 6), ('+', 1, 5, 3, 5), ('+', 1, 5, 4, 4), ('+', 1, 5, 5, 3), ('+', 1, 5, 6, 2), ('+', 1, 6, 1, 6), ('+', 1, 6, 2, 5), ('+', 1, 6, 3, 4), ('+', 1, 6, 4, 3), ('+', 1, 6, 5, 2), ('+', 1, 6, 6, 1), ('+', 2, 1, 5, 6), ('+', 2, 1, 6, 5), ('+', 2, 2, 4, 6), ('+', 2, 2, 5, 5), ('+', 2, 2, 6, 4), ('+', 2, 3, 3, 6), ('+', 2, 3, 4, 5), ('+', 2, 3, 5, 4), ('+', 2, 3, 6, 3), ('+', 2, 4, 2, 6), ('+', 2, 4, 3, 5), ('+', 2, 4, 4, 4), ('+', 2, 4, 5, 3), ('+', 2, 4, 6, 2), ('+', 2, 5, 1, 6), ('+', 2, 5, 2, 5), ('+', 2, 5, 3, 4), ('+', 2, 5, 4, 3), ('+', 2, 5, 5, 2), ('+', 2, 5, 6, 1), ('+', 2, 6, 1, 5), ('+', 2, 6, 2, 4), ('+', 2, 6, 3, 3), ('+', 2, 6, 4, 2), ('+', 2, 6, 5, 1), ('+', 3, 1, 4, 6), ('+', 3, 1, 5, 5), ('+', 3, 1, 6, 4), ('+', 3, 2, 3, 6), ('+', 3, 2, 4, 5), ('+', 3, 2, 5, 4), ('+', 3, 2, 6, 3), ('+', 3, 3, 2, 6), ('+', 3, 3, 3, 5), ('+', 3, 3, 4, 4), ('+', 3, 3, 5, 3), ('+', 3, 3, 6, 2), ('+', 3, 4, 1, 6), ('+', 3, 4, 2, 5), ('+', 3, 4, 3, 4), ('+', 3, 4, 4, 3), ('+', 3, 4, 5, 2), ('+', 3, 4, 6, 1), ('+', 3, 5, 1, 5), ('+', 3, 5, 2, 4), ('+', 3, 5, 3, 3), ('+', 3, 5, 4, 2), ('+', 3, 5, 5, 1), ('+', 3, 6, 1, 4), ('+', 3, 6, 2, 3), ('+', 3, 6, 3, 2), ('+', 3, 6, 4, 1), ('+', 4, 1, 3, 6), ('+', 4, 1, 4, 5), ('+', 4, 1, 5, 4), ('+', 4, 1, 6, 3), ('+', 4, 2, 2, 6), ('+', 4, 2, 3, 5), ('+', 4, 2, 4, 4), ('+', 4, 2, 5, 3), ('+', 4, 2, 6, 2), ('+', 4, 3, 1, 6), ('+', 4, 3, 2, 5), ('+', 4, 3, 3, 4), ('+', 4, 3, 4, 3), ('+', 4, 3, 5, 2), ('+', 4, 3, 6, 1), ('+', 4, 4, 1, 5), ('+', 4, 4, 2, 4), ('+', 4, 4, 3, 3), ('+', 4, 4, 4, 2), ('+', 4, 4, 5, 1), ('+', 4, 5, 1, 4), ('+', 4, 5, 2, 3), ('+', 4, 5, 3, 2), ('+', 4, 5, 4, 1), ('+', 4, 6, 1, 3), ('+', 4, 6, 2, 2), ('+', 4, 6, 3, 1), ('+', 5, 1, 2, 6), ('+', 5, 1, 3, 5), ('+', 5, 1, 4, 4), ('+', 5, 1, 5, 3), ('+', 5, 1, 6, 2), ('+', 5, 2, 1, 6), ('+', 5, 2, 2, 5), ('+', 5, 2, 3, 4), ('+', 5, 2, 4, 3), ('+', 5, 2, 5, 2), ('+', 5, 2, 6, 1), ('+', 5, 3, 1, 5), ('+', 5, 3, 2, 4), ('+', 5, 3, 3, 3), ('+', 5, 3, 4, 2), ('+', 5, 3, 5, 1), ('+', 5, 4, 1, 4), ('+', 5, 4, 2, 3), ('+', 5, 4, 3, 2), ('+', 5, 4, 4, 1), ('+', 5, 5, 1, 3), ('+', 5, 5, 2, 2), ('+', 5, 5, 3, 1), ('+', 5, 6, 1, 2), ('+', 5, 6, 2, 1), ('+', 6, 1, 1, 6), ('+', 6, 1, 2, 5), ('+', 6, 1, 3, 4), ('+', 6, 1, 4, 3), ('+', 6, 1, 5, 2), ('+', 6, 1, 6, 1), ('+', 6, 2, 1, 5), ('+', 6, 2, 2, 4), ('+', 6, 2, 3, 3), ('+', 6, 2, 4, 2), ('+', 6, 2, 5, 1), ('+', 6, 3, 1, 4), ('+', 6, 3, 2, 3), ('+', 6, 3, 3, 2), ('+', 6, 3, 4, 1), ('+', 6, 4, 1, 3), ('+', 6, 4, 2, 2), ('+', 6, 4, 3, 1), ('+', 6, 5, 1, 2), ('+', 6, 5, 2, 1), ('+', 6, 6, 1, 1)])
        con18.add_satisfying_tuples([('*', 1, 4, 5, 5, 6, 6), ('*', 1, 4, 5, 6, 5, 6), ('*', 1, 4, 5, 6, 6, 5), ('*', 1, 4, 6, 5, 5, 6), ('*', 1, 4, 6, 5, 6, 5), ('*', 1, 4, 6, 6, 5, 5), ('*', 1, 5, 4, 5, 6, 6), ('*', 1, 5, 4, 6, 5, 6), ('*', 1, 5, 4, 6, 6, 5), ('*', 1, 5, 5, 4, 6, 6), ('*', 1, 5, 5, 6, 4, 6), ('*', 1, 5, 5, 6, 6, 4), ('*', 1, 5, 6, 4, 5, 6), ('*', 1, 5, 6, 4, 6, 5), ('*', 1, 5, 6, 5, 4, 6), ('*', 1, 5, 6, 5, 6, 4), ('*', 1, 5, 6, 6, 4, 5), ('*', 1, 5, 6, 6, 5, 4), ('*', 1, 6, 4, 5, 5, 6), ('*', 1, 6, 4, 5, 6, 5), ('*', 1, 6, 4, 6, 5, 5), ('*', 1, 6, 5, 4, 5, 6), ('*', 1, 6, 5, 4, 6, 5), ('*', 1, 6, 5, 5, 4, 6), ('*', 1, 6, 5, 5, 6, 4), ('*', 1, 6, 5, 6, 4, 5), ('*', 1, 6, 5, 6, 5, 4), ('*', 1, 6, 6, 4, 5, 5), ('*', 1, 6, 6, 5, 4, 5), ('*', 1, 6, 6, 5, 5, 4), ('*', 2, 2, 5, 5, 6, 6), ('*', 2, 2, 5, 6, 5, 6), ('*', 2, 2, 5, 6, 6, 5), ('*', 2, 2, 6, 5, 5, 6), ('*', 2, 2, 6, 5, 6, 5), ('*', 2, 2, 6, 6, 5, 5), ('*', 2, 3, 4, 5, 5, 6), ('*', 2, 3, 4, 5, 6, 5), ('*', 2, 3, 4, 6, 5, 5), ('*', 2, 3, 5, 4, 5, 6), ('*', 2, 3, 5, 4, 6, 5), ('*', 2, 3, 5, 5, 4, 6), ('*', 2, 3, 5, 5, 6, 4), ('*', 2, 3, 5, 6, 4, 5), ('*', 2, 3, 5, 6, 5, 4), ('*', 2, 3, 6, 4, 5, 5), ('*', 2, 3, 6, 5, 4, 5), ('*', 2, 3, 6, 5, 5, 4), ('*', 2, 4, 3, 5, 5, 6), ('*', 2, 4, 3, 5, 6, 5), ('*', 2, 4, 3, 6, 5, 5), ('*', 2, 4, 5, 3, 5, 6), ('*', 2, 4, 5, 3, 6, 5), ('*', 2, 4, 5, 5, 3, 6), ('*', 2, 4, 5, 5, 6, 3), ('*', 2, 4, 5, 6, 3, 5), ('*', 2, 4, 5, 6, 5, 3), ('*', 2, 4, 6, 3, 5, 5), ('*', 2, 4, 6, 5, 3, 5), ('*', 2, 4, 6, 5, 5, 3), ('*', 2, 5, 2, 5, 6, 6), ('*', 2, 5, 2, 6, 5, 6), ('*', 2, 5, 2, 6, 6, 5), ('*', 2, 5, 3, 4, 5, 6), ('*', 2, 5, 3, 4, 6, 5), ('*', 2, 5, 3, 5, 4, 6), ('*', 2, 5, 3, 5, 6, 4), ('*', 2, 5, 3, 6, 4, 5), ('*', 2, 5, 3, 6, 5, 4), ('*', 2, 5, 4, 3, 5, 6), ('*', 2, 5, 4, 3, 6, 5), ('*', 2, 5, 4, 5, 3, 6), ('*', 2, 5, 4, 5, 6, 3), ('*', 2, 5, 4, 6, 3, 5), ('*', 2, 5, 4, 6, 5, 3), ('*', 2, 5, 5, 2, 6, 6), ('*', 2, 5, 5, 3, 4, 6), ('*', 2, 5, 5, 3, 6, 4), ('*', 2, 5, 5, 4, 3, 6), ('*', 2, 5, 5, 4, 6, 3), ('*', 2, 5, 5, 6, 2, 6), ('*', 2, 5, 5, 6, 3, 4), ('*', 2, 5, 5, 6, 4, 3), ('*', 2, 5, 5, 6, 6, 2), ('*', 2, 5, 6, 2, 5, 6), ('*', 2, 5, 6, 2, 6, 5), ('*', 2, 5, 6, 3, 4, 5), ('*', 2, 5, 6, 3, 5, 4), ('*', 2, 5, 6, 4, 3, 5), ('*', 2, 5, 6, 4, 5, 3), ('*', 2, 5, 6, 5, 2, 6), ('*', 2, 5, 6, 5, 3, 4), ('*', 2, 5, 6, 5, 4, 3), ('*', 2, 5, 6, 5, 6, 2), ('*', 2, 5, 6, 6, 2, 5), ('*', 2, 5, 6, 6, 5, 2), ('*', 2, 6, 2, 5, 5, 6), ('*', 2, 6, 2, 5, 6, 5), ('*', 2, 6, 2, 6, 5, 5), ('*', 2, 6, 3, 4, 5, 5), ('*', 2, 6, 3, 5, 4, 5), ('*', 2, 6, 3, 5, 5, 4), ('*', 2, 6, 4, 3, 5, 5), ('*', 2, 6, 4, 5, 3, 5), ('*', 2, 6, 4, 5, 5, 3), ('*', 2, 6, 5, 2, 5, 6), ('*', 2, 6, 5, 2, 6, 5), ('*', 2, 6, 5, 3, 4, 5), ('*', 2, 6, 5, 3, 5, 4), ('*', 2, 6, 5, 4, 3, 5), ('*', 2, 6, 5, 4, 5, 3), ('*', 2, 6, 5, 5, 2, 6), ('*', 2, 6, 5, 5, 3, 4), ('*', 2, 6, 5, 5, 4, 3), ('*', 2, 6, 5, 5, 6, 2), ('*', 2, 6, 5, 6, 2, 5), ('*', 2, 6, 5, 6, 5, 2), ('*', 2, 6, 6, 2, 5, 5), ('*', 2, 6, 6, 5, 2, 5), ('*', 2, 6, 6, 5, 5, 2), ('*', 3, 2, 4, 5, 5, 6), ('*', 3, 2, 4, 5, 6, 5), ('*', 3, 2, 4, 6, 5, 5), ('*', 3, 2, 5, 4, 5, 6), ('*', 3, 2, 5, 4, 6, 5), ('*', 3, 2, 5, 5, 4, 6), ('*', 3, 2, 5, 5, 6, 4), ('*', 3, 2, 5, 6, 4, 5), ('*', 3, 2, 5, 6, 5, 4), ('*', 3, 2, 6, 4, 5, 5), ('*', 3, 2, 6, 5, 4, 5), ('*', 3, 2, 6, 5, 5, 4), ('*', 3, 3, 4, 4, 5, 5), ('*', 3, 3, 4, 5, 4, 5), ('*', 3, 3, 4, 5, 5, 4), ('*', 3, 3, 5, 4, 4, 5), ('*', 3, 3, 5, 4, 5, 4), ('*', 3, 3, 5, 5, 4, 4), ('*', 3, 4, 2, 5, 5, 6), ('*', 3, 4, 2, 5, 6, 5), ('*', 3, 4, 2, 6, 5, 5), ('*', 3, 4, 3, 4, 5, 5), ('*', 3, 4, 3, 5, 4, 5), ('*', 3, 4, 3, 5, 5, 4), ('*', 3, 4, 4, 3, 5, 5), ('*', 3, 4, 4, 5, 3, 5), ('*', 3, 4, 4, 5, 5, 3), ('*', 3, 4, 5, 2, 5, 6), ('*', 3, 4, 5, 2, 6, 5), ('*', 3, 4, 5, 3, 4, 5), ('*', 3, 4, 5, 3, 5, 4), ('*', 3, 4, 5, 4, 3, 5), ('*', 3, 4, 5, 4, 5, 3), ('*', 3, 4, 5, 5, 2, 6), ('*', 3, 4, 5, 5, 3, 4), ('*', 3, 4, 5, 5, 4, 3), ('*', 3, 4, 5, 5, 6, 2), ('*', 3, 4, 5, 6, 2, 5), ('*', 3, 4, 5, 6, 5, 2), ('*', 3, 4, 6, 2, 5, 5), ('*', 3, 4, 6, 5, 2, 5), ('*', 3, 4, 6, 5, 5, 2), ('*', 3, 5, 2, 4, 5, 6), ('*', 3, 5, 2, 4, 6, 5), ('*', 3, 5, 2, 5, 4, 6), ('*', 3, 5, 2, 5, 6, 4), ('*', 3, 5, 2, 6, 4, 5), ('*', 3, 5, 2, 6, 5, 4), ('*', 3, 5, 3, 4, 4, 5), ('*', 3, 5, 3, 4, 5, 4), ('*', 3, 5, 3, 5, 4, 4), ('*', 3, 5, 4, 2, 5, 6), ('*', 3, 5, 4, 2, 6, 5), ('*', 3, 5, 4, 3, 4, 5), ('*', 3, 5, 4, 3, 5, 4), ('*', 3, 5, 4, 4, 3, 5), ('*', 3, 5, 4, 4, 5, 3), ('*', 3, 5, 4, 5, 2, 6), ('*', 3, 5, 4, 5, 3, 4), ('*', 3, 5, 4, 5, 4, 3), ('*', 3, 5, 4, 5, 6, 2), ('*', 3, 5, 4, 6, 2, 5), ('*', 3, 5, 4, 6, 5, 2), ('*', 3, 5, 5, 2, 4, 6), ('*', 3, 5, 5, 2, 6, 4), ('*', 3, 5, 5, 3, 4, 4), ('*', 3, 5, 5, 4, 2, 6), ('*', 3, 5, 5, 4, 3, 4), ('*', 3, 5, 5, 4, 4, 3), ('*', 3, 5, 5, 4, 6, 2), ('*', 3, 5, 5, 6, 2, 4), ('*', 3, 5, 5, 6, 4, 2), ('*', 3, 5, 6, 2, 4, 5), ('*', 3, 5, 6, 2, 5, 4), ('*', 3, 5, 6, 4, 2, 5), ('*', 3, 5, 6, 4, 5, 2), ('*', 3, 5, 6, 5, 2, 4), ('*', 3, 5, 6, 5, 4, 2), ('*', 3, 6, 2, 4, 5, 5), ('*', 3, 6, 2, 5, 4, 5), ('*', 3, 6, 2, 5, 5, 4), ('*', 3, 6, 4, 2, 5, 5), ('*', 3, 6, 4, 5, 2, 5), ('*', 3, 6, 4, 5, 5, 2), ('*', 3, 6, 5, 2, 4, 5), ('*', 3, 6, 5, 2, 5, 4), ('*', 3, 6, 5, 4, 2, 5), ('*', 3, 6, 5, 4, 5, 2), ('*', 3, 6, 5, 5, 2, 4), ('*', 3, 6, 5, 5, 4, 2), ('*', 4, 1, 5, 5, 6, 6), ('*', 4, 1, 5, 6, 5, 6), ('*', 4, 1, 5, 6, 6, 5), ('*', 4, 1, 6, 5, 5, 6), ('*', 4, 1, 6, 5, 6, 5), ('*', 4, 1, 6, 6, 5, 5), ('*', 4, 2, 3, 5, 5, 6), ('*', 4, 2, 3, 5, 6, 5), ('*', 4, 2, 3, 6, 5, 5), ('*', 4, 2, 5, 3, 5, 6), ('*', 4, 2, 5, 3, 6, 5), ('*', 4, 2, 5, 5, 3, 6), ('*', 4, 2, 5, 5, 6, 3), ('*', 4, 2, 5, 6, 3, 5), ('*', 4, 2, 5, 6, 5, 3), ('*', 4, 2, 6, 3, 5, 5), ('*', 4, 2, 6, 5, 3, 5), ('*', 4, 2, 6, 5, 5, 3), ('*', 4, 3, 2, 5, 5, 6), ('*', 4, 3, 2, 5, 6, 5), ('*', 4, 3, 2, 6, 5, 5), ('*', 4, 3, 3, 4, 5, 5), ('*', 4, 3, 3, 5, 4, 5), ('*', 4, 3, 3, 5, 5, 4), ('*', 4, 3, 4, 3, 5, 5), ('*', 4, 3, 4, 5, 3, 5), ('*', 4, 3, 4, 5, 5, 3), ('*', 4, 3, 5, 2, 5, 6), ('*', 4, 3, 5, 2, 6, 5), ('*', 4, 3, 5, 3, 4, 5), ('*', 4, 3, 5, 3, 5, 4), ('*', 4, 3, 5, 4, 3, 5), ('*', 4, 3, 5, 4, 5, 3), ('*', 4, 3, 5, 5, 2, 6), ('*', 4, 3, 5, 5, 3, 4), ('*', 4, 3, 5, 5, 4, 3), ('*', 4, 3, 5, 5, 6, 2), ('*', 4, 3, 5, 6, 2, 5), ('*', 4, 3, 5, 6, 5, 2), ('*', 4, 3, 6, 2, 5, 5), ('*', 4, 3, 6, 5, 2, 5), ('*', 4, 3, 6, 5, 5, 2), ('*', 4, 4, 3, 3, 5, 5), ('*', 4, 4, 3, 5, 3, 5), ('*', 4, 4, 3, 5, 5, 3), ('*', 4, 4, 5, 3, 3, 5), ('*', 4, 4, 5, 3, 5, 3), ('*', 4, 4, 5, 5, 3, 3), ('*', 4, 5, 1, 5, 6, 6), ('*', 4, 5, 1, 6, 5, 6), ('*', 4, 5, 1, 6, 6, 5), ('*', 4, 5, 2, 3, 5, 6), ('*', 4, 5, 2, 3, 6, 5), ('*', 4, 5, 2, 5, 3, 6), ('*', 4, 5, 2, 5, 6, 3), ('*', 4, 5, 2, 6, 3, 5), ('*', 4, 5, 2, 6, 5, 3), ('*', 4, 5, 3, 2, 5, 6), ('*', 4, 5, 3, 2, 6, 5), ('*', 4, 5, 3, 3, 4, 5), ('*', 4, 5, 3, 3, 5, 4), ('*', 4, 5, 3, 4, 3, 5), ('*', 4, 5, 3, 4, 5, 3), ('*', 4, 5, 3, 5, 2, 6), ('*', 4, 5, 3, 5, 3, 4), ('*', 4, 5, 3, 5, 4, 3), ('*', 4, 5, 3, 5, 6, 2), ('*', 4, 5, 3, 6, 2, 5), ('*', 4, 5, 3, 6, 5, 2), ('*', 4, 5, 4, 3, 3, 5), ('*', 4, 5, 4, 3, 5, 3), ('*', 4, 5, 4, 5, 3, 3), ('*', 4, 5, 5, 1, 6, 6), ('*', 4, 5, 5, 2, 3, 6), ('*', 4, 5, 5, 2, 6, 3), ('*', 4, 5, 5, 3, 2, 6), ('*', 4, 5, 5, 3, 3, 4), ('*', 4, 5, 5, 3, 4, 3), ('*', 4, 5, 5, 3, 6, 2), ('*', 4, 5, 5, 4, 3, 3), ('*', 4, 5, 5, 6, 1, 6), ('*', 4, 5, 5, 6, 2, 3), ('*', 4, 5, 5, 6, 3, 2), ('*', 4, 5, 5, 6, 6, 1), ('*', 4, 5, 6, 1, 5, 6), ('*', 4, 5, 6, 1, 6, 5), ('*', 4, 5, 6, 2, 3, 5), ('*', 4, 5, 6, 2, 5, 3), ('*', 4, 5, 6, 3, 2, 5), ('*', 4, 5, 6, 3, 5, 2), ('*', 4, 5, 6, 5, 1, 6), ('*', 4, 5, 6, 5, 2, 3), ('*', 4, 5, 6, 5, 3, 2), ('*', 4, 5, 6, 5, 6, 1), ('*', 4, 5, 6, 6, 1, 5), ('*', 4, 5, 6, 6, 5, 1), ('*', 4, 6, 1, 5, 5, 6), ('*', 4, 6, 1, 5, 6, 5), ('*', 4, 6, 1, 6, 5, 5), ('*', 4, 6, 2, 3, 5, 5), ('*', 4, 6, 2, 5, 3, 5), ('*', 4, 6, 2, 5, 5, 3), ('*', 4, 6, 3, 2, 5, 5), ('*', 4, 6, 3, 5, 2, 5), ('*', 4, 6, 3, 5, 5, 2), ('*', 4, 6, 5, 1, 5, 6), ('*', 4, 6, 5, 1, 6, 5), ('*', 4, 6, 5, 2, 3, 5), ('*', 4, 6, 5, 2, 5, 3), ('*', 4, 6, 5, 3, 2, 5), ('*', 4, 6, 5, 3, 5, 2), ('*', 4, 6, 5, 5, 1, 6), ('*', 4, 6, 5, 5, 2, 3), ('*', 4, 6, 5, 5, 3, 2), ('*', 4, 6, 5, 5, 6, 1), ('*', 4, 6, 5, 6, 1, 5), ('*', 4, 6, 5, 6, 5, 1), ('*', 4, 6, 6, 1, 5, 5), ('*', 4, 6, 6, 5, 1, 5), ('*', 4, 6, 6, 5, 5, 1), ('*', 5, 1, 4, 5, 6, 6), ('*', 5, 1, 4, 6, 5, 6), ('*', 5, 1, 4, 6, 6, 5), ('*', 5, 1, 5, 4, 6, 6), ('*', 5, 1, 5, 6, 4, 6), ('*', 5, 1, 5, 6, 6, 4), ('*', 5, 1, 6, 4, 5, 6), ('*', 5, 1, 6, 4, 6, 5), ('*', 5, 1, 6, 5, 4, 6), ('*', 5, 1, 6, 5, 6, 4), ('*', 5, 1, 6, 6, 4, 5), ('*', 5, 1, 6, 6, 5, 4), ('*', 5, 2, 2, 5, 6, 6), ('*', 5, 2, 2, 6, 5, 6), ('*', 5, 2, 2, 6, 6, 5), ('*', 5, 2, 3, 4, 5, 6), ('*', 5, 2, 3, 4, 6, 5), ('*', 5, 2, 3, 5, 4, 6), ('*', 5, 2, 3, 5, 6, 4), ('*', 5, 2, 3, 6, 4, 5), ('*', 5, 2, 3, 6, 5, 4), ('*', 5, 2, 4, 3, 5, 6), ('*', 5, 2, 4, 3, 6, 5), ('*', 5, 2, 4, 5, 3, 6), ('*', 5, 2, 4, 5, 6, 3), ('*', 5, 2, 4, 6, 3, 5), ('*', 5, 2, 4, 6, 5, 3), ('*', 5, 2, 5, 2, 6, 6), ('*', 5, 2, 5, 3, 4, 6), ('*', 5, 2, 5, 3, 6, 4), ('*', 5, 2, 5, 4, 3, 6), ('*', 5, 2, 5, 4, 6, 3), ('*', 5, 2, 5, 6, 2, 6), ('*', 5, 2, 5, 6, 3, 4), ('*', 5, 2, 5, 6, 4, 3), ('*', 5, 2, 5, 6, 6, 2), ('*', 5, 2, 6, 2, 5, 6), ('*', 5, 2, 6, 2, 6, 5), ('*', 5, 2, 6, 3, 4, 5), ('*', 5, 2, 6, 3, 5, 4), ('*', 5, 2, 6, 4, 3, 5), ('*', 5, 2, 6, 4, 5, 3), ('*', 5, 2, 6, 5, 2, 6), ('*', 5, 2, 6, 5, 3, 4), ('*', 5, 2, 6, 5, 4, 3), ('*', 5, 2, 6, 5, 6, 2), ('*', 5, 2, 6, 6, 2, 5), ('*', 5, 2, 6, 6, 5, 2), ('*', 5, 3, 2, 4, 5, 6), ('*', 5, 3, 2, 4, 6, 5), ('*', 5, 3, 2, 5, 4, 6), ('*', 5, 3, 2, 5, 6, 4), ('*', 5, 3, 2, 6, 4, 5), ('*', 5, 3, 2, 6, 5, 4), ('*', 5, 3, 3, 4, 4, 5), ('*', 5, 3, 3, 4, 5, 4), ('*', 5, 3, 3, 5, 4, 4), ('*', 5, 3, 4, 2, 5, 6), ('*', 5, 3, 4, 2, 6, 5), ('*', 5, 3, 4, 3, 4, 5), ('*', 5, 3, 4, 3, 5, 4), ('*', 5, 3, 4, 4, 3, 5), ('*', 5, 3, 4, 4, 5, 3), ('*', 5, 3, 4, 5, 2, 6), ('*', 5, 3, 4, 5, 3, 4), ('*', 5, 3, 4, 5, 4, 3), ('*', 5, 3, 4, 5, 6, 2), ('*', 5, 3, 4, 6, 2, 5), ('*', 5, 3, 4, 6, 5, 2), ('*', 5, 3, 5, 2, 4, 6), ('*', 5, 3, 5, 2, 6, 4), ('*', 5, 3, 5, 3, 4, 4), ('*', 5, 3, 5, 4, 2, 6), ('*', 5, 3, 5, 4, 3, 4), ('*', 5, 3, 5, 4, 4, 3), ('*', 5, 3, 5, 4, 6, 2), ('*', 5, 3, 5, 6, 2, 4), ('*', 5, 3, 5, 6, 4, 2), ('*', 5, 3, 6, 2, 4, 5), ('*', 5, 3, 6, 2, 5, 4), ('*', 5, 3, 6, 4, 2, 5), ('*', 5, 3, 6, 4, 5, 2), ('*', 5, 3, 6, 5, 2, 4), ('*', 5, 3, 6, 5, 4, 2), ('*', 5, 4, 1, 5, 6, 6), ('*', 5, 4, 1, 6, 5, 6), ('*', 5, 4, 1, 6, 6, 5), ('*', 5, 4, 2, 3, 5, 6), ('*', 5, 4, 2, 3, 6, 5), ('*', 5, 4, 2, 5, 3, 6), ('*', 5, 4, 2, 5, 6, 3), ('*', 5, 4, 2, 6, 3, 5), ('*', 5, 4, 2, 6, 5, 3), ('*', 5, 4, 3, 2, 5, 6), ('*', 5, 4, 3, 2, 6, 5), ('*', 5, 4, 3, 3, 4, 5), ('*', 5, 4, 3, 3, 5, 4), ('*', 5, 4, 3, 4, 3, 5), ('*', 5, 4, 3, 4, 5, 3), ('*', 5, 4, 3, 5, 2, 6), ('*', 5, 4, 3, 5, 3, 4), ('*', 5, 4, 3, 5, 4, 3), ('*', 5, 4, 3, 5, 6, 2), ('*', 5, 4, 3, 6, 2, 5), ('*', 5, 4, 3, 6, 5, 2), ('*', 5, 4, 4, 3, 3, 5), ('*', 5, 4, 4, 3, 5, 3), ('*', 5, 4, 4, 5, 3, 3), ('*', 5, 4, 5, 1, 6, 6), ('*', 5, 4, 5, 2, 3, 6), ('*', 5, 4, 5, 2, 6, 3), ('*', 5, 4, 5, 3, 2, 6), ('*', 5, 4, 5, 3, 3, 4), ('*', 5, 4, 5, 3, 4, 3), ('*', 5, 4, 5, 3, 6, 2), ('*', 5, 4, 5, 4, 3, 3), ('*', 5, 4, 5, 6, 1, 6), ('*', 5, 4, 5, 6, 2, 3), ('*', 5, 4, 5, 6, 3, 2), ('*', 5, 4, 5, 6, 6, 1), ('*', 5, 4, 6, 1, 5, 6), ('*', 5, 4, 6, 1, 6, 5), ('*', 5, 4, 6, 2, 3, 5), ('*', 5, 4, 6, 2, 5, 3), ('*', 5, 4, 6, 3, 2, 5), ('*', 5, 4, 6, 3, 5, 2), ('*', 5, 4, 6, 5, 1, 6), ('*', 5, 4, 6, 5, 2, 3), ('*', 5, 4, 6, 5, 3, 2), ('*', 5, 4, 6, 5, 6, 1), ('*', 5, 4, 6, 6, 1, 5), ('*', 5, 4, 6, 6, 5, 1), ('*', 5, 5, 1, 4, 6, 6), ('*', 5, 5, 1, 6, 4, 6), ('*', 5, 5, 1, 6, 6, 4), ('*', 5, 5, 2, 2, 6, 6), ('*', 5, 5, 2, 3, 4, 6), ('*', 5, 5, 2, 3, 6, 4), ('*', 5, 5, 2, 4, 3, 6), ('*', 5, 5, 2, 4, 6, 3), ('*', 5, 5, 2, 6, 2, 6), ('*', 5, 5, 2, 6, 3, 4), ('*', 5, 5, 2, 6, 4, 3), ('*', 5, 5, 2, 6, 6, 2), ('*', 5, 5, 3, 2, 4, 6), ('*', 5, 5, 3, 2, 6, 4), ('*', 5, 5, 3, 3, 4, 4), ('*', 5, 5, 3, 4, 2, 6), ('*', 5, 5, 3, 4, 3, 4), ('*', 5, 5, 3, 4, 4, 3), ('*', 5, 5, 3, 4, 6, 2), ('*', 5, 5, 3, 6, 2, 4), ('*', 5, 5, 3, 6, 4, 2), ('*', 5, 5, 4, 1, 6, 6), ('*', 5, 5, 4, 2, 3, 6), ('*', 5, 5, 4, 2, 6, 3), ('*', 5, 5, 4, 3, 2, 6), ('*', 5, 5, 4, 3, 3, 4), ('*', 5, 5, 4, 3, 4, 3), ('*', 5, 5, 4, 3, 6, 2), ('*', 5, 5, 4, 4, 3, 3), ('*', 5, 5, 4, 6, 1, 6), ('*', 5, 5, 4, 6, 2, 3), ('*', 5, 5, 4, 6, 3, 2), ('*', 5, 5, 4, 6, 6, 1), ('*', 5, 5, 6, 1, 4, 6), ('*', 5, 5, 6, 1, 6, 4), ('*', 5, 5, 6, 2, 2, 6), ('*', 5, 5, 6, 2, 3, 4), ('*', 5, 5, 6, 2, 4, 3), ('*', 5, 5, 6, 2, 6, 2), ('*', 5, 5, 6, 3, 2, 4), ('*', 5, 5, 6, 3, 4, 2), ('*', 5, 5, 6, 4, 1, 6), ('*', 5, 5, 6, 4, 2, 3), ('*', 5, 5, 6, 4, 3, 2), ('*', 5, 5, 6, 4, 6, 1), ('*', 5, 5, 6, 6, 1, 4), ('*', 5, 5, 6, 6, 2, 2), ('*', 5, 5, 6, 6, 4, 1), ('*', 5, 6, 1, 4, 5, 6), ('*', 5, 6, 1, 4, 6, 5), ('*', 5, 6, 1, 5, 4, 6), ('*', 5, 6, 1, 5, 6, 4), ('*', 5, 6, 1, 6, 4, 5), ('*', 5, 6, 1, 6, 5, 4), ('*', 5, 6, 2, 2, 5, 6), ('*', 5, 6, 2, 2, 6, 5), ('*', 5, 6, 2, 3, 4, 5), ('*', 5, 6, 2, 3, 5, 4), ('*', 5, 6, 2, 4, 3, 5), ('*', 5, 6, 2, 4, 5, 3), ('*', 5, 6, 2, 5, 2, 6), ('*', 5, 6, 2, 5, 3, 4), ('*', 5, 6, 2, 5, 4, 3), ('*', 5, 6, 2, 5, 6, 2), ('*', 5, 6, 2, 6, 2, 5), ('*', 5, 6, 2, 6, 5, 2), ('*', 5, 6, 3, 2, 4, 5), ('*', 5, 6, 3, 2, 5, 4), ('*', 5, 6, 3, 4, 2, 5), ('*', 5, 6, 3, 4, 5, 2), ('*', 5, 6, 3, 5, 2, 4), ('*', 5, 6, 3, 5, 4, 2), ('*', 5, 6, 4, 1, 5, 6), ('*', 5, 6, 4, 1, 6, 5), ('*', 5, 6, 4, 2, 3, 5), ('*', 5, 6, 4, 2, 5, 3), ('*', 5, 6, 4, 3, 2, 5), ('*', 5, 6, 4, 3, 5, 2), ('*', 5, 6, 4, 5, 1, 6), ('*', 5, 6, 4, 5, 2, 3), ('*', 5, 6, 4, 5, 3, 2), ('*', 5, 6, 4, 5, 6, 1), ('*', 5, 6, 4, 6, 1, 5), ('*', 5, 6, 4, 6, 5, 1), ('*', 5, 6, 5, 1, 4, 6), ('*', 5, 6, 5, 1, 6, 4), ('*', 5, 6, 5, 2, 2, 6), ('*', 5, 6, 5, 2, 3, 4), ('*', 5, 6, 5, 2, 4, 3), ('*', 5, 6, 5, 2, 6, 2), ('*', 5, 6, 5, 3, 2, 4), ('*', 5, 6, 5, 3, 4, 2), ('*', 5, 6, 5, 4, 1, 6), ('*', 5, 6, 5, 4, 2, 3), ('*', 5, 6, 5, 4, 3, 2), ('*', 5, 6, 5, 4, 6, 1), ('*', 5, 6, 5, 6, 1, 4), ('*', 5, 6, 5, 6, 2, 2), ('*', 5, 6, 5, 6, 4, 1), ('*', 5, 6, 6, 1, 4, 5), ('*', 5, 6, 6, 1, 5, 4), ('*', 5, 6, 6, 2, 2, 5), ('*', 5, 6, 6, 2, 5, 2), ('*', 5, 6, 6, 4, 1, 5), ('*', 5, 6, 6, 4, 5, 1), ('*', 5, 6, 6, 5, 1, 4), ('*', 5, 6, 6, 5, 2, 2), ('*', 5, 6, 6, 5, 4, 1), ('*', 6, 1, 4, 5, 5, 6), ('*', 6, 1, 4, 5, 6, 5), ('*', 6, 1, 4, 6, 5, 5), ('*', 6, 1, 5, 4, 5, 6), ('*', 6, 1, 5, 4, 6, 5), ('*', 6, 1, 5, 5, 4, 6), ('*', 6, 1, 5, 5, 6, 4), ('*', 6, 1, 5, 6, 4, 5), ('*', 6, 1, 5, 6, 5, 4), ('*', 6, 1, 6, 4, 5, 5), ('*', 6, 1, 6, 5, 4, 5), ('*', 6, 1, 6, 5, 5, 4), ('*', 6, 2, 2, 5, 5, 6), ('*', 6, 2, 2, 5, 6, 5), ('*', 6, 2, 2, 6, 5, 5), ('*', 6, 2, 3, 4, 5, 5), ('*', 6, 2, 3, 5, 4, 5), ('*', 6, 2, 3, 5, 5, 4), ('*', 6, 2, 4, 3, 5, 5), ('*', 6, 2, 4, 5, 3, 5), ('*', 6, 2, 4, 5, 5, 3), ('*', 6, 2, 5, 2, 5, 6), ('*', 6, 2, 5, 2, 6, 5), ('*', 6, 2, 5, 3, 4, 5), ('*', 6, 2, 5, 3, 5, 4), ('*', 6, 2, 5, 4, 3, 5), ('*', 6, 2, 5, 4, 5, 3), ('*', 6, 2, 5, 5, 2, 6), ('*', 6, 2, 5, 5, 3, 4), ('*', 6, 2, 5, 5, 4, 3), ('*', 6, 2, 5, 5, 6, 2), ('*', 6, 2, 5, 6, 2, 5), ('*', 6, 2, 5, 6, 5, 2), ('*', 6, 2, 6, 2, 5, 5), ('*', 6, 2, 6, 5, 2, 5), ('*', 6, 2, 6, 5, 5, 2), ('*', 6, 3, 2, 4, 5, 5), ('*', 6, 3, 2, 5, 4, 5), ('*', 6, 3, 2, 5, 5, 4), ('*', 6, 3, 4, 2, 5, 5), ('*', 6, 3, 4, 5, 2, 5), ('*', 6, 3, 4, 5, 5, 2), ('*', 6, 3, 5, 2, 4, 5), ('*', 6, 3, 5, 2, 5, 4), ('*', 6, 3, 5, 4, 2, 5), ('*', 6, 3, 5, 4, 5, 2), ('*', 6, 3, 5, 5, 2, 4), ('*', 6, 3, 5, 5, 4, 2), ('*', 6, 4, 1, 5, 5, 6), ('*', 6, 4, 1, 5, 6, 5), ('*', 6, 4, 1, 6, 5, 5), ('*', 6, 4, 2, 3, 5, 5), ('*', 6, 4, 2, 5, 3, 5), ('*', 6, 4, 2, 5, 5, 3), ('*', 6, 4, 3, 2, 5, 5), ('*', 6, 4, 3, 5, 2, 5), ('*', 6, 4, 3, 5, 5, 2), ('*', 6, 4, 5, 1, 5, 6), ('*', 6, 4, 5, 1, 6, 5), ('*', 6, 4, 5, 2, 3, 5), ('*', 6, 4, 5, 2, 5, 3), ('*', 6, 4, 5, 3, 2, 5), ('*', 6, 4, 5, 3, 5, 2), ('*', 6, 4, 5, 5, 1, 6), ('*', 6, 4, 5, 5, 2, 3), ('*', 6, 4, 5, 5, 3, 2), ('*', 6, 4, 5, 5, 6, 1), ('*', 6, 4, 5, 6, 1, 5), ('*', 6, 4, 5, 6, 5, 1), ('*', 6, 4, 6, 1, 5, 5), ('*', 6, 4, 6, 5, 1, 5), ('*', 6, 4, 6, 5, 5, 1), ('*', 6, 5, 1, 4, 5, 6), ('*', 6, 5, 1, 4, 6, 5), ('*', 6, 5, 1, 5, 4, 6), ('*', 6, 5, 1, 5, 6, 4), ('*', 6, 5, 1, 6, 4, 5), ('*', 6, 5, 1, 6, 5, 4), ('*', 6, 5, 2, 2, 5, 6), ('*', 6, 5, 2, 2, 6, 5), ('*', 6, 5, 2, 3, 4, 5), ('*', 6, 5, 2, 3, 5, 4), ('*', 6, 5, 2, 4, 3, 5), ('*', 6, 5, 2, 4, 5, 3), ('*', 6, 5, 2, 5, 2, 6), ('*', 6, 5, 2, 5, 3, 4), ('*', 6, 5, 2, 5, 4, 3), ('*', 6, 5, 2, 5, 6, 2), ('*', 6, 5, 2, 6, 2, 5), ('*', 6, 5, 2, 6, 5, 2), ('*', 6, 5, 3, 2, 4, 5), ('*', 6, 5, 3, 2, 5, 4), ('*', 6, 5, 3, 4, 2, 5), ('*', 6, 5, 3, 4, 5, 2), ('*', 6, 5, 3, 5, 2, 4), ('*', 6, 5, 3, 5, 4, 2), ('*', 6, 5, 4, 1, 5, 6), ('*', 6, 5, 4, 1, 6, 5), ('*', 6, 5, 4, 2, 3, 5), ('*', 6, 5, 4, 2, 5, 3), ('*', 6, 5, 4, 3, 2, 5), ('*', 6, 5, 4, 3, 5, 2), ('*', 6, 5, 4, 5, 1, 6), ('*', 6, 5, 4, 5, 2, 3), ('*', 6, 5, 4, 5, 3, 2), ('*', 6, 5, 4, 5, 6, 1), ('*', 6, 5, 4, 6, 1, 5), ('*', 6, 5, 4, 6, 5, 1), ('*', 6, 5, 5, 1, 4, 6), ('*', 6, 5, 5, 1, 6, 4), ('*', 6, 5, 5, 2, 2, 6), ('*', 6, 5, 5, 2, 3, 4), ('*', 6, 5, 5, 2, 4, 3), ('*', 6, 5, 5, 2, 6, 2), ('*', 6, 5, 5, 3, 2, 4), ('*', 6, 5, 5, 3, 4, 2), ('*', 6, 5, 5, 4, 1, 6), ('*', 6, 5, 5, 4, 2, 3), ('*', 6, 5, 5, 4, 3, 2), ('*', 6, 5, 5, 4, 6, 1), ('*', 6, 5, 5, 6, 1, 4), ('*', 6, 5, 5, 6, 2, 2), ('*', 6, 5, 5, 6, 4, 1), ('*', 6, 5, 6, 1, 4, 5), ('*', 6, 5, 6, 1, 5, 4), ('*', 6, 5, 6, 2, 2, 5), ('*', 6, 5, 6, 2, 5, 2), ('*', 6, 5, 6, 4, 1, 5), ('*', 6, 5, 6, 4, 5, 1), ('*', 6, 5, 6, 5, 1, 4), ('*', 6, 5, 6, 5, 2, 2), ('*', 6, 5, 6, 5, 4, 1), ('*', 6, 6, 1, 4, 5, 5), ('*', 6, 6, 1, 5, 4, 5), ('*', 6, 6, 1, 5, 5, 4), ('*', 6, 6, 2, 2, 5, 5), ('*', 6, 6, 2, 5, 2, 5), ('*', 6, 6, 2, 5, 5, 2), ('*', 6, 6, 4, 1, 5, 5), ('*', 6, 6, 4, 5, 1, 5), ('*', 6, 6, 4, 5, 5, 1), ('*', 6, 6, 5, 1, 4, 5), ('*', 6, 6, 5, 1, 5, 4), ('*', 6, 6, 5, 2, 2, 5), ('*', 6, 6, 5, 2, 5, 2), ('*', 6, 6, 5, 4, 1, 5), ('*', 6, 6, 5, 4, 5, 1), ('*', 6, 6, 5, 5, 1, 4), ('*', 6, 6, 5, 5, 2, 2), ('*', 6, 6, 5, 5, 4, 1)])
        con19.add_satisfying_tuples([('*', 4, 5, 6), ('*', 4, 6, 5), ('*', 5, 4, 6), ('*', 5, 6, 4), ('*', 6, 4, 5), ('*', 6, 5, 4)])
        con20.add_satisfying_tuples([('-', 1, 1, 1, 4), ('-', 1, 1, 2, 5), ('-', 1, 1, 3, 6), ('-', 1, 1, 4, 1), ('-', 1, 1, 5, 2), ('-', 1, 1, 6, 3), ('-', 1, 2, 1, 5), ('-', 1, 2, 2, 6), ('-', 1, 2, 5, 1), ('-', 1, 2, 6, 2), ('-', 1, 3, 1, 6), ('-', 1, 3, 6, 1), ('-', 1, 4, 1, 1), ('-', 1, 5, 1, 2), ('-', 1, 5, 2, 1), ('-', 1, 6, 1, 3), ('-', 1, 6, 2, 2), ('-', 1, 6, 3, 1), ('-', 2, 1, 1, 5), ('-', 2, 1, 2, 6), ('-', 2, 1, 5, 1), ('-', 2, 1, 6, 2), ('-', 2, 2, 1, 6), ('-', 2, 2, 6, 1), ('-', 2, 5, 1, 1), ('-', 2, 6, 1, 2), ('-', 2, 6, 2, 1), ('-', 3, 1, 1, 6), ('-', 3, 1, 6, 1), ('-', 3, 6, 1, 1), ('-', 4, 1, 1, 1), ('-', 5, 1, 1, 2), ('-', 5, 1, 2, 1), ('-', 5, 2, 1, 1), ('-', 6, 1, 1, 3), ('-', 6, 1, 2, 2), ('-', 6, 1, 3, 1), ('-', 6, 2, 1, 2), ('-', 6, 2, 2, 1), ('-', 6, 3, 1, 1)])
        con21.add_satisfying_tuples([('-', 1, 6), ('-', 6, 1)])
        con22.add_satisfying_tuples([('+', 1, 4), ('+', 2, 3), ('+', 3, 2), ('+', 4, 1)])

        cons = [con0, con1, con2, con3, con4, con5, con6, con7, con8, con9, con10, con11, con12, con13, con14, con15, con16, con17, con18, con19, con20, con21, con22]

        var_array = [
            [var0, var1, var2, var3, var4, var5],
            [var6, var7, var8, var9, var10, var11],
            [var12, var13, var14, var15, var16, var17],
            [var18, var19, var20, var21, var22, var23],
            [var24, var25, var26, var27, var28, var29],
            [var30, var31, var32, var33, var34, var35],
            var36,
            var37,
            var38,
            var39,
            var40,
            var41,
            var42,
            var43,
            var44,
            var45,
            var46
        ]

        vars = [
            var0, var1, var2, var3, var4, var5,
            var6, var7, var8, var9, var10, var11,
            var12, var13, var14, var15, var16, var17,
            var18, var19, var20, var21, var22, var23,
            var24, var25, var26, var27, var28, var29,
            var30, var31, var32, var33, var34, var35,
            var36,
            var37,
            var38,
            var39,
            var40,
            var41,
            var42,
            var43,
            var44,
            var45,
            var46
        ]

        csp = CSP("Cagey", vars)

        for c in cons:
            csp.add_constraint(c)

        return csp, var_array