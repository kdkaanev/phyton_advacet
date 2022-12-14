def students_credits(*args):
    diyan_dict = {}
    total_credits = 0
    for string in args:
        course_name, credit, max_test_points, diyans_points = string.split('-')
        percent_points = int(diyans_points) / int(max_test_points)
        point = int(credit) * percent_points
        total_credits += point
        diyan_dict[course_name] = point

    if total_credits >= 240:
        result = f"Diyan gets a diploma with {total_credits:.1f} credits."
    else:

        result = f"Diyan needs {240 - total_credits:.1f} credits more for a diploma."
    sorted_dict = dict(sorted(diyan_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_dict.items():
        result = result + "\n" + f'{key} - {value:.1f}'
    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
