# pi_python.py
from numpy.random import rand
import sys

def calc_pi_loop(n):
    hits = 0  # Count of points inside the circle
    for _ in range(n):
        x, y = rand(), rand()  # Generate random x, y in [0, 1)
        if x * x + y * y < 1.0:
            hits += 1
    return 4.0 * hits / float(n)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pi_python.py <number_of_samples>")
        sys.exit(1)
    n = int(sys.argv[1])
    pi_est = calc_pi_loop(n)
    print(f"n={n}, pi={pi_est}")
