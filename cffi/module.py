from cffi import FFI

ffibuilder = FFI()

# For every function that you want to have a python binding,
# specify its declaration here
ffibuilder.cdef("""
    void wrapped_no_op();
	bool wrapped_no_op_return();
	int wrapped_add(int i, int j);
                """)

# Here go the sources, most likely only includes and additional functions if necessary
ffibuilder.set_source("module",
    """
    #include "main.h"
    """, sources=["main.c"])

if __name__ == "__main__":
    ffibuilder.compile()