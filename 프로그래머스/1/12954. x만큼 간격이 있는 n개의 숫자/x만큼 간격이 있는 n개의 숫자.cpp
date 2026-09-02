#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int temp = x;
    for(int i = 1; i <= n; i++)
    {
        answer.push_back(x);
        x += temp;
    }
    return answer;
}