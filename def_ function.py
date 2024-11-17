def add():    # paranthetis
    num1 = 10
    num2 = 20
    print(num1 + num2) 
add()   #parameter 

def add(a,b): # parameter
    num1 = a
    num2 = b
    print(num1+num2)
add(100,200)    # argument
add(100,400)    # argument
add(600,200)    # argument
add(100,900)    # argument
add(100,200)    # argument
add(1000,200)    # argument


# require parameter

def add(a,b): # parameter
    num1 = a
    num2 = b
    print(num1+num2)
add(100,200) 

def add(a=150,b=20): # parameter
    num1 = a
    num2 = b
    print(num1+num2)
add()

def add(a,b): # parameter
    num1 = a
    num2 = b
    print(num1+num2)
add(100,8)

def add(a=150,b=20): # parameter
    num1 = a
    num2 = b
    print(num1+num2)
add(200,300) 


# variable length argument (tuple)

def add(*number): # parameter
    
    print(number)
add(1,2,30,400,"arafat", 3.4, True) 


# dynamiic babe run kore

def add(*numbers): # parameter
    for number in numbers:
      print(number)
add(1,2,30,400,"arafat", 3.4, True) 


# keyword argument  (dictronary)

def add(**persion): # parameter
    
    print(persion)
add( 
    name ="arafat",
    age=24,
    city="dhaka"
    ) 

def add(**persion): # parameter
    
    print(persion["age"])
add( 
    name ="arafat",
    age=24,
    city="dhaka"
    ) 

def add(**persion):
    for key,value in persion.items():
        print(f'{key} : {value}')
        print(key+":"+str(value))

add(
    name ="arafat",
    age=24,
    city="dhaka"
    )


def add(**persion):
    for key,value in persion.items():
        print(key+":"+str(value))

add(
    name ="arafat",
    age=24,
    city="dhaka"
    )