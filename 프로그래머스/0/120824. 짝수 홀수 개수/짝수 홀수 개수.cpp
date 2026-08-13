#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer(2,0);
    for(auto n : num_list)
    {
        if(n & 1) answer[1]++;
        else answer[0]++;
    }
    return answer;
}