from typing import *

from sympy import latex,Symbol,Expr,Matrix
import sympy as sym


# global symbol declarations

# number of time steps, number of grid points
t_dim, x_dim = sym.symbols('t_dim x_dim', integer = True)
# grid spacing
Delta_x : 1 = Symbol('Delta_x')
Delta_t : Symbol = Symbol('Delta_t')

# # array containing data for each time step and gridpoint
v : sym.IndexedBase = sym.IndexedBase('v', shape = (x_dim, t_dim))
u : sym.IndexedBase = sym.IndexedBase('u')
# indicies into grid and timesteps, respectively
i, n = sym.symbols('i n') #, cls = sym.Idx)

DISCRETIZATION_VARS : Dict[str, Tuple[Symbol,Symbol]] = {
	'space' : (i, Delta_x), 
	'time' : (n, Delta_t),
}

# class IndexedSymbol(sym.Indexed):

# other
gamma : Symbol = Symbol('gamma')

# DIFFERENCE_OPERATORS_SPACE
DIFFERENCE_OPERATORS : Dict[str, sym.Expr] = {
	'D_0' : lambda f, x, h : (f[x + 1] - f[x - 1]) / (2 * h),
	'D_+' : lambda f, x, h : (f[x+1] - f[x]) / h,
	'D_-' : lambda f, x, h : (f[x] - f[x-1]) / h,
}

DIFFERENCE_OPERATORS_INT : Dict[str, int] = {
	'D_0' : 0,
	'D_+' : 1,
	'D_-' : -1,
}

SOLVEFOR_IDXS : Dict[str, List[int]] = {
	# 'D_0' : [+1, 0],
	'D_0' : [+1],
	'D_+' : [+1],
	'D_-' : [0],
}

# DIFFERENCE_OPERATORS_TIME : Dict[str, sym.Expr] = {
# 	'0' : lambda f, x, h : (f[:,x + 1] - f[:,x - 1]) / (2 * h),
# 	'+' : lambda f, x, h : (f[:,x+1] - f[:,x]) / h,
# 	'-' : lambda f, x, h : (f[:,x] - f[:,x-1]) / h,
# }


def tester():
	print(latex(v[i,n]))
	print(latex(DIFFERENCE_OPERATORS['+'](u, n, Delta_t)))


def exprprint(
		expr : Union[Iterable, sym.Expr],
		name : Optional[str] = None, 
		rhs : Optional[Expr] = None,
		multi : bool = False, 
	) -> str:

	# handle list conversion
	if not isinstance(expr, Iterable):
		expr = [expr]
		rhs = [rhs]

	expr = list(expr)
	rhs = list(rhs)

	assert len(expr) == len(rhs), f"list of `expr`'s and `rhs`'s should be equal length, got {len(expr)=} {len(rhs)=}"

	# naming stuff
	if name is not None:
		name += '  \n'


	if not multi:
		print(
			f"{name if name is not None else ''}$$ {latex(expr[0])} {f'= {latex(rhs[0])}' if rhs is not None else ''} $$"
		)
	else:

		expr = Matrix(expr).T
		rhs = Matrix(rhs).T
		print(
			name if name is not None else '',
			'$$ ',
			latex(expr),
			' = ',
			latex(rhs),
			' $$',
		)

def main():

	for discretization,(idx_sym, grid_size) in DISCRETIZATION_VARS.items():
		for operator,diff_op in DIFFERENCE_OPERATORS.items():

			idx_offset : List[int] = SOLVEFOR_IDXS[operator]
			solvefor_lst : List[Expr] = [ u[ idx_sym + idx ] for idx in idx_offset ]
			solvefor : Expr = solvefor_lst[0]
			
			# print(f'{discretization=} {operator=} {idx_sym=} {grid_size=} {solvefor=}    ')
			print(f' - {discretization} discretization with operator ${operator}$, solving for ${latex(solvefor)}$    ')
			
			eqn : Expr = diff_op(u, idx_sym, grid_size) - gamma * u[idx_sym]
			solns : Dict[Expr,Expr] = sym.solve(eqn, solvefor)[0]

			print(solns)
			
			exprprint(eqn, rhs = 0)
			exprprint(solns, rhs = solvefor)
			# exprprint([ solns[r] for r in solvefor ], rhs = solvefor)

			print('\n')

main()





