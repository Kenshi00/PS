#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

int solution(vector<int> array, int n) {
    int answer = 0;
    int m = 99999;
    for(auto i : array)
    {
        if(m > abs(n-i))
        {
            m = abs(n - i);
            answer = i;
        }
        else if(m == abs(n - i))
        {
            answer = min(answer, i);
        }
    }
    return answer;
}