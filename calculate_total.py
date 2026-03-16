prices = [100, 200, 300]

def calculate_total(prices, *discounts , **options):
    sum_prices = 0
    for i in prices:
        sum_prices+=i
    for j in discounts:
        sum_prices=sum_prices*(100-j)/100
        print(sum_prices)
    sum_prices = sum_prices*(options.get('tax')+100)/100
    result = round(sum_prices, options.get('round_1'))
    return result