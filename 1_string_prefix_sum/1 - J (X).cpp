// O X △
#include <bits/stdc++.h>
using namespace std;

// 경우의 수를 옷 부위마다 구해서 곱해주는 아이디어
// 나는 계속 순열 조합생각함
// cin >> a >> b 로, hat headgear같은 공백 문자열 입력 구분 가능
// headgear가 두개면, (1번 기어 입기 + 2번 기어 입기 + 둘다 안입기)
// N개면 N + 1개의 경우의 수 존재 (부위마다 각각)
// (N+1)(M+1) -1  -> -1을 붙여줘야 하더라..
// map의 key와 value에는 각각 m.first, m.second로 접근함

// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tc;
    cin >> tc;
    for(int i = 0; i < tc; i++)
    {
        int n, answer = 1;
        cin >> n;
        map<string, int> m;
        for(int i = 0; i < n; i++)
        {
            string temp,category;
            cin >> temp >> category;
            m[category]++;
        }
        for(auto k : m)
        {
            answer *= (k.second + 1);
        }
        cout << answer - 1 << '\n';
    }
    return 0;
}