# Problem : https://www.codechef.com/problems/HAPPYSTR
# Name : Chef and Happy String

def solution(string) :
    if 'a' or 'e' or 'i' or 'o' or 'u' in string :
        for i in range(len(string)-2) :
            if (string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u') and (string[i+1]=='a' or string[i+1]=='e' or string[i+1]=='i' or string[i+1]=='o' or string[i+1]=='u') and (string[i+2]=='a' or string[i+2]=='e' or string[i+2]=='i' or string[i+2]=='o' or string[i+2]=='u') :
                return 'Happy'
        else :
            return 'Sad'
    else :
        return 'Sad'
    
testCase = int(input())

while testCase > 0 :
    string = input()
    result = solution(string)
    print(result)
    testCase -= 1