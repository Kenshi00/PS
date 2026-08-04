#include <string>
#include <vector>

using namespace std;

int solution(int chicken) {
    int total_coupon = chicken;
    int service_chicken = 0;
    while(total_coupon >= 10)
    {
        service_chicken += total_coupon / 10;
        total_coupon = total_coupon / 10 + total_coupon % 10;
    }
    return service_chicken;
}