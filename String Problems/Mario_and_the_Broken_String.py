def isTrue(size, string) :
    strParam1 = string[: size//2]
    strParam2 = string[size//2 :]
    
    return 'Yes' if (strParam1 and strParam2) + (strParam2 and strParam1) == string else 'No'

testCase = int(input())

while testCase > 0 :
    size = int(input())
    string = input()
    
    answer = isTrue(size, string)
    print(answer)
    testCase -= 1