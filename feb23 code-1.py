l=[]
n=int(input('enter the value : '))
for i in range(n):
    e=int(input('enter x value : '))
    l.append(e)

min=l[0]
for i in range(1,n):
    if l[i]<min:
        min=l[i]

max=l[0]
for i in range(1,n):
    if l[i]>max:
        max=l[i]
print(f'minimum value in list : {min}')
print(f'maximum value in list : {max}')