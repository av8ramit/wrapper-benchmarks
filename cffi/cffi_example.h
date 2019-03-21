#include <stdbool.h>

#ifndef __CPP_WRAPPER_H__
#define __CPP_WRAPPER_H__

#ifdef __cplusplus
extern "C" {
#endif

void no_op();

bool no_op_return();

int add(int i, int j);

#ifdef __cplusplus
}
#endif

#endif /* __CPP_WRAPPER_H__ */