def isPalindrome(num) :
    return True if num == int(str(num)[::-1]) else False

testCase = int(input())

while testCase > 0 :
    
    number = int(input())
    
    result = isPalindrome(number)
    
    print('wins') if result else print('loses')
    
    testCase -= 1