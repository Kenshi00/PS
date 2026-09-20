#include <string>
#include <vector>
#include <bits/stdc++.h>
//65 97
using namespace std;

string solution(string s) {
    for(auto& i : s) if(isupper(i)) i -= 60;
    sort(s.begin(), s.end());
    reverse(s.begin(), s.end());
    for(auto& i : s) if(!('a' <= i && i <= 'z')) i += 60;
    return s;
}