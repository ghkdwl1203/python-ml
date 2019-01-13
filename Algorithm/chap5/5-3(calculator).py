def push(item,stack):
    stack.append(item, stack)

def pop():
    return stack.pop()
global stack
stack = []

def Calculator(input):
   for num in input:

      if input[num]!= "+":
       push(input[num],stack)
      else:
       push (input[num],stack2)

       return print(stack)

Calculator("1+2*3+4")
""
a="1+2*3+4"
type(a[0])