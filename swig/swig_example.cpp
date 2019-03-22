#include "swig_example.h"
#include <vector>

void no_op() {
}

bool no_op_return() {
	return true;
}

int add(int i, int j) {
    return i + j;
}

bool is_prime(int num) {
    bool flag=true;
    for(int i = 2; i <= num / 2; i++) {
       if(num % i == 0) {
          flag = false;
          break;
       }
    }
    return flag;
}