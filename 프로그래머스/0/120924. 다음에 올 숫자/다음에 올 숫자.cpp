#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> common) {
    int answer = 0, flag = 0;
    // common의 길이가 최소 3임
    // 1. 등차수열인지 확인 -> flag = 1
    // 2. 등비수열인지 확인 -> flag = 0
    // 공차 or 공비
    int d = 0;
    
    if(common[1] - common[0] == common[2] - common[1]) flag = 1;
    if(flag == 1)
    {
        answer = common[size(common) - 1] + (common[1] - common[0]);
    }
    else
    {
        answer = common[size(common) - 1] * (common[1] / common[0]);
    }
    return answer;
}