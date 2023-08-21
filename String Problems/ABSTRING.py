# Problem : https://www.codechef.com/problems/ABSTRING
# Name : String Game

def solution(str1) :
    for item in set(str1) :
        if str1.count(item) % 2 != 0 :
            return 'No'
    else :
        return 'Yes'

for _ in range(int(input())) :
    length = int(input())
    print(solution(input()))