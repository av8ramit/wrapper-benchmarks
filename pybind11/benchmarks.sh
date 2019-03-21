#!/usr/bin/env bash

pushd pybind11

virtualenv -p python3.5 venv
source ${PWD}/venv/bin/activate

pip install pybind11

c++ -O3 -Wall -shared -std=c++11 -fPIC `python -m pybind11 --includes` pybind11_example.cpp -o pybind11_example`python-config --extension-suffix`

python benchmarks.py

deactivate
rm -rf venv
