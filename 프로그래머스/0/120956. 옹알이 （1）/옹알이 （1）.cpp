#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> v = {"aya", "ye", "woo", "ma"};
    for(auto& s : babbling)
    {
        // aya
        for(auto k : v)
        {
            if(s.find(k) != string::npos)
            {
                int i = s.find(k);
                //s = s.substr(i, size(k));
                s = s.substr(0,i) + " " + s.substr(i + size(k));
            }
        }
        int flag = 1;
        for(auto c : s)
        {
            if('a' <= c && c <= 'z') flag = 0;
        }
        if(flag) answer++;
    }
    return answer;
}