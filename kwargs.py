def multiply(**kwargs):
    result=1
    for i in kwargs:
        result *=i
    print(f"The product is: {result}")    

multiply(3,6,8,4)    
