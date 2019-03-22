# wrapper-benchmarks
This repo contains code for C++ - Python wrapper benchmarks.

```
./run_all_benchmarks.sh 


Benchmarks for swig:

Testing a no-op
0.006232046987861395
Testing a no-op with a return
0.006324008048977703
Testing an add
0.012546848971396685
Testing is prime
0.20738002395955846


Benchmarks for pybind11:

Testing a no-op
0.007010767003521323
Testing a no-op with a return
0.007151249970775098
Testing an add
0.01796565594850108
Testing is prime
0.13039427204057574


Benchmarks for CFFI:

Testing a no-op
0.00485191197367385
Testing a no-op with a return
0.00510295998537913
Testing an add
0.008913404017221183
Testing is prime
0.13159637397620827
```
