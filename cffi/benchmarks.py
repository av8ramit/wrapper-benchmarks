import timeit

print ("\n\nBenchmarks for CFFI:\n")
print ("Testing a no-op")
print (timeit.timeit('lib.no_op()', setup="from cppmodule import ffi, lib", number=100000))

print ("Testing a no-op with a return")
print (timeit.timeit('lib.no_op_return()', setup="from cppmodule import ffi, lib", number=100000))

print ("Testing an add")
print (timeit.timeit('lib.add(1, 2)', setup="from cppmodule import ffi, lib", number=100000))

print ("Testing is prime")
print (timeit.timeit('lib.is_prime(1234231)', setup="from cppmodule import ffi, lib", number=100))
