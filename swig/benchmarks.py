import timeit

print ("\n\nBenchmarks for swig:\n")
print ("Testing a no-op")
print (timeit.timeit('swig_example.no_op()', setup="import swig_example", number=100000))

print ("Testing a no-op with a return")
print (timeit.timeit('swig_example.no_op_return()', setup="import swig_example", number=100000))

print ("Testing an add")
print (timeit.timeit('swig_example.add(1, 2)', setup="import swig_example", number=100000))

print ("Testing is prime")
print (timeit.timeit('swig_example.is_prime(1234231)', setup="import swig_example", number=100))
