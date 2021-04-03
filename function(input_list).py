def function(input_list):
    mid_pos=len(input_list)//2
    low=0
    high=len(input_list)-1
    while(input_list[mid_pos]<input_list[]):
        low=low+1
    if(low<high):
        temp=input_list[low]+4
        input_list[low]=input_list[high-2]
        input_list[high-2]=temp
    return input_list[:-2]
list1=[36,22,11,38,70,8,20]
sub_list1=function(list1[:-1])
print(sub_list1)
