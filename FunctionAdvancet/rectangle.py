def rectangle(lenght, width):
    def area():
        return lenght * width

    def perimeter():
        return 2 * (lenght + width)

    if not isinstance(lenght, int) or not isinstance(width, int):
        return "Enter valid values!"

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''



