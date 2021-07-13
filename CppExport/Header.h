#pragma once

#ifdef CPPEXPORT_EXPORTS
#define CPPEXPORT_API __declspec(dllexport)
#else
#define CPPEXPORT_API __declspec(dllimport)
#endif

extern "C" CPPEXPORT_API double sin_impl(double x);