x=20   # global variable 
y=10   # global variable
def sum1():
    print(x+y)
sum1()
print(x+y)

#same name local and global variable

text = "I am global"
def sum1():
    text = "I am local"
    print(text)
sum1()    

print(text)  



# modify

x =10
def sum1 ():
    global x
    x=20
    x1 = x+1
    print(x1)
sum1()

def sum2 ():
    x2 = x+2
    print(x2)
sum2()    