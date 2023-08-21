# Problem : https://www.codechef.com/problems/BSCOST
# Name : Binary String Cost

def solution(str1, x, y) :
    return 0 if str1.count('0') == 0 or str1.count('1') == 0 else x if x < y else y

for _ in range(int(input())) :
    n, x, y = map(int, input().split())
    print(solution(input(), x, y))