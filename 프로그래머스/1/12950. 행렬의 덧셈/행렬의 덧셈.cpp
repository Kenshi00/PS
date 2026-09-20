#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer(size(arr1), vector<int>(size(arr1[0]), 0));
    for(int i = 0; i < size(arr1); i++)
    {
        for(int j = 0; j < size(arr1[0]); j++)
        {
            answer[i][j] = arr1[i][j] + arr2[i][j];
        }
    }
    return answer;
}