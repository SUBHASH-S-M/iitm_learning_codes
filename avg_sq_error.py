y=[0.0319,0.8692,1.9566,3.0433]
y1=[0,1,2,3]
y2=[1,2,3,4]
y3=[-1,1,3,5]
y4=[0,2,4,6]
loss=[0,0,0,0]

for i in range(len(y)):
    loss[0]=(y1[i]-y[i])**2
    loss[1]=(y2[i]-y[i])**2
    loss[2]=(y3[i]-y[i])**2
    loss[3]=(y4[i]-y[i])**2
print(loss)
print(loss/4)
