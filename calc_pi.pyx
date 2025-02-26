# calc_pi.pyx
# cython: language_level=3
cimport cython
from libc.stdlib cimport rand, RAND_MAX

@cython.boundscheck(False)
@cython.wraparound(False)
def calc_pi_cython(int n):
    cdef int i, hits = 0
    cdef double x, y
    for i in range(n):
        x = rand() / RAND_MAX
        y = rand() / RAND_MAX
        if x*x + y*y < 1.0:
            hits += 1
    return 4.0 * hits / n
