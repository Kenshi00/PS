#include <string>
#include <vector>
#include <iostream>
using namespace std;

long long solution(string numbers) {
    long long result = 0;
    vector<string> v = {
        "zero","one","two","three","four","five","six","seven","eight","nine"
    };
    vector<int> n = {0,1,2,3,4,5,6,7,8,9};
    
    while(numbers != "")
    {
        for(int i = 0; i < 10; i++)
        {
            int size_v = v[i].size();
            
            if(numbers.find(v[i]) == 0)
            {
                numbers = numbers.substr(size_v);
                result *= 10;
                result += n[i];
                break;
            }
        }
    }
    return result;
}