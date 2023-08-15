def solution(string, guess) :
    M = ''
    for i in range(len(string)) :
        if string[i] == guess[i] :
            M += 'G'
        else :
            M += 'B'
    else :
        return M

testCase = int(input())

while testCase>0 :
    m = solution(input(), input())
    print(m)
    testCase -= 1