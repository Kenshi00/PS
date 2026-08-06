#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

int solution(string before, string after) {
    unordered_map<char,int> before_dict;
    unordered_map<char,int> after_dict;
    
    for(auto s : before)
    {
        before_dict[s] += 1;
    }
    for(auto s : after)
    {
        after_dict[s] += 1;
    }
    for(auto s : after)
    {
        if(before_dict[s] != after_dict[s]) return 0;
    }
    return 1;
}