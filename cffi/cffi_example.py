from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
    void no_op();
	bool no_op_return();
	int add(int i, int j);
    int is_prime(int);
    """)

ffibuilder.set_source("cppmodule",
r''' 
	extern "C" {
	    void no_op() { }
		bool no_op_return() { return true; }
		int add(int i, int j) { return i + j; }
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
	} 
''',
source_extension='.cpp') 

if __name__ == "__main__":
    ffibuilder.compile()