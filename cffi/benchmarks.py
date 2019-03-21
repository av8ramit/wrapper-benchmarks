import timeit

print ("\n\nBenchmarks for pybind11:\n")
print ("Testing a no-op")
print (timeit.timeit('lib.no_op()', setup="from module import ffi, lib", number=100000))

print ("Testing a no-op with a return")
print (timeit.timeit('lib.no_op_return()', setup="from module import ffi, lib", number=100000))

print ("Testing an add")
print (timeit.timeit('lib.add(1, 2)', setup="from module import ffi, lib", number=100000))
