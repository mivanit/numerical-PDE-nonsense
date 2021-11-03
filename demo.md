**basics**

identity:
$$ \left[\begin{matrix}1 & 0 & 0 & 0 & 0\\0 & 1 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0\\0 & 0 & 0 & 1 & 0\\0 & 0 & 0 & 0 & 1\end{matrix}\right] $$

diag_moved_up:
$$ \left[\begin{matrix}0 & 1 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0\\0 & 0 & 0 & 1 & 0\\0 & 0 & 0 & 0 & 1\\1 & 0 & 0 & 0 & 0\end{matrix}\right] $$

diag_moved_down:
$$ \left[\begin{matrix}0 & 0 & 0 & 0 & 1\\1 & 0 & 0 & 0 & 0\\0 & 1 & 0 & 0 & 0\\0 & 0 & 1 & 0 & 0\\0 & 0 & 0 & 1 & 0\end{matrix}\right] $$

**diff ops**

D_+:
$$ \left[\begin{matrix}- \frac{1}{h} & \frac{1}{h} & 0 & 0 & 0\\0 & - \frac{1}{h} & \frac{1}{h} & 0 & 0\\0 & 0 & - \frac{1}{h} & \frac{1}{h} & 0\\0 & 0 & 0 & - \frac{1}{h} & \frac{1}{h}\\\frac{1}{h} & 0 & 0 & 0 & - \frac{1}{h}\end{matrix}\right] $$

D_-:
$$ \left[\begin{matrix}\frac{1}{h} & 0 & 0 & 0 & - \frac{1}{h}\\- \frac{1}{h} & \frac{1}{h} & 0 & 0 & 0\\0 & - \frac{1}{h} & \frac{1}{h} & 0 & 0\\0 & 0 & - \frac{1}{h} & \frac{1}{h} & 0\\0 & 0 & 0 & - \frac{1}{h} & \frac{1}{h}\end{matrix}\right] $$

central_diff:
$$ \left[\begin{matrix}0 & \frac{1}{2 h} & 0 & 0 & - \frac{1}{2 h}\\- \frac{1}{2 h} & 0 & \frac{1}{2 h} & 0 & 0\\0 & - \frac{1}{2 h} & 0 & \frac{1}{2 h} & 0\\0 & 0 & - \frac{1}{2 h} & 0 & \frac{1}{2 h}\\\frac{1}{2 h} & 0 & 0 & - \frac{1}{2 h} & 0\end{matrix}\right] $$

**theta eqn**

theta_eqn_LHS:
$$ \left[\begin{matrix}\frac{2 \Delta_{t} \eta \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0 & 0 & - \Delta_{t} \theta \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right)\\- \Delta_{t} \theta \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & \frac{2 \Delta_{t} \eta \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0 & 0\\0 & - \Delta_{t} \theta \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & \frac{2 \Delta_{t} \eta \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0\\0 & 0 & - \Delta_{t} \theta \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & \frac{2 \Delta_{t} \eta \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right)\\- \Delta_{t} \theta \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0 & 0 & - \Delta_{t} \theta \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & \frac{2 \Delta_{t} \eta \theta}{h^{2}} + 1\end{matrix}\right] $$

theta_eqn_RHS:
$$ \left[\begin{matrix}- \frac{2 \Delta_{t} \eta \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0 & 0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right)\\\Delta_{t} \left(1 - \theta\right) \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & - \frac{2 \Delta_{t} \eta \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0 & 0\\0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & - \frac{2 \Delta_{t} \eta \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0\\0 & 0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & - \frac{2 \Delta_{t} \eta \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right)\\\Delta_{t} \left(1 - \theta\right) \left(\frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & 0 & 0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{a}{2 h} + \frac{\eta}{h^{2}}\right) & - \frac{2 \Delta_{t} \eta \left(1 - \theta\right)}{h^{2}} + 1\end{matrix}\right] $$

### case: $a=1, \ \eta=0$
**theta eqn**

theta_eqn_LHS:
$$ \left[\begin{matrix}1 & - \frac{\Delta_{t} \theta}{2 h} & 0 & 0 & \frac{\Delta_{t} \theta}{2 h}\\\frac{\Delta_{t} \theta}{2 h} & 1 & - \frac{\Delta_{t} \theta}{2 h} & 0 & 0\\0 & \frac{\Delta_{t} \theta}{2 h} & 1 & - \frac{\Delta_{t} \theta}{2 h} & 0\\0 & 0 & \frac{\Delta_{t} \theta}{2 h} & 1 & - \frac{\Delta_{t} \theta}{2 h}\\- \frac{\Delta_{t} \theta}{2 h} & 0 & 0 & \frac{\Delta_{t} \theta}{2 h} & 1\end{matrix}\right] $$

theta_eqn_RHS:
$$ \left[\begin{matrix}1 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h}\\- \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0\\0 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0\\0 & 0 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h}\\\frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1\end{matrix}\right] $$

### case: $a=0, \ \eta=1$
**theta eqn**

theta_eqn_LHS:
$$ \left[\begin{matrix}\frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \frac{\Delta_{t} \theta}{h^{2}} & 0 & 0 & - \frac{\Delta_{t} \theta}{h^{2}}\\- \frac{\Delta_{t} \theta}{h^{2}} & \frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \frac{\Delta_{t} \theta}{h^{2}} & 0 & 0\\0 & - \frac{\Delta_{t} \theta}{h^{2}} & \frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \frac{\Delta_{t} \theta}{h^{2}} & 0\\0 & 0 & - \frac{\Delta_{t} \theta}{h^{2}} & \frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \frac{\Delta_{t} \theta}{h^{2}}\\- \frac{\Delta_{t} \theta}{h^{2}} & 0 & 0 & - \frac{\Delta_{t} \theta}{h^{2}} & \frac{2 \Delta_{t} \theta}{h^{2}} + 1\end{matrix}\right] $$

theta_eqn_RHS:
$$ \left[\begin{matrix}- \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & 0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}}\\\frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & 0 & 0\\0 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & 0\\0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}}\\\frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & 0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{h^{2}} & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1\end{matrix}\right] $$

### case: $a=1, \ \eta=1$
**theta eqn**

theta_eqn_LHS:
$$ \left[\begin{matrix}\frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0 & 0 & - \Delta_{t} \theta \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right)\\- \Delta_{t} \theta \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & \frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0 & 0\\0 & - \Delta_{t} \theta \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & \frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0\\0 & 0 & - \Delta_{t} \theta \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & \frac{2 \Delta_{t} \theta}{h^{2}} + 1 & - \Delta_{t} \theta \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right)\\- \Delta_{t} \theta \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0 & 0 & - \Delta_{t} \theta \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & \frac{2 \Delta_{t} \theta}{h^{2}} + 1\end{matrix}\right] $$

theta_eqn_RHS:
$$ \left[\begin{matrix}- \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0 & 0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right)\\\Delta_{t} \left(1 - \theta\right) \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0 & 0\\0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0\\0 & 0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1 & \Delta_{t} \left(1 - \theta\right) \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right)\\\Delta_{t} \left(1 - \theta\right) \left(\frac{1}{2 h} + \frac{1}{h^{2}}\right) & 0 & 0 & \Delta_{t} \left(1 - \theta\right) \left(- \frac{1}{2 h} + \frac{1}{h^{2}}\right) & - \frac{2 \Delta_{t} \left(1 - \theta\right)}{h^{2}} + 1\end{matrix}\right] $$

[null, null]
