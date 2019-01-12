'''
[문제6] Duplicate Numbers
0~9까지의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9까지의 모든 숫자가 각각 한 번씩만 사용된 것인지 확인하는 함수를 작성해 보자.
입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: true false false true false
'''
'''
data= "0123456789"
0 == data[0]
sol = 1
cri = 1
for i in range(1,10):
    for n in range(1,len(data) ):

     if str(i-1) == data[n-1]:
           t = data[n-1]
           cri = cri * 0 #참

     else :
            cri = cri * 1 #거짓
    cri2 = cri + 1
    sol = sol*cri2
    cri = 1

if sol == 1:
    sol="true"

else :
    sol="false"

print(sol)

'''

def chkDupNum(s):
     result = [ ]
     for num in s:
         if num not in result: ##result 안에 없으면
             result.append(num) ##숫자 넣고 append : 덧붙이는 기능
         else:
             return False ##없으면 false리턴
     return len(result) == 10 ##0~9까지 다 넣어서 길이가 10이 안되면 false 리턴 되면 true 리턴



print(chkDupNum("0123456789")) # True 리턴
print(chkDupNum("01234")) # False 리턴
print(chkDupNum("01234567890")) # False 리턴
print(chkDupNum("6789012345")) # True 리턴
print(chkDupNum("012322456789")) # False 리턴
