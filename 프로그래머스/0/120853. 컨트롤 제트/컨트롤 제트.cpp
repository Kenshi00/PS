#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string s) {
    int answer = 0;
    stringstream ss(s);
    string word;
    int past = 0, temp;
    while(ss >> word)
    {
        if(word != "Z") 
        {
            answer += stoi(word);
            past = stoi(word);
        }
        else
        {
            answer -= past;
        }
    }
    return answer;
}