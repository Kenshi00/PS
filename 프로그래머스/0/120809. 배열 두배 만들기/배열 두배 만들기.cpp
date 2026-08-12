#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    //vector<int> answer;
    for(auto& i : numbers) i *= 2;
    return numbers;
}