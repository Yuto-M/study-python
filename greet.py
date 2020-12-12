# 関数の書き方
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

# 辞書(dict。phpでいうところの連想配列)
jobs = {
    "John": "Guitar",
    "Paul": "Guitar",
    "George": "Bass",
    "Ringo": "Drums",
}

# forループ
for name, job in jobs.items():
    print('{}: {}'.format(name, job))

# 配列(list。)
names = ["John", "Paul", "George", "Ringo"]
for index, name in enumerate(names):
    print('{}: {}'.format(index, name[index]))