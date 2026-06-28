def decorator(function):
    def wrapper(a,b):
        print("The addition is: ")
        function(a,b)
        print("Addition is complete")
    return wrapper
@decorator
def Addition(a,b):
    print(f"{a+b}")

print(Addition(9,7)    )
