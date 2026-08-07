#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n) {
    int answer = 1;
    int temp = 1;
    while(n >= temp)
    {
        answer++;
        temp *= answer;
    }
    return answer - 1;
}