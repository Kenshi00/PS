#include <string>
#include <vector>

using namespace std;

vector<string> solution(string my_str, int n) {
    vector<string> answer;
    while(size(my_str) > n)
    {
        answer.push_back(my_str.substr(0, n));
        my_str = my_str.substr(n);
    }
    answer.push_back(my_str);
    return answer;
}