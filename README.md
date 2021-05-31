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
* solve - is used to solve differential equations, returns a list of results and a list of time points.
* solve_time - is used to solve differential equations, returns the last result and the time needed for the calculation. The results are not saved, so only the time needed to calculate the result at a given point is counted.
* solve_system - is used to solve a system of differential equations. Returns a list with vectors and a list with time points.

CalcError:
* absolute - it is used to calculate the absolute error
* relative - it is used to calculate the relative error
