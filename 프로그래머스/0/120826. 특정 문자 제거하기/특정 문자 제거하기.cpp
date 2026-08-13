#include <string>
#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    string answer = "";
    for(auto c : my_string)
    {
        char l = letter[0];
        if(c != l) answer += c;
    }
    return answer;
}