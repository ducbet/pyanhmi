cdef int loop_total = 10000


cpdef int called_func3():
    return 2


cpdef void called_func2():
    cdef int i
    for i in range(loop_total):
        called_func3()


cpdef int c_called_func():
    cdef int i
    for i in range(loop_total):
        called_func2()
    return 1996