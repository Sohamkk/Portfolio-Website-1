import numpy as np
import matplotlib.pyplot as plt

# Define the time range for plotting
t = np.linspace(-2, 3, 1000)

# Define the unit step function u(1 - t)
u_1_minus_t = np.heaviside(1 - t, 1)

# Plot the function
plt.figure(figsize=(8, 4))
plt.plot(t, u_1_minus_t, label='$u(1 - t)$', color='blue')
plt.title('Unit Step Function $u(1 - t)$')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.ylim(-0.1, 1.1)
plt.axvline(x=1, color='gray', linestyle='--', label='t = 1')
plt.legend()
plt.grid(True)
plt.show()
