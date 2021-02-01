#include <opencv2/opencv.hpp>
#include <string>
#include <fstream>

#include "ImageToText.h"

#define brightness "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?+-~i!Il;:,^.' "


int imageToText(std::string& filename, unsigned int* scale, std::ofstream& output) {
	cv::Mat img;
	img = cv::imread(filename);

	if (img.empty()) {
		return -1;
	}

	cv::cvtColor(img, img, cv::COLOR_BGR2GRAY, 1);
	cv::resize(img, img, cv::Size(std::round(img.rows / scale[0]), std::round(img.cols / scale[1])), cv::INTER_NEAREST);

	for (int x = 0; x < img.rows; x++) {
		for (int y = 0; y < img.cols; y++) {
			char pixel = brightness[(img.at<uchar>(x, y) * 64) >> 8];
			output << pixel;
		}
		output << '\n';
	}

	return -1;
}
