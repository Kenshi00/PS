#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> keyinput, vector<int> board) {
    vector<int> answer;
    // up down left right
    int dx[4] = {0,0,-1,1};
    int dy[4] = {1,-1,0,0};
    int x = 0, y = 0;
    for(int i = 0; i < keyinput.size(); i++)
    {
        int nx, ny;
        if(keyinput[i] == "up")
        {
            nx = x + dx[0];
            ny = y + dy[0];    
        }
        else if(keyinput[i] == "down")
        {
            nx = x + dx[1];
            ny = y + dy[1];    
        }
        else if(keyinput[i] == "left")
        {
            nx = x + dx[2];
            ny = y + dy[2];    
        }
        else if(keyinput[i] == "right")
        {
            nx = x + dx[3];
            ny = y + dy[3];    
        }
        
        if(-(board[0]/2) <= nx && nx <= (board[0]/2)) x = nx;
        if(-(board[1]/2) <= ny && ny <= (board[1]/2)) y = ny;
        //cout << x << " " << y << "\n";
    }
    answer.push_back(x);
    answer.push_back(y);
    return answer;
}