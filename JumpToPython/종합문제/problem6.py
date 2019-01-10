'''
[문제6] Duplicate Numbers
0~9까지의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9까지의 모든 숫자가 각각 한 번씩만 사용된 것인지 확인하는 함수를 작성해 보자.
입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: true false false true false
'''

data= "012345789"
sol = "False"
cri = 1
t=1
for i in range(1,10):
    for n in range(1,len(data) ):

        if data[n-1] == (i-1):
           t = data[n-1]
           cri *= 0
        else :
            cri *= 1





print(cri)
