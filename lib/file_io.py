def write_file(file_name, file_content):
    with open (f'{file_name}.txt', mode='w', encoding='utf-8' ) as file_name :
        file_name.write(file_content)
        
write_file(file_name="logfile" ,file_content="This is a test content.")

def append_file(file_name, append_content):
    with open(f'{file_name}.txt' , mode='a' , encoding='utf-8' ) as file_name :
        file_name.write(append_content)
append_file(file_name='logfile' , append_content='This is an Appended content.')

def read_file(file_name):
    with open (f'{file_name}.txt' ,  encoding='utf-8') as test_file :
      content= test_file.read()
      return content 
file_content = read_file(file_name="logfile")
print(file_content)
