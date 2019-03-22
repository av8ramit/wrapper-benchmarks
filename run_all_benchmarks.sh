#!/usr/bin/env bash

./swig/benchmarks.sh
echo
./pybind11/benchmarks.sh
echo
./cffi/benchmarks.sh
echo
