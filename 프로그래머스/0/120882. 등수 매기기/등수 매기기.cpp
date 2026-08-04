#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<vector<int>> score) {
    // 작으면 증가시킴
    // 150, 140, 110, 130
    // 1 1 1 1
    // 1 2 2 2
    // 1 2 3 3
    // 1 2 3 3
    // 1 2 4 3
    vector<int> sum;
    for(int i = 0; i < score.size(); i++)
    {
        sum.push_back(score[i][0] + score[i][1]);
    }
    vector<int> answer(sum.size(),1);
    for(int i = 0; i < sum.size(); i++)
    {
        for(int j = 0; j < sum.size(); j++)
        {
            if(sum[i] > sum[j]) answer[j] += 1;
        }
    }
    
    return answer;
}