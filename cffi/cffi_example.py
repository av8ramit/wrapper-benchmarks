from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
    void no_op();
	bool no_op_return();
	int add(int i, int j);
    """)

ffibuilder.set_source("cppmodule", r''' 
extern "C" {
    void no_op() { }
	bool no_op_return() { return true; }
	int add(int i, int j) { return i + j; }
} 
''', source_extension='.cpp') 

if __name__ == "__main__":
    ffibuilder.compile()