// 1 - B / 알파벳 개수
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int num;
    cin >> num;
    string input;
    cin >> input;
    vector<string> v(num);
    for(int i = 0; i < num; i++)
    {
        cin >> v[i];
    }
    string front, rear;
    int flag = 0;
    for(auto c : input)
    {
        if(c == '*')
        {
            flag = 1;
            continue;
        }
        else if(flag == 0)
        {
            front += c;
        }
        else
        {
            rear += c; 
        }
    }

    for(string s : v)
    {
        if(s.find(front) == 0 && s.rfind(rear) == size(s) - size(rear))
        {
            cout << "DA" << '\n';
        }
        else
        {
            cout << "NE" << '\n';
        }
    }
    
    return 0;
}