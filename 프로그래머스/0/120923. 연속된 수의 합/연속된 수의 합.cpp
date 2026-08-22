#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int num, int total) {
    vector<int> answer;
    int medium, start;
    if(num % 2 == 1)
    {
        medium = total / num;
        start = medium - (num / 2);
        for(int i = 0; i < num; i++)
        {
            answer.push_back(start);
            start++;
        }
    }
    else
    {
        medium = total / num + 1;
        start = medium - (num / 2);
        for(int i = 0; i < num; i++)
        {
            answer.push_back(start);
            start++;
        }
    }
    // 6  15  0 1 2 3 4 5
    return answer;
}