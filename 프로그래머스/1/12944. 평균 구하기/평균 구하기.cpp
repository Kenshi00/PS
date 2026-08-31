#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    answer = accumulate(arr.begin(), arr.end(), 0);
    answer /= size(arr);
    return answer;
}