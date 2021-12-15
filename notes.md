
# Lab Things to know (2021-12-13 14:16):

## Lab 1

- Norms
- order of accuracy: 
	$$
		E_{order} = \frac{
			\log \left( \frac{e_{old}}{ e_{new} } \right)
		}{
			\log \left( \frac{N_{new}}{N_{old}} \right)
		}
	$$
- Fourier series


## Lab 2

- Fourier series
- assumptions required for Fourier expansion
  - $C_1$ piecewise 
    - continuous in the first derivative, piecewise
    - finitely many discontinuities over the interval
  - $L_2$ (square integrable)
    - if $C_1$ piecewise, that is a stricted condition than $L_2$
  - periodic
- Bessel's equality
	- sum of the square of the Fourier coefficients is the norm
- $\ell_2$ error - $\Vert\cdot\Vert_2$ of the difference


## Lab 3

- difference operators $D_0, D_-, D_+$
- general central divided differences formula
	$$
		D_0^k f(x) = (2h)^{-k} 
		\sum_{j \in \mathbb{N}_k }
		(-1)^j \binom{k}{j}
		f( x + (k - 2j) h)
		\qquad
		\forall \ k \in \mathbb{Z}_{\geq 0} 
	$$


## Lab 4

- CFL
  - CFL is the ratio of exact wavespeed over numerical wavespeed
- amplification factor $Q$
  - plug Fourier modes into scheme
  - $Q$ has the CFL baked into it
- determining bounds on the CFL
  - $|Q| \leq 1$ gives condition on CFL
  - if $|Q| = 1$, then conserving energy
- energy analysis
  - **probably will be on exam**
  - usually defined with $2$-norm
  - take the derivative, work through until you get the boundary terms
  - put inside the governing equation??
  - energy conserving means derivative of energy will be 0

> energy analysis example for $u_t + a u_x = 0$
> $$ u \cdot u_t = - a \cdot u_x \cdot u $$
> $$ \frac{d u^2}{dt} = 2 u \cdot u_t $$
> $$ \frac{1}{2} \int_\Omega \frac{d|u|^2}{dt} d x $$



## Lab 5

- dissapative, dispersive, diffusive errors
  - use modified equation
    - take scheme and taylor expand everything
    - take governing equation and shove it to the left, everything else on the right
    - what's left on the right is truncation error 
      - truncation error is before you take $\Delta_x$, $\Delta_t$ to $\lambda$
    - to get to the modified equation, put all the $\Delta_t$ in terms of $\lambda$ using the CFL definition (depends on eqn)
    - then, use the governing equation to replace all time derivs with spatial ones (everything in terms of $\Delta_x$) **this is the modified equation**

- look at leading error term in terms of $\Delta_x$, look at order of spatial derivatives
  - if you have even derivatives, error is dissapative (melting)
  - odd derivatives, dispersive (waves shifting)
  - both is diffusive

- she may ask us to look at a plot and say things about the plot
  - for example, what is the error?
  - shifts means dispersive
  - decays means dissapative
  - both means diffusive

- taking a second order and splitting it up into a system
- decoupling a system
  - looking for the eigen modes?
  - define 2 variables: $u$ which you solve for, and $v$ defined by $v_t = u_x$
  - @joel upload notes


## Lab 6

- implicit schemes
  - make matrix operators, take the inverse
  $$
	A u^{n+1} = B u^n
	\qquad\implies\qquad
	u^{n+1} = A^{-1} B u^n	   
  $$

- amplification factor (matrix) for multiple timestep schemes (leapfrog)
  - see equation 5
  - want to keep the vector $\left[ \begin{smallmatrix} \hat{u}^{n+1} \\ \hat{u}^n \end{smallmatrix} \right]$ to have norm constant or decreasing
  - do this by making sure the matrix is a contracting map (eigenvals bounded by 1 in magnitude)


## Lab 7 

stability regions `:(`

- temporal stability plot:
  - form the differential equation $\frac{\partial v}{\partial t} = \gamma \cdot v$
  - approximate the time derivative using the time deriv approx from the scheme
  - find where the solution is stable or decays in time (be constant or go to zero, we dont want it to blow up)
    - either solve the scheme explicitly, or use the amplification factor type argument
  - set $\gamma = 1$, plot $\Delta_t$ in the complex plane

- spatial stability plot
  - take the spatial discretization that we have in the scheme and build a matrix out of it
  - inside of that matrix, set $\Delta_x, \Delta_y = 1$
  - determine $\Delta_t$ from the CFL condition (will have to try multiple)
  - compute the eigenvalues for some number of gridpoints $N$ and plot them on top of the temporal stability (dots)
  - if you have multiple time levels on top of the scheme:
  	- **good luck**
  	- block matrix system?????????




## Lab 8

how to make a first order system out of a second order equation (example is wave equation)

- set
	$$v = u_t, \qquad w = u_x$$
	> note: this works for second order linear, but idk about others

- substitute one of $v,w$ into the governing equation 
- other one is the "compatibility condition"
  - Lax pairs? $v_x = w_t$ (not important)
- take those two equations and shove them into the linear system
- $$\vec{v}_t = A \vec{v}_x$$
- $$ \vec{v} = \begin{bmatrix} v \\ w \end{bmatrix} $$
- take the eigenvals, eigenvects of $A$
- ????
- look at the lab, it explains things


## Lab 9

block matrices? idk its hard


when you have a 2D system, you get block matrices when you discretize it


## Lab 10, Lab 11

spectral stuff, not on exam!



# Homeworks 2021-12-13 16:47

- taylor expand
- temportal as spatial
- drawing stencil
- truncation errors
- modified equation

> **Note:** "using Fourier analysis" or "taking a Fourier transform" just means plug in a Fourier mode


## Well-posedness (hw2)

3 conditions:

- existence
- uniqueness
- varies continuously with initial condition
  - bound on the Fourier mode
  - $$ \Vert u(x,t) \Vert_2 \leq A e^{at} \Vert u(x,0) \Vert_2 $$


### idk what this part is
need to restrict the coefficient of the highest order even derivative
 - consider the case when that is zero?
   - go to the next highest order?


# Debugging

- CFL:
  - funny oscillations (Gibbs phenomena)
  - if you take $\Delta_t$, it should work (this removes the CFL as a problem)
    - if setting $\Delta_t$ to be small fixes the problem, then the issue is with the CFL
    - if setting it to be small does **not** fix the problem, then the issue is with the method

- Boundary conditions
  - if the solution is seeming to "leak" out, then there might be an issue with the boundary conditions
  - if it looks fine in the middle, but not on the edges, also check BCs

- Initial conditions:
  - evolve a really small amount, see if it works
  - if wrong in early timestep, then probably an IC issue


- check indexing





# Exam

## CFL:

- ratio of exact wavespeed to numerical wavespeed
- if greater than one, then the method is unstable (usually..,)


## Lax-Richmeyer equivalence theorem

- stability:
  - $$ |Q|^{n+1} \leq K(T_f) \qquad \text{as} \qquad \sup_n,  \quad \lim_{\Delta_t, \Delta_x \to 0} $$

- consistency:
  $\lim_{\Delta_t, \Delta_x \to 0}$ of modified equation is the actual equation (truncation error goes to zero)

- converges:
  $\lim_{\Delta_t, \Delta_x \to 0}$ of the grid function, is the actual function (pointwise)

**theorem:**
A linear scheme that is both *consistent* and *stable* converges.









