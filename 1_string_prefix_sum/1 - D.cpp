// 1 - B / 알파벳 개수
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int answer;
    string input;
    cin >> input;
    string temp = input;
    reverse(input.begin(), input.end());
    if(temp == input) answer = 1;
    else answer = 0;
    cout << answer;
    return 0;
}