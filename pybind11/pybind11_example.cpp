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

bool is_prime(int num){
    bool flag=true;
    for(int i = 2; i <= num / 2; i++) {
       if(num % i == 0) {
          flag = false;
          break;
       }
    }
    return flag;
}

PYBIND11_MODULE(pybind11_example, m) {
  m.doc() = "pybind11 example plugin";
  m.def("no_op", &no_op);
  m.def("no_op_return", &no_op_return);
  m.def("add", &add);
  m.def("is_prime", &is_prime);
}