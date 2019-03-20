#!/usr/bin/env bash

pushd swig

virtualenv venv
source ${PWD}/venv/bin/activate

swig -c++ -python swig_example.i
g++ -fpic -c swig_example.h swig_example_wrap.cxx swig_example.cpp -I${PWD}/venv/include/python2.7/
gcc -shared swig_example_wrap.o swig_example.o -o _swig_example.so -lstdc++

python benchmarks.py

deactivate
rm -rf venv