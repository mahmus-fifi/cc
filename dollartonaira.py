import locale
locale.setlocale(locale.LC_ALL, '')
item_Price = float(input('Enter price of item: '))
#print('please enter numbers eg 12, 13 only')
DOLLAR_RATE = 380
price = round((item_Price * DOLLAR_RATE),4)
buying_two = price * 2
buying_three = price * 3
num = 0
max_num = 100
#print(f' item price ${item_Price}\n  Naira Equivalent: N{price:,} ')
print(f' item price ${item_Price}\n  price in Naira: N{price:n} \n rate:@ ${380}/Naira')
for buyingmore in range(num,max_num):
    num = num + 1
    buying_additional_items = price * num
    print(f'items:{num} price N:{buying_additional_items:n}') 
#print('{:,}'.format(price)
#print('{:n}'.format(price))



    
    





