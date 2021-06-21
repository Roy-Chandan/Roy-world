import shutil
import os
import re

shutil.unpack_archive ('C:\\Users\\roych\\anaconda3\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip','','zip')

with open ('C:\\Users\\roych\\anaconda3\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content\\Instructions.txt') as f:
    print (f.read())
    
def search (file,pattern=r'\d{3}-d{3}-d{4}'):
    with open ('file','r') as var:
        text = var.read()
       
    if re.search(pattern,text):
        return re.search(pattern,text)
    
    else:
        pass


    
results = []
    
for folder , sub_folders , files in os.walk('C:\\Users\\roych\\anaconda3\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\extracted_content'):
    
    for f in files:
        full_path = folder+'\\'+f
         
        results.append(search(full_path)) 
        
for r in results:
    if r != '':
        print(r.group())
