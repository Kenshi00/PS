#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    sort(numbers.begin(), numbers.end());
    int s = size(numbers);
    answer = numbers[s - 2] * numbers[s - 1];
    return answer;
}