#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<string> solution(vector<string> quiz) {
    vector<string> answer;
    for(auto s : quiz)
    {
        stringstream ss(s);
        string word;
        int num1 = 0, num2 = 0, num3 = 0;
        string op = "";
        while(ss >> word)
        {
            if(word == "+") op = "+";
            else if(word == "-") op = "-";
            else if(word == "=") continue;
            else
            {
                if(num1 == 0) num1 = stoi(word);
                else if(num2 == 0) num2 = stoi(word);
                else num3 = stoi(word);
            }
        }
        
        if(op == "+")
        {
            if(num1 + num2 == num3) answer.push_back("O");
            else answer.push_back("X");
        }
        else
        {
            if(num1 - num2 == num3) answer.push_back("O");
            else answer.push_back("X");
        }
    }
    return answer;
}