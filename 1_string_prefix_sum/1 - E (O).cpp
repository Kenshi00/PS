// 1 - B / 알파벳 개수
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string answer = "";
    vector<string> v;
    int arr[26] = {0, };
    int num;
    string temp;
    cin >> num;
    for(int i = 0; i < num; i++)
    {
        cin >> temp;
        v.push_back(temp);
    }
    for(auto s : v)
    {
        arr[s[0] - 'a']++;
    }
    for(int i = 0; i < size(arr); i++)
    {
        if(arr[i] >= 5) answer += (i + 'a');
    }
    sort(answer.begin(), answer.end());
    if(size(answer)) cout << answer;
    else cout << "PREDAJA";
}