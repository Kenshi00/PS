#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> numlist, int n) {
    vector<int> answer;
    sort(numlist.begin(), numlist.end());
    while(size(numlist) != 0)
    {
        int temp = 99999, val = 0, index = -1;
        for(int i = 0; i < size(numlist); i++)
        {
            if(temp >= abs(numlist[i] - n))
            {
                temp = abs(numlist[i] - n);
                val = numlist[i];
                index = i;
            }
        }
        answer.push_back(val);
        numlist.erase(numlist.begin() + index);
    }
    return answer;
}