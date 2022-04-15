#makefile

STD = -std=c++11

default: stringgen

stringgen: stringgen.o 
		g++ $(STD) -g -o stringgen stringgen.o $*

stringgen.o: stringgen.cpp
		g++ $(STD) -g -c $^ -o $@

clean:
	rm *.o
	rm stringgen
