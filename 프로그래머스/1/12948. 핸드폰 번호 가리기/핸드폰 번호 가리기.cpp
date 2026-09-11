#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string phone_number) {
    for(int i = 0; i < size(phone_number) - 4; i++)
    {
        phone_number[i] = '*';
    }
    
    return phone_number;
}