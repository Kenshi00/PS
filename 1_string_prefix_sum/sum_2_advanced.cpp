// 구현 2 하얀칸

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<string> v;
    int answer = 0;
    for(int i = 0; i < 8; i++)
    {
        string temp;
        cin >> temp;
        v.push_back(temp);
    }
    for(int i = 0; i < 8; i++)
    {
        if(i % 2 == 0)
        {
            for(int j = 0; j < 8; j+=2)
            {
                if(v[i][j] == 'F') answer++;
            }
        }
        else
        {
            for(int j = 1; j < 8; j+=2)
            {
                if(v[i][j] == 'F') answer++;
            }
        }
    }
    cout << answer;
    return 0;
}