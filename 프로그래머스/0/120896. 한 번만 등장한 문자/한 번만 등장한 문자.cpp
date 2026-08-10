#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

string solution(string s) {
    string answer = "";
    map<char,int> m;
    for(auto c : s)
    {
        m[c]++;
    }
    for(auto c : m)
    {
        if(c.second == 1) answer += c.first;
    }
    sort(answer.begin(), answer.end());
    return answer;
}