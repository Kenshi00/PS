#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> board) {
    int answer = 0;
    int n = size(board[0]);
    vector<vector<int>> temp(n,vector<int>(n, 0));
    // 8가지 방향 탐색
    int dx[] = {0, 1, 0, -1, -1, -1, 1, 1};
    int dy[] = {1, 0, -1, 0, -1, 1, 1, -1};
    
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(board[i][j] == 1)
            {
                temp[i][j] = 1;
                for(int k = 0; k < 8; k++)
                {
                    // nx, ny가 배열 범위를 넘어가는지 체크
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if(0 <= nx && nx < n && 0 <= ny && ny < n) temp[nx][ny] = 1;
                }
            }
        }
    }
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(temp[i][j] == 0) answer++;
        }
    }
    return answer;
}