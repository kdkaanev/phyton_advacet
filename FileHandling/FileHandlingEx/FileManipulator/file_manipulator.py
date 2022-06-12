from os import remove
from os.path import exists

command = input()
while command != "End":
    info = command.split('-')
    action, file_name = info[0], info[1]
    if action == 'Create':
        with open(f'./{file_name}', 'w') as file:
            file.write('')
    elif action == 'Add':
        content = info[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(f'{content},/n')
    elif action == 'Replace':
        old_string, new_string = info[2], info[3]
        with open(f'./{file_name}', 'w') as file:
            if exists(file_name):
                for line in file:
                    line.replace(old_string, new_string)
            else:
                print('An error occurred')
    elif action == 'Delete':
        if exists(file_name):
            remove(file_name)
        else:
            print('An error occurred')

    command = input()
print()
