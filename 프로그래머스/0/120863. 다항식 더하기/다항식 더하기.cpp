#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string polynomial) {
    string answer = "";
    stringstream ss(polynomial);
    string word = "";
    int num = 0;
    int temp = 0;
    while(ss >> word)
    {
        // 사이즈가 1보다 크고, x가 포함되어있으면 계수를 저장해놓는다.
        // x만 포함되어 있으면 계수 1을 더함.
        // 나머지는 int로 변환해서 값 더하기
        // 연산자는 넘긴다
        if(size(word) >= 2 && word.find("x") != string::npos)
        {
            temp += stoi(word.substr(0, size(word) - 1));
        }
        else if(word == "x")
        {
            temp += 1;
        }
        else if(word == "+")
        {
            continue;
        }
        else
        {
            num += stoi(word);
        }
    }
    
    // 결과 출력
    if(temp != 0 && num != 0)
    {
        if(temp == 1) answer += ("x + " + to_string(num));
        else answer += (to_string(temp) + "x + " + to_string(num));
    }
    else if(temp != 0 && num == 0)
    {
        if(temp == 1) answer += "x";
        else answer += (to_string(temp) + "x");
    }
    else if(temp == 0 && num != 0)
    {
        answer += to_string(num); 
    }
    else
    {
        answer += "0";
    }
    return answer;
}