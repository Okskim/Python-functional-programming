import math

class ListRange():

    def __init__(self, a, N):
        self.a, self.max = a, N

    def __iter__(self):
        return self
    def __next__(self):
        if self.a < self.max:
            if self.a % 2 != 0:
                a = math.pow(self.a,2)+1
                self.a=self.a+1
                
            elif self.a % 2 == 0:
                a = (2*self.a)-1
                self.a=self.a+1
            return a       

        else:
            raise StopIteration



class ListRangeSecond(ListRange):
       
    def __next__(self):
        ListRange.__next__(self)
        if self.a < self.max:
            if self.a < 2.5:
                a = self.a * 2.5
                self.a+=1
                
            elif self.a >= 0:
                a = self.a/2.5
                self.a+=1
            return a       

        else:
            raise StopIteration


Z=ListRange(1,20)
print(list(Z))


D=ListRangeSecond(1,10)
print(list(D))