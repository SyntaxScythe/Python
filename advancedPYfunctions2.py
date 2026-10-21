s1 = (2, 3, 1)
s2 = ('b','a','c')
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [1, 2, 3, 4, 5]
list2 = [100, 200, 300, 400, 500]

for x, y in list(zip(list1, list2)):
    print(x, y)
    
stocks = ('reliance', 'infosys', 'tcs')
prices = (2175, 1127, 2750)

new_dict = {stocks: prices for stocks,
            prices in zip(stocks, prices)}
print('\n', new_dict, "\n")