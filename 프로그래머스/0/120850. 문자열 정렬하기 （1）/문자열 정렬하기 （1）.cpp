#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(string my_string) {
    vector<int> answer;
    for(auto s : my_string)
    {
        if('0' <= s && s <= '9')
        {
            answer.push_back(s-'0');
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}