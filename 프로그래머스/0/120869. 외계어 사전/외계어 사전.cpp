#include <string>
#include <vector>

using namespace std;

int solution(vector<string> spell, vector<string> dic) {
    for(int i = 0; i < dic.size(); i++)
    {
        int cnt = 0;
        for(int j = 0; j < spell.size(); j++)
        {
            if(dic[i].find(spell[j]) != -1) cnt += 1;
        }
        if(cnt == spell.size()) return 1;
    }
    return 2;
}