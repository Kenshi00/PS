#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    sort(d.begin(), d.end());
    for(int i = 0; i < size(d); i++)
    {
        int temp = budget - d[i];
        if(temp >= 0)
        {
            budget = temp;
            answer++;
        }
        else break;
    }
    return answer;
}