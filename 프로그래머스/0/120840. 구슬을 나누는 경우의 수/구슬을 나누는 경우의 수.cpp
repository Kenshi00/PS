#include <string>
#include <vector>
#include <iostream>
using namespace std;

// int Factorial(int n)
// {
//     if(n <= 1) return 1;
//     else return n * Factorial(n - 1);
// }

// int Permutation(int n, int m)
// {
//     return (Factorial(n) / Factorial(n-m)) / Factorial(m);
// }

int solution(int n, int m) {
    double answer;
    double temp = 1, temp2 = 1;
    for(double i = n - m + 1; i <= n; i++)
    {
        temp *= i;
    }
    for(double i = 1; i <= m; i++)
    {
        temp2 *= i;
    }
    answer = temp / temp2;
    return answer;
}