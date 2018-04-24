list_x = [1,2,3,4,5,6,7,8]
def square(x):
    return x * x

f = map(lambda x:x*x,list_x)
print(list(f))