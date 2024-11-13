import numpy as np
import matplotlib.pyplot as plt

# Parameters
Am = 2
n = 3
L = 2 ** n

Vmin = -Am
Vmax = Am
delta = (Vmax - Vmin) / (L - 1)
steps = np.arange(Vmin, Vmax + delta, delta)
quant = np.arange(Vmin - delta/2, Vmax + delta/2 + delta, delta)

# Plotting
plt.figure(figsize=(8, 5))
plt.step(steps, quant[1:], linewidth=1.5, where='post')
plt.title('Uniform PCM Quantizer Characteristic Curve')
plt.xlabel('Input Signal (Steps)')
plt.ylabel('Quantized Output')
plt.legend(['Quantization Levels'])
plt.grid()
plt.xlim(Vmin - delta, Vmax + delta)
plt.ylim(Vmin - delta, Vmax + delta)
plt.show()
