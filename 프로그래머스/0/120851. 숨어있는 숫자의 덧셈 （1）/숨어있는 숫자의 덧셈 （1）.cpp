#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    for(auto c : my_string)
    {
        if('0' <= c && c <= '9')
        {
            answer += (c - '0');
        }
    }
    return answer;
}