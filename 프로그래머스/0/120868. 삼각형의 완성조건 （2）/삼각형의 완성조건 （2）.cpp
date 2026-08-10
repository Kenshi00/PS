#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    int min_val, max_val;
    min_val = min(sides[0], sides[1]);
    max_val = max(sides[0], sides[1]);
    answer = 2 * min_val - 1;
    return answer;
}