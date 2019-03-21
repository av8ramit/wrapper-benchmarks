#!/usr/bin/env bash

pushd cffi > /dev/null

virtualenv -q -p python3.5 venv
source ${PWD}/venv/bin/activate

pip -q install cffi

python benchmarks.py

deactivate
rm -rf venv

git clean -qdfx

popd > /dev/null
