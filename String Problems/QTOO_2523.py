# Problem : https://www.codechef.com/problems/QTOO_2523
# Name : Bi_lindrome!

def solution(length, str1) :
    if length < 2 :
        return -1
    else :
        for item in set(str1) :
            if str1.count(item) >= 2 :
                return length - 2
        else :
            return -1

for _ in range(int(input())) :
    length = int(input())
    str1 = input()
    print(solution(length, str1))