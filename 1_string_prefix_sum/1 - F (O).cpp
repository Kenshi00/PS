// 1 - B / 알파벳 개수
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string answer = "";
    string temp;
    //cin >> temp;
    getline(cin, temp);
    for(auto c : temp)
    {
        if(('A' <= c && c <= 'M') || ('a' <= c && c <= 'm'))
        {
            answer += c + 13;
        }
        else if (('N' <= c && c <= 'Z') || ('n' <= c && c <= 'z'))
        {
            answer += c - 13;
        }
        else
        {
            answer += c;
        }
    }
    cout << answer;
    return 0;
}