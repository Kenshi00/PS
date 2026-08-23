#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> lines) {
    int answer = 0;
    vector<int> v(201, 0);
    for(auto arr : lines)
    {
        int start = arr[0] + 100;
        int end = arr[1] + 100;
        
        for(int i = start + 1; i <= end; i++) v[i]++;
    }
    for(int i = 0; i <= size(v); i++)
    {
        if(v[i] >= 2) answer++;
    }
    return answer;
}