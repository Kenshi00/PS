// O X △
#include <bits/stdc++.h>
using namespace std;
// 빌드는 Ctrl + F5


vector<int> v;
int n1, n2, sum;


void permutation(int n, int r, int depth)
{
    if(r == depth)
    {
        if(sum - v[0] - v[1] == 100)
        {
            vector<int> result(v.begin() + 2, v.end());
            sort(result.begin(), result.end());

            for(int num : result) cout << num << '\n';
            
            exit(0);
        }
        return;
    }
    
    for(int i = depth; i < n; i++)
    {
        swap(v[i], v[depth]);
        permutation(n, r, depth + 1);
        swap(v[i], v[depth]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for(int i = 0; i < 9; i++)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
        sum += temp;
    }

    permutation(9,2,0);

    return 0;
}