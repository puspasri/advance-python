num=[1,2,3,4,5,6,7,8,9,0]
name =["Srishti", "Harshita", "Priyanka"]

zips =  list(zip(num,name))
print(zips)


num1=[10,20,30]
num2=[40,50,60]

for x,y in zip(num1,num2):
    print(x,y)