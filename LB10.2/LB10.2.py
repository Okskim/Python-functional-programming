str="Hello World"
print(str)


def filter_str(str_change):
    str_1=str_change.split()
    str_2=map(lambda word:" ".join(word[1:]), str_1)
    return list(str_2)

def reverse_str(str_change):
    str_1=str_change.split()
    res=[]
    for i in str_1:
        res.append(i[0]+i[4]+i[2]+i[3]+i[1])
    return res
 

result=filter_str(str)
print(result)


result1=reverse_str(str)
print(result1)
