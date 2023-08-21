# Problem : https://www.codechef.com/problems/TTENIS
# Name : Chef and Table Tennis

def solution(str1) :
    return 'LOSE' if str1.count('0') > str1.count('1') else 'WIN' if str1.count('0') < str1.count('1') else 'WIN' if str1.count('0') == str1.count('1') and str1.count('11') >= str1.count('00') else 'LOSE'

for _ in range(int(input())) :
    str1 = input()
    print(solution(str1))