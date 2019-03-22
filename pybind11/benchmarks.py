import timeit

print ("\n\nBenchmarks for pybind11:\n")
print ("Testing a no-op")
print (timeit.timeit('pybind11_example.no_op()', setup="import pybind11_example", number=100000))

print ("Testing a no-op with a return")
print (timeit.timeit('pybind11_example.no_op_return()', setup="import pybind11_example", number=100000))

print ("Testing an add")
print (timeit.timeit('pybind11_example.add(1, 2)', setup="import pybind11_example", number=100000))

print ("Testing is prime")
print (timeit.timeit('pybind11_example.is_prime(1234231)', setup="import pybind11_example", number=100))
