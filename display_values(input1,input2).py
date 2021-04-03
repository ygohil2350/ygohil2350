def display_values(input1,input2):
    for index in range(0,len(input1)):
        if input1[index]%input2==0:
            print(input1[index])
display_values([3,4],2)
