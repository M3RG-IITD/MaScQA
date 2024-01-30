from sympy import solve, Eq
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

eqns = ['4x + 3y = 20', '-5x + 9y = 26']
transformations = (standard_transformations +
                   (implicit_multiplication_application,))
parsed_eqs = []
for eq in eqns:
        sides = [parse_expr(s, transformations=transformations)
                for s in eq.split('=')]
        parsed_eqs.append(Eq(sides[0], sides[1]))
soln = solve(parsed_eqs)
test_sol_values = [soln.get(list(soln.keys())[0]), soln.get(list(soln.keys())[1])]

result = True if list(sle(eqns).values()) == test_sol_values else False