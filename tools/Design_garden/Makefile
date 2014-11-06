CC = g++
CFLAGS = -Wall
INCLUDE = 
LDFLAGS = 

ALL =  first_Factory   # modify this later

all :$(ALL)

first_Factory : first_Factory.o
	$(CC) -o first_Factory first_Factory.o   

first_Factory.o : first_Factory.cpp
	$(CC) -c first_Factory.cpp 

clean:
	rm -rf *.o $(ALL)
