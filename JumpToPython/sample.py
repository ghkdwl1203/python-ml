print(ord("A")) #대문자 ASCII : 65시작, 소문자 : 90 시작
list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
data = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
dataList = data.split(" ")
print(dataList)
answer = ""
for char in dataList :
    if char == '' :
        answer = answer + " "
    else :
        for n in range(0, len(list)) :
            if list[n] == char :
                answer = answer + chr(n+65)

print(answer)