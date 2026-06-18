txt_data = "I Love You"
file_path = "output.txt"
with open(file_path,"w") as file2: # w for write , x also to write but used when the text file doesnt exist!
    file2.write(txt_data)
    print(f"{file_path} as a text file was created")