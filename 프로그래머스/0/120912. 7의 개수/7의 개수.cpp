#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    for(auto i : array)
    {
        int temp = 0;
        while(i)
        {
            if(i % 10 == 7) answer++;
            i /= 10;
        }
    }
    return answer;
}