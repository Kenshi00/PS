#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max1 = -9999, max2 = -9999;
    for(int i = 0; i < size(sizes); i++)
    {
        if(sizes[i][0] < sizes[i][1]) swap(sizes[i][0], sizes[i][1]);
        if(max1 < sizes[i][0]) max1 = sizes[i][0];
        if(max2 < sizes[i][1]) max2 = sizes[i][1];
    }
    answer = max1*max2;
    return answer;
}