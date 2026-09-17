#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    int rt = size(t) - size(p);
    for(int i = 0; i <= rt; i++)
    {
        string temp = t.substr(i,size(p));
        if(p >= temp) answer++;
    }
    return answer;
}