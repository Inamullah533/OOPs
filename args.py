def multiply(*args):
    result=1
    for i in args:
        result *=i
    print(f"The product is: {result}")    

multiply(3,6,8,4)    
