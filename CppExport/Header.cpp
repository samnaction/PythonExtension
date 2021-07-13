#include "pch.h"
#include "Header.h"
#include <cmath>

const double e = 2.7182818284590452353602874713527;
double sin_impl(double x)
{
    return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x));
}
