// Next to my Life, Software is My Passion  ---  Robert C.Martin

// the first one , is the

/* ----------- factory mode ------------- */

#include <iostream>
using namespace std;

// first, the definitions, you can move them to the dot h file.

class Product
{
public:
	virtual ~Product() = 0;

protected:
	Product();

private:
	


};

class ConcreteProduct: public Product
{
public:
	~ConcreteProduct();

	ConcreteProduct();

protected:

private:


};

Product::Product()
{

}

Product::~Product()
{

}

ConcreteProduct::ConcreteProduct()
{

cout<<"ConcreteProduct"<<endl;

}

ConcreteProduct::~ConcreteProduct()
{
}

class Factory
{
public:
	virtual ~Factory() = 0;

	virtual Product* CreateProduct() = 0;

protected:
	Factory();

private:

};


class ConcreteFactory: public Factory
{
public:
	~ConcreteFactory();

	ConcreteFactory();

	Product* CreateProduct();

protected:

private:


};

Factory::Factory()
{

}

Factory::~Factory()
{

}

ConcreteFactory::ConcreteFactory()
{
	cout<<"ConcreteFactory....."<<endl;
}

ConcreteFactory::~ConcreteFactory()
{
}

Product* ConcreteFactory::CreateProduct()
{

	return new ConcreteProduct();	

}

int main(int argc,char **argv)
{

	Factory *fac = new ConcreteFactory();

	Product *p = fac->CreateProduct();

	return 0;

}
