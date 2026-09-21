// O X △
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // 부분합 psum 이용해야할듯
    // 1,-6, -13,-9,3,10,20,21,5
    int num1, num2;
    cin >> num1 >> num2;
    vector<int> v;
    for(int i = 0; i < num1; i++)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    int temp = num1 - num2 + 1; 
    int arr[temp] = {0, };
    for(int i = 0; i < num2; i++)
    {
        arr[0] += v[i];
    }
    for(int i = 1; i < temp; i++)
    {
        arr[i] = (arr[i - 1] + v[i + num2 - 1] - v[i - 1]);
    }
    
    int answer = -21000000;
    for(int n : arr)
    {
        if(n > answer) answer = n;
    }
    cout << answer;
    return 0;
}