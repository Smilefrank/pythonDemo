
def print_func(num1,num2,num3=33,*args,**kwargs):
    print(num1)
    print(num2)
    print(num3)
    print(args)
    print(kwargs)

print_func(12,23,32,232,222,2)


A = (34,55,66)
B = {"name":"wangbaofeng","age":31}

print_func(23,34,55,*A,**B)   #*A 元祖  **B字典 拆包过程





