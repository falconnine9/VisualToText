#include <iostream>
#include <cstring>
#include "ImageToText.h"


int main() {
	std::string filename;
	std::string output_filename;
	double scale[2];

	std::cout << "Enter image file: ";
	std::cin >> filename;
	
	std::cout << "X scale: ";
	std::cin >> scale[0];

	std::cout << "Y scale: ";
	std::cin >> scale[1];

	std::cout << "Output file name: ";
	std::cin >> output_filename;

	std::ofstream output;
	output.open(output_filename);

	imageToText(filename, scale, output);
	
	output.close();
}