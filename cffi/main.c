#include <stdio.h>
#include "main.h"
#include "cffi_example.h"

void wrapped_no_op() {
	no_op();
}

bool wrapped_no_op_return() {
	return no_op_return();
}

int wrapped_add(int i, int j) {
    return add(i, j);
}

int main(int argc, char **argv)
{
	printf("%d\n", wrapped_add(1,2));
}