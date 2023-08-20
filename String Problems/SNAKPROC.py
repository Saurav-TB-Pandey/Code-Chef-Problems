# Problem : https://www.codechef.com/problems/SNAKPROC
# Name : Snake Procession

def solution(str1) :
    if 'H' not in str1 and 'T' not in str1 :
        return 'Valid'
    elif 'HH' in str1.replace('.', '') or 'TT' in str1.replace('.', '') :
        return 'Invalid'
    elif str1.strip('.').startswith('H') and str1.strip('.').endswith('T') :
        return 'Valid'
    else :
        return 'Invalid'

reports = int(input())
while reports > 0 :
    length = int(input())
    result = solution(input())
    print(result)
    reports -= 1