#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(string s) {
    vector<int> ans;
    string answer = "";
    for(auto temp : s)
    {
        int num = answer.rfind(temp); 
        if(num == -1) ans.push_back(-1);
        else ans.push_back(size(answer) - num);
        answer += temp;
    }
    return ans;
}