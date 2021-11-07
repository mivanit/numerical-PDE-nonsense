from typing import *
import sys

from sympy import latex,Symbol,Expr,Matrix
import sympy as sym

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.path as mplPath

from theta_scheme_numerics import MATRIX_DIFFOPS,BoundaryCondition,EXPORT_FILE_EXTENSION


EPSILON : float = 1e-6

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


MAT_DIFFOP_PLOT_FMT : Dict[str,str] = {
	'D_0' : '.',
	'D_+' : '+',
	'D_-' : 'x',
	'D_- D_+' : '.',
	'D_+^2' : '+',
	'D_-^2' : 'x',
}

MAT_DIFFOP_BYORDER : Dict[int, Set[str]] = {
	1 : {'D_0', 'D_+', 'D_-'},
	2 : {'D_- D_+', 'D_+^2', 'D_-^2'},
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


def matrix_to_smallmatrix(mat : str) -> str:
	return mat.replace(r'{matrix}', r'{smallmatrix}')



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


DIFFOP_AREAPLOT_NAMES : Dict[str, str] = {
	'D_0' : 'Central Difference',
	'D_+' : 'Forward Euler',
	'D_-' : 'Backward Euler',
}

def sort_radial(x, y, remove_center : bool = True) -> np.ndarray:

	x0 = np.mean(x)
	y0 = np.mean(y)

	center = np.array([x0, y0])

	r = np.sqrt((x-x0)**2 + (y-y0)**2)

	angles = np.where((y-y0) > 0, np.arccos((x-x0)/r), 2*np.pi-np.arccos((x-x0)/r))

	mask = np.argsort(angles)

	x_sorted = x[mask]
	y_sorted = y[mask]

	sorted_points = np.array([x_sorted, y_sorted])

	if remove_center:
		# remove any point that is within `EPSILON` of the center
		mask = [
			np.linalg.norm(pt - center) > 0.1 * np.mean(r)
			for pt in sorted_points.T
		]
		sorted_points = sorted_points[:,mask]

	return sorted_points


def plot_stab_region(
		eigvals : Dict[str, np.ndarray], 
		cfl : float = 1.0,
		remove_center : bool = True,
	) -> tuple:

	fig,ax = plt.subplots()
	for key in DIFFOP_AREAPLOT_NAMES.keys():
		sorted_eigs : np.ndarray = np.array(sort_radial(
			eigvals[key].real / cfl,
			eigvals[key].imag / cfl,
			remove_center = remove_center,
		))

		if key == 'D_0':
			ax.plot(
				sorted_eigs[0], sorted_eigs[1],
				'k-',
				label = DIFFOP_AREAPLOT_NAMES[key],
			)
		else:

			ax.fill(
				sorted_eigs[0], sorted_eigs[1],
				alpha = 0.2,
				label = DIFFOP_AREAPLOT_NAMES[key],
			)
	ax.set_aspect('equal')

	return fig,ax

def gen_stab_table(
		eigvals : Dict[str, np.ndarray], 
		cfl : float = 1.0,
		order : int = 1,
	) -> Dict[str, Dict[str, bool]]:

	table : Dict[str, Dict[str, bool]] = dict()

	# iterate over rows
	for scheme,schemename in DIFFOP_AREAPLOT_NAMES.items():
		table[schemename] = dict()

		stab_are_eigs_sorted : Tuple[np.ndarray, np.ndarray] = sort_radial(
			eigvals[scheme].real / cfl,
			eigvals[scheme].imag / cfl,
		)
		stabAreaPath : mplPath.Path = mplPath.Path(np.array(stab_are_eigs_sorted).T)

		for diffop in MAT_DIFFOP_BYORDER[order]:
			eig : np.ndarray = eigvals[diffop]
			sorted_eigs : np.ndarray = np.array(sort_radial(
				eig.real,
				eig.imag,
			))
			
			if scheme == 'D_0':
				# for central difference, 
				# check the real part is 0 and imaginary is < 1/lambda in magnitude
				table[schemename][diffop] = (
					all(abs(x) < EPSILON for x in sorted_eigs[0])
					and
					all(abs(x) < 1/cfl for x in sorted_eigs[1])
				)
			elif scheme == 'D_+':
				# check that the eigenvalues are in the stability region
				points_in_region : np.ndarray = stabAreaPath.contains_points(sorted_eigs.T)
				
				table[schemename][diffop] = all(points_in_region)
			
			elif scheme == 'D_-':
				# check that the eigenvalues are in the stability region
				# fudging: to compensate for numerical error,
				# move everything a bit to the left

				sorted_eigs_left : np.ndarray = sorted_eigs.copy()
				sorted_eigs_left[0,:] -= 1e-5

				points_in_region : np.ndarray = stabAreaPath.contains_points(sorted_eigs_left.T)

				table[schemename][diffop] = not any(points_in_region)

			else:
				raise KeyError(f"unknown diffop {diffop}")
	return table

def doubledict_to_table(
		data : Dict[str, Dict[str, Any]], 
		mapping : Callable = str,
		col_mapping : Callable = lambda x : f"${x}$",
	) -> str:
	"""convert a doubly nested dict to a LaTeX formatted table"""

	row_lst : List[str] = list(data.keys())
	n_rows : int = len(row_lst)
	cols_lst : List[str] = list(set().union(*[set(data[row].keys()) for row in row_lst]))
	n_cols : int = len(cols_lst)

	# print(f"{row_lst=}, {cols_lst=}", file = sys.stderr)


	# table defn
	table : List[str] = [
		r'\begin{tabular}{',
		'|'.join(['c']*(n_cols+1)),
		'}\n',
		# '\hline\n',
		# ' & '.join(mapping(key) for key in data.keys()),
		# '\\\n',
		# '\hline\n',
	]

	# header
	table.append(' & '.join([' '] + [ col_mapping(x) for x in cols_lst ]))
	table.append('\\\\ \n')
	table.append('\\hline\n')

	for row in row_lst:
		table.append(row)
		table.append(' & ')
		table.append(' & '.join( mapping(data[row][col]) for col in cols_lst ))
		table.append('\\\\ \n')

	table.append(r'\end{tabular}')
	table.append('\n')

	return ''.join(table)



def print_eigvals_conditions(
		egival : List[Expr], 
		grid_size : Expr,
		sym_solve : Expr = gamma, 
		indent : str = '',
		# n_pts_plot : int = 25,
	) -> None:
	
	print(f'{indent}- condition on ${latex(gamma)}$ derived from requiring each eigenvalue be less than 1 in abosolute value')
	print(
		indent,
		"$$ ",
		'\\qquad'.join([ latex(abs(e)) + '\\leq 1' for e in egival ]),
		" $$",
	)

	print(f'{indent}- substituting ${latex(grid_size)} = 1$')
	eigval_grid_subs : List[Expr] = [ sym.simplify(e.subs(grid_size, 1)) for e in egival ]
	print(
		indent,
		"$$ ",
		'\\qquad'.join([ latex(abs(e)) + '\\leq 1' for e in eigval_grid_subs ]),
		" $$",
	)

	# print(f'{indent}- solving for ${latex(sym_solve)}$ when eigenvalues are exactly 1')
	# print(
	# 	indent,
	# 	"$$ ",
	# 	'\\qquad'.join([ latex(e - 1) + '= 0' for e in eigval_grid_subs ]),
	# 	" $$",
	# )


	# solved_expr : List[Expr] = [ sym.solve(e - 1, sym_solve) for e in eigval_grid_subs ]
	
	# print(f'{indent}- solving for ${latex(sym_solve)}$, substituting ${latex(grid_size)} = 1$')
	# print(
	# 	indent,
	# 	"$$ ",
	# 	'\\qquad'.join([
	# 		f'{latex(sym_solve)} = ' + latex(e) 
	# 		for e in solved_expr
	# 	]),
	# 	" $$",
	# )



	# # generate `n_pts_plot` points satisfying `egival` condition exactly
	# pts = [
	# 	sym.solve(
	# 		sym.Eq(sym_solve, e),
	# 		sym_solve,
	# 		dict=True,
	# 	)[0]['sol']




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
				print_eigvals_conditions(sln_mat_eigvals, grid_size = grid_size, indent = '    ')


			print('\n')


BDRY_CONDITIONS_FOR_DIFF_OPS : Dict[str, BoundaryCondition] = {
	'D_0' : 'periodic',
	'D_+' : 'periodic',
	'D_-' : 'periodic',
	'D_- D_+' : 'dirichlet',
	'D_+^2' : 'dirichlet',
	'D_-^2' : 'dirichlet',
}


def analyze_diffop_matrix(
		N : int = 5, 
		num_N : int = 25, 
		gridsize : float = 1.0,
	) -> Dict[str, np.ndarray]:
	
	_h : Symbol = Symbol('h')
	output_eigvals : Dict[str, np.ndarray] = dict()
	for key,matfunc in MATRIX_DIFFOPS.items():
		bdry : BoundaryCondition = BDRY_CONDITIONS_FOR_DIFF_OPS[key]
		mat : Matrix = matfunc(N, _h, bdry)
		print(
			f" - difference operator ${key}$, for $N={N}$, width {bdry} boundary conditions:\n",
			"  $$ ",
			key,
			" = ",
			matrix_to_smallmatrix(latex(mat)),
			" $$",
		)

		print(f"   - eigenvalues of ${key}$:\n")
		eigvals : List[Expr] = set(sym.simplify(e) for e in mat.eigenvals().keys())
		print(
			"    $$ _{",
			latex(eigvals),
			"} $$",
		)
		
		# print(f"   - numerically computed eigenvalues for ${latex(_h)} = {gridsize}$ and $N = {num_N}$")
		mat_np : np.ndarray = np.array(matfunc(num_N, gridsize, bdry)).astype(np.float64)
		eigvals_np : np.ndarray = np.linalg.eigvals(mat_np)
		output_eigvals[key] = eigvals_np
	
	# plot eigenvalues
	for diff_order,diff_ops in MAT_DIFFOP_BYORDER.items():
		for diff_op in diff_ops:
			plt.plot(
				output_eigvals[diff_op].real,
				output_eigvals[diff_op].imag,
				MAT_DIFFOP_PLOT_FMT[diff_op],
				label = f"${diff_op}$",
			)
	
		# save image, and print markdown image link
		filename : str = f"py_img/diffop_eigvals_Ord-{diff_order}_N{N}_{num_N}_h{gridsize}.{EXPORT_FILE_EXTENSION}"
		plt.axes().set_aspect('equal')
		plt.legend()
		plt.savefig(filename)
		print(f"\n![Eigenvalues for {diff_order}{'st' if diff_order == 1 else 'nd'} order difference operators plotted in the complex plane]({filename})\n")
		plt.cla()
		plt.clf()

	return output_eigvals
		

def stability_plots(
		order : int,
		eigvals : Dict[str, np.ndarray],
		cfl_vals : List[float] = [0.5, 1.0, 3.0],
	) -> None:

	diff_ops_eqn : List[str] = list(MAT_DIFFOP_BYORDER[order])
	
	for cfl in cfl_vals:
		fig,ax = plot_stab_region(eigvals, cfl)
		ax.set_xlabel(f"$\\Re {latex(gamma)}$")
		ax.set_ylabel(f"$\\Im {latex(gamma)}$")

		for diffop in diff_ops_eqn:
			ax.plot(
				eigvals[diffop].real,
				eigvals[diffop].imag,
				MAT_DIFFOP_PLOT_FMT[diffop],
				label = f"Eigenvalues of ${diffop}$",
			)
		
		ax.set_title(f"$\\lambda = {cfl}$")
		
		filename : str = f"py_img/stabplot_Ord{order}_cfl_{cfl}.{EXPORT_FILE_EXTENSION}"
		ax.set_aspect('equal')
		fig.legend()
		fig.savefig(filename)
		print(f"\n![Stability plot for difference schemes with $\\lambda = {cfl}$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.]({filename})\n")

		stab_table : Dict[str, Dict[str, bool]] = gen_stab_table(eigvals, cfl, order)
		print(
			r"\begin{table}\begin{center}", "\n",
			doubledict_to_table(
				stab_table, 
				mapping = lambda x : 'Stable' if x else 'Unstable',
			),
			r"\end{center}", "\n",
			r"\caption{",
			f"Stability of schemes and difference operators for $\\lambda = {cfl}$",
			r"}", "\n",
			r"\end{table}",
		)



def main():
	print(r'# difference operator analysis', '\n')
	eigvals : Dict[str, np.ndarray] = analyze_diffop_matrix(N = 5, num_N = 25)
	print('\n')
	print(r'# equation $u_t = - u_x$', '\n')
	stability_eval(DIFF_FIRSTORDER)
	stability_plots(1, eigvals)
	print('\n')
	print(r'# equation $u_t = u_{xx}$', '\n')
	stability_eval(DIFF_SECONDORDER)
	stability_plots(2, eigvals)

if __name__ == '__main__':
	main()





