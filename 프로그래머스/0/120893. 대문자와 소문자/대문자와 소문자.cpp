#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for(auto c : my_string)
    {
        if(islower(c)) answer += toupper(c);
        else answer += tolower(c);
    }
    return answer;
}