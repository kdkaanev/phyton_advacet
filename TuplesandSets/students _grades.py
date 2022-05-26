def average(v):
    return sum(v) / len(v)


students_number = int(input())
students_dict = {}
for _ in range(students_number):
    students_info = input().split(' ')
    name, grade = students_info[0], students_info[1]
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(grade))

for key, value in students_dict.items():
    print(f'{key} -> {" ".join(map(str, value))} (avg: {average(value):.2f})')
