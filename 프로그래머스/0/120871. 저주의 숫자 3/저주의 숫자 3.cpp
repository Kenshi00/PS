#include <string>
#include <vector>
#include <iostream>
using namespace std;
// cnt써서 while돌리기
int solution(int n) {
    int answer = 0;
    int cnt = 0;
    while(cnt < n)
        {
            answer++;
            cnt++;
            while(answer % 3 == 0 || to_string(answer).find("3") != -1)
            {
                answer++;
            }
        }
    return answer;
}