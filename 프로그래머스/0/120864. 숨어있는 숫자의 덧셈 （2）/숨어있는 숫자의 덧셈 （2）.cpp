#include <string>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

int solution(string my_string) {
    // to_string(), stoi()
    int answer = 0;
    for(int i = 0; i < my_string.size(); i++)
    {
        if(!('0' <= my_string[i] && my_string[i] <= '9'))
        {
            my_string[i] = ' ';
        }
    }
    stringstream ss(my_string);
    string num;
    while(ss >> num) answer += stoi(num);
    return answer;
}