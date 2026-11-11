def create():
    a={}
    n=int(input("enter the number of elements :"))
    print(n)
    for i in range(n):
        print("enter data at", i,end=" : ")
        a[i]=int(input(f"enter data at {i}: "))
    return a

def display(a):
    for i in range(len(a)):
        print(f"a[{i}] = " ,a[i])

def access(a,i):
    if 0<=i and i<len(a):
        print("the element at position ",i,"is",a[i])
    else:
        print("the index is more than the size of array")

def insert(a,i,x):
    if i<0:
        print("location is below the range")
        return a
    elif i>len(a):
        print("location is out of the range")
        return a
    else:
        for j in range(len(a)-1,i-1,-1):
            a[j+1]=a[j]
        a[i]=x
        return a

def delit(a,i):
    if i<0:
        print("location is below the range")
        return a
    elif i>=len(a):
        print("location is out of the range")
        return a
    else:
        for j in range(i,len(a)-1):
            a[j]=a[j+1]
        del a[len(a)-1]
        return a

#main program
Arr=create()
print("\n ---the element in the array is ----")
display(Arr)

print("\n ----data at location ----")
i=int(input("element at which position element to get:"))
access(Arr,i)

print("\n ----insert at a location ----")
j=int(input("specify the location to insert:"))
y=int(input("specify the data:"))
Arr=insert(Arr,j,y)
display(Arr)

print("\n ----deletion at position ----")
j=int(input("specify the location to delete:"))
Arr=delit(Arr,j)
display(Arr)
