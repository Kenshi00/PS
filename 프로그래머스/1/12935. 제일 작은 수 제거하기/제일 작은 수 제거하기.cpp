#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    if(size(arr) == 1) answer.push_back(-1);
    else
    {
        int m = 999999;
        int index = -1;
        for(int i = 0; i < size(arr); i++)
        {
            if(m > arr[i])
            {
                m = arr[i];
                index = i;
            }
        }
        arr.erase(arr.begin() + index);
        answer = arr;
    }
    return answer;
}