#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(vector<int> food) {
    string answer = "";
    for(int i = 1; i < size(food); i++)
    {
        int temp = food[i] / 2;
        for(int j = 0; j < temp; j++)
        {
            answer += to_string(i);
        }
    }
    string temp = answer;
    reverse(temp.begin(),temp.end());
    answer += (to_string(0) + temp);
    return answer;
}