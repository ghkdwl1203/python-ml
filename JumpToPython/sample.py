dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
} ## 저자는 Dictionary 씀
def morse(src):
    result = []
    for word in src.split("  "): ## 띄어쓰기 구분
        for char in word.split(" "): ## 글자 구분
            result.append(dic[char]) ## 글자 찾기
        result.append(" ") ## 띄어쓰기인 경우 space 추가
    return "".join(result)
print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))