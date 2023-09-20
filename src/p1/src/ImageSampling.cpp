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

    int subRow, subCol = 0;

    int row, col, Q2;

    // read image header
    readImageHeader(argv[1], N, M, Q, type);

    // allocate memory for the image array

    ImageType image(N, M, Q);

    // read image
    readImage(argv[1], image);

    cout << "Enter Sub Sampling Factor: ";
    cin >> subSampleFactor;

    ImageType subSampleImage(floor(N / subSampleFactor), floor(M / subSampleFactor), Q);

    subSampleImage.getImageInfo(row, col, Q2);

    for (i = 0; i < N; i += subSampleFactor)
    {

        for (j = 0; j < M; j += subSampleFactor)
        {

            image.getPixelVal(i, j, val);

            subSampleImage.setPixelVal(subRow, subCol, val);

            // Fills in some values before sampled for new image. Need to run this loop after doing sub Sample operation then write to file

            // for (k = j; k < k + subSampleFactor && k < floor(row / subSampleFactor) - subSampleFactor; k++)
            // {
            //     image.setPixelVal(i, k, val);
            // }

            subCol += 1;
        }
        subCol = 0;
        subRow += 1;
    }

    int l, m = 0;

    for (i = 0; i < N; i += subSampleFactor)
    {

        for (j = 0; j < M; j += subSampleFactor)
        {
            subSampleImage.getImageInfo(l, m, val);
            for (k = j; k < k + subSampleFactor && k < floor(row / subSampleFactor) - subSampleFactor; k++)
            {
                image.setPixelVal(i, k, val);
            }
        }
        l += 1;
        m += 1;
    }

    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            image.getPixelVal(i, j, val);
            cout << "Val @ [" << i << "][" << j << "]: " << val << endl;
        }
    }

    cout << "Sub Sampled Image Values: " << endl;

    for (i = 0; i < 2; i++)
    {
        for (j = 0; j < 2; j++)
        {
            subSampleImage.getPixelVal(i, j, val);
            cout << "Val @ [" << i << "][" << j << "]: " << val << endl;
        }
    }

    // writeImage(argv[2], subSampleImage);

    // threshold image

    // for (i = 0; i < N; i++ )
    //     for (j = 0; j < M; j++)
    //     {
    //         image.getPixelVal(i, j, val);
    //         if (val < thresh)
    //             image.setPixelVal(i, j, 255);
    //         else
    //             image.setPixelVal(i, j, 0);
    //     }

    // write image
    // writeImage(argv[2], image);

    return (1);
}
