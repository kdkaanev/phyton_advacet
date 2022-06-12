from os import remove
from os.path import exists

command = input()
while command != "End":
    info = command.split('-')
    action, file_name = info[0], info[1]
    if action == 'Create':
        with open(f'./{file_name}', 'w') as file:
            pass
    elif action == 'Add':
        content = info[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '/n')
    elif action == 'Replace':
        if not  exists(f'./{file_name}'):
            print('An error occurred')
        else:
            old_string, new_string = info[2], info[3]
            with open(f'./{file_name}', 'r+') as file:
                text = file.read()
                text = text.replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(text)
    elif action == 'Delete':
        if not exists(f'./{file_name}'):
            print('An error occurred')
        else:
            remove(file_name)


    command = input()
