#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    int answer = 1;
    int slice_sum = slice;
    while(slice_sum < n)
    {
        slice_sum += slice;
        answer++;
    }
    return answer;
}