/*
누적합
*/

/*
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int a[100004], b, c, psum[100004], n, m;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 1; i <= n; i++)
    {
        cin >> a[i];
        // 누적합 psum 배열 정의 (중요!)
        psum[i] = psum[i - 1] + a[i];
    }
    for(int i = 0; i < m; i++)
    {
        cin >> b >> c;
        cout << psum[c] - psum[b - 1] << "\n";
    }
    return 0;
}

*/

/*
    구현
*/

/*
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    string dopa = "umzunsik";
    string temp1 = dopa.substr(0, 3);
    cout << temp1 << "\n";
    reverse(dopa.begin(), dopa.end());
    cout << dopa << '\n';
    dopa += "umzunsik";
    cout << dopa << '\n';
    return 0;
}

*/


#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int num;
    double answer = 0;
    cin >> num;
    vector<int> v(num);
    for(int i = 0; i < num; i++)
    {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
    for(double i : v)
    {
        cout << i << " ";
        answer += i;
    }
    cout << fixed << setprecision(2) << answer / 5 << "\n";
    return 0;
}


/*
빠른 템플릿
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    return 0;
}
*/