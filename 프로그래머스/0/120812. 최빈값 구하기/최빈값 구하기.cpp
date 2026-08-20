#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    vector<int> v(1001,0);
    for(auto i : array) v[i]++;
    int m = -1;
    for(int i = 0; i < size(v); i++)
    {
        if(v[i] > m)
        {
            answer = i;
            m = v[i];
        }
        else if(v[i] == m) answer = -1;
    }
    return answer;
}