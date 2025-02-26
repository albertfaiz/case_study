# pi_numba.py
import random, sys
from numba import njit, prange

@njit
def calc_pi_numba(n):
    hits = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y < 1.0:
            hits += 1
    return 4.0 * hits / n

@njit(nopython=True, nogil=True, parallel=True)
def calc_pi_parallel(n):
    hits = 0
    for _ in prange(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y < 1.0:
            hits += 1
    return 4.0 * hits / n

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pi_numba.py <number_of_samples>")
        sys.exit(1)
    n = int(sys.argv[1])
    # Uncomment one of the following lines to test serial or parallel version:
    pi_est = calc_pi_numba(n)
    # pi_est = calc_pi_parallel(n)
    print(f"n={n}, pi={pi_est}")
