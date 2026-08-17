#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string cipher, int code) {
    string answer = "";
    for(int i = 0; i < size(cipher); i++)
    {
        if(i % code == (code - 1)) answer += cipher[i];
    }
    return answer;
}