#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> numbers, string direction) {
    vector<int> answer;
    if(direction == "right")
    {
        int t = numbers[size(numbers) - 1];
        answer.push_back(t);
        for(int i = 0; i < size(numbers) - 1; i++)
        {
            answer.push_back(numbers[i]);
        }
    }
    else
    {
        int t = numbers[0];
        for(int i = 1; i < size(numbers); i++)
        {
            answer.push_back(numbers[i]);
        }
        answer.push_back(t);
    }
    return answer;
}