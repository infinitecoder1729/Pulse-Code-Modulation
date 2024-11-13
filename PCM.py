import numpy as np
import matplotlib.pyplot as plt

# Parameters
fm = 3
fs = 30
t = np.arange(0, 1, 0.001/fm)
Am = 2
n = 3
L = 2 ** n
ts = np.arange(0, 1, 1/fs)

# Message signal
x_t = Am * np.sin(2 * np.pi * fm * t)

# Sampled signal
x_s = Am * np.sin(2 * np.pi * fm * ts)

# Quantization parameters
Vmin = -Am
Vmax = Am
delta = (Vmax - Vmin) / (L - 1)
delta_steps = np.arange(Vmin, Vmax + delta, delta)
quant = np.arange(Vmin - delta/2, Vmax + delta/2, delta)

# Quantization
ind = np.digitize(x_s, delta_steps) - 1
ind[ind < 0] = 0
ind[ind >= L] = L - 1  # Ensure indices do not exceed range
x_q = quant[ind]

# Encoding signal
encoded_signal = np.array([np.binary_repr(i, width=n) for i in ind])

# Flatten encoded bits for plotting
encoded_bits = np.array([int(bit) for bits in encoded_signal for bit in bits])

# Plotting
plt.figure(figsize=(10, 10))

plt.subplot(4, 1, 1)
plt.plot(t, x_t, 'k-', linewidth=1.5, label='Original Signal')
plt.stem(ts, x_s, 'g-', label='Sampled Signal', use_line_collection=True)
plt.title('Sampling')
plt.xlabel('Time t (in sec)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.subplot(4, 1, 2)
plt.stem(ts, x_s, 'go', use_line_collection=True, label='Sampled values')
plt.stem(ts, x_q, 'r.', use_line_collection=True, label='Quantized values')
plt.title('Sampled vs Quantized')
plt.xlabel('Time t (in sec)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.subplot(4, 1, 3)
plt.step(ts, x_q, 'r--', linewidth=1.5, label='Quantized Signal')
plt.stem(ts, x_s, 'go', use_line_collection=True, label='Sampled Signal')
plt.title('Quantization')
plt.xlabel('Time t (in sec)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

plt.subplot(4, 1, 4)
plt.step(np.arange(len(encoded_bits)), encoded_bits, 'b-', linewidth=1.5, label='Encoded digital signal')
plt.title('Encoding')
plt.xlabel('Encoded bits')
plt.ylabel('Binary Signal')
plt.grid()

plt.tight_layout()
plt.show()

# Calculating parameters
Rb = fs * n
Tb = 1 / Rb
Qe_max = delta / 2
P_signal = np.mean(x_t ** 2)
P_signal_dB = 10 * np.log10(P_signal)
P_noise = delta ** 2 / 12
P_noise_dB = 10 * np.log10(P_noise)
SQNR_dB = P_signal_dB - P_noise_dB
SQNR_formula_dB = 6.02 * n + 1.76

# Display results
print(f'Bit rate (Rb): {Rb:.2f} bits/sec')
print(f'Bit duration (Tb): {Tb:.2e} sec')
print(f'Step size (δ): {delta:.4f} volts')
print(f'Maximum quantization error (Qe_max): {Qe_max:.4f} volts')
print(f'Signal power: {P_signal_dB:.2f} dB')
print(f'Quantization noise power: {P_noise_dB:.2f} dB')
print(f'SQNR (calculated): {SQNR_dB:.2f} dB')
print(f'SQNR (formula): {SQNR_formula_dB:.2f} dB')
