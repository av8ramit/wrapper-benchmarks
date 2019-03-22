%module swig_example

%{
#define SWIG_FILE_WITH_INIT
#include "swig_example.h"
%}

void no_op();
bool no_op_return();
int add(int i, int j);
bool is_prime(int num);