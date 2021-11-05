## equation $u_t = - u_x$ 

 - space discretization with operator $D_0$, solving for $\left[ {u}_{i + 1}, \  {u}_{i}, \  {u}_{i - 1}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{{u}_{i + 1} - {u}_{i - 1}}{2 \Delta_{x}}  =  0  $$
   - solving for next timestep
      $$  2 \Delta_{x} \gamma {u}_{i} + {u}_{i - 1}  =  {u}_{i + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i + 1}\\{u}_{i}\end{matrix}\right]  =  \left[\begin{matrix}2 \Delta_{x} \gamma & 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i}\\{u}_{i - 1}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{x} \gamma - \sqrt{\Delta_{x}^{2} \gamma^{2} + 1}}\right|\leq 1\qquad\left|{\Delta_{x} \gamma + \sqrt{\Delta_{x}^{2} \gamma^{2} + 1}}\right|\leq 1  $$


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


## equation $u_t = u_{xx}$ 

 - space discretization with operator $D_- D_+$, solving for $\left[ {u}_{i + 1}, \  {u}_{i}, \  {u}_{i - 1}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{{u}_{i + 1} + {u}_{i - 1} - 2 {u}_{i}}{\Delta_{x}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{x}^{2} \gamma {u}_{i} - {u}_{i - 1} + 2 {u}_{i}  =  {u}_{i + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i + 1}\\{u}_{i}\end{matrix}\right]  =  \left[\begin{matrix}\Delta_{x}^{2} \gamma + 2 & -1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i}\\{u}_{i - 1}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{x}^{2} \gamma}{2} - \frac{\Delta_{x} \sqrt{\gamma \left(\Delta_{x}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1\qquad\left|{\frac{\Delta_{x}^{2} \gamma}{2} + \frac{\Delta_{x} \sqrt{\gamma \left(\Delta_{x}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1  $$


 - space discretization with operator $D_+^2$, solving for $\left[ {u}_{i + 2}, \  {u}_{i + 1}, \  {u}_{i}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{- 2 {u}_{i + 1} + {u}_{i + 2} + {u}_{i}}{\Delta_{x}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{x}^{2} \gamma {u}_{i} + 2 {u}_{i + 1} - {u}_{i}  =  {u}_{i + 2}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i + 2}\\{u}_{i + 1}\end{matrix}\right]  =  \left[\begin{matrix}2 & \Delta_{x}^{2} \gamma - 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i + 1}\\{u}_{i}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{x} \sqrt{\gamma} - 1}\right|\leq 1\qquad\left|{\Delta_{x} \sqrt{\gamma} + 1}\right|\leq 1  $$


 - space discretization with operator $D_-^2$, solving for $\left[ {u}_{i}, \  {u}_{i - 1}, \  {u}_{i - 2}\right]$, and $z := \gamma\Delta_{x}$    
   - original difference scheme
      $$  - \gamma {u}_{i} + \frac{- 2 {u}_{i - 1} + {u}_{i - 2} + {u}_{i}}{\Delta_{x}^{2}}  =  0  $$
   - solving for next timestep
      $$  \frac{- 2 {u}_{i - 1} + {u}_{i - 2}}{\Delta_{x}^{2} \gamma - 1}  =  {u}_{i}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{i}\\{u}_{i - 1}\end{matrix}\right]  =  \left[\begin{matrix}- \frac{2}{\Delta_{x}^{2} \gamma - 1} & \frac{1}{\Delta_{x}^{2} \gamma - 1}\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{i - 1}\\{u}_{i - 2}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{x} \sqrt{\gamma}}{\Delta_{x}^{2} \gamma - 1} + \frac{1}{\Delta_{x}^{2} \gamma - 1}}\right|\leq 1\qquad\left|{\frac{\Delta_{x} \sqrt{\gamma}}{\Delta_{x}^{2} \gamma - 1} - \frac{1}{\Delta_{x}^{2} \gamma - 1}}\right|\leq 1  $$


 - time discretization with operator $D_- D_+$, solving for $\left[ {u}_{n + 1}, \  {u}_{n}, \  {u}_{n - 1}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{{u}_{n + 1} + {u}_{n - 1} - 2 {u}_{n}}{\Delta_{t}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{t}^{2} \gamma {u}_{n} - {u}_{n - 1} + 2 {u}_{n}  =  {u}_{n + 1}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n + 1}\\{u}_{n}\end{matrix}\right]  =  \left[\begin{matrix}\Delta_{t}^{2} \gamma + 2 & -1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n}\\{u}_{n - 1}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{t}^{2} \gamma}{2} - \frac{\Delta_{t} \sqrt{\gamma \left(\Delta_{t}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1\qquad\left|{\frac{\Delta_{t}^{2} \gamma}{2} + \frac{\Delta_{t} \sqrt{\gamma \left(\Delta_{t}^{2} \gamma + 4\right)}}{2} + 1}\right|\leq 1  $$


 - time discretization with operator $D_+^2$, solving for $\left[ {u}_{n + 2}, \  {u}_{n + 1}, \  {u}_{n}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{- 2 {u}_{n + 1} + {u}_{n + 2} + {u}_{n}}{\Delta_{t}^{2}}  =  0  $$
   - solving for next timestep
      $$  \Delta_{t}^{2} \gamma {u}_{n} + 2 {u}_{n + 1} - {u}_{n}  =  {u}_{n + 2}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n + 2}\\{u}_{n + 1}\end{matrix}\right]  =  \left[\begin{matrix}2 & \Delta_{t}^{2} \gamma - 1\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n + 1}\\{u}_{n}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\Delta_{t} \sqrt{\gamma} - 1}\right|\leq 1\qquad\left|{\Delta_{t} \sqrt{\gamma} + 1}\right|\leq 1  $$


 - time discretization with operator $D_-^2$, solving for $\left[ {u}_{n}, \  {u}_{n - 1}, \  {u}_{n - 2}\right]$, and $z := \gamma\Delta_{t}$    
   - original difference scheme
      $$  - \gamma {u}_{n} + \frac{- 2 {u}_{n - 1} + {u}_{n - 2} + {u}_{n}}{\Delta_{t}^{2}}  =  0  $$
   - solving for next timestep
      $$  \frac{- 2 {u}_{n - 1} + {u}_{n - 2}}{\Delta_{t}^{2} \gamma - 1}  =  {u}_{n}  $$
   - matrix equation
     $$  \left[\begin{matrix}{u}_{n}\\{u}_{n - 1}\end{matrix}\right]  =  \left[\begin{matrix}- \frac{2}{\Delta_{t}^{2} \gamma - 1} & \frac{1}{\Delta_{t}^{2} \gamma - 1}\\1 & 0\end{matrix}\right] \cdot \left[\begin{matrix}{u}_{n - 1}\\{u}_{n - 2}\end{matrix}\right]  $$
   - condition on $\gamma$ derived from requiring each eigenvalue be less than 1 in abosolute value
     $$  \left|{\frac{\Delta_{t} \sqrt{\gamma}}{\Delta_{t}^{2} \gamma - 1} + \frac{1}{\Delta_{t}^{2} \gamma - 1}}\right|\leq 1\qquad\left|{\frac{\Delta_{t} \sqrt{\gamma}}{\Delta_{t}^{2} \gamma - 1} - \frac{1}{\Delta_{t}^{2} \gamma - 1}}\right|\leq 1  $$


