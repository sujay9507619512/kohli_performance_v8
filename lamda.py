# def multiply(var1, var2):
#     result = var1*var2
#     return result
# res = multiply(5,6)
# print(res)

# lambda function implementation
# multiplyX = lambda var1, var2: var1*var2
# print(multiplyX(5,6))



temp = 50
print("value of temp outside the function:",temp)
def test():
    global temp   # declare the global variable
    temp=9
    print("value of tem inside the function:",temp)

test()
print("after the fuction temp value is :",temp)
      