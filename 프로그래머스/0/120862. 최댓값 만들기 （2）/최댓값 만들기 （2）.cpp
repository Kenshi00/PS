#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> numbers) {
    int max = numbers[0] * numbers[1];
    for(int i = 0; i < size(numbers); i++)
    {
        for(int j = i + 1; j < size(numbers); j++)
        {
            int temp = numbers[i] * numbers[j];
            if(max < temp) max = temp;
        }
    }
    return max;
}