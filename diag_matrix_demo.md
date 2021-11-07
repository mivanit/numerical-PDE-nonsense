**diff ops**

$D_+$:
$$ \frac{1}{h} \left[\begin{smallmatrix}-1 & 1 & 0 & 0 & 0 & 0 & 0\\0 & -1 & 1 & 0 & 0 & 0 & 0\\0 & 0 & -1 & 1 & 0 & 0 & 0\\0 & 0 & 0 & -1 & 1 & 0 & 0\\0 & 0 & 0 & 0 & -1 & 1 & 0\\0 & 0 & 0 & 0 & 0 & -1 & 1\\0 & 1 & 0 & 0 & 0 & 0 & -1\end{smallmatrix}\right] $$

$D_-$:
$$ \frac{1}{h} \left[\begin{smallmatrix}1 & 0 & 0 & 0 & 0 & -1 & 0\\-1 & 1 & 0 & 0 & 0 & 0 & 0\\0 & -1 & 1 & 0 & 0 & 0 & 0\\0 & 0 & -1 & 1 & 0 & 0 & 0\\0 & 0 & 0 & -1 & 1 & 0 & 0\\0 & 0 & 0 & 0 & -1 & 1 & 0\\0 & 0 & 0 & 0 & 0 & -1 & 1\end{smallmatrix}\right] $$

$D_0$:
$$ \frac{2}{h} \left[\begin{smallmatrix}0 & \frac{1}{4} & 0 & 0 & 0 & - \frac{1}{4} & 0\\- \frac{1}{4} & 0 & \frac{1}{4} & 0 & 0 & 0 & 0\\0 & - \frac{1}{4} & 0 & \frac{1}{4} & 0 & 0 & 0\\0 & 0 & - \frac{1}{4} & 0 & \frac{1}{4} & 0 & 0\\0 & 0 & 0 & - \frac{1}{4} & 0 & \frac{1}{4} & 0\\0 & 0 & 0 & 0 & - \frac{1}{4} & 0 & \frac{1}{4}\\0 & \frac{1}{4} & 0 & 0 & 0 & - \frac{1}{4} & 0\end{smallmatrix}\right] $$

$D_- D_+$:
$$ \frac{1}{h^{2}} \left[\begin{smallmatrix}-2 & 1 & 0 & 0 & 0 & 1 & 0\\1 & -2 & 1 & 0 & 0 & 0 & 0\\0 & 1 & -2 & 1 & 0 & 0 & 0\\0 & 0 & 1 & -2 & 1 & 0 & 0\\0 & 0 & 0 & 1 & -2 & 1 & 0\\0 & 0 & 0 & 0 & 1 & -2 & 1\\0 & 1 & 0 & 0 & 0 & 1 & -2\end{smallmatrix}\right] $$

**theta eqn**

theta scheme, LHS:
$$ \frac{\Delta_{t} \theta}{h^{2}} \left[\begin{smallmatrix}2 \eta + \frac{h^{2}}{\Delta_{t} \theta} & \frac{a h}{2} - \eta & 0 & 0 & 0 & - \frac{a h}{2} - \eta & 0\\- \frac{a h}{2} - \eta & 2 \eta + \frac{h^{2}}{\Delta_{t} \theta} & \frac{a h}{2} - \eta & 0 & 0 & 0 & 0\\0 & - \frac{a h}{2} - \eta & 2 \eta + \frac{h^{2}}{\Delta_{t} \theta} & \frac{a h}{2} - \eta & 0 & 0 & 0\\0 & 0 & - \frac{a h}{2} - \eta & 2 \eta + \frac{h^{2}}{\Delta_{t} \theta} & \frac{a h}{2} - \eta & 0 & 0\\0 & 0 & 0 & - \frac{a h}{2} - \eta & 2 \eta + \frac{h^{2}}{\Delta_{t} \theta} & \frac{a h}{2} - \eta & 0\\0 & 0 & 0 & 0 & - \frac{a h}{2} - \eta & 2 \eta + \frac{h^{2}}{\Delta_{t} \theta} & \frac{a h}{2} - \eta\\0 & \frac{a h}{2} - \eta & 0 & 0 & 0 & - \frac{a h}{2} - \eta & 2 \eta + \frac{h^{2}}{\Delta_{t} \theta}\end{smallmatrix}\right] $$

theta scheme, RHS:
$$ \Delta_{t} \left[\begin{smallmatrix}\frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}} & 0 & 0 & 0 & - \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & 0\\- \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & \frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}} & 0 & 0 & 0 & 0\\0 & - \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & \frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}} & 0 & 0 & 0\\0 & 0 & - \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & \frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}} & 0 & 0\\0 & 0 & 0 & - \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & \frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}} & 0\\0 & 0 & 0 & 0 & - \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & \frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}}\\0 & \frac{\left(\theta - 1\right) \left(a h - 2 \eta\right)}{2 h^{2}} & 0 & 0 & 0 & - \frac{\left(\theta - 1\right) \left(a h + 2 \eta\right)}{2 h^{2}} & \frac{2 \Delta_{t} \eta \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}}\end{smallmatrix}\right] $$



### case: $a=1, \ \eta=0$
**theta eqn**

theta scheme, LHS:
$$ \left[\begin{smallmatrix}1 & \frac{\Delta_{t} \theta}{2 h} & 0 & 0 & 0 & - \frac{\Delta_{t} \theta}{2 h} & 0\\- \frac{\Delta_{t} \theta}{2 h} & 1 & \frac{\Delta_{t} \theta}{2 h} & 0 & 0 & 0 & 0\\0 & - \frac{\Delta_{t} \theta}{2 h} & 1 & \frac{\Delta_{t} \theta}{2 h} & 0 & 0 & 0\\0 & 0 & - \frac{\Delta_{t} \theta}{2 h} & 1 & \frac{\Delta_{t} \theta}{2 h} & 0 & 0\\0 & 0 & 0 & - \frac{\Delta_{t} \theta}{2 h} & 1 & \frac{\Delta_{t} \theta}{2 h} & 0\\0 & 0 & 0 & 0 & - \frac{\Delta_{t} \theta}{2 h} & 1 & \frac{\Delta_{t} \theta}{2 h}\\0 & \frac{\Delta_{t} \theta}{2 h} & 0 & 0 & 0 & - \frac{\Delta_{t} \theta}{2 h} & 1\end{smallmatrix}\right] $$

theta scheme, RHS:
$$ \left[\begin{smallmatrix}1 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0\\\frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0 & 0 & 0\\0 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0 & 0\\0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0\\0 & 0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0\\0 & 0 & 0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h}\\0 & - \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 0 & 0 & 0 & \frac{\Delta_{t} \left(1 - \theta\right)}{2 h} & 1\end{smallmatrix}\right] $$



### case: $a=0, \ \eta=1$
**theta eqn**

theta scheme, LHS:
$$ \Delta_{t} \theta \left[\begin{smallmatrix}\frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & - \frac{1}{h^{2}} & 0 & 0 & 0 & - \frac{1}{h^{2}} & 0\\- \frac{1}{h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & - \frac{1}{h^{2}} & 0 & 0 & 0 & 0\\0 & - \frac{1}{h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & - \frac{1}{h^{2}} & 0 & 0 & 0\\0 & 0 & - \frac{1}{h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & - \frac{1}{h^{2}} & 0 & 0\\0 & 0 & 0 & - \frac{1}{h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & - \frac{1}{h^{2}} & 0\\0 & 0 & 0 & 0 & - \frac{1}{h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & - \frac{1}{h^{2}}\\0 & - \frac{1}{h^{2}} & 0 & 0 & 0 & - \frac{1}{h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta}\end{smallmatrix}\right] $$

theta scheme, RHS:
$$ \Delta_{t} \left[\begin{smallmatrix}\frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{1 - \theta}{h^{2}} & 0 & 0 & 0 & \frac{1 - \theta}{h^{2}} & 0\\\frac{1 - \theta}{h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{1 - \theta}{h^{2}} & 0 & 0 & 0 & 0\\0 & \frac{1 - \theta}{h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{1 - \theta}{h^{2}} & 0 & 0 & 0\\0 & 0 & \frac{1 - \theta}{h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{1 - \theta}{h^{2}} & 0 & 0\\0 & 0 & 0 & \frac{1 - \theta}{h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{1 - \theta}{h^{2}} & 0\\0 & 0 & 0 & 0 & \frac{1 - \theta}{h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{1 - \theta}{h^{2}}\\0 & \frac{1 - \theta}{h^{2}} & 0 & 0 & 0 & \frac{1 - \theta}{h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}}\end{smallmatrix}\right] $$



### case: $a=1, \ \eta=1$
**theta eqn**

theta scheme, LHS:
$$ \Delta_{t} \theta \left[\begin{smallmatrix}\frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & \frac{h - 2}{2 h^{2}} & 0 & 0 & 0 & - \frac{h + 2}{2 h^{2}} & 0\\- \frac{h + 2}{2 h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & \frac{h - 2}{2 h^{2}} & 0 & 0 & 0 & 0\\0 & - \frac{h + 2}{2 h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & \frac{h - 2}{2 h^{2}} & 0 & 0 & 0\\0 & 0 & - \frac{h + 2}{2 h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & \frac{h - 2}{2 h^{2}} & 0 & 0\\0 & 0 & 0 & - \frac{h + 2}{2 h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & \frac{h - 2}{2 h^{2}} & 0\\0 & 0 & 0 & 0 & - \frac{h + 2}{2 h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta} & \frac{h - 2}{2 h^{2}}\\0 & \frac{h - 2}{2 h^{2}} & 0 & 0 & 0 & - \frac{h + 2}{2 h^{2}} & \frac{2}{h^{2}} + \frac{1}{\Delta_{t} \theta}\end{smallmatrix}\right] $$

theta scheme, RHS:
$$ \Delta_{t} \left[\begin{smallmatrix}\frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0 & 0 & 0 & - \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0\\- \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0 & 0 & 0 & 0\\0 & - \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0 & 0 & 0\\0 & 0 & - \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0 & 0\\0 & 0 & 0 & - \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0\\0 & 0 & 0 & 0 & - \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}} & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}}\\0 & \frac{\left(h - 2\right) \left(\theta - 1\right)}{2 h^{2}} & 0 & 0 & 0 & - \frac{\left(h + 2\right) \left(\theta - 1\right)}{2 h^{2}} & \frac{2 \Delta_{t} \left(\theta - 1\right) + h^{2}}{\Delta_{t} h^{2}}\end{smallmatrix}\right] $$

