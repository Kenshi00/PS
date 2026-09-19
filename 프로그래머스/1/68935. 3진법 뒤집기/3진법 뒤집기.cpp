#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 0;
    string temp = "";
    while(n != 0)
    {
        temp += to_string(n % 3);
        n /= 3;
    }
    cout << temp;
    int mul = 1;
    for(int i = size(temp) - 1; i >= 0 ; i--)
    {
        answer += (temp[i] - '0') * mul;
        mul *= 3;
    }
    return answer;
}