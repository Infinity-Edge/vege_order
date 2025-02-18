import numpy as np
import matplotlib.pyplot as plt

# Constants specific to potato
frequency_khz = np.linspace(20, 500, 100)  # Frequency range in kHz
frequency_hz = frequency_khz * 1e3  # Convert kHz to Hz
alpha_0 = 0.1  # Approximate attenuation coefficient for potato (Np/m·MHz)
n = 1  # Attenuation factor exponent for potato
alpha = alpha_0 * (frequency_hz / 1e6)**n  # Attenuation coefficient (Np/m)
speed_of_sound = 1500  # Speed of sound in potato (m/s)

# Calculate penetration depth in mm (d = 1 / (2 * alpha))
penetration_depth_mm = 1 / (2 * alpha) * 1e3  # Convert meters to mm

# Calculate wavelength (λ = v / f)
wavelength_mm = speed_of_sound / frequency_hz * 1e3  # Convert meters to mm

# Plotting the graphs
plt.figure(figsize=(14, 6))

# Plot 1: Penetration Depth vs Frequency
plt.subplot(1, 2, 1)
plt.plot(frequency_khz, penetration_depth_mm, label="Penetration Depth", color='green', linewidth=2)
plt.title("Penetration Depth vs Frequency", fontsize=14)
plt.xlabel("Frequency (kHz)", fontsize=12)
plt.ylabel("Penetration Depth (mm)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Plot 2: Wavelength vs Frequency
plt.subplot(1, 2, 2)
plt.plot(frequency_khz, wavelength_mm, label="Wavelength", color='blue', linewidth=2)
plt.title("Wavelength vs Frequency", fontsize=14)
plt.xlabel("Frequency (kHz)", fontsize=12)
plt.ylabel("Wavelength (mm)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()