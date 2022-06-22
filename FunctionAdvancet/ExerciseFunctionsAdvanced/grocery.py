def grocery_store(**kwargs):
    sorted_store = [f'{key}:{value}' for key, value in
                    sorted(kwargs.items(), key=lambda x: (x[1], len(x[0]), x[0]), reverse=True)]

    return '\n'.join(sorted_store)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
