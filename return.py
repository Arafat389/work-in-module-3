#single
def add (a,b):
    num1 = a
    num2 = b
    sum= num1+num2
    return sum
result=add(12,8)
print(result)

#multiple (tuple)
def add (a,b):
    num1 = a
    num2 = b
    sum= num1+num2
    sub= num1-num2
    mul= num1*num2
    div= num1/num2
    return sum,sub,mul,div
result=add(12,8)
print(result)

#multiple (list)
def add (a,b):
    num1 = a
    num2 = b
    sum= num1+num2
    sub= num1-num2
    mul= num1*num2
    div= num1/num2
    return [sum,sub,mul,div]
result=add(12,8)
print(result)

#multiple (dic)
def add (a,b):
    num1 = a
    num2 = b
    sum= num1+num2
    sub= num1-num2
    mul= num1*num2
    div= num1/num2
    return {"sum":sum,"sub":sub,"mul":mul,"div":div}
   
result=add(12,8)
print(result)

# early return
def numbers(num):
    for number in  num:
        if number%2==1:
            return number
        return None
result=numbers([12,11,14])    
print(result)    

