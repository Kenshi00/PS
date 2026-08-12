#include <string>
#include <vector>
#include <algorithm> // std::reverse를 사용하기 위해 필요
#include <iostream>

using namespace std;

int bin_to_dec(string s)
{
    int val = 0;
    reverse(s.begin(), s.end());
    int m = 1;
    for(auto c : s)
    {
        if(c == '1') val += m;
        m *= 2;
    }
    return val;
}

string dec_to_bin(int i)
{
    // 0일 경우 예외처리
    if(i == 0) return "0";
    
    string val = "";
    while(i > 0)
    {
        // 6 -> 011 -> 110
        val += to_string(i % 2);
        i /= 2;
    }
    reverse(val.begin(), val.end());
    return val;
}


string solution(string bin1, string bin2) {
    string answer = "";
    int num1 = bin_to_dec(bin1);
    int num2 = bin_to_dec(bin2);
    int num3 = num1 + num2;
    answer = dec_to_bin(num3);
    return answer;
}