from libc.math cimport pow

cdef double power(x,y):
    return pow(x,y)

def cock(x,y):
    return power(x,y)