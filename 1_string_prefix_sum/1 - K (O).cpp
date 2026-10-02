// O X △
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    map<char,int> m;
    for(auto c : s)
    {
        m[c]++;
    }

    int odd_cnt = 0;
    string temp;
    string answer;

    for(auto k : m)
    {
        if(k.second % 2 != 0)
        {
            odd_cnt++;
        }

        if(odd_cnt > 1)
        {
            answer = "I'm Sorry Hansoo";
            cout << answer << '\n';
            break;
        }
    }

    if(answer != "I'm Sorry Hansoo")
    {
        answer = "";
        for(auto k : m)
        {
            if(k.second % 2 != 0)
            {
                k.second -= 1;
                temp = k.first;       
            }
            k.second /= 2;
            for(int i = 0; i < k.second; i++)
            {
                answer += k.first;
            }
            //answer += (k.first * k.second);
            //string(5, "A");
        }

        sort(answer.begin(), answer.end());
        string real_answer = answer + temp;
        reverse(answer.begin(), answer.end());
        real_answer += answer;
        cout << real_answer << '\n';
    }
    return 0;
}