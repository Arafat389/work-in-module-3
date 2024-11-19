
# create file

with open("new.text","w") as file:
    print("created")

# write file text
with open("new.text","w") as file:

  file.write("hello world Arafat islam ")  
  file.write("hello")   

#read file text
with open("new.text","r") as file:
  c = file.read()
  print(c)


# rename

import os
os.rename("new.text","new_new.text")



