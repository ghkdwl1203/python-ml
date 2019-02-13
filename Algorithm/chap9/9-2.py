import random
import time
swap_counter = 0
def shell_sort(random_list):
    global swap_counter
    h=1
    while h<len(random_list):
        h = h*3 +1
    h= h//3

    while h>0:
        for i in range(h):
            start_index = i + h
            print(h)
            while start_index < len(random_list):
                temp = random_list[start_index]
                insert_index= start_index
                swap_counter += 1
                while insert_index > h-1 and random_list[insert_index-h] >temp:
                    random_list[insert_index] = random_list[insert_index-h]
                    insert_index = insert_index - h
                    swap_counter += 1
                random_list[insert_index] = temp
                start_index = start_index + h
                swap_counter += 1
        h=h//3 # set new h
        print(h)
if __name__=='__main__':

    list =[]
    input_n = input(" 정렬할 데이터의 수 :")
    for i in range(int(input_n)):
        list.append( random.randint(1,int(input_n)))
    print("< 정렬전>")
    print(list)
    shell_sort(list)

    print("< 정렬후>")
    print(list)

    print("교환 횟수 : {}".format(swap_counter))
