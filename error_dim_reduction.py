#case1
x=[(1,0.5),(2,2.3),(3,3.1),(4,3.9)]
f=[a-b for a,b in x ]
g=[(i/2,i/2) for i in f]
print("encoder : ",f)
print("decoder: ",g)
loss=0
for index,value in enumerate(zip(g, x)):
    print(index)
    print(value[0][0],value[1][0],":::",value[0][1],value[1][1])
    print(value[0][0]-value[1][0],":::",value[0][1]-value[1][1])
    temp=(value[0][0]-value[1][0])**2+(value[0][1]-value[1][1])**2
    print(temp)
    loss+=temp
    print("Loss :",loss)
    
print("final: ",loss/len(x))
# result = [(index, value1, value2) for index, (value1, value2) in enumerate(zip(list1, list2))]
# x=[(1,0.5),(2,2.3),(3,3.1),(4,3.9)]
# f=[(a+b)/2 for a,b in x ]
# g=[(i/2,i/2) for i in f]
# print("encoder : ",f)
# print("decoder: ",g)
# loss=0
# for index,value in enumerate(zip(g, x)):
#     print(index)
#     print(value[0][0],value[1][0],":::",value[0][1],value[1][1])
#     print(value[0][0]-value[1][0],":::",value[0][1]-value[1][1])
#     temp=(value[0][0]-value[1][0])**2+(value[0][1]-value[1][1])**2
#     print(temp)
#     loss+=temp
#     print("Loss :",loss)
    
# print("final: ",loss/len(x))
