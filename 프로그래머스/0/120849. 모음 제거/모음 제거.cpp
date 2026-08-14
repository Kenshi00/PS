#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    string mo = "aeiou";
    for(auto c : my_string)
    {
        if(mo.find(c) == string::npos)
        {
            answer += c;
        }
    }
    return answer;
}