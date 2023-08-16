# Problem : https://www.codechef.com/problems/DIGARR
# Name : Rearranging digits to get a multiple of 5

def solution(number) :
    return 'Yes' if '5' in number or '0' in number else 'No'
    
testCase = int(input())

while testCase > 0 :
    digits = int(input())
    number = input()
    result = solution(number)
    print(result)
    testCase -= 1