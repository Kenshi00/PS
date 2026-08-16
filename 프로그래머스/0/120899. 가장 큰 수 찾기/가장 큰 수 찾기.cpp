#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    int max = -1, index = -1;
    for(int i = 0; i < size(array); i++)
    {
        if(max < array[i])
        {
            max = array[i];
            index = i;
        }
    }
    answer.push_back(max);
    answer.push_back(index);
    
    return answer;
}