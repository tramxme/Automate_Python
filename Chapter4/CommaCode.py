def main(list_value):
    string = ", ".join(list_value[0:-1])
    string += ", and " + list_value[-1]

    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
print(main(spam))
