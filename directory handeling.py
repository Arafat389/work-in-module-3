#create directory/ folder

"""
import os
os.mkdir("new")

"""

"""
# write
import os
with open("new/new.text","w") as file:
    file.write("hello world") 
"""

"""

# read

import os
with open ("new/new.text","r") as file:
    o = file.read()
    print(o)

"""
"""
# rename 

import os
os.rename("new", "new_folder")

"""

"""
# remove 

import os
os.remove("new_folder/new.text")
os.rmdir("new_folder")


"""

# file list

import os
#os.mkdir("new")

list_dic = os.listdir("new")
print(list_dic)
for list_item in list_dic:
  print(list_item)