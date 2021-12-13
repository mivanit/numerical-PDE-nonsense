
# Things to know (2021-12-13 14:16):
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
  - CFL is the numerical wavespeed
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









