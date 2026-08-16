#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int n, vector<int> numlist) {
    vector<int> answer;
    for(auto s : numlist)
    {
        if(s % n == 0) answer.push_back(s);
    }
    return answer;
}