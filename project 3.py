import os
import shutil
from_dir = "C:/Users/Negha Rajeshkhanna/Downloads"
to_dir = "C:/Users/Negha Rajeshkhanna/Downloads/Downloaded documents"
list_of_files = os.listdir(from_dir)
print(list_of_files)
#move all image files from download folder to another folder
for file_name in list_of_files :
    name , extention = os.path.splitext(file_name)
    print(name)
    print(extention)
    if extention == "":
        continue
    if extention in [".txt",".pdf",".doc",".docx"]:
        path1 = from_dir + "/"+ file_name       #Downloads/imagename1.jpg
        path2 = to_dir+ "/"+ "Doc_file"       #Downloadedimages/image_file
        path3 = to_dir + "/" + "Doc_file"+ "/" + file_name
        print("path1",path1)
        print("path2",path2)
        print("path3",path3)
        if os.path.exists(path2):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+ file_name)
            shutil.move(path1,path3)
    
        

