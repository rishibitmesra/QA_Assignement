
num=100
for Number in range (1, num):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if Number % i == 0:
            count = count + 1
            break
    if count == 0 and Number != 1:
        print(Number, end = '  ')

'''
Test Cases:
1. Verify the program if number is 100 , all prime number should be displayed under 100
2. Verify the program if number is 99, all prime number should be displayed under 99
3. Verify the program if number is 101, all prime number should be displayed under 101
4. Verify the program if number is -100, Should not be displayed any thing
5. Verify the program if number is 100.0 , TypeError should shown and program finsished with error code 1 
6. Verify the program if number is as string "100", TypeError should shown and program finsished with error code 1
7. Verify the program if number is as +100 , all prime number should be displayed under 100
8. Verify the program if number is as +-100 , Should not be displayed any thing
9. Verify the program if number is as 4e+30 , TypeError should shown and program finsished with error code 1 
10. Verify the program if number is 0, Should not be displayed any thing
'''
