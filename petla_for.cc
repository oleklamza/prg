#include <iostream>

int main()
{
	
	for (;;) {
		std::cout << "*";
	}


	for (int i=1; i<=10; i+=1) {
		std::cout << i << std::endl;
	}


	int i = 1;
	while (i <= 10) {
		std::cout << i << std::endl;
		i += 1;		// i++
	}

}