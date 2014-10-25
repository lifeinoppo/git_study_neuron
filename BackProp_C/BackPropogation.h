// the defs for all structures



#ifndef BACKPROP_C_H
#define BACKPROP_C_H

typedef struct TypeOfRandNum
{
int timestamp;  // kept for future expension
int glue;  // 
int RegionNumber;   //  specify the region
int typeid;  // used now for specify the type of variable
RandNumberType plus(RandNumberType mOther);
RandNumberType minus(RandNumberType mOther);
RandNumberType multi(RandNumberType mOther);
RandNumberType devide(RandNumberType mOther);
// better use function pointer, point to outer function implementation

}RandNumType; // used for random number specify in rand function



typedef struct TypeOfMatrix
{


}MatrixType; // used for matrix calculation


#endif
