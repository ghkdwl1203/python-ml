class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def init_list():
        global node_A   #전역변수
        node_A = Node("A")
        node_B = Node("B")
        # node_C = Node("C")
        node_D = Node("D")
        node_E = Node("E")

        node_A.next = node_Bi
        # node_B.next = node_C
        node_B.next = node_D
        node_D.next = node_E

def delete_node(del_data):
    global node_A
    pre_node = node_A
    next_node = pre_node.next

    if pre_node.data==del_data:
        node_A=next_node
        del_pre_node
        return
    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
    pre_node = next_node
    next_node = next_node.next

def insert_node(data):
    global node_A
    new_node = Node(data)
    node_P = node_A
    node_T = node_A
    while node_T.data <= data:
       node_P = node_T
       node_T = node_T.next
    new_node.next = node_T
    node_P.next = new_node


def print_list():
        global node_A
        node=node_A
        while node:
            print(node.data)
            node = node.next
        print #있으나 없으나 뭔차이


if __name__=='__main__':  # 해당 파이썬 파일을 실행했을때만 동작하는 if문
        init_list()
        print_list()
        print("노드 c를 추가한 후")
        insert_node("C")
        #print_list()