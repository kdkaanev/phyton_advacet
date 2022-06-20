def even_odd_filter(**kwarks):
    result = {}
    for key, value in kwarks.items():
        if key == 'odd':
            odd_numbers = [int(x) for x in value if x % 2 != 0]
            result['odd'] = odd_numbers
        elif key == 'even':
            even_numbers = [int(x) for x in value if x % 2 == 0]
            result['even'] = even_numbers

    sorted_result = dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))
    return sorted_result


print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))
