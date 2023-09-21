#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>

#include "image.h"

using namespace std;

int readImageHeader(char[], int &, int &, int &, bool &);
int readImage(char[], ImageType &);
int writeImage(char[], ImageType &);

int main(int argc, char *argv[])
{
    int i, j, k;
    int M, N, Q;
    bool type;
    int val;
    int subSampleFactor;

    int subI, subJ = 0;

    int N2, M2, Q2;

    // read original image header

    readImageHeader(argv[1], N, M, Q, type);

    // allocate memory for the original image array

    ImageType originalImage(N, M, Q);

    // read original image

    readImage(argv[1], originalImage);

    // get sub sample factors from user

    cout << "Enter Sub Sampling Factor: ";
    cin >> subSampleFactor;

    // allocate memory for sub sample image array

    ImageType subSampleImage(floor(N / subSampleFactor), floor(M / subSampleFactor), Q);

    // read sub sample image header

    subSampleImage.getImageInfo(N2, M2, Q2);

    // Fill sub sample image pixel values

    for (i = 0; i < N; i += subSampleFactor)
    {

        for (j = 0; j < M; j += subSampleFactor)
        {

            originalImage.getPixelVal(i, j, val);
            subSampleImage.setPixelVal(subI, subJ, val);
            subJ += 1;
        }
        subJ = 0;
        subI += 1;
    }

    // allocate memory for resized image from original image header values

    ImageType resizedImage(N, M, Q);

    // Resize sub sample into original image memory

    int colIterations = 0;
    int rowIterations = 0;
    subI = 0;
    subJ = 0;

    for (i = 0; i < N; i += 1)
    {

        for (j = 0; j < M; j += 1)
        {
            if (colIterations > subSampleFactor - 1)
            {
                subJ += 1;
                colIterations = 0;
            }

            subSampleImage.getPixelVal(subI, subJ, val);

            resizedImage.setPixelVal(i, j, val);
            colIterations++;
        }
        if (rowIterations > subSampleFactor - 1)
        {
            subI += 1;
            rowIterations = 0;
        }

        colIterations = 0;
        rowIterations++;
        subJ = 0;
    }

    writeImage(argv[2], subSampleImage);
    writeImage(argv[3], resizedImage);

    std::cout << "Image Sub Sampling of size: " << subSampleFactor << " performed" << std::endl;
    std::cout << "Sub sampled image of size: "
              << "[" << N2 << "]"
              << " by "
              << "[" << M2 << "]" << std::endl;

    return (1);
}
