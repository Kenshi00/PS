#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

string solution(string letter) {
    string answer = "";
    unordered_map<string, char> morse = { 
        {".-", 'a'}, {"-...", 'b'}, {"-.-.", 'c'}, {"-..", 'd'}, {".", 'e'},
        {"..-.", 'f'}, {"--.", 'g'}, {"....", 'h'}, {"..", 'i'}, {".---", 'j'},
        {"-.-", 'k'}, {".-..", 'l'}, {"--", 'm'}, {"-.", 'n'}, {"---", 'o'},
        {".--.", 'p'}, {"--.-", 'q'}, {".-.", 'r'}, {"...", 's'}, {"-", 't'},
        {"..-", 'u'}, {"...-", 'v'}, {".--", 'w'}, {"-..-", 'x'}, {"-.--", 'y'},
        {"--..", 'z'}
    };
    string temp;
    for(int i = 0; i < letter.size(); i++)
    {
        if(letter[i] != ' ') temp += letter[i];
        else if(letter[i] == ' ')
        {
            answer += morse[temp];
            temp = "";
        }
    }
    answer += morse[temp];
    return answer;
}