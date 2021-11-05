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

DIFF_FIRSTORDER : List[str] = ['D_0', 'D_+', 'D_-']
DIFF_SECONDORDER : List[str] = ['D_- D_+', 'D_+^2', 'D_-^2']

# DIFFERENCE_OPERATORS_SPACE
DIFFERENCE_OPERATORS : Dict[str, Callable] = {
	# first order
	'D_0' : lambda f, x, h : (f[x + 1] - f[x - 1]) / (2 * h),
	'D_+' : lambda f, x, h : (f[x+1] - f[x]) / h,
	'D_-' : lambda f, x, h : (f[x] - f[x-1]) / h,
	# second order
	'D_- D_+' : lambda f, x, h : ( f[x+1] - 2 * f[x] + f[x-1] ) / (h**2),
	'D_+^2' : lambda f, x, h : ( f[x+2] - 2 * f[x+1] + f[x] ) / (h**2),
	'D_-^2' : lambda f, x, h : ( f[x] - 2 * f[x-1] + f[x-2] ) / (h**2),
}

# DIFFERENCE_OPERATORS_INT : Dict[str, int] = {
# 	'D_0' : 0,
# 	'D_+' : 1,
# 	'D_-' : -1,
# 	'D_- D_+' : 1,
# 	'D_+^2' : 2,
# 	'D_-^2' : -2,
# }

SOLVEFOR_IDXS : Dict[str, List[int]] = {
	'D_0' : [+1,0,-1],
	'D_+' : [+1],
	'D_-' : [0],
	'D_- D_+' : [+1,0,-1],
	'D_+^2' : [+2,+1,0],
	'D_-^2' : [0,-1,-2],
}

def solve_matrix_diffops(soln : Expr, solvefor_lst : List[Expr], indent = '    ') -> Matrix:
	"""given an equation relating indices [n,..,n+k], solve for [n+1,..,n+k] as a function of [n,..,n+k-1]"""

	# construct the matrix by extracting coefficients from the solved equations
	A : Matrix = Matrix([
		[
			sym.simplify( soln.subs(
				{ s_i : 0 for s_i in solvefor_lst[1:] if s_i != s_q }
			) / s_q )
			for s_q in solvefor_lst[1:]
		],
		*[
			[
				1 if s_j == s_q else 0
				for s_j in solvefor_lst[1:]
			]
			for s_q in solvefor_lst[1:-1]
		],
	])

	print(
		indent,
		"$$ ",
		latex(Matrix(solvefor_lst[:-1])),
		" = ",
		latex(A),
		"\\cdot",
		latex(Matrix(solvefor_lst[1:])),
		" $$",
	)

	return A




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
		comp_op : str = '=',
		multi : bool = False, 
		indent : str = '',
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
			name if name is not None else '',
			indent,
			"$$ ",
			latex(expr[0]),
			f" {comp_op} ",
			latex(rhs[0]) if rhs is not None else '',
			" $$",
		)
	else:
		raise NotImplementedError()
		# expr = Matrix(expr)
		# rhs = Matrix(rhs)
		# print(
		# 	name if name is not None else '',
		# 	"$$ ",
		# 	latex(expr),
		# 	f" {comp_op} ",
		# 	latex(rhs),
		# 	" $$",
		# )

def print_eigvals_conditions(
		egiv : List[Expr], 
		sym_solve : Expr = gamma, 
		indent : str = '',
	) -> None:
	
	# print base eigenvalue condition
	print(
		indent,
		"$$ ",
		'\\qquad'.join([ latex(abs(e)) + '\\leq 1' for e in egiv ]),
		" $$",
	)

def stability_eval(diff_ops_eqn : List[str]):

	for discretization,(idx_sym, grid_size) in DISCRETIZATION_VARS.items():
		for operator in diff_ops_eqn:
			diff_op : Callable = DIFFERENCE_OPERATORS[operator]

			idx_offset : List[int] = SOLVEFOR_IDXS[operator]
			solvefor_lst : List[Expr] = [ u[ idx_sym + idx ] for idx in idx_offset ]
			solvefor : Expr = solvefor_lst[0]
			
			# print(f'{discretization=} {operator=} {idx_sym=} {grid_size=} {solvefor=}    ')
			print(f' - {discretization} discretization with operator ${operator}$, solving for ${latex(solvefor_lst)}$, and $z := {latex(gamma)}{latex(grid_size)}$    ')
			
			eqn : Expr = diff_op(u, idx_sym, grid_size) - gamma * u[idx_sym]
			soln : Expr = sym.solve(eqn, solvefor)[0]
			# solns : List[Expr] = [
			# 	sym.solve(eqn, slvfr)[0]
			# 	for slvfr in solvefor_lst
			# ]
			
			print('   - original difference scheme')
			exprprint(eqn, rhs = 0, indent = '    ')
			print('   - solving for next timestep')
			exprprint(soln, rhs = solvefor, indent = '    ')
			
			if len(solvefor_lst) == 1:
				print(f'   - condition on ${latex(gamma)}$')
				exprprint(
					abs(soln / u[idx_sym + SOLVEFOR_IDXS[operator][0] - 1 ]), 
					comp_op = '\\leq',
					rhs = 1,
					indent = '    ',
				)
			else:
				print(f'   - matrix equation')
				sln_mat : Matrix = solve_matrix_diffops(soln, solvefor_lst, indent = '    ')
				sln_mat_eigvals : List[Expr] = sln_mat.eigenvals()
				print(f'   - condition on ${latex(gamma)}$ derived from requiring each eigenvalue be less than 1 in abosolute value')
				print_eigvals_conditions(sln_mat_eigvals, indent = '    ')


			print('\n')




def main():
	print(r'# equation $u_t = - u_x$', '\n')
	stability_eval(DIFF_FIRSTORDER)
	print(r'# equation $u_t = u_{xx}$', '\n')
	stability_eval(DIFF_SECONDORDER)

if __name__ == '__main__':
	main()





