#!/usr/bin/env bash

pushd swig > /dev/null

virtualenv -q -p python3.5 venv
source ${PWD}/venv/bin/activate

swig -c++ -python swig_example.i
g++ -fpic -c swig_example.h swig_example_wrap.cxx swig_example.cpp -I${PWD}/venv/include/python3.5m/
gcc -shared swig_example_wrap.o swig_example.o -o _swig_example.so -lstdc++

python benchmarks.py

deactivate
rm -rf venv

git clean -qdfx

popd > /dev/null
