# difference operator analysis 

 - difference operator $D_0$, for $N=5$, width periodic boundary conditions:
   $$  D_0  =  \left[\begin{smallmatrix}0 & \frac{1}{2 h} & 0 & - \frac{1}{2 h} & 0\\- \frac{1}{2 h} & 0 & \frac{1}{2 h} & 0 & 0\\0 & - \frac{1}{2 h} & 0 & \frac{1}{2 h} & 0\\0 & 0 & - \frac{1}{2 h} & 0 & \frac{1}{2 h}\\0 & \frac{1}{2 h} & 0 & - \frac{1}{2 h} & 0\end{smallmatrix}\right]  $$
   - eigenvalues of $D_0$:

    $$ _{ \left\{0, - \frac{i}{h}, \frac{i}{h}\right\} } $$
 - difference operator $D_+$, for $N=5$, width periodic boundary conditions:
   $$  D_+  =  \left[\begin{smallmatrix}- \frac{1}{h} & \frac{1}{h} & 0 & 0 & 0\\0 & - \frac{1}{h} & \frac{1}{h} & 0 & 0\\0 & 0 & - \frac{1}{h} & \frac{1}{h} & 0\\0 & 0 & 0 & - \frac{1}{h} & \frac{1}{h}\\0 & \frac{1}{h} & 0 & 0 & - \frac{1}{h}\end{smallmatrix}\right]  $$
   - eigenvalues of $D_+$:

    $$ _{ \left\{0, - \frac{2}{h}, - \frac{1}{h}, \frac{-1 + i}{h}, - \frac{1 + i}{h}\right\} } $$
 - difference operator $D_-$, for $N=5$, width periodic boundary conditions:
   $$  D_-  =  \left[\begin{smallmatrix}\frac{1}{h} & 0 & 0 & - \frac{1}{h} & 0\\- \frac{1}{h} & \frac{1}{h} & 0 & 0 & 0\\0 & - \frac{1}{h} & \frac{1}{h} & 0 & 0\\0 & 0 & - \frac{1}{h} & \frac{1}{h} & 0\\0 & 0 & 0 & - \frac{1}{h} & \frac{1}{h}\end{smallmatrix}\right]  $$
   - eigenvalues of $D_-$:

    $$ _{ \left\{0, \frac{1}{h}, \frac{2}{h}, \frac{1 - i}{h}, \frac{1 + i}{h}\right\} } $$
 - difference operator $D_- D_+$, for $N=5$, width dirichlet boundary conditions:
   $$  D_- D_+  =  \left[\begin{smallmatrix}- \frac{2}{h^{2}} & \frac{1}{h^{2}} & 0 & \frac{2}{h^{2}} & 0\\0 & - \frac{2}{h^{2}} & \frac{1}{h^{2}} & 0 & 0\\0 & \frac{1}{h^{2}} & - \frac{2}{h^{2}} & \frac{1}{h^{2}} & 0\\0 & 0 & \frac{1}{h^{2}} & - \frac{2}{h^{2}} & 0\\0 & 0 & 0 & \frac{1}{h^{2}} & - \frac{2}{h^{2}}\end{smallmatrix}\right]  $$
   - eigenvalues of $D_- D_+$:

    $$ _{ \left\{- \frac{2}{h^{2}}, \frac{-2 + \sqrt{2}}{h^{2}}, - \frac{\sqrt{2} + 2}{h^{2}}\right\} } $$
 - difference operator $D_+^2$, for $N=5$, width dirichlet boundary conditions:
   $$  D_+^2  =  \left[\begin{smallmatrix}\frac{1}{h^{2}} & - \frac{2}{h^{2}} & \frac{1}{h^{2}} & - \frac{2}{h^{2}} & 0\\0 & \frac{1}{h^{2}} & - \frac{1}{h^{2}} & 0 & 0\\0 & 0 & \frac{1}{h^{2}} & - \frac{1}{h^{2}} & 0\\0 & 0 & 0 & \frac{1}{h^{2}} & 0\\0 & 0 & 0 & 0 & \frac{1}{h^{2}}\end{smallmatrix}\right]  $$
   - eigenvalues of $D_+^2$:

    $$ _{ \left\{\frac{1}{h^{2}}\right\} } $$
 - difference operator $D_-^2$, for $N=5$, width dirichlet boundary conditions:
   $$  D_-^2  =  \left[\begin{smallmatrix}\frac{1}{h^{2}} & 0 & 0 & - \frac{2}{h^{2}} & 0\\0 & \frac{1}{h^{2}} & \frac{1}{h^{2}} & 0 & 0\\0 & - \frac{2}{h^{2}} & \frac{1}{h^{2}} & \frac{1}{h^{2}} & 0\\0 & \frac{1}{h^{2}} & - \frac{2}{h^{2}} & \frac{1}{h^{2}} & 0\\0 & 0 & \frac{1}{h^{2}} & - \frac{2}{h^{2}} & \frac{1}{h^{2}}\end{smallmatrix}\right]  $$
   - eigenvalues of $D_-^2$:

    $$ _{ \left\{\frac{1}{h^{2}}, \frac{\frac{8 \sqrt[3]{18}}{3} + \frac{\left(1 - \sqrt{3} i\right) \sqrt[3]{9 + \sqrt{849}} \left(12 + \left(-1 + \sqrt{3} i\right) \sqrt[3]{108 + 12 \sqrt{849}}\right)}{12}}{h^{2} \left(1 - \sqrt{3} i\right) \sqrt[3]{9 + \sqrt{849}}}, \frac{\frac{8 \sqrt[3]{18}}{3} - \frac{\left(-12 + \left(1 + \sqrt{3} i\right) \sqrt[3]{108 + 12 \sqrt{849}}\right) \left(1 + \sqrt{3} i\right) \sqrt[3]{9 + \sqrt{849}}}{12}}{h^{2} \left(1 + \sqrt{3} i\right) \sqrt[3]{9 + \sqrt{849}}}, - \frac{4 \sqrt[3]{18}}{3 h^{2} \sqrt[3]{9 + \sqrt{849}}} + \frac{1}{h^{2}} + \frac{\sqrt[3]{108 + 12 \sqrt{849}}}{6 h^{2}}\right\} } $$

![Eigenvalues for 1st order difference operators plotted in the complex plane](py_img/diffop_eigvals_Ord-1_N5_25_h1.0.png)


![Eigenvalues for 2nd order difference operators plotted in the complex plane](py_img/diffop_eigvals_Ord-2_N5_25_h1.0.png)



# equation $u_t = - u_x$ 

 - space discretization with operator $D_0$, solving for $\left[ {u}_{i + 1}, \  {u}_{i}, \  {u}_{i - 1}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{{u}_{i + 1} - {u}_{i - 1}}{2 \Delta_{x}}  =  0  $$
   - solving for next timestep
      $$  2 \Delta_{x} \gamma {u}_{i} + {u}_{i - 1}  =  {u}_{i + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i + 1}\\{u}_{i}\end{matrix}\right]  =  \left[\begin{matrix}2 \Delta_{x} \gamma & 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i}\\{u}_{i - 1}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{x} \gamma - \sqrt{\Delta_{x}^{2} \gamma^{2} + 1}}\right|\leq 1\qquad\left|{\Delta_{x} \gamma + \sqrt{\Delta_{x}^{2} \gamma^{2} + 1}}\right|\leq 1  $$
    - substituting $\Delta_{x} = 1$
     $$  \left|{\gamma - \sqrt{\gamma^{2} + 1}}\right|\leq 1\qquad\left|{\gamma + \sqrt{\gamma^{2} + 1}}\right|\leq 1  $$


 - space discretization with operator $D_+$, solving for $\left[ {u}_{i + 1}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{{u}_{i + 1} - {u}_{i}}{\Delta_{x}}  =  0  $$
   - solving for next timestep
      $$  \left(\Delta_{x} \gamma + 1\right) {u}_{i}  =  {u}_{i + 1}  $$
   - condition on $\gamma$
      $$  \left|{\Delta_{x} \gamma + 1}\right|  \leq  1  $$


 - space discretization with operator $D_-$, solving for $\left[ {u}_{i}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{- {u}_{i - 1} + {u}_{i}}{\Delta_{x}}  =  0  $$
   - solving for next timestep
      $$  - \frac{{u}_{i - 1}}{\Delta_{x} \gamma - 1}  =  {u}_{i}  $$
   - condition on $\gamma$
      $$  \frac{1}{\left|{\Delta_{x} \gamma - 1}\right|}  \leq  1  $$


 - time discretization with operator $D_0$, solving for $\left[ {u}_{n + 1}, \  {u}_{n}, \  {u}_{n - 1}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{{u}_{n + 1} - {u}_{n - 1}}{2 \Delta_{t}}  =  0  $$
   - solving for next timestep
      $$  2 \Delta_{t} \gamma {u}_{n} + {u}_{n - 1}  =  {u}_{n + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n + 1}\\{u}_{n}\end{matrix}\right]  =  \left[\begin{matrix}2 \Delta_{t} \gamma & 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n}\\{u}_{n - 1}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{t} \gamma - \sqrt{\Delta_{t}^{2} \gamma^{2} + 1}}\right|\leq 1\qquad\left|{\Delta_{t} \gamma + \sqrt{\Delta_{t}^{2} \gamma^{2} + 1}}\right|\leq 1  $$
    - substituting $\Delta_{t} = 1$
     $$  \left|{\gamma - \sqrt{\gamma^{2} + 1}}\right|\leq 1\qquad\left|{\gamma + \sqrt{\gamma^{2} + 1}}\right|\leq 1  $$


 - time discretization with operator $D_+$, solving for $\left[ {u}_{n + 1}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{{u}_{n + 1} - {u}_{n}}{\Delta_{t}}  =  0  $$
   - solving for next timestep
      $$  \left(\Delta_{t} \gamma + 1\right) {u}_{n}  =  {u}_{n + 1}  $$
   - condition on $\gamma$
      $$  \left|{\Delta_{t} \gamma + 1}\right|  \leq  1  $$


 - time discretization with operator $D_-$, solving for $\left[ {u}_{n}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{- {u}_{n - 1} + {u}_{n}}{\Delta_{t}}  =  0  $$
   - solving for next timestep
      $$  - \frac{{u}_{n - 1}}{\Delta_{t} \gamma - 1}  =  {u}_{n}  $$
   - condition on $\gamma$
      $$  \frac{1}{\left|{\Delta_{t} \gamma - 1}\right|}  \leq  1  $$



![Stability plot for difference schemes with $\lambda = 0.5$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.](py_img/stabplot_Ord1_cfl_0.5.png)

\begin{table}\begin{center} 
 \begin{tabular}{c|c|c|c}
  & $D_0$ & $D_+$ & $D_-$\\ 
\hline
Central Difference & Stable & Unstable & Unstable\\ 
Forward Euler & Unstable & Unstable & Unstable\\ 
Backward Euler & Stable & Stable & Unstable\\ 
\end{tabular}
 \end{center} 
 \caption{ Stability of schemes and difference operators for $\lambda = 0.5$ } 
 \end{table}

![Stability plot for difference schemes with $\lambda = 1.0$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.](py_img/stabplot_Ord1_cfl_1.0.png)

\begin{table}\begin{center} 
 \begin{tabular}{c|c|c|c}
  & $D_0$ & $D_+$ & $D_-$\\ 
\hline
Central Difference & Unstable & Unstable & Unstable\\ 
Forward Euler & Unstable & Unstable & Unstable\\ 
Backward Euler & Stable & Stable & Unstable\\ 
\end{tabular}
 \end{center} 
 \caption{ Stability of schemes and difference operators for $\lambda = 1.0$ } 
 \end{table}

![Stability plot for difference schemes with $\lambda = 3.0$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.](py_img/stabplot_Ord1_cfl_3.0.png)

\begin{table}\begin{center} 
 \begin{tabular}{c|c|c|c}
  & $D_0$ & $D_+$ & $D_-$\\ 
\hline
Central Difference & Unstable & Unstable & Unstable\\ 
Forward Euler & Unstable & Unstable & Unstable\\ 
Backward Euler & Stable & Stable & Stable\\ 
\end{tabular}
 \end{center} 
 \caption{ Stability of schemes and difference operators for $\lambda = 3.0$ } 
 \end{table}


# equation $u_t = u_{xx}$ 

 - space discretization with operator $D_- D_+$, solving for $\left[ {u}_{i + 1}, \  {u}_{i}, \  {u}_{i - 1}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{{u}_{i + 1} + {u}_{i - 1} - 2 {u}_{i}}{\Delta_{x}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{x}^{2} \gamma {u}_{i} - {u}_{i - 1} + 2 {u}_{i}  =  {u}_{i + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i + 1}\\{u}_{i}\end{matrix}\right]  =  \left[\begin{matrix}\Delta_{x}^{2} \gamma + 2 & -1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i}\\{u}_{i - 1}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{x}^{2} \gamma}{2} - \frac{\Delta_{x} \sqrt{\gamma \left(\Delta_{x}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1\qquad\left|{\frac{\Delta_{x}^{2} \gamma}{2} + \frac{\Delta_{x} \sqrt{\gamma \left(\Delta_{x}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1  $$
    - substituting $\Delta_{x} = 1$
     $$  \left|{\frac{\gamma}{2} - \frac{\sqrt{\gamma \left(\gamma + 4\right)}}{2} + 1}\right|\leq 1\qquad\left|{\frac{\gamma}{2} + \frac{\sqrt{\gamma \left(\gamma + 4\right)}}{2} + 1}\right|\leq 1  $$


 - space discretization with operator $D_+^2$, solving for $\left[ {u}_{i + 2}, \  {u}_{i + 1}, \  {u}_{i}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{- 2 {u}_{i + 1} + {u}_{i + 2} + {u}_{i}}{\Delta_{x}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{x}^{2} \gamma {u}_{i} + 2 {u}_{i + 1} - {u}_{i}  =  {u}_{i + 2}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i + 2}\\{u}_{i + 1}\end{matrix}\right]  =  \left[\begin{matrix}2 & \Delta_{x}^{2} \gamma - 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i + 1}\\{u}_{i}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{x} \sqrt{\gamma} - 1}\right|\leq 1\qquad\left|{\Delta_{x} \sqrt{\gamma} + 1}\right|\leq 1  $$
    - substituting $\Delta_{x} = 1$
     $$  \left|{\sqrt{\gamma} - 1}\right|\leq 1\qquad\left|{\sqrt{\gamma} + 1}\right|\leq 1  $$


 - space discretization with operator $D_-^2$, solving for $\left[ {u}_{i}, \  {u}_{i - 1}, \  {u}_{i - 2}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{- 2 {u}_{i - 1} + {u}_{i - 2} + {u}_{i}}{\Delta_{x}^{2}}  =  0  $$
   - solving for next timestep
      $$  \frac{- 2 {u}_{i - 1} + {u}_{i - 2}}{\Delta_{x}^{2} \gamma - 1}  =  {u}_{i}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i}\\{u}_{i - 1}\end{matrix}\right]  =  \left[\begin{matrix}- \frac{2}{\Delta_{x}^{2} \gamma - 1} & \frac{1}{\Delta_{x}^{2} \gamma - 1}\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i - 1}\\{u}_{i - 2}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{x} \sqrt{\gamma}}{\Delta_{x}^{2} \gamma - 1} + \frac{1}{\Delta_{x}^{2} \gamma - 1}}\right|\leq 1\qquad\left|{\frac{\Delta_{x} \sqrt{\gamma}}{\Delta_{x}^{2} \gamma - 1} - \frac{1}{\Delta_{x}^{2} \gamma - 1}}\right|\leq 1  $$
    - substituting $\Delta_{x} = 1$
     $$  \left|{\frac{\sqrt{\gamma} + 1}{\gamma - 1}}\right|\leq 1\qquad\left|{\frac{\sqrt{\gamma} - 1}{\gamma - 1}}\right|\leq 1  $$


 - time discretization with operator $D_- D_+$, solving for $\left[ {u}_{n + 1}, \  {u}_{n}, \  {u}_{n - 1}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{{u}_{n + 1} + {u}_{n - 1} - 2 {u}_{n}}{\Delta_{t}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{t}^{2} \gamma {u}_{n} - {u}_{n - 1} + 2 {u}_{n}  =  {u}_{n + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n + 1}\\{u}_{n}\end{matrix}\right]  =  \left[\begin{matrix}\Delta_{t}^{2} \gamma + 2 & -1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n}\\{u}_{n - 1}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{t}^{2} \gamma}{2} - \frac{\Delta_{t} \sqrt{\gamma \left(\Delta_{t}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1\qquad\left|{\frac{\Delta_{t}^{2} \gamma}{2} + \frac{\Delta_{t} \sqrt{\gamma \left(\Delta_{t}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1  $$
    - substituting $\Delta_{t} = 1$
     $$  \left|{\frac{\gamma}{2} - \frac{\sqrt{\gamma \left(\gamma + 4\right)}}{2} + 1}\right|\leq 1\qquad\left|{\frac{\gamma}{2} + \frac{\sqrt{\gamma \left(\gamma + 4\right)}}{2} + 1}\right|\leq 1  $$


 - time discretization with operator $D_+^2$, solving for $\left[ {u}_{n + 2}, \  {u}_{n + 1}, \  {u}_{n}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{- 2 {u}_{n + 1} + {u}_{n + 2} + {u}_{n}}{\Delta_{t}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{t}^{2} \gamma {u}_{n} + 2 {u}_{n + 1} - {u}_{n}  =  {u}_{n + 2}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n + 2}\\{u}_{n + 1}\end{matrix}\right]  =  \left[\begin{matrix}2 & \Delta_{t}^{2} \gamma - 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n + 1}\\{u}_{n}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{t} \sqrt{\gamma} - 1}\right|\leq 1\qquad\left|{\Delta_{t} \sqrt{\gamma} + 1}\right|\leq 1  $$
    - substituting $\Delta_{t} = 1$
     $$  \left|{\sqrt{\gamma} - 1}\right|\leq 1\qquad\left|{\sqrt{\gamma} + 1}\right|\leq 1  $$


 - time discretization with operator $D_-^2$, solving for $\left[ {u}_{n}, \  {u}_{n - 1}, \  {u}_{n - 2}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{- 2 {u}_{n - 1} + {u}_{n - 2} + {u}_{n}}{\Delta_{t}^{2}}  =  0  $$
   - solving for next timestep
      $$  \frac{- 2 {u}_{n - 1} + {u}_{n - 2}}{\Delta_{t}^{2} \gamma - 1}  =  {u}_{n}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n}\\{u}_{n - 1}\end{matrix}\right]  =  \left[\begin{matrix}- \frac{2}{\Delta_{t}^{2} \gamma - 1} & \frac{1}{\Delta_{t}^{2} \gamma - 1}\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n - 1}\\{u}_{n - 2}\end{matrix}\right]  $$
    - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{t} \sqrt{\gamma}}{\Delta_{t}^{2} \gamma - 1} + \frac{1}{\Delta_{t}^{2} \gamma - 1}}\right|\leq 1\qquad\left|{\frac{\Delta_{t} \sqrt{\gamma}}{\Delta_{t}^{2} \gamma - 1} - \frac{1}{\Delta_{t}^{2} \gamma - 1}}\right|\leq 1  $$
    - substituting $\Delta_{t} = 1$
     $$  \left|{\frac{\sqrt{\gamma} + 1}{\gamma - 1}}\right|\leq 1\qquad\left|{\frac{\sqrt{\gamma} - 1}{\gamma - 1}}\right|\leq 1  $$



![Stability plot for difference schemes with $\lambda = 0.5$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.](py_img/stabplot_Ord2_cfl_0.5.png)

\begin{table}\begin{center} 
 \begin{tabular}{c|c|c|c}
  & $D_-^2$ & $D_- D_+$ & $D_+^2$\\ 
\hline
Central Difference & Unstable & Unstable & Stable\\ 
Forward Euler & Unstable & Stable & Stable\\ 
Backward Euler & Unstable & Stable & Stable\\ 
\end{tabular}
 \end{center} 
 \caption{ Stability of schemes and difference operators for $\lambda = 0.5$ } 
 \end{table}

![Stability plot for difference schemes with $\lambda = 1.0$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.](py_img/stabplot_Ord2_cfl_1.0.png)

\begin{table}\begin{center} 
 \begin{tabular}{c|c|c|c}
  & $D_-^2$ & $D_- D_+$ & $D_+^2$\\ 
\hline
Central Difference & Unstable & Unstable & Stable\\ 
Forward Euler & Unstable & Unstable & Stable\\ 
Backward Euler & Stable & Stable & Stable\\ 
\end{tabular}
 \end{center} 
 \caption{ Stability of schemes and difference operators for $\lambda = 1.0$ } 
 \end{table}

![Stability plot for difference schemes with $\lambda = 3.0$. Note that for Forward Euler, the stability region is shaded, while it is the region of instability that is shaded for Backward Euler.](py_img/stabplot_Ord2_cfl_3.0.png)

\begin{table}\begin{center} 
 \begin{tabular}{c|c|c|c}
  & $D_-^2$ & $D_- D_+$ & $D_+^2$\\ 
\hline
Central Difference & Unstable & Unstable & Stable\\ 
Forward Euler & Unstable & Unstable & Stable\\ 
Backward Euler & Stable & Stable & Stable\\ 
\end{tabular}
 \end{center} 
 \caption{ Stability of schemes and difference operators for $\lambda = 3.0$ } 
 \end{table}
