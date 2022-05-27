def average(v):
    return sum(v) / len(v)


students_number = int(input())
students_dict = {}
for _ in range(students_number):
    students_info = input().split(' ')
    name, grade = students_info[0], float(students_info[1])
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for key, value in students_dict.items():
    value_formated = ' '.join(f'{v:.2f}' for v in value )
    print(f'{key} -> {value_formated} (avg: {average(value):.2f})')
