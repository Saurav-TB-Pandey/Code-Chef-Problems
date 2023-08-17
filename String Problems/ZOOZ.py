# Problem : https://www.codechef.com/problems/ZOOZ
# Name : Zero Ones Equal One Zeros

def getBinary(n) :
    binaryNumber = ""
    if n % 2 == 0 :
        for i in range(n) :
            if (i == 0 or i == n - 1) :
                binaryNumber += '1'
            else :
                binaryNumber += '0'
    if n % 2 != 0 :
        for i in range(n) :
            if (i == 0 or i == n - 1) :
                binaryNumber += '0'
            else :
                binaryNumber += '1'
    return binaryNumber

testCase = int(input())
while testCase > 0 :
    length = int(input())
    result = getBinary(length)
    print(result)
    testCase -= 1