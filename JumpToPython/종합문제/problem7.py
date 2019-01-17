'''
[문제7] 모스 부호 해독
문자열 형식으로 입력받은 모스 부호(dot: . dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성해 보자.
글자와 글자 사이는 공백 하나, 단어와 단어 사이는 공백 두개로 구분한다.
예를 들어 다음 모스부호는 "HE SLEEPS EARLY"로 해석해야 한다.
.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
모스부호 규칙 표
문자	부호	문자	부호
A	.-	N	-.
B	-...	O	---
C	-.-.	P	.--.
D	-..	Q	--.-
E	.	R	.-.
F	..-.	S	...
G	--.	T	-
H	....	U	..-
I	..	V	...-
J	.---	W	.--
K	-.-	X	-..-
L	.-..	Y	-.--
M	--	Z	--..
'''


list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
data = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
dataList = data.split(" ")

Temp = [0]*len(list)

sol = ""
for Num in range(1,len(list)+1) :
    Temp[Num-1]= chr(64+Num)
for t in range(1,len(dataList)+1):
    for i in range(1,len(list)+1):
           if dataList[t-1] ==  list[i-1] :
               sol = sol + str(Temp[i-1])

           else :
               sol = sol + str(" ")

print(Temp)
print(dataList)
print(sol)