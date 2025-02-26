# test_cython.py
from calc_pi import calc_pi_cython
from time import time
import sys

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
    start = time()
    pi = calc_pi_cython(n)
    end = time()
    print(f"Estimated Pi: {pi} [Samples: {n}, Time: {end - start:.3f} s]")
