def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)    ## if cnt : 의 의미.. cnt가 0이면 false, 그외 숫자면 true
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result
print (compress_string("aaabbcccccca")) #a3b2c6a1 출력
