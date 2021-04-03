def function(string,list1):
    num=1
    while num!=len(string):
        if len(string)%2==0 or (string[:-1].count('a')>=1):
            list1.append(string[num])
        num+=1
        list1=function(string[num:],list1)
        break
    return list1
print(function("Irradiation",[]))

## Output ##
# ['r', 'a', 'i', 't']
