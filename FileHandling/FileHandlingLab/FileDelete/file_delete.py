import os.path
from os import remove

try:
    remove('deleted')
    print('File Deleted')
except FileNotFoundError:
    print('File Already Deleted')