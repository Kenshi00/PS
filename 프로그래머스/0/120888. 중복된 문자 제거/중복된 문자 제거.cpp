#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string my_string) {
    string answer = "";
    for(auto s : my_string)
    {
        if(answer.find(s) == string::npos)
        {
            answer += s;
        }
        
    }
    return answer;
}