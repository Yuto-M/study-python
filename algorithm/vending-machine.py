import sys

# 整数チェック
input_price = input('insert: ')
if not input_price.isdecimal():
    print('整数を入力してください')
    sys.exit()

# 整数チェック
product_price = input('product: ')
if not product_price.isdecimal():
    print('整数を入力してください')
    sys.exit()

# 購入金額 - 商品価格がマイナスにならないかチェック
charge = int(input_price) - int(product_price)

if charge < 0:
    print('金額が不足しています')
    sys.exit()

# 商がお札の数、余りを次の単位で割る
coins = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coins:
    r = charge // i
    charge %= i
    print(str(i) + ': ' + str(r))
