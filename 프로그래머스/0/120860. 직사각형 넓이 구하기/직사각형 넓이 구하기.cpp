#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> dots) {
    int x1, x2, y1, y2, rec;
    x1 = dots[0][0];
    y1 = dots[0][1];
    for(int i = 1; i < 4; i++)
    {
        if(dots[i][0] != x1) x2 = dots[i][0];
        if(dots[i][1] != y1) y2 = dots[i][1];
    }
    
    rec = (x2-x1) * (y2-y1);
    
    if(rec < 0) return -rec;
    else return rec;
}