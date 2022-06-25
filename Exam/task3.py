def shopping_cart(*args):
    cart = {}
    for elements in args:
        if elements == 'Stop':
            break
        meals, product = elements
        if meals not in cart:
            cart[meals] = []
        if meals == 'Soup' and len(cart[meals]) < 3:
            cart[meals].append(product)
        elif meals == 'Pizza' and len(cart[meals]) < 4:
            cart[meals].append(product)
        elif meals == 'Dessert' and len(cart[meals]) < 2:
            cart[meals].append(product)

    for k, v in cart.items():
        cart[k].sort()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
