# Michael Ivanitskiy
# Fall 2021
# Math 550
# Homework 2


from typing import *
import sys
import os

import sympy as sym
from sympy import Matrix,latex,exp,Expr
import numpy as np
from nptyping import NDArray
import matplotlib.pyplot as plt
from pydbg import dbg

# sys.path.append('../')
# from util import *

EXPORT_FILE_EXTENSION : str = 'png'

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
  'periodic-naive', # fill in corners - but this is wrong!
  'dirichlet', # TODO
  None,
  # 'explicit', # provide explicit solution to use for endpoints (Callable)
  # 'neumann', # TODO
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
  # print('> ', s, *args, file = sys.stderr, **kwargs)
  pass

def dict_to_filename(
    data : Dict[str,float], 
    key_order : Optional[List[str]] = None,
    short_keys : Optional[int] = None,
    delim_pair : str = '_',
    delim_items : str = ',',
  ) -> str:
  """convert a dictionary to a filename
  
  format:
  `key_value,otherkey_otherval,morekey_-0.1`
  dont do this with long dicts, and dont use unsafe keys!
  if `short_keys` is true, trims each key to that many chars
  
  ### Parameters:
   - `data : Dict[str,float]`   
     dict to turn into a filename. if keys are dotlists, use the last element of the dotlist
   - `key_order : Optional[List[str]]`   
     if specfied, list the keys in this order
     (defaults to `None`)
   - `short_keys : Optional[int]`   
     if specified, shorten each key to this many chars
     (defaults to `None`)
  
  ### Returns:
   - `str` 
     string from the dict
  """

  if key_order is None:
    key_order = list(data.keys())

  output : List[str] = []

  for k in key_order:
    # shorten the keys by splitting by dot, 
    # and taking the first `short_keys` chars of the last bit
    if data[k] is not None:
      output.append(f'{k}{delim_pair}{data[k]:.3}')
  
  return delim_items.join(output)

def off_diag_mat(N : int, offset : int = 0, val : float = 1, bdry : BoundaryCondition = None) -> Matrix:
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
   - `bdry : BoundaryCondition`
      boundary condition to apply to the matrix. if dirichlet, assumed to be zero
      (defaults to `None`)
  
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
    zero_col : Matrix = sym.zeros(N, 1)

    if offset < 0:
      offset = abs(offset)

      output[offset:, :-offset] = submat

      if bdry is not None:
        if bdry == 'periodic':
          output[offset-1, -offset-1] = submat_per
        elif bdry == 'periodic-naive':
          output[:offset, -offset:] = submat_per
        elif bdry == 'dirichlet':
          output[offset-1, -offset-1] = submat_per
          output[:, 0] = zero_col
          output[:, -1] = zero_col
        else:
          raise ValueError(f'invalid boundary condition: {bdry}')

      return output

    elif offset > 0:
      output[:-offset,offset:] = submat

      if bdry is not None:
        if bdry == 'periodic':
          output[-offset, offset] = submat_per
        elif bdry == 'periodic-naive':
          output[-offset:, :offset] = submat_per
        elif bdry == 'dirichlet':
          output[offset-1, -offset-1] = submat_per
          output[:, 0] = zero_col
          output[:, -1] = zero_col
        else:
          raise ValueError(f'invalid boundary condition: {bdry}')


      return output

    else:
      raise ValueError(f'this is an innacessible state, smh. {N=} {offset=} {val=} {output=} {submat=}')

MATRIX_DIFFOPS : Dict[str, Callable[[int, float, BoundaryCondition], Matrix]] = {
  'D_0' : lambda N,h,bdry=None : (off_diag_mat(N, 1, 1, bdry) + off_diag_mat(N, -1, -1, bdry)) / (2 * h),
  'D_+' : lambda N,h,bdry=None : (off_diag_mat(N, 1, 1, bdry) + off_diag_mat(N, 0, -1, bdry)) / h,
  'D_-' : lambda N,h,bdry=None : (off_diag_mat(N, 0, 1, bdry) + off_diag_mat(N, -1, -1, bdry)) / h,
  # second order
  'D_- D_+' : lambda N,h,bdry=None : ( 
      off_diag_mat(N, -1, 1, bdry) - 2 * off_diag_mat(N, 0, 1, bdry) + off_diag_mat(N, 1, 1, bdry) 
    ) / (h**2),
  'D_+^2' : lambda N,h,bdry=None : ( 
    off_diag_mat(N, 2, 1, bdry) - 2 * off_diag_mat(N, 1, 1, bdry) + off_diag_mat(N, 0, 1, bdry) 
  ) / (h**2),
  'D_-^2' : lambda N,h,bdry=None : ( 
    off_diag_mat(N, 0, 1, bdry) - 2 * off_diag_mat(N, -1, 1, bdry) + off_diag_mat(N, -2, 1, bdry) 
  ) / (h**2),
  # 'D_+ D_-' : lambda N,h,bdry=None : ( 
  #     off_diag_mat(N, 1, 1, bdry) - 2 * off_diag_mat(N, 0, 1, bdry) + off_diag_mat(N, -1, 1, bdry) 
  #   ) / (h**2),
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
  
  bdry : BoundaryCondition = BC.type

  return (
    sym.eye(N)
    - theta * Delta_t * (
      - a * MATRIX_DIFFOPS['D_0'](N, h, bdry)
      + eta * MATRIX_DIFFOPS['D_- D_+'](N, h, bdry)
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

  bdry : BoundaryCondition = BC.type

  return (
    sym.eye(N)
    + (1 - theta) * Delta_t * (
      - a * MATRIX_DIFFOPS['D_0'](N, h, bdry)
      + eta * MATRIX_DIFFOPS['D_- D_+'](N, h, bdry)
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

def matrixprinter(name : str, expr : sym.Expr, factorout : Optional[Expr] = None) -> None:
  if factorout is not None:
    expr = sym.simplify(expr / factorout)
    print(f'{name}:\n$$ {latex(factorout)} {latex(expr)} $$\n'.replace(r'{matrix}', r'{smallmatrix}'))
  else:
    print(f'{name}:\n$$ {latex(expr)} $$\n'.replace(r'{matrix}', r'{smallmatrix}'))

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

  _h = kwdict['h']

  if not onlytheta:
    # print('**basics**\n')
    # matrixprinter('identity', off_diag_mat(N, 0, 1))
    # matrixprinter('positive off-diagonal', off_diag_mat(N, 1, 1, periodic = True))
    # matrixprinter('negative off_diagonal', off_diag_mat(N, -1, 1, periodic = True))

    print('**diff ops**\n')
    matrixprinter('$D_+$', MATRIX_DIFFOPS['D_+'](N,_h, bdry = 'periodic'), 1/_h)
    matrixprinter('$D_-$', MATRIX_DIFFOPS['D_-'](N,_h, bdry = 'periodic'), 1/_h)
    matrixprinter('$D_0$', MATRIX_DIFFOPS['D_0'](N,_h, bdry = 'periodic'), 2 * 1/_h)
    matrixprinter('$D_- D_+$', MATRIX_DIFFOPS['D_- D_+'](N,_h, bdry = 'periodic'), 1/_h**2)

  print('**theta eqn**\n')
  theta_factor_lhs : Expr = CONSTS['Delta_t'] * CONSTS['theta'] / (_h ** 2)
  theta_factor_rhs : Expr = CONSTS['Delta_t']
  if (kwdict['a'] == 1) and (kwdict['eta'] == 0):
    theta_factor_lhs = None
    theta_factor_rhs = None
  if (kwdict['a'] == 0) and (kwdict['eta'] == 1):
    theta_factor_lhs = CONSTS['Delta_t'] * CONSTS['theta']
    theta_factor_rhs = CONSTS['Delta_t']
  if (kwdict['a'] == 1) and (kwdict['eta'] == 1):
    theta_factor_lhs = CONSTS['Delta_t'] * CONSTS['theta']
    theta_factor_rhs = CONSTS['Delta_t']
    

  matrixprinter('theta scheme, LHS', theta_eqn_mat_LHS(N, **kwdict), theta_factor_lhs)
  matrixprinter('theta scheme, RHS', theta_eqn_mat_RHS(N, **kwdict), theta_factor_rhs)
  if inverse:
    matrixprinter('theta scheme', theta_scheme_eqn(N, **kwdict))


P3ii_CASES : List[Dict[str, Numerical]] = [
    { 'a': 1, 'eta': 0 },
    { 'a': 0, 'eta': 1 },
    { 'a': 1, 'eta': 1 },
  ]

def matrix_assembly_cases(N : int) -> None:
  for d in P3ii_CASES:
    header_str : str = ', \\ '.join([
      ('\\' if k=='eta' else '') + f'{k}={v}' 
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
    theta : float = 1.0,
    eta : float = 1.0,
    alpha : float = 1.0,
    n_gridpoints : int = 8,
    bounds : Tuple[float, float] = (0, np.pi),
    mat_generator : Optional[Callable[[int,Any], NDArray]] = theta_scheme_eqn,
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
  h : float = x_arr[1] - x_arr[0]
  dt : float = h
  if theta <= 0.5:
    dt = 0.1 * h**2.0 / abs(eta)

  # print(f'$$\\lambda = {cfl}, \\quad \\Delta_t = {dt}, \\quad \\Delta_x = {(x_arr[1] - x_arr[0])}$$')

  # init time arrays
  n_tsteps : int = int(t_final // dt) + 2
  t_arr : NDArray[n_tsteps, float] = np.linspace(0.0, t_final, n_tsteps, endpoint = True)
  Delta_t : float = t_arr[1] - t_arr[0]

  # get matrix
  scheme_mat_num : NDArray[n_gridpoints,n_gridpoints] = mat_generator(
    n_gridpoints, 
    h = h,
    eta = eta,
    a = alpha,
    theta = theta, 
    Delta_t = Delta_t,
    BC = BC,
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
    IC : Callable[[FloatArrayLike], FloatArrayLike] = lambda x: np.sin(x),
    BC : BCparam = BCparam('periodic', None),
    plot : Union[bool,str] = True,
    show : bool = False,
    print_table : bool = True,
    **scheme_kwargs,
  ):
  """run the solver for several grid sizes
  
  TODO: allow for different options of `a`, `eta`
  """

  print(
    f"{try_n_grids=}, {t_final=}, {alpha=}, {scheme_kwargs=}",
    file = sys.stderr,
  )

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

  if scheme_kwargs is None:
    scheme_kwargs = dict()

  for m,n_gridpoints in enumerate(try_n_grids):
    errprint(f'running with {n_gridpoints=}')
    x_arr,t_arr,v_grid = matrix_iter(
      t_final = t_final,
      n_gridpoints = n_gridpoints,
      bounds = bounds,
      mat_generator = mat_generator,
      IC = IC,
      BC = BC,
      **scheme_kwargs,
    )

    errprint(f'\trun finished, saving and plotting data')

    err[m] = np.linalg.norm(v_grid[-1] - exact_soln(t_final, x_arr)) / n_gridpoints

    if plot:
      plt.plot(x_arr, v_grid[-1], label = f'n = {n_gridpoints}')

  errprint(f'processing filename')
  fname_params_dict : Dict[str,float] = {
    'a' : alpha,
    'Tf' : t_final,
    'theta' : scheme_kwargs.get('theta', None),
    'eta' : scheme_kwargs.get('eta', None),
  }
  if isinstance(plot, bool):
    filename : str = (
      f'py_img/theta_scheme/{mat_generator.__name__}_'
      + f'{dict_to_filename(fname_params_dict)}.{EXPORT_FILE_EXTENSION}'
    )
  elif isinstance(plot, str):
    filename = str(plot)
  else:
    raise NotImplementedError(f'plot type {plot} : {type(plot)} not supported')
  

  if print_table:
    errprint(f'printing table')
    print('\n\n')
    print(
      f"## errors for $\\theta = {fname_params_dict['theta']:.2}$,",
      " $\\eta = {fname_params_dict['eta']:.2}$, $a = {alpha:.2}$, $T_f = {t_final:.3}$\n",
    )
    
    # print(r'\begin{figure}\begin{centering}')
    # print(f'\\includegraphics[width=0.5\\linewidth]{{{filename}}}\n')
    print(f"![]({filename}){{width=50%}}")

    print(r'\begin{tabular}{l|l}')
    print(f'$n$ gridpoints & error \\\\ \\hline')
    for n,e in zip(try_n_grids, err):
      print(f'{n} & {e:.4} \\\\')
    print(r'\end{tabular}')

    # print(
    #   r'\caption{',
    #   f"errors for $\\theta = {fname_params_dict['theta']:.2}$, $\\eta = \
    # {fname_params_dict['eta']:.2}$, $a = {alpha:.2}$, $T_f = {t_final:.3}$",
    #   r'}',
    # )
    # print(r'\end{centering}\end{figure}')

  if plot:
    errprint(f'final plotting')
    # plot the solutions
    plt.legend()
    if show:
      plt.show()
    plt.savefig(filename)
    plt.clf()
    plt.cla()

  return err


# lst_t_final : List[float] = [0.1, 0.5, 1.0, 2.0],
# lst_alpha : List[float] = [0.5, 1.0, 2.0],
# lst_theta : List[float] = [0.5, 1.0, 2.0],
# lst_eta : List[float] = [0.5, 1.0, 2.0],

def run_multi(
    lst_t_final : List[float] = [0.1, 0.5, 1.0],
    lst_alpha : List[float] = [0.0, 1.0,],
    lst_theta : List[float] = [0.5, 1.0, 2.0],
    lst_eta : List[float] = [0.0, 1.0],
    **kwargs,
  ):

  for alpha in lst_alpha:
    for theta in lst_theta:
      for eta in lst_eta:
        for t_final in lst_t_final:
          exact_soln = lambda t,x : np.exp(- eta * t) * np.sin(x - alpha * t)
          run(
            t_final = t_final,
            alpha = alpha,
            theta = theta,
            eta = eta,
            exact_soln = exact_soln,
            **kwargs,
          )




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
            plot = f'py_img/{scheme_name}_{ic_key}_a{alpha:.2}_Tf{t_final:.3}.{EXPORT_FILE_EXTENSION}',
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
        filename_log_errs : str = f'py_img/{scheme_name}_{ic_key}_a{alpha:.2}_log-errs.{EXPORT_FILE_EXTENSION}'
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



def symbolic_old():
  r"u(x,t) = \e^{ - t \eta} ( c_1 \e^{ - i (t a - x) } + c_{-1} \e^{ i (t a - x) } )"

  u : sym.Function = sym.Function('u')
  a, eta = sym.symbols('a eta')
  # the constants c_1, c_2 are \hat{u}_{1}(0), \hat{u}_{-1}(0) respectively
  c_1, c_m1 = sym.symbols(r'c_1 c_{-1}') 
  x, t = sym.symbols('x t')

  # the latex function above, expressed in sympy
  u_sym : Expr = exp(-t * eta) * (
    c_1 * exp(- sym.I * (t * a - x)) + c_m1 * exp(sym.I * (t * a - x))
  )

  print(latex(u_sym))

  print(latex(sym.simplify(u_sym)))


def eqnprint(eqn : Expr, **kwargs):
  return print(f"$$\n\t{latex(eqn, **kwargs)} \n$$\n", **kwargs)

def symbolic():
  u : sym.Function = sym.Function('u')
  a, eta = sym.symbols('a eta')
  x, t = sym.symbols('x t')

  # the original equation
  r"u_t + a u_x = \eta u_{xx}"
  u_eqn : Expr = u(x,t).diff(t) + a * u(x,t).diff(x) - eta * u(x,t).diff(x, x)

  # the explicit solution
  r"u(x,t) = \e^{-\eta t} \sin(x - a t)"
  u_soln : Expr = sym.exp(-eta * t) * sym.sin(x - a * t)

  solncheck = u_eqn.subs(u(x,t), u_soln)
  print(sym.simplify(solncheck))
  print(solncheck)
  eqnprint(solncheck)
  eqnprint(sym.simplify(solncheck))
  




if __name__ == '__main__':
  import fire
  fire.Fire({
    'demo' : lambda N : (
      test_matrix_assembly(N, onlytheta = False), 
      matrix_assembly_cases(N),
    ),
    'oldmain' : oldmain,
    'run' : run,
    'run_multi' : run_multi,
    'symbolic' : symbolic,
  })








