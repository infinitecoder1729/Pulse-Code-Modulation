fm = 3;
fs = 30;
t = 0:0.001/fm:1;
Am = 2;
n = 3;
L = 2^n;
ts = 0:1/fs:1;

% Message signal
x_t = Am * sin(2 * pi * fm * t);

% Sampled signal
x_s = Am * sin(2 * pi * fm * ts);

% Quantization parameters
Vmin = -Am;
Vmax = Am;
delta = (Vmax - Vmin) / (L - 1);
delta_steps = Vmin:delta:Vmax;
quant = (Vmin - delta/2):delta:(Vmax + delta/2);

% Quantization
[ind, x_q] = quantiz(x_s, delta_steps, quant);
NonZeroInd = find(ind ~= 0);
ind(NonZeroInd) = ind(NonZeroInd) - 1;
encoded_signal = de2bi(ind,n, 'left-msb');

figure;
subplot(4, 1, 1);
plot(t, x_t, 'k-', 'LineWidth', 1.5); % Original signal in black
hold on;
stem(ts, x_s, 'g', 'LineWidth', 1.5); % Sampled signal in green
title('Sampling');
xlabel('Time t (in sec)');
ylabel('Amplitude');
legend('Original Signal', 'Sampled Signal');
grid on;

subplot(4, 1, 2);
stem(ts, x_s, 'go', 'LineWidth', 1.5); % Sampled values in green
hold on;
stem(ts, x_q, 'r.', 'LineWidth', 1.5); % Quantized values in red
title('Sampled vs Quantized');
xlabel('Time t (in sec)');
ylabel('Amplitude');
legend('Sampled values', 'Quantized values');
grid on;

subplot(4, 1, 3);
stairs(ts, x_q, 'r--', 'LineWidth', 1.5); % Quantized signal in red dashed line
hold on;
stem(ts, x_s, 'go', 'LineWidth', 1.5); % Sampled signal in green
title('Quantization');
xlabel('Time t (in sec)');
ylabel('Amplitude');
legend('Quantized Signal', 'Sampled Signal');
grid on;

subplot(4, 1, 4);
encoded_bits = reshape(encoded_signal', 1, []);
stairs(1:length(encoded_bits), encoded_bits, 'b-', 'LineWidth', 1.5); % Encoded digital signal in blue
title('Encoding');
xlabel('Encoded bits');
ylabel('Binary Signal');
grid on;

Rb = fs * n;
Tb = 1 / Rb;
delta = (Vmax - Vmin) / (L - 1);
Qe_max = delta / 2;
P_signal = mean(x_t.^2);
P_signal_dB = 10 * log10(P_signal);
P_noise = delta^2 / 12;
P_noise_dB = 10 * log10(P_noise);
SQNR_dB = P_signal_dB - P_noise_dB;
SQNR_formula_dB = 6.02 * n + 1.76;

% Display results
fprintf('Bit rate (Rb): %.2f bits/sec\n', Rb);
fprintf('Bit duration (Tb): %.2e sec\n', Tb);
fprintf('Step size (δ): %.4f volts\n', delta);
fprintf('Maximum quantization error (Qe_max): %.4f volts\n', Qe_max);
fprintf('Signal power: %.2f dB\n', P_signal_dB);
fprintf('Quantization noise power: %.2f dB\n', P_noise_dB);
fprintf('SQNR (calculated): %.2f dB\n', SQNR_dB);
fprintf('SQNR (formula): %.2f dB\n', SQNR_formula_dB);
