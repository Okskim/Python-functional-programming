import math

class ListRange():

    def __init__(self, N):
        self.a, self.k, self.max = 0, 0, N

    def __iter__(self):
        return self

    def __next__(self):
        if self.k < self.max:
            a, self.k, self.a = self.a, self.a+1, self.k+1
            return a
        else:
            raise StopIteration
        
class ListCalc():

    def calc(self, list_range):
        P=[]
        for i in list_range:
            P.append(0.13*(math.pow(i,3))-2.5*i+8)
        return P



new_calc=ListCalc()
new_list=new_calc.calc(ListRange(19))
print(new_list)

for i in new_list:
    if i < 0:
        print(i)
print('Отрицательные числа отсутствуют')

