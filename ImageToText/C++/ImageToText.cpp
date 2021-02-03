#include <opencv2/opencv.hpp>
#include <string>
#include <fstream>

#include "ImageToText.h"

#define brightness "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?+-~i!Il;:,^.' "


int imageToText(std::string& filename, double* scale, std::ofstream& output) {
	cv::Mat img;
	img = cv::imread(filename, 0);

	if (img.empty()) {
		return -1;
	}

	cv::resize(img, img, cv::Size(std::round(img.rows / scale[0]), std::round(img.cols / scale[1])), cv::INTER_NEAREST);

	std::string output_str;
	int pos = 0;
	output_str.resize(img.rows * (img.cols + 1));
	for (int x = 0; x < img.rows; x++) {
		for (int y = 0; y < img.cols; y++) {
			output_str[pos] = brightness[(img.at<uchar>(x, y) * 64) >> 8];
			pos++;
		}
		output_str[pos] = '\n';
		pos++;
	}

	output << output_str;

	return 0;
}