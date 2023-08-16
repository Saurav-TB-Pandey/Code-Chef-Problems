# Problem : https://www.codechef.com/problems/EZSPEAK
# Name : Easy Pronunciation

def  isEasy(string, lengthOfStr) :
    vowel = ['a', 'e', 'i', 'o', 'u']
    if lengthOfStr < 4 :
        return 'Yes'
    else :
        for i in range(lengthOfStr - 3) :
            if string[i] not in vowel and string[i+1] not in vowel and string[i+2] not in vowel and string[i+3] not in vowel:
                return 'No'
        else :
            return 'Yes'
    
testCase = int(input())

while testCase > 0 :
    lengthOfStr = int(input())
    string = input()
    result = isEasy(string, lengthOfStr)
    print(result)
    testCase -= 1