
def recursive(n):
    if( n > 1 ):
        recursive(n - 1)
    print(n)

recursive(10)