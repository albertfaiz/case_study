# pi_numpy.py
from numpy import sum, random
import sys

def calc_pi_numpy(n):
    x = random.rand(n)
    y = random.rand(n)
    hits = sum(x*x + y*y < 1.0)
    return 4.0 * hits / float(n)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pi_numpy.py <number_of_samples>")
        sys.exit(1)
    n = int(sys.argv[1])
    pi_est = calc_pi_numpy(n)
    print(f"n={n}, pi={pi_est}")
