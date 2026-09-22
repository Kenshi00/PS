// 1 - B / 알파벳 개수
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string str;
    cin >> str;
    int abc[26] = {0,};
    for(int i = 0; i < size(str); i++)
    {
        abc[str[i] - 'a']++;
    }
    for(int i : abc)
    {
        cout << i << " ";
    }
    return 0;
}