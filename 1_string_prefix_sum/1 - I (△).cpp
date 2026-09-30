// O X △
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5

// △인 이유는, 특수 테스트 케이스인 시간초과되는 케이스를 통과하지 못함
// for문을 두번쓰면 100000 x 100000 이 되기 때문에
// for문으로 입력받을때 처음에, 숫자 -> 문자를 위한 벡터와
// 문자 -> 숫자를 위한 map<string,int>, m[문자]=숫자 도 작성
// 입력받을때 한번에 변수 두개를 만드는 아이디어 생각못함

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    vector<string> v;
    map<string, int> m;
    for(int i = 0; i < N; i++)
    {
        string temp;
        cin >> temp;
        v.push_back(temp);
        m[temp] = i + 1;
    }
    for(int i = 0; i < M; i++)
    {
        string temp;
        cin >> temp;
        if('0' <= temp[0] && temp[0] <= '9')
        {
            cout << v[stoi(temp)-1] << '\n';
        }
        else
        {
            cout << m[temp] << '\n';
        }
    }
    
    return 0;
}