#include <string>
#include <vector>
#include <bits/stdc++.h>


using namespace std;

int solution(vector<vector<int>> dots) {
    int answer = 0;
    for(int i = 0; i < 4; i++)
    {
        for(int j = i + 1; j < 4; j++)
        {
            int a, b;
            if(i == 0 && j == 1)
            {
                a = 2;
                b = 3;
            }
            else if(i == 0 && j == 2)
            {
                a = 1;
                b = 3;
            }
            else if(i == 0 && j == 3)
            {
                a = 1;
                b = 2;
            }
            else if(i == 1 && j == 2)
            {
                a = 0;
                b = 3;
            }
            else if(i == 1 && j == 3)
            {
                a = 0;
                b = 2;
            }
            else if(i == 2 && j == 3)
            {
                a = 0;
                b = 1;
            }
            double x = dots[i][0] - dots[j][0];
            double y = dots[i][1] - dots[j][1];
            double x_a = dots[a][0] - dots[b][0];
            double y_b = dots[a][1] - dots[b][1];
            if(y / x == y_b / x_a)  answer = 1;
        }
    }
    return answer;
}