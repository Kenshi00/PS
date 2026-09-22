// 구현 1 더하기
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string str;
    cin >> str;
    for(int i = 0; i < size(str); i++)
    {
        if(str[i] == ',') str[i] = ' ';
    }
    stringstream s(str);
    string word;
    int answer = 0;
    while(s >> word)
    {
        answer += stoi(word);
    }
    cout << answer;
    return 0;
}