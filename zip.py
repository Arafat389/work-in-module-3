"""
# create zip file

import zipfile
with zipfile.ZipFile("new_file.zip","w") as zip:
    zip.write("a11.text")
    zip.write("a21.text")



"""

"""


 # extract / unzip file

import zipfile
with zipfile.ZipFile("new_file.zip","r")as zip:
    zip.extractall()
    extracted_file = zip.namelist()
    print(extracted_file) 

    """

import shutil
shutil.make_archive("arafat islam","zip","arafat")
