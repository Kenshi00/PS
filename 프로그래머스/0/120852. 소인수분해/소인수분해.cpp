#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    vector<int> v(n + 1, 0);
    int num = n;
    for(int i = 2; i <= n; i++)
    {
        while(num % i == 0)
        {
            num /= i;
            v[i]++;
        }
    }
    for(int i = 1; i <= n; i++)
    {
        if(v[i] != 0) answer.push_back(i);
    }
    return answer;
}