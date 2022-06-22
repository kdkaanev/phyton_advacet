def age_assignment(*args, **kwargs):
    result = {}
    names = [n for n in args]
    dict = {key:value for key,value in kwargs.items()}
    for letter, age in dict.items():
        for name in names:
            if name[0] == letter:
                result[name] = age
    sorted_result = [f'{name} is {age} years old' for name, age in sorted(result.items())]
    return '\n'.join(sorted_result)


print(age_assignment("Peter", "George", G=26, P=19))