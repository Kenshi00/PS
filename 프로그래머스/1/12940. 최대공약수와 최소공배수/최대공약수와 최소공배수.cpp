#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;
// gcd - 최대공약수 , lcd - 최소공배수
vector<int> solution(int n, int m) {
    vector<int> answer;
    answer.push_back(gcd(n,m));
    answer.push_back(lcm(n,m));
    
    return answer;
}