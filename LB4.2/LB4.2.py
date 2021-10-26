import math
from math import fabs

dec_func= lambda fn: lambda x: lambda y: lambda z: (fn(x,y,z))

func_pow=lambda fn: lambda arg: lambda args: fn(arg,args)
func_p=func_pow(math.pow)

func_=lambda fn: lambda arg: fn(arg)
func_c=func_(math.cos)
func_s=func_(math.sin)
func_f=func_(math.fabs)
func_a=func_(math.atan)
func_l=func_(math.log)
func_sqrt=func_(math.sqrt)
        
@dec_func
def func(x,y,z):   
    res=func_f(func_c(x)-func_c(y))
    res1=(1+2*(func_p(func_s(y))(2)))
    res3=func_p(res)(res1)
    res4=(1+z+(func_p(z)(2))/2)+((func_p(z)(3))/3)+((func_p(z)(4))/4)
    res_=res3*res4   
    return res_

@dec_func
def func_new(x,y,z):    
    res=func_l(func_p(y)(-func_sqrt(func_f(x))))
    res1=res*(x-y/2)    
    res2=func_sqrt(func_s(func_a(z)))   
    res_=res1+res2    
    return res_


print(func(0.4e+4)(-0.875)(-0.475e-3))

print(func_new(-15.246)(4.642e-2)(20.001e+2))

