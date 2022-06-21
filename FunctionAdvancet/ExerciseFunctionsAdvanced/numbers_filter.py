def even_odd_filter(**kwarks):
    result = {}
    for key, value in kwarks.items():
        check = 0 if key == 'even' else 1
        filtred_numbers = [int(x) for x in value if x % 2 == check]
        result[key] = filtred_numbers


    sorted_result = dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))
    return sorted_result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
