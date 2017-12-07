#include <mandelbrot_4.h>
#include <complex>
void mandelbrot(int Nx, double *real, int Ny, double *imag,int max_escape_time, int** iterations){
	double complex c, fc, tmp;
	int iterations[Nx][Ny];
	for (int i=0;i<Nx;i++){
		for (int j=0;j<Ny;j++){
			c = real[i] + I*imag[j];
			fc = c;
			iterations[i][j] = max_escape_time;
			for (int k=0;k<max_escape_time;k++){
				tmp = fc*fc + c;
				double complex divergent = conj(tmp);
				double complex check = 2*2;
				if(divergent > check){
					if(iterations[i][j] == max_escape_time){
						iterations[i][j] = k;
					}
				}
				fc = tmp;
			}
		}
	}
}
				
