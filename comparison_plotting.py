import subprocess
import matplotlib.pyplot as plt
import numpy as np

# Install necessary libraries if they are not already installed
try:
    import matplotlib
    import numpy
except ImportError:
    print("Installing matplotlib and numpy...")
    subprocess.check_call(['python', '-m', 'pip', 'install', 'matplotlib', 'numpy'])
    import matplotlib
    import numpy

# Data from Table 1
n_values = [10**6, 10**7]  # Representative n values
abs_errors = {
    "Pure Python": [0.0066, None],  # Only have data for one n value
    "NumPy": [None, 0.0004],
    "Numba": [None, 0.0001],
    "Cython": [0.0015, None],
    "C++": [None, 0.0010]
}

# --- Mean Absolute Error vs. n ---
plt.figure(figsize=(8, 6))

for label, errors in abs_errors.items():
    if errors[0] is not None and errors[1] is not None:
        plt.plot(n_values, errors, marker='o', label=label)
        n_values_fit = np.logspace(6, 7, 10)
        popt, _ = np.polyfit(np.log(n_values), np.log(errors), 1)
        fit_errors = np.exp(popt[1]) * n_values_fit**popt[0]
        plt.plot(n_values_fit, fit_errors, '--', label=f"{label} Fit")

    elif errors[0] is not None:
        plt.plot(n_values[0], errors[0], marker='o', label=label)
    elif errors[1] is not None:
        plt.plot(n_values[1], errors[1], marker='o', label=label)

plt.xscale('log')
plt.yscale('log')
plt.xlabel("n")
plt.ylabel("Mean Absolute Error")
plt.title("Mean Absolute Error vs. n")
plt.grid(True)
plt.legend()


# --- Placeholder for Standard Deviation of π estimates vs. n ---
# (Requires additional data which isn't in the table)
plt.figure(figsize=(8, 6))
plt.xlabel("n")
plt.ylabel("Standard Deviation of π estimates")
plt.title("Standard Deviation of π estimates vs. n")
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.legend()

plt.show()