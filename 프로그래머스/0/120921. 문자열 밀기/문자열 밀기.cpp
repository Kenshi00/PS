#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(string A, string B) {
    int answer = 0, flag = 0;
    if(A == B) 
    {
        flag = 1;
        answer = 0;
    }
    else
    {
        for(auto s : A)
        {
            answer++;
            rotate(A.begin(), A.begin() + (size(A) - 1), A.end());
            if(A == B)
            {
                flag = 1;
                break;
            }
        }    
    }
    if(flag == 0) answer = -1;
    return answer;
}