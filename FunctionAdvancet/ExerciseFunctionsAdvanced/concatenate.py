def concatenate(*args, **kwargs):
    def string(*args):
        text = ''
        for word in args:
            text += word
        return text
    text = string(*args)
    for key, value in kwargs.items():
        if key in text:
            text = text.replace(key, value)
    return text

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
