#include <string>
#include <vector>
#include <sstream>
#include <bits/stdc++.h>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    stringstream ss(my_string);
    string first,word,op;
    
    ss >> first;
    int temp = stoi(first);
    while(ss >> op >> word)
    {
        if(op == "+") temp += stoi(word);
        else temp -= stoi(word);    
    }
    return temp;
}