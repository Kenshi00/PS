#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<int> v(n + 1, 0); // 0~10 index의 배열만듬
    for(int i = 1; i <= n; i++)
    {
        for(int j = i; j <= n; j += i) v[j]++;
    }
    for(int i = 1; i <= n; i++) if(v[i] > 2) answer++;
    return answer;
}