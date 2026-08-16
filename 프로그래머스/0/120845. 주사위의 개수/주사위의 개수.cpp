#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> box, int n) {
    int answer = 0;
    int row = box[0] / n;
    int col = box[1] / n;
    int height = box[2] / n;
    answer = row * col * height;
    return answer;
}