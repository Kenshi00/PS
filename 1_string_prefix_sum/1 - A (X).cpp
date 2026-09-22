// O X △
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int answer = 0;
    vector<int> v;
    for(int i = 0; i < 9; i++)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());
    do{
        int temp = 0;
        for(int i = 0; i < 7; i++)
        {
            temp += v[i];
        }
        if(temp == 100)
        {
            for(int i = 0; i < 7; i++)
            {
                cout << v[i] << '\n';
            }
            break;
        }
    }while(next_permutation(v.begin(), v.end()));
    return 0;
}