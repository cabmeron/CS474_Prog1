#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>
#include <unordered_map>
#include <vector>
#include <cmath>
#include "image.h"

using namespace std;

int readImageHeader(char[], int &, int &, int &, bool &);
int readImage(char[], ImageType &);
int writeImage(char[], ImageType &);

int main(int argc, char *argv[])
{
    int i, j;
    int M, N, Q;
    bool type;
    int val;
    int subSampleFactor;

    // read original image header

    readImageHeader(argv[1], N, M, Q, type);

    double totalPixelCount = M * N;

    // allocate memory for the original image array

    ImageType originalImage(N, M, Q);

    // read original image

    readImage(argv[1], originalImage);

    /* unordered maps for storing pixel intensity frequencies, intensity probabilities,
    and equalized frequencies
    */

    unordered_map<int, int> intensityFrequencies;
    unordered_map<int, double> intensityProbability;
    unordered_map<int, int> equalizedFrequencies;

    // Fill unorded map with keys and empty values

    for (i = 0; i <= Q; i++)
    {
        intensityFrequencies[i] = 0;
        intensityProbability[i] = 0;
        equalizedFrequencies[i] = 0;
    }

    // Count frequencies from input image

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < M; j++)
        {
            originalImage.getPixelVal(i, j, val);
            intensityFrequencies[val] = intensityFrequencies[val] + 1;
        }
    }

    // Calculate and store intensity probabilities

    for (i = 0; i < Q; i++)
    {
        intensityProbability[i] = intensityFrequencies[i] / totalPixelCount;
    }

    // Vector to grow as we iterate through intensity values for summation

    vector<int> newPixel;
    newPixel.push_back(0);

    // Summation for new equalized pixel values

    for (int j = 0; j < Q; j++)
    {
        double newPixelVal = 0;
        for (i = 0; i < newPixel.size(); i++)
        {
            newPixelVal += intensityProbability[i];
        }

        // De-normalize
        newPixelVal *= (Q - 1);

        // Truncate
        newPixelVal = round(newPixelVal);

        equalizedFrequencies[j] = newPixelVal;

        if (j > 0)
        {
            newPixel.push_back(j);
        }
    }

    // Map original pixel values to new equalized values

    for (i = 0; i < N; i++)
    {
        for (j = 0; j < M; j++)
        {
            originalImage.getPixelVal(i, j, val);
            int equalizedPixelVal = equalizedFrequencies[val];

            originalImage.setPixelVal(i, j, equalizedPixelVal);
        }
    }

    // Write new values over original image memory allocation

    writeImage(argv[2], originalImage);

    return (1);
}
