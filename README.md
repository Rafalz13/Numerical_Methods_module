# Module with algorithms for solving differential equations

Files in repository:
* numericalODE - main module file
* main - the file contains an example module usage
* functions - the file contains functions needed to work with the module
* Tests - the file contains tests and analysis using the module

numericalODE:
--------------
It consists of the main class RR and the derived classes Euler and RK4. Euler implements an algorithm for solving differential equations using the Euler method. RK4 implements Runge-Kutta's fourth order algorithm for solving differential equations. Additionally, there is an Blad class in the module.

The classes consist of three methods:
* licz - is used to solve differential equations, returns a list of results and a list of time points.
* licz_czas - is used to solve differential equations, returns the last result and the time needed for the calculation. The results are not saved, so only the time needed to calculate the result at a given point is counted.
* licz_uklad_rownan - is used to solve a system of differential equations. Returns a list with vectors and a list with time points.

Blad:
* licz_bezwzg - it is used to calculate the absolute error
* licz_wzg - it is used to calculate the relative error
