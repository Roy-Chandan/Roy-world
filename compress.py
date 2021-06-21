
import zipfile


with open ('file1.txt','w+') as f1:
	f1.write ("line one of file1")



with open ('file2.txt','w+') as f2:
	f2.write ("Line one of file 2")



comp_file = zipfile.ZipFile('comp_file.zip','w')


comp_file.write("file1.txt",compress_type=zipfile.ZIP_DEFLATED)

comp_file.write("file2.txt",compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()



zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")