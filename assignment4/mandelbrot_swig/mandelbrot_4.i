%module mandelbrot
%{
  #define SWIG_FILE_WITH_INIT
  #include "mandelbrot_4.h"
%}

%include "numpy.i"
%init %{
import_array();
%}

%apply (int DIM1, double* IN_ARRAY1, int ARGOUT_ARRAY2[Nx][Ny]), {(int Nx, double *real), (int Ny, double *imag), (int Nx, int Ny, int** iterations )};
%include mandelbrot_4.h

