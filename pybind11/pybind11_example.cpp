#include "pybind11_example.h"
#include <pybind11/pybind11.h>

namespace py = pybind11;

void no_op() {
}

bool no_op_return() {
	return true;
}

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(pybind11_example, m) {
  m.doc() = "pybind11 example plugin";
  m.def("no_op", &no_op);
  m.def("no_op_return", &no_op_return);
  m.def("add", &add);
}