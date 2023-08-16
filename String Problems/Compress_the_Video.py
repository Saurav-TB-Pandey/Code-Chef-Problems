# Problem : https://www.codechef.com/problems/COMPRESSVD

def minFrame(value):
    i = 0
    for j in range(1, len(value)):
        if value[j] != value[i]:
            i += 1
            value[i] = value[j]
    return i + 1
    

testCase = int(input())
while testCase > 0 :
    size = int(input())
    value = input().split()
    result = minFrame(value)
    print(result)
    testCase -= 1