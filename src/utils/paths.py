from os import path, getcwd

project_directory = getcwd() # Project directoy

data_directory = path.join(path.join(project_directory), 'data') # Data directory

images_directory = path.join(path.join(data_directory), 'images') # Images directory


src_directory = path.join(path.join(project_directory), 'src') # 
auth_directory = path.join(path.join(src_directory), 'auth') # Images directory
users_database = path.join(path.join(auth_directory), 'Locker.db') # Images directory