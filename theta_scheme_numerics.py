# Michael Ivanitskiy
# Fall 2021
# Math 550
# Homework 2


from typing import *
import sys
import os

import sympy as sym
from sympy import Matrix,latex
import numpy as np
from nptyping import NDArray
import matplotlib.pyplot as plt
from pydbg import dbg

# sys.path.append('../')
# from util import *

def raise_ValueError(msg : str) -> None:
  raise ValueError(msg)

def freeze_setitem(obj : object) -> None:
  """freezes an object's __setitem__ method
  
  ### Parameters:
   - `obj : object`   
     object to freeze
  """
  obj.__setitem__ = lambda self, key, value : raise_ValueError(f'setting values not allowed for {obj=}')

FloatArrayLike = Union[float, NDArray[float]]
Numerical = Union[float, int, sym.Symbol]

BoundaryCondition = Literal[
  'periodic', # set endpoints equal to each other (None)
  'explicit', # provide explicit solution to use for endpoints (Callable)
  'dirichlet', # TODO
  'neumann', # TODO
]

BCparam = NamedTuple('BCparam', [
  ('type', BoundaryCondition),
  ('func', Any),
])

CONSTS : Dict[str,sym.Symbol] = {
  'theta' : sym.Symbol('theta'),
  'a' : sym.Symbol('a'),
  'eta' : sym.Symbol('eta'),
  'Delta_t' : sym.Symbol('Delta_t'),
  'h' : sym.Symbol('h'),
}

def errprint(s : str, *args,**kwargs):
  print('> ', s, *args, file = sys.stderr, **kwargs)

def off_diag_mat(N : int, offset : int = 0, val : float = 1, periodic : bool = False) -> Matrix:
  """generates a square matrix with elements on an off-diagonal
  
  ### Parameters:
   - `N : int`   
     matrix dimension
   - `offset : int`   
      offset of diagonal elements (positive for above, negative for below)
     (defaults to `0`)
   - `val : float`   
     value of off-diagonal elements
     (defaults to `1`)
   - `periodic : bool`   
     whether to fill in the opposite corner of the matrix
     (defaults to `False`)
  
  ### Returns:
   - `Matrix` 
  
  ### Raises:
   - `ValueError` : invalid offset
  """
  if offset == 0:
    return val * sym.eye(N)

  else:
  
    output : Matrix = sym.zeros(N, N)
    submat : Matrix = val * sym.eye(N - abs(offset))
    submat_per : Matrix = val * sym.eye(abs(offset))

    if offset < 0:
      offset = abs(offset)

      output[offset:, :-offset] = submat

      if periodic:
        output[:offset, -offset:] = submat_per

      return output

    elif offset > 0:
      output[:-offset,offset:] = submat

      if periodic:
        output[-offset:, :offset] = submat_per

      return output

    else:
      raise ValueError(f'this is an innacessible state, smh. {N=} {offset=} {val=} {output=} {submat=}')

MATRIX_DIFFOPS : Dict[str, Callable[[int, float], Matrix]] = {
  '0' : lambda N,h,per=False : (off_diag_mat(N, 1, 1, per) + off_diag_mat(N, -1, -1, per)) / (2 * h),
  '+' : lambda N,h,per=False : (off_diag_mat(N, 1, 1, per) + off_diag_mat(N, 0, -1, per)) / h,
  '-' : lambda N,h,per=False : (off_diag_mat(N, 0, 1, per) + off_diag_mat(N, -1, -1, per)) / h,
}

def theta_eqn_mat_LHS(
    N : int,
    BC : BCparam = BCparam(type='periodic', func=None),
    theta : Numerical = CONSTS['theta'], 
    a : Numerical = CONSTS['a'],
    eta : Numerical = CONSTS['eta'],
    Delta_t : Numerical = CONSTS['Delta_t'],
    h : Numerical = CONSTS['h'],
  ) -> Matrix:
  """left hand side of the theta scheme
  
  $$ ( I - \Theta \Delta_t ( a D_0 + \eta D_+ D_- ) ) $$
  """
  
  per : bool =  BC.type == 'periodic'

  return (
    sym.eye(N)
    - theta * Delta_t * (
      a * MATRIX_DIFFOPS['0'](N, h, per)
      + eta * MATRIX_DIFFOPS['+'](N, h, per) * MATRIX_DIFFOPS['-'](N, h, per)
    )
  )

def theta_eqn_mat_RHS(
    N : int, 
    BC : BCparam = BCparam(type='periodic', func=None),
    theta : Numerical = CONSTS['theta'], 
    a : Numerical = CONSTS['a'],
    eta : Numerical = CONSTS['eta'],
    Delta_t : Numerical = CONSTS['Delta_t'],
    h : Numerical = CONSTS['h'],
  ) -> Matrix:
  """right hand side of the theta scheme

  $$ ( I + (1 - \Theta) \Delta_t ( a D_0 + \eta D_+ D_- ) ) $$
  """

  per : bool =  BC.type == 'periodic'

  return (
    sym.eye(N)
    + (1 - theta) * Delta_t * (
      a * MATRIX_DIFFOPS['0'](N, h, per)
      + eta * MATRIX_DIFFOPS['+'](N, h, per) * MATRIX_DIFFOPS['-'](N, h, per)
    )
  )

def theta_scheme_eqn(
    N : int, 
    use_ndarr : bool = False,
    **kwargs,
  ) -> Union[NDArray,Matrix]:
  """get the full transition matrix for the theta scheme

  NOTE: if `use_ndarr` is `False`, then inverting the matrix might take a loooong time
  
  ### Parameters:
   - `N : int`   
      matrix dimension
   - `use_ndarr : bool`   
      whether to return a numpy array or a sympy matrix
     (defaults to `False`)
  
  ### Returns:
   - `Union[NDArray,Matrix]` 
    `NDArray` if `use_ndarr` is `True`, otherwise `Matrix`
  
  ### Raises:
   - `ValueError` : [description]
  """

  LHS : Matrix = theta_eqn_mat_LHS(N, **kwargs)
  RHS : Matrix = theta_eqn_mat_RHS(N, **kwargs)

  if use_ndarr:
    if fsymb := set().union(
        LHS.free_symbols,
        RHS.free_symbols,
      ):
      raise ValueError(f'unexpected free symbols in operator matrix: {fsymb} \n{LHS=} \n{RHS=}')

    # errprint(f'matrices: \n{LHS=} \n{RHS=}')

    return np.linalg.inv(np.array(LHS.tolist()).astype(np.float64)) @ np.array(RHS.tolist()).astype(np.float64)
  else:
    return LHS.inv() * RHS


def testprinter(name : str, expr : sym.Expr) -> None:
  print(f'{name}:\n$$ {latex(expr)} $$\n')

def test_matrix_assembly(
    N : int, 
    onlytheta : bool = True,
    inverse : bool = False, 
    **kwargs,
  ) -> None:

  kwdict : Dict[str, Numerical] = {
    'theta' : CONSTS['theta'],
    'a' : CONSTS['a'],
    'eta' : CONSTS['eta'],
    'Delta_t' : CONSTS['Delta_t'],
    'h' : CONSTS['h'],
    **kwargs,
  }

  if not onlytheta:
    print('**basics**\n')
    testprinter('identity', off_diag_mat(N, 0, 1))
    testprinter('diag_moved_up', off_diag_mat(N, 1, 1, periodic = True))
    testprinter('diag_moved_down', off_diag_mat(N, -1, 1, periodic = True))

    print('**diff ops**\n')
    testprinter('D_+', MATRIX_DIFFOPS['+'](N, kwdict['h'], per = True))
    testprinter('D_-', MATRIX_DIFFOPS['-'](N, kwdict['h'], per = True))
    testprinter('central_diff', MATRIX_DIFFOPS['0'](N, kwdict['h'], per = True))

  print('**theta eqn**\n')
  testprinter('theta_eqn_LHS', theta_eqn_mat_LHS(N, **kwdict))
  testprinter('theta_eqn_RHS', theta_eqn_mat_RHS(N, **kwdict))
  if inverse:
    testprinter('theta scheme', theta_scheme_eqn(N, **kwdict))


P3ii_CASES : List[Dict[str, Numerical]] = [
    { 'a': 1, 'eta': 0 },
    { 'a': 0, 'eta': 1 },
    { 'a': 1, 'eta': 1 },
  ]

def matrix_assembly_cases(N : int) -> None:
  for d in P3ii_CASES:
    header_str : str = ', \\ '.join([
      '\\' + f'{k}={v}' 
      for k,v in d.items()
    ])
    print(f"### case: $" + header_str + "$")
    test_matrix_assembly(N, **d)



"""
#### ######## ######## ########
 ##     ##    ##       ##     ##
 ##     ##    ##       ##     ##
 ##     ##    ######   ########
 ##     ##    ##       ##   ##
 ##     ##    ##       ##    ##
####    ##    ######## ##     ##
"""

def matrix_iter(
    t_final : float = 1.0,
    # alpha : float = 1.0,
    n_gridpoints : int = 8,
    bounds : Tuple[float, float] = (0, np.pi),
    # dt : float = 0.005,
	  # cfl : float = .1,
    mat_generator : Optional[Callable[[int,Any], NDArray]] = theta_scheme_eqn,
    scheme_kwargs : Optional[Dict[str, Any]] = None,
    IC : Callable[[FloatArrayLike], FloatArrayLike] = lambda x: np.zeros_like(x),
    BC : BCparam = BCparam('periodic', None),
  ):

  errprint('\tinitializing matrix iteration')

  # init grid
  x_arr : NDArray[n_gridpoints, float] = np.linspace(
    bounds[0], bounds[1], 
    n_gridpoints,
  )

  # compute dt to make cfl correct
  # TODO: replace placeholder
  dt : float = (x_arr[1] - x_arr[0]) * 0.01
  h = x_arr[1] - x_arr[0]

  # print(f'$$\\lambda = {cfl}, \\quad \\Delta_t = {dt}, \\quad \\Delta_x = {(x_arr[1] - x_arr[0])}$$')

  # init time arrays
  n_tsteps : int = int(t_final // dt)
  t_arr : NDArray[n_tsteps, float] = np.linspace(0.0, t_final, n_tsteps)

  # get matrix
  # TODO: remove placeholder values
  if scheme_kwargs is None:
    scheme_kwargs = dict()

  scheme_mat_num : NDArray[n_gridpoints,n_gridpoints] = mat_generator(
    n_gridpoints, 
    h = h,
    eta = 0.01,
    a = 0.01,
    theta = 0.01, 
    Delta_t = 0.01,
    BC = BC,
    **scheme_kwargs,
    use_ndarr = True,
  )

  # set initial conditions
  v_init : NDArray[n_gridpoints, float] = IC(x_arr)

  v_grid : NDArray[[n_tsteps, n_gridpoints], float] = np.full(
    (n_tsteps, n_gridpoints),
    np.nan,
  )

  v_grid[0] = v_init


  errprint('\tperforming actual iteration...')

  # iterate forward in time 
  for _t_idx_m1,time in enumerate(t_arr[1:]):
    t_idx : int = _t_idx_m1 + 1

    # take approximation at all points except endpoints
    v_grid[t_idx] = scheme_mat_num @ v_grid[t_idx-1]


  return x_arr,t_arr,v_grid



"""
########  ##     ## ##    ##
##     ## ##     ## ###   ##
##     ## ##     ## ####  ##
########  ##     ## ## ## ##
##   ##   ##     ## ##  ####
##    ##  ##     ## ##   ###
##     ##  #######  ##    ##
"""

def run(
    try_n_grids : List[int] = [8,16,32], # [16,32,64,128]
    t_final : float = 1.0,
    alpha : float = 1.0,
    bounds : Tuple[float, float] = (0, np.pi),
    exact_soln : Callable[[float, FloatArrayLike], FloatArrayLike] = lambda t,x: np.zeros_like(x),
    mat_generator : Optional[Callable[[int,Any], Matrix]] = theta_scheme_eqn,
    scheme_kwargs : Optional[Dict[str, Any]] = None,
    IC : Callable[[FloatArrayLike], FloatArrayLike] = lambda x: np.zeros_like(x),
    BC : BCparam = BCparam('periodic', None),
    plot : Union[bool,str] = True,
    show : bool = False,
    print_table : bool = True,
    **iter_kwargs,
  ):
  """run the solver for several grid sizes
  
  TODO: allow for different options of `a`, `eta`
  """

  errprint('initializing')

  num_solvers : int = len(try_n_grids)

  err : NDArray[num_solvers, float] = np.full(num_solvers, np.nan, dtype = np.float64)

  if plot:
    errprint('setting up plot')
    plt.title(f'{mat_generator.__name__} for $a = {alpha:.2}$ and $T_f = {t_final:.3}$')
    x_arr_main : NDArray[try_n_grids[-1]*10, float] = np.linspace(
      bounds[0], bounds[1], 
      try_n_grids[-1]*10,
    )
    plt.plot(
      x_arr_main,
      exact_soln(t_final, x_arr_main),
      label = 'exact',
    )

  for m,n_gridpoints in enumerate(try_n_grids):
    errprint(f'running with {n_gridpoints=}')
    x_arr,t_arr,v_grid = matrix_iter(
      t_final = t_final,
      n_gridpoints = n_gridpoints,
      bounds = bounds,
      mat_generator = mat_generator,
      scheme_kwargs = scheme_kwargs,
      IC = IC,
      BC = BC,
    )

    errprint(f'\trun finished, saving and plotting data')

    err[m] = np.linalg.norm(v_grid[-1] - exact_soln(t_final, x_arr)) / n_gridpoints

    if plot:
      plt.plot(x_arr, v_grid[-1], label = f'n = {n_gridpoints}')

  errprint(f'processing filename')
  if isinstance(plot, bool):
    filename : str = f'py_img/{mat_generator.__name__}_a{alpha:.2}_Tf{t_final:.3}.eps'
  elif isinstance(plot, str):
    filename = str(plot)
  else:
    raise NotImplementedError(f'plot type {plot} : {type(plot)} not supported')
  

  if print_table:
    errprint(f'printing table')
    print('\n\n')
    print(f'## {mat_generator.__name__} errors for a = {alpha:.2} and T_f = {t_final:.3}\n')
    print(f'![]({filename}){{width=50%}}\n')

    print('\\begin{tabular}{l|l}')
    print(f'$n$ gridpoints & error \\\\ \\hline')
    for n,e in zip(try_n_grids, err):
      print(f'{n} & {e:.4} \\\\')
    print('\\end{tabular}')

  if plot:
    errprint(f'final plotting')
    os.mkdir('py_img', exist_ok = True)
    # plot the solutions
    plt.legend()
    if show:
      plt.show()
    plt.savefig(filename)
    plt.clf()
    plt.cla()

  return err



"""
##     ##    ###    #### ##    ##
###   ###   ## ##    ##  ###   ##
#### ####  ##   ##   ##  ####  ##
## ### ## ##     ##  ##  ## ## ##
##     ## #########  ##  ##  ####
##     ## ##     ##  ##  ##   ###
##     ## ##     ## #### ##    ##
"""

def oldmain():
  HEATMAPS : bool = False
  # variables for sweeping
  bounds : Tuple[float,float] = (-1.0, 1.0)
  alpha_vals : List[float] = [-1.0, 1.0]
  t_final_vals : List[float] = [0.5, 1.0, 2.5, 5.0]
  try_n_grids : List[int] = [8,16,32,64,128,256]
  ic_funcs_dict : Dict[
    str,
    Callable[[FloatArrayLike], FloatArrayLike],
  ] = {
    'smooth-eq2' : lambda x,_: np.sin(2 * np.pi * x),
    'bumps-eq3' : _eqn3_IC_vec,
  }

  print_table : bool = True

  # nested loops >:O
  for scheme_name in ['lax-wendroff']:
    for ic_key,ic_func in ic_funcs_dict.items():
      heatmap : NDArray[float] = np.full(
        (len(t_final_vals), len(alpha_vals)),
        np.nan,
      )
      for j,alpha in enumerate(alpha_vals):
        tf_errors : Dict[float,Any] = dict()
        for i,t_final in enumerate(t_final_vals):
          if not print_table:
            print(f'# scheme: {scheme_name},\tic: {ic_key},\tT: {t_final},\ta: {alpha}')
          # actually perform the iteration
          err = run(
            scheme_name = scheme_name,
            try_n_grids = try_n_grids,
            IC = ic_func,
            BC = BCparam('periodic', None),
            exact_soln = lambda t,x: ic_func(x - alpha * t, bounds),
            bounds = bounds,
            alpha = alpha,
            t_final = t_final,
            plot = f'py_img/{scheme_name}_{ic_key}_a{alpha:.2}_Tf{t_final:.3}.eps',
            print_table = print_table,
          )

          # log-log error plot
          
          tf_errors[t_final] = err
          heatmap[i,j] = err[-1]

        for tf,err in tf_errors.items():
          plt.plot(np.log10(try_n_grids), np.log10(err), 'o-', label = f'$T_f = ${tf}')
        plt.legend()
        plt.xlabel(r'$\log_{10} (N)$ gridpoints')
        plt.ylabel(r'$\log_{10} (e)$ error')
        filename_log_errs : str = f'py_img/{scheme_name}_{ic_key}_a{alpha:.2}_log-errs.eps'
        plt.savefig(filename_log_errs)
        plt.clf()
        plt.cla()
        print(f'\n\n![log-log error plot]({filename_log_errs})\n')

      # draw pretty pictures
      if HEATMAPS:
        # making the heatmap
        heatmap = np.log10(heatmap)
        plt.clf()
        plt.cla()
        fig, ax = plt.subplots()
        # plt.imshow(heatmap, interpolation = 'nearest')
        hm = ax.pcolor(heatmap, cmap=plt.cm.hot)
        plt.colorbar(hm)

        # We want to show all ticks...
        ax.set_xticks(np.arange(len(t_final_vals)))
        ax.set_yticks(np.arange(len(alpha_vals)))
        # ... and label them with the respective list entries
        ax.set_xticklabels(f'{s:.3}' for s in t_final_vals)
        ax.set_yticklabels(f'{s:.2}' for s in alpha_vals)
        ax.set_xlabel('T_final')
        ax.set_ylabel('alpha')
        ax.set_title(f'{scheme_name} log error')
        
        plt.show()




if __name__ == '__main__':
  import fire
  fire.Fire({
    'demo' : lambda N : (
      test_matrix_assembly(N, onlytheta = False), 
      matrix_assembly_cases(N),
    ),
    'oldmain' : oldmain,
    'run' : run,
  })








