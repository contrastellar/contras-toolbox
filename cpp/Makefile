#makefile

STD = -std=c++11
FLAGS = -fpermissive

default: stringgen randProof

randProof: randProof.o
		g++ $(STD) $(FLAGS) -g -o randProof randProof.o $*

stringgen: stringgen.o 
		g++ $(STD) $(FLAGS) -g -o stringgen stringgen.o $*

randProof.o: randProof.cpp
		g++ $(STD) $(FLAGS) -g -c $^ -o $@

stringgen.o: stringgen.cpp
		g++ $(STD) $(FLAGS) -g -c $^ -o $@

clean:
	rm *.o
	rm stringgen
	rm randProof

