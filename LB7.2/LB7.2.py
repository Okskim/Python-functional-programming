import math

dec_func= lambda fn: lambda list_name: fn(list_name) 


func_pow=lambda fn: lambda arg: lambda args: fn(arg,args)
func_p=func_pow(math.pow)
func_=lambda fn: lambda arg: fn(arg)
func_c=func_(math.cos)
    

def list_range(i,j):
    list_new=list(range(i,j))
    return list_new

@dec_func
def list_calc(list_new):
    mas=[]
    for i in list_new:
        mas.append((5*i+func_p(func_c(i))(2)/2.35))
    return mas


Y=list_range(1,26)
print(Y)

R=list_calc(Y)
print(R)