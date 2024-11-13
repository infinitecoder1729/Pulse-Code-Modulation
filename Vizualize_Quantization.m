Am = 2;
n = 3;
L = 2^n;

Vmin = -Am;
Vmax = Am;
delta = (Vmax - Vmin) / (L - 1);
steps = Vmin:delta:Vmax;
quant = Vmin - delta/2 : delta : Vmax + delta/2;

figure;
stairs(steps, quant(2:end), 'LineWidth', 1.5);
title('Uniform PCM Quantizer Characteristic Curve');
xlabel('Input Signal (Steps)');
ylabel('Quantized Output');
legend('Quantization Levels');
grid on;
