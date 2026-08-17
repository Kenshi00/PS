#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> solution(vector<int> num_list, int n) {
    vector<vector<int>> answer;
    vector<int> temp;
    int cnt = 0;
    for(int i = 0; i < size(num_list); i++)
    {
        if(cnt == n)
        {
            answer.push_back(temp);
            temp.clear();
            cnt = 0;
        }
        temp.push_back(num_list[i]);
        cnt++;
    }
    answer.push_back(temp);
    return answer;
}