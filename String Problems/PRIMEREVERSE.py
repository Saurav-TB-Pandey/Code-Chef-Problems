# Problem : https://www.codechef.com/problems/PRIMEREVERSE
# Name : Prime Reversal

def solution(str1, str2) :
    if str1 == str2 :
        return 'Yes'
    else :
        for item in set(str1) :
            if str1.count(item) != str2.count(item) :
                return 'No'
        else :
            return 'Yes'

testCase = int(input())
while testCase > 0 :
    length = int(input())
    result = solution(input(), input())
    print(result)
    testCase -= 1