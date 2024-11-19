
"""
result = 10/0
print(result)

"""


"""
# single exception handeling
try:
    result=10/0
    print(result)
except:
    print("division by zero") 

    """
# multiple exception handeling
try:
    with open ("arafat.text","r")as file:
        content=file.read()
        result=10/int(content)
        print(result)
except Exception as e:
       print(e)
finally:
     print("execution complete")