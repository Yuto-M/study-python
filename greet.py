def greet(hour):
    if 4 < hour < 12:
        print('good morning')
    elif 12 < hour < 18:
        print('good afternoon')
    else:
        print('good evening')

greet(8)
greet(17)
greet(21)