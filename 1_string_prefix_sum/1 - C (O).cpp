// 1 - C / 트럭주차
// O <= X < O -> 이런식으로 [O,O) 이상,미만으로 설정해야한다.

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int A,B,C;
    int answer = 0;
    cin >> A >> B >> C;
    int cnt[101] = {0,};
    int a, b;
    for(int i = 0; i < 3; i++)
    {
        cin >> a >> b;
        for(int i = a; i < b; i++)
        {
            cnt[i]++;
        }
    }
    for(int i = 0; i < size(cnt); i++)
        {
            if(cnt[i] == 1) answer += A * 1;
            else if(cnt[i] == 2) answer += B * 2;
            else if(cnt[i] == 3) answer += C * 3;
        }
    cout << answer;
}