def write_file(data):
    with open('file.txt','a') as file:
        file.writelines(data)
          
def read_file():
    with open('file.txt','r') as file:
        return file.readlines()
    
      